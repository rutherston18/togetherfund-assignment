#!/usr/bin/env python3
"""
Cleans scraped markdown articles for use in ChromaDB RAG pipeline.

Removes:
  - Boilerplate sections (References, Author Contributions, IRB statements,
    Conflicts of Interest, Funding, Supplementary Materials, etc.)
  - Market research boilerplate (methodology, stakeholders, report objectives,
    sales/customization CTAs)
  - Inline superscript citation numbers (e.g. "economy2 but" → "economy but")
  - Footnote back-reference lines (lines with ↩︎)
  - Author biography paragraphs (trailing bios with no heading)
  - Misc noise: "Backed by X" lines, "Retrieved from URL" lines

Input:  data/markdown_articles/
Output: data/cleaned_articles/
"""

import re
from pathlib import Path

INPUT_DIR  = Path("data/markdown_articles")
OUTPUT_DIR = Path("data/cleaned_articles")

# Heading text patterns (matched case-insensitively against the heading title)
# When matched, the heading AND all content until the next same-or-higher-level
# heading is removed.
BOILERPLATE_HEADINGS = [
    r"^references?$",
    r"^author contributions?$",
    r"^authors?$",
    r"^author bios?$",
    r"^institutional review board statement$",
    r"^informed consent statement$",
    r"^data availability statement$",
    r"^conflicts? of interest$",
    r"^funding statement$",
    r"^footnotes?$",
    r"^supplementary materials?$",
    r"^associated data$",
    r"^primary research$",
    r"^secondary research$",
    r"^market size estimation$",
    r"^data triangulation$",
    r"^market definition$",
    r"^stakeholders?$",
    r"^report objectives?$",
    r"^need a tailored report\??$",
    r"^custom market research services?$",
    r"^delivered customizations?$",
    r"^personali[sz]e this research$",
    r"^let us help you$",
    r"^table of contents$",
    r"^data sources? and methodology$",
    r"^methodology$",
    r"^recent developments?$",
    r"^what is in it for you.*",    # MarketsandMarkets Q&A/comments section
]

# Bold-text pseudo-headings (lines like "**Data Sources and Methodology**")
# that some articles use instead of proper ## headings.
BOILERPLATE_BOLD_HEADINGS = [
    r"Data Sources? and Methodology",
]


def _is_boilerplate_heading(heading_text: str) -> bool:
    text = heading_text.strip()
    return any(re.match(p, text, re.IGNORECASE) for p in BOILERPLATE_HEADINGS)


def remove_boilerplate_sections(text: str) -> str:
    """Remove markdown sections whose headings match known boilerplate patterns."""
    lines = text.split("\n")
    result = []
    skipping = False
    skip_level = 0

    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            level = len(m.group(1))
            heading_text = m.group(2).strip()

            # A same-or-higher-level heading ends the skipped block
            if skipping and level <= skip_level:
                skipping = False

            if not skipping and _is_boilerplate_heading(heading_text):
                skipping = True
                skip_level = level
                continue  # drop the heading line itself

        if not skipping:
            result.append(line)

    return "\n".join(result)


def remove_bold_pseudo_sections(text: str) -> str:
    """Remove sections introduced by a bolded paragraph header (not a ## heading).

    Matches from the bold header to the next blank-line-separated block that
    looks like a heading, or to end-of-file if nothing follows.
    """
    for pattern in BOILERPLATE_BOLD_HEADINGS:
        # Match the bold header line at the start of a line, then consume
        # everything until the next markdown heading or EOF.
        text = re.sub(
            r"(?m)^\*\*" + pattern + r"\*\*[\s\S]*?(?=\n#{1,6}\s|\Z)",
            "",
            text,
            flags=re.IGNORECASE,
        )
    return text


def truncate_at_user_comments(text: str) -> str:
    """Remove scraped website Q&A / user comment blocks and everything after them.

    These appear in MarketsandMarkets reports as:
        ## Firstname
        Month, YYYY
        Comment text...

    The '## Name' heading is a higher heading level than the section that
    introduced the block, so normal section removal stops skipping too early.
    Instead, detect the characteristic (heading + date-line) signature and
    truncate there since real content never follows these blocks.
    """
    month_re = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*"
    match = re.search(
        rf"(?m)^## [A-Za-z]+\s*\n\s*\n{month_re},\s*\d{{4}}",
        text,
    )
    if not match:
        return text

    cut = match.start()
    # Walk back past any trailing blank lines
    while cut > 0 and text[cut - 1] in ("\n", " "):
        cut -= 1
    return text[:cut]


def truncate_at_footnote_block(text: str) -> str:
    """Remove the footnote-definition block and everything after it.

    Handles the Menlo-VC style where footnotes appear as a bullet list with
    ↩︎ back-reference markers, followed by author biographies — all at the
    very end of the file.
    """
    lines = text.split("\n")
    first_footnote_idx = None

    for i, line in enumerate(lines):
        if "↩︎" in line:
            first_footnote_idx = i
            break

    if first_footnote_idx is None:
        return text

    # Walk backward past any blank lines to find the clean cut point
    cut = first_footnote_idx
    while cut > 0 and lines[cut - 1].strip() == "":
        cut -= 1

    return "\n".join(lines[:cut])


def remove_inline_citations(text: str) -> str:
    """Remove bare superscript-style citation numbers embedded in prose.

    Targets two unambiguous patterns:
      1. A letter followed by a comma then 1-2 digit number then space:
         "industry,1 which" → "industry, which"
      2. A lowercase letter followed directly by a 1-2 digit number then space:
         "economy2 but"     → "economy but"

    Deliberately limited to 1-2 digits and lowercase context to avoid
    clobbering legitimate numbers (years, dollar amounts, percentages).
    """
    # Pattern 1: comma+number after a letter  (e.g. "study,3 found")
    text = re.sub(r"(?<=[a-zA-Z]),(\d{1,2})(?=\s)", ",", text)
    # Pattern 2: number glued directly to a lowercase word end (e.g. "margins5 ")
    text = re.sub(r"(?<=[a-z])(\d{1,2})(?=\s)", "", text)
    return text


def remove_misc_noise(text: str) -> str:
    """Remove one-off noise patterns."""
    # "*Backed by Company" attribution lines
    text = re.sub(r"^\*Backed by .+$", "", text, flags=re.MULTILINE)
    # "Retrieved from https://..." scraper artifact lines
    text = re.sub(r"^Retrieved from https?://\S+\s*$", "", text, flags=re.MULTILINE)
    # Marketing CTA lines ("Get 10% FREE Customization" etc.)
    text = re.sub(r"^.{0,80}FREE Customi[sz]ation.*$", "", text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r"^Get \d+% Free Customi[sz]ation.*$", "", text, flags=re.MULTILINE | re.IGNORECASE)
    # Standalone "Level" lines (scraping artifact in market dynamics sections)
    text = re.sub(r"^Level\s*$", "", text, flags=re.MULTILINE)
    # Publisher disclaimer notes often starting with "Disclaimer/Publisher's Note:"
    text = re.sub(r"^\*\*Disclaimer/Publisher.s Note:\*\*.*$", "", text, flags=re.MULTILINE)
    return text


def normalize_whitespace(text: str) -> str:
    """Collapse runs of 3+ blank lines to a single blank line."""
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_article(text: str) -> str:
    text = remove_boilerplate_sections(text)
    text = remove_bold_pseudo_sections(text)
    text = truncate_at_user_comments(text)
    text = truncate_at_footnote_block(text)
    text = remove_inline_citations(text)
    text = remove_misc_noise(text)
    text = normalize_whitespace(text)
    return text


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(INPUT_DIR.glob("*.md"))
    if not md_files:
        print(f"No markdown files found in {INPUT_DIR}")
        return

    total_orig = total_clean = 0
    for filepath in md_files:
        original = filepath.read_text(encoding="utf-8")
        cleaned  = clean_article(original)

        out_path = OUTPUT_DIR / filepath.name
        out_path.write_text(cleaned, encoding="utf-8")

        orig_lines  = len(original.splitlines())
        clean_lines = len(cleaned.splitlines())
        removed_pct = (1 - clean_lines / orig_lines) * 100 if orig_lines else 0
        total_orig  += orig_lines
        total_clean += clean_lines
        print(f"{filepath.name:20s}  {orig_lines:4d} → {clean_lines:4d} lines  ({removed_pct:4.1f}% removed)")

    overall_pct = (1 - total_clean / total_orig) * 100 if total_orig else 0
    print(f"\nTotal: {total_orig} → {total_clean} lines ({overall_pct:.1f}% removed)")
    print(f"Cleaned articles written to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
