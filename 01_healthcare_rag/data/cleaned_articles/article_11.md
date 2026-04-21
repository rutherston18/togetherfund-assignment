# Review ArticleLeading artificial intelligence–driven drug discovery platforms: 2025 landscape and global outlook

## Graphical abstract

## Abbreviations

## I. Introduction

2

,

11

,

26For example, Insilico Medicine’s generative–AI-designed idiopathic pulmonary fibrosis (IPF) drug progressed from target discovery to phase I in 18 months.

2

,

6

,

7

,

11

,27, 28, 29, 30 Meanwhile, AI algorithms are enabling more efficient lead optimization.

5

,31, 32, 33 However, despite accelerated progress into clinical stages, no AI-discovered drug has been approved yet, with most programs remaining in early-stage trials.34, 35, 36, 37 This raises the question: Is AI truly delivering better success, or just faster failures? A critical analysis is needed to differentiate concrete and realistic progress from the hype that surrounds AI technologies.38, 39, 40, 41

16

,

17

,42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 (2) Insilico Medicine,

11

,

27

,57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70 (3) Recursion,

48

,71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83 (4) BenevolentAI,

10

,

16

,

48

,

51

,84, 85, 86, 87, 88, 89, 90, 91, 92 and (5) Schrödinger.93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106 These platforms span a spectrum of AI approaches from generative chemistry and physics-based simulations to phenotypic screening and knowledge graph–driven target discovery (Fig. 2).

32

,107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128 A comparative summary table contrasts performance metrics such as discovery speed, cost efficiency, clinical pipeline size, and success rates. Finally, we discuss overarching regulatory and ethical considerations, including recent US Food and Drug Administration (FDA) and European Medicines Agency (EMA) guidance on AI in drug development, and challenges around transparency, explainability, data bias, and accountability.129, 130, 131, 132, 133, 134, 135, 136, 137, 138 By critically examining these developments, this review aims to provide a high-impact academic audience with a current, nuanced perspective on how AI is reshaping clinical-stage drug discovery worldwide.

5

,

139Although early examples appeared around 2018–2020, the past 3 years have seen a surge as both startups and pharmaceutical companies are embracing AI–driven discovery. The achievements and approaches of the 5 leading AI–driven drug discovery companies are described below.

### A. Exscientia: Generative design and the “Centaur Chemist” approach

46

,

48

,

140

,

141Its end-to-end platform combined algorithmic creativity with human domain expertise, a strategy coined the “Centaur Chemist” approach to iteratively design, synthesize, and test novel compounds.

142

,

143By integrating AI at every stage from target selection to lead optimization, Exscientia aimed to dramatically compress the design–make–test–learn cycle.

71

17

,

144Uniquely, Exscientia incorporated patient-derived biology into its discovery workflow, and it acquired Allcyte in 2021 to enable high-content phenotypic screening of AI-designed compounds on real patient tumor samples.

145

,

146This patient-first strategy helped ensure that candidate drugs are not only potent in vitro, but also efficacious in ex vivo disease models, improving their translational relevance.

#### 1. Platform progress and 2024–2025 updates

42

,

114

,

140Notably, in 2020, its algorithmically generated drug, DSP-1181 (Fig. 4), designed and developed in collaboration with the Japanese pharmaceutical company, Sumitomo Dainippon Pharma—became the world’s first AI-designed drug to enter a phase I trial for obsessive compulsive disorder.

147By 2023, Exscientia had designed 8 clinical compounds, both in-house and with partners, reaching development “at a pace substantially faster than industry standards.”

148These include candidates for immuno-oncology (eg, A2A receptor antagonist, EXS-21546),

16

,

149

,

150oncology, (cyclin-dependent kinase 7 [CDK7] inhibitor, GTAEXS-617, etc),

42

,

45

,

49

,

50and inflammation.

76

148The remaining internal focus is on a CDK7 inhibitor (GTAEXS-617) in a phase I/II trial for solid tumors, and a lysine-specific demethylase 1 (LSD1) inhibitor (EXS-74539; Fig. 4), which had an investigational new drug (IND) approval and a phase I trial initiated in early 2024.

148

148

,

151On the other hand, an A2A antagonist program (EXS-21546)152, 153, 154, 155 was halted after competitor data suggested that it would likely not achieve a sufficient therapeutic index.

148Exscientia also expanded its partnerships—for example, in September 2023, it initiated a new AI drug design collaboration with Merck KGaA (Germany) for €20 million, covering up to 3 targets.

44

,

76

,

114

,

148This adds to existing major alliances with ongoing multitarget deals, including Bristol Myers Squibb (BMS) and Sanofi, among others.

77

,

156

,

157

158Postmerger, Exscientia’s capabilities are being integrated to enhance the combined platform, for example, using Exscientia’s AI to generate novel compounds that Recursion can validate in phenotypic assays.

71

,

76

,

161

158In summary, Exscientia’s journey illustrates both the promise of AI design (multiple “fast-to-clinic” candidates and productive partnerships) and the challenges, namely pipeline pruning and a need to bolster biological validation, which the Recursion collaboration and deal seek to address.

#### 2. Clinical impact

42

,

140

,

162The true test will be whether these compounds show superior clinical outcomes or success rates versus conventionally discovered drugs. Nonetheless, the company’s reported metrics are impressive. For example, 1 program examining a CDK7 inhibitor achieved a clinical candidate after synthesizing only 136 compounds, whereas traditional programs often require thousands.

49

,

163

,

164This suggests that AI–driven efficiency gains can be achieved streamlining medicinal chemistry workflows.

77

,

165As Chief Executive Officer, Andrew Hopkins noted that the best way to create many novel medicines is to pair Exscientia’s design platform with strong partners.

44

,

148This supports the concept that AI is most powerful when augmented with domain expertise and robust experimental feedback loops.

### B. Recursion pharmaceuticals: High-throughput phenotypic discovery

82Instead of starting with a specific protein target, Recursion’s platform interrogates disease biology by systematically perturbing cell models and analyzing the results with computer vision and ML.

71

,

166

,

167At the heart of this technology is the Recursion operating system, an integrated system of automated wet-lab infrastructure and AI algorithms.

168

,

169

2

,

71

,

170Notably, high-content microscopy refers to a type of automated, computer-assisted imaging system that combines advanced microscopy with image analysis software to extract large amounts of quantitative biological data from cells or tissues.

171By comparing these profiles, Recursion’s AI can detect when a treatment rescues a disease-associated phenotype, even if the mechanism is unknown.

172This allows the platform to identify active molecules or genetic modifiers with therapeutic potential, yielding hits that a hypothesis-driven approach might overlook. It also generates massive relational datasets (Recursion has over 21 petabytes of image data, mapping trillions of gene and compound relationships).

173Recursion then follows up on these AI-generated leads with traditional validation, for example, identifying the compound’s target via proteomics and testing efficacy in animal models.

#### 1. Platform evolution and 2024–2025 updates

172A notable example is REC-994, a previously “shelved” compound identified by Recursion’s AI platform that reversed cellular defects in cerebral cavernous malformation, a rare neurovascular disease, and advanced to a phase II trial (Table 1).

71

,74, 75, 76

,

168Leveraging phenomics, the company also mapped genetic modifiers that rescue disease phenotypes to pinpoint and dissect promising targets.

71

,

76

| Compound | Target/Mechanism | Indication | Current Stage | Therapeutic Area |
|---|---|---|---|---|
| REC-617 | CDK7 inhibitor | Solid tumors | Phase I/II | Oncology |
| REC-1245 | RBM39 degrader | Solid tumors/lymphoma | Phase I | Oncology |
| REC-3565 | MALT1 inhibitor | B-cell malignancies | Preclinical | Oncology |
| REC-4539 | LSD1 inhibitor | Small-cell lung cancer | Phase I | Oncology |
| REC-994 | Superoxide scavenger | Cerebral cavernous malformation | Phase II (completed) | Rare disease |
| REC-2282 | Pan-HDAC inhibitor | Neurofibromatosis type 2 | Phase II | Rare disease |
| REV-102 | ENPP1 agonist | Hypophosphatasia | Preclinical | Rare disease |
| REC-4881 | MEK1/2 inhibitor | Familial adenomatous polyposis | Phase II | Rare disease |
| REC-3964 | Toxin B neutralizer | Clostridium difficile infection | Preclinical | Other |
| REC-4209 | Antifibrotic | IPF | Preclinical | Other |

158However, clinical successes were inconsistent. In the SYCAMORE phase II trial of REC-994 (SYCAMORE is the official name of the Phase II clinical trial NCT05085561 evaluating REC-994 for cerebral cavernous malformation), the compound met its primary safety endpoint but demonstrated only modest, nonsignificant trends toward reduced lesion volume on magnetic resonance imaging and improved modified Rankin scale scores at the highest dose, without clear patient- or physician-reported benefit. Although these results provided proof-of-concept for safety and exploratory efficacy, the lack of definitive clinical benefit ultimately led Recursion to discontinue the program.

71

,

74

,

77

,

158

75

,

158

,

174Similarly, another early program (REC-2282 for neurofibromatosis type 2; Table 1) was halted after phase II trials due to insufficient efficacy.

158

,

175

,

176These setbacks prompted Recursion to restructure its pipeline in 2024–2025, focusing on areas with stronger preliminary data.

71

,

158

,

165By mid-2025, the combined company identity narrowed to 6 active development programs, 4 in oncology and 2 in rare diseases.

72

,

77

,

158Several earlier programs were deprioritized, either discontinued or slated for out-licensing,

158as Recursion doubled down on opportunities where its integrated “data + AI” approach had the highest potential impact.

72

32In July 2023, it received a $50 million strategic investment from NVIDIA (a leading high-performance computing and graphics processing company widely used for AI model training) and began leveraging NVIDIA’s latest supercomputing hardware.

32

,

177

,

178By 2024, Recursion built BioHive-2, a dedicated AI supercomputer with 2 exaflops of performance (504 NVIDIA H100 graphics processing units) to train its models.

76

,

179This enabled the development of large “foundation models” on Recursion’s cell image data. For example, the Phenom model suite was trained on >3.5 billion images, learning generalizable representations of cellular biology.

173

,

179

*β*, was made available on NVIDIA’s cloud for external use.

179In 2025, Recursion open-sourced Boltz-2, a billion-parameter generative model for predicting protein 3D structure and ligand binding affinities, achieving near physics-accuracy, but 1000× faster.

180Boltz-2 was developed with the Massachusetts Institute of Technology and NVIDIA and was downloaded by over 40,000 users within weeks, demonstrating Recursion’s growing role as a cutting-edge AI research contributor.

180These efforts reflect Recursion’s vision of a “Virtual Cell,” namely a computational platform that can predict how complex biological systems will respond to interventions. Enhanced by Exscientia’s chemistry AI, Recursion can now not only find hits phenotypically but also design new molecules to exploit those insights.

32

,

71Already, the merged entity reported hitting a $7 million milestone from Sanofi in 2025, as that partnership advanced 4 programs to discovery milestones in just 18 months.

72

,

76

,

77

,

180Partnerships with Roche/Genentech (neuroscience, oncology) and Bayer (undruggable targets) are also continuing and are yielding vast datasets, such as a trillion-cell clustered regularly interspaced short palindromic repeats phenotypic map for neuroscience (Table 2).

180

,

181

| Partner | Nature of Partnership/Value Proposition | Representative Drug/Program (Publicly Disclosed) |
|---|---|---|
| Bayer | Precision oncology collaboration for up to 7 programs; potential value ≈ $1.5 billion + royalties. | REC-617 (CDK7 inhibitor; Recursion) |
| Roche/Genentech | Neuroscience and oncology collaboration: ∼US$150 million upfront, up to 40 programs, >US$12 billion potential value. | REC-4881 (MEK1/2 inhibitor for FAP; Recursion) |
| Exscientia (Acquisition) | Recursion acquisition of Exscientia (∼US$688 million) to integrate precision chemistry and expand pipeline. | Not publicly disclosed |
| Sanofi and Merck KGaA | Access via Exscientia/Recursion, immunology and oncology collaborations. | Not publicly disclosed |
| NVIDIA | Technology infrastructure partner (BioHive-2 compute platform). | Not applicable |
| Google Cloud/Helix/Faro Health | Technology/data ecosystem for platform scale-up. | Not applicable |

165

,

180includes oncology (CDK7 inhibitor REC-617 in phase I/II; RBM39 degrader REC-1245 in phase I/II) and rare disease (eg, REC-4881 for familial adenomatous polyposis in phase II) and highlights key partnership programs with Roche, Sanofi, Bayer, and Merck KGaA (Table 2). The merger has created a diversified pipeline with multiple near-term readouts.

#### 2. Reflections

71The decision to merge with Exscientia underscores that combining strengths does provide a path forward. In this case, Recursion gained cutting-edge generative chemistry and several clinical-stage compounds, whereas Exscientia’s programs benefited from Recursion’s biological expertise and infrastructure.

158

,

165This convergence of AI capabilities with biological expertise is a broader trend across the field.

158An improved success rate, or even a single breakthrough within the next 2 years, could be highly impactful in validating the phenomics-driven paradigm. Furthermore, as in other areas of the pharmaceutical sector, conceptualization, execution, and translation are highly capital-intensive, requiring sustained financing to maintain progress.

180The company’s strong financial position (over $500 million in cash as of mid-2025)

180and backing from tech investors such as NVIDIA indicate confidence that this data-heavy approach could pay off. Nonetheless, Recursion exemplifies the “TechBio” model: a synergy of big data, high-performance computing, and biology, betting that smart algorithms can uncover therapies that humans alone might miss.

182

,

183

### C. Insilico Medicine: End-to-end artificial intelligence and generative successes

184

,

185Its comprehensive Pharma.AI platform comprises interconnected modules: PandaOmics for AI-powered target identification (mining omics and literature for novel disease drivers), Chemistry for generative molecule design, and InClinico for clinical trial outcome prediction (Table 3).

6

,

168

,

186

,

187Using this “toolkit,” Insilico seeks to both discover first-in-class targets and generate drug candidates against them, a “full-stack” AI approach.

| Category | Details |
|---|---|
| Platform | Pharma.AI suite: PandaOmics (target ID), Chemistry (generative design), InClinico (trial prediction); ChatPandaGPT (2023). Incorporates AlphaFold and quantum computing into workflows. |
| Lead program IPF | ISM001-055 (Rentosertib, TNIK inhibitor):(i) Target prioritized 2019; candidate generated in ∼18 mo. (ii) Multinational phase 0–II (2022–2025). (iii) China phase IIa (2024): 12-wk placebo-controlled; safe, dose-dependent forced vital capacity improvement (+98 mL at 60 mg vs –20 mL placebo).(iv) Published in Nature Medicine (June 2025). (v) United States Adopted Names name Rentosertib approved March 2025. (vi) Phase IIb/III planned in the fourth quarter of 2025. |
| Other clinical programs | (i) ISM3312: immunomodulator for COVID-19/viral infections; phase I completed 2024 (safe).(ii) ISM3091: USP1 inhibitor for cancer; IND approval 2023, entering phase I. |
| Preclinical programs | (i) TEAD inhibitor (solid tumors); other fibrosis/oncology /immunology assets. (ii) Reported 100% IND success rate (no AI-designed preclinical candidates terminated before trials). |
| Funding and partnerships | (i) Sanofi deal (2022): multi-target, up to $1.2 billion. (ii) Series D (2022): $95 million. (iii) Series E (2023): $110 million. (iv) >20 preclinical programs across multiple disease areas. |
| Significance | (i) First fully AI-developed drug (Rentosertib) to reach phase II. (ii) Proof-of-concept that AI can deliver a novel target and drug with early efficacy. (iii) Risks remain: first-in-class targets historically have lower late-stage success. |

188

,

189A signature achievement came in 2021–2022, when Insilico’s AI system identified a novel fibrotic disease target, the enzyme TNIK, for IPF. It then generated a small-molecule TNIK inhibitor (ISM001-055; now Rentosertib; Fig. 5) against that target.

2

,

8

,

11

,

190This program advanced from an AI–driven hypothesis to a clinical candidate in about 18 months,

2

,

30making it one of the first examples of an AI-discovered target and AI-designed molecule entering human trials.

188

#### 1. Pipeline and 2024–2025 progress

11

,

191In 2023, Insilico initiated parallel phase IIa trials of ISM001-055 in IPF patients in China and the United States.

28

,

190

,

192

,

193The China phase IIa trial in 2024 consisted of a 12-week, placebo-controlled readout that led to positive results (Table 3). In fact, the drug met its primary safety endpoint and demonstrated a dose-dependent improvement in lung function at the highest dose, whereas placebo patients continued to decline.

194Specifically, a 60 mg dose of Rentosertib daily led to a +98 mL mean increase in forced vital capacity versus a −20 mL decline on placebo over 3 months (Table 3).

11

,

28

*Nature Medicine*in June 2025.

11Hence, targeting TNIK appears safe and may provide benefit, warranting larger and longer trials.

11Insilico is now planning late-stage trials for IPF (potentially phase IIb/III) to start by the fourth quarter of 2025 (Fig. 5).

28Notably, in March 2025, the United States Adopted Names Council officially approved “Rentosertib” as the nonproprietary generic name for the drug previously known by its code, ISM001-055, underscoring its maturity as a drug candidate (Fig. 5).

195

60

,196, 197, 198 Another is an AI-designed USP1 enzyme inhibitor for cancer (ISM3091), which received IND approval in 2023

196

,

199

,

200and is entering phase I. Insilico has also generated preclinical candidates for oncology applications, for example, a pantranscriptional enhancer activator domain family of transcription factor (TEAD) inhibitor for solid tumors

196and other diseases.

196

,

201and, in 2023, it launched a generative biology tool (“ChatPandaGPT”) for automating hypothesis generation.

187

,

196

,

202

168

,

196under which Sanofi is leveraging Insilico’s platform to discover new targets and molecules for up to 6 diseases. Additionally, Insilico closed a $95 million Series D in 2022 and a $110 million Series E capital-raising financing round in 2023 to fund its pipeline expansion.

168With these resources, Insilico now boasts 20+ preclinical programs spanning fibrosis, oncology, immunology, etc, many aiming at first-in-class targets.

#### 2. Outlook and significance

11The TNIK inhibitor for IPF is particularly noteworthy as it introduced a completely new target for a difficult-to-treat disease via AI.

194If Rentosertib ultimately succeeds in late-stage trials, it could become the first AI-discovered drug to market, potentially in the later years of this decade.

11Even now, the early success of AI has energized the industry. In fact, 1 commentary noted that Insilico’s IPF program represents a “proof-of-concept success for AI–driven drug discovery.”

194

,

203That said, challenges remain.

139

,

204

,

205although the sample size remains small and long-term outcomes past phase II are not yet proven.

2Insilico’s comprehensive approach, which unifies target discovery, chemistry, and clinical design AI, also exemplifies a trend of platform convergence, where AI companies aim to own the whole value chain.

196establishing Insilico as a key player. The company is leading the charge in AI in drug discovery into its next phase, and delivering not just candidates faster, but potentially effective drugs to patients.

### D. BenevolentAI: Knowledge graphs, repurposing, and a cautionary tale

188

,

206

,

207Its platform centers on a vast knowledge graph that integrates scientific literature, biomedical databases, omics data, and clinical information (Fig. 6).

208

,

209By applying natural language processing and graph ML, BenevolentAI’s system can propose novel links between genes, diseases, and compounds that might not be obvious to human researchers.

208

,

210

,

211The goal is to generate hypotheses for either new targets in disease or new uses for existing drugs.

26

,

215This demonstrated the power of AI–driven repurposing, especially in an urgent scenario.

#### 1. Pipeline and 2024 updates

5

,

209

,

211

,

216By 2022, it had advanced at least 2 novel small molecules into the clinic: BEN-2293 (Table 4), a topical pan-Trk inhibitor for atopic dermatitis (eczema), and BEN-8744, an oral PDE10 inhibitor for ulcerative colitis.

10

,

90

,

186Unfortunately, these programs highlight the risks and realities of AI-hypothesized biology.

39

,

87

| Program | Target/Mechanism | Indication | Phase/Status |
|---|---|---|---|
| BEN-8744 | Phosphodiesterase 10 (PDE10) inhibitor | Ulcerative colitis | Phase Ia completed (safe) → phase I dosing underway |
| BEN-2293 | Pan–tropomyosin receptor kinase (Pan-Trk) inhibitor | Atopic dermatitis (eczema) | Phase IIa completed (efficacy not met) |
| BEN-28010 | Checkpoint kinase 1 (CHK1) inhibitor | Glioblastoma multiforme | Preclinical; IND-ready (to partner/out-license) |
| BEN-34712 | Retinoic acid receptor (RAR) α/β agonist | ALS | IND-enabling stage; partnering active |
| Others | Various novel targets | Multiple (eg, Parkinson’s, fibrosis) | Early-stage/preclinical; evaluated for advancement |

89

186

16

,

51

,

197

,

217PDE10 was a novel target for inflammatory bowel disease suggested by Benevolent’s platform, and if this agent shows efficacy in upcoming phase II trials, it would vindicate the approach. BenevolentAI also has preclinical programs, such as an amyotrophic lateral sclerosis (ALS) project implementing a RAR-

*α*/

*γ*agonist that is in partnership discussions.

218However, due to the mixed outcomes and a challenging funding climate, 2023–2024 was a turbulent period for BenevolentAI.

219

,

220The company de-emphasized venturing into late-stage drug development alone and instead prioritized offering its AI capabilities in partnership with others earlier in development to mitigate balance-sheet risk and extend its cash runway into late in the third quarter of 2025.

219

221By late 2024, the company even contemplated delisting from the Amsterdam exchange and going private as it restructured and extended its cash runway into 2025 by cutting costs.

219

222In September 2023, Merck KGaA also signed a 3-target deal with BenevolentAI (in parallel with 1 with Exscientia) with up to $594 million in milestones.

219These partnerships provide external validation and potential upside if partnered programs succeed.

#### 2. Analysis

85It demonstrated how AI–driven knowledge mining can yield real results; the baricitinib success likely saved many lives in the pandemic.

212

,

213

,

223It also advanced new pharmacology, for example, PDE10 in colitis, etc, that might still yield benefits.

16

,

51The company’s struggles underscore key challenges for AI drug hunters, with the quality of input data being a critical factor. It is well known that AI predictions are only as good as the evidence base; significant gaps or biases in the biomedical literature can mislead AI models.

219Even a correctly identified target may require optimal pharmacological intervention.

114

### E. Schrödinger: Physics-based simulation meets machine learning

100

,

190

,

224

,

225Schrödinger’s core technology is a physics-based molecular simulation platform, which for decades has been used in structure-based drug design, for example, virtual screening and free-energy calculations for binding affinity (Fig. 7).

226

,

227Around 2018, Schrödinger began pairing these physics-based methods, like docking and molecular dynamics, with modern ML algorithms to enhance predictive power.

228The result is a “digital chemistry” platform that can design and optimize small molecules with high precision, provided a clear target structure is available.

10

| Year | Milestone |
|---|---|
| 1990 | Founded in New York |
| 2017 | Multi-target collaboration with Takeda |
| 2020 | IPO raised ∼$202 million (Nasdaq: SDGR) |
| December 2022 | Takeda agrees $4 billion upfront acquisition of Nimbus Tyrosine Kinase 2 (TYK2) program (up to $2 billion more in milestones) |
| February 2023 | Acquisition closes: Schrödinger receives $111 million (with $36 million more forthcoming) |
| 2022–2023 | Internal oncology programs enter phase I (MALT1, CDC7, and WEE1) |
| 2023 | Partner expansions: BMS and Otsuka (neurology/central nervous system targets) |
| 2024 | Novartis collaboration: $150 million upfront + up to ∼$2.3 billion milestone potential |
| 2025 | Expected phase I data readouts for internal oncology programs |

229Importantly, Schrödinger has a dual business model; it sells its software to pharma and biotech companies, which is a profitable segment that funds its research and also pursues an internal drug pipeline via collaborations and proprietary programs.

100This strategy provides financial stability and a breadth of real-world data from many users’ projects to “feed” its AI models.

99

10

,

100

,230, 231, 232 This agent is now in phase III clinical trials and could become one of the first approved AI-influenced drugs.

2checkpoint kinase/membrane-associated tyrosine- and threonine-specific cdc2-inhibitory kinase dual inhibitor) for solid tumors (Table 5).

93

,

94

,

97

,233, 234, 235

233Early indications are promising, with SGR-1505 demonstrating potent target suppression in lymphoma, and SGR-2921 achieving pharmacologically relevant exposures in acute myeloid leukemia patients with a manageable safety profile. Formal data readouts are expected later.

96

,

100

,

233Schrödinger is also advancing preclinical candidates, such as the Son of Sevenless homolog 1 inhibitor, SGR-4174, to target RAS-driven cancers, which showed strong tumor inhibition in models.

98

,

233In the fourth quarter of 2024, the company’s collaborative ethos continued with it expanding a drug discovery collaboration with Eli Lilly, adding a new target to an ongoing project.

100

,

236

,

237

96

,

100Collaboration revenue from upfronts and milestones is expected to grow to $45–$50 million in 2025.

236These outcomes suggest its partners are advancing its pharmaceutical programs successfully. As 1 example, Schrödinger earned $5.7 million from a Novartis collaboration in the first quarter of 2025, likely representing payments for a drug development program achieving a lead optimization milestone.

233

238The company developed a proprietary predictive modeling suite for absorption, distribution, metabolism, excretion, and toxicity, which aligns with the FDA’s initiative to reduce animal testing by using computational methods.

233

,

239In 2025, it published a

*Nature Communications*article on a novel AI–driven crystal structure prediction method that addresses polymorph risk in formulation.

233

,

240Schrödinger’s use of deep learning for hit generation was evidenced by a late 2023 achievement using generative models to design a series of CDC7 kinase inhibitors that progressed rapidly to the clinic.

96

,

233

233Although still operating at a net loss due to heavy R&D investment, its operating expense outflow is modest relative to its peers, and it had over $500 million in cash, boosted by a 2021 Initial Public Offering to fund its pipeline.

#### 1. Perspective

188

,

241Its decades of domain experience in computational chemistry gave it credibility and a solid knowledge base to build upon with AI. This likely contributed to its higher success rate in generating viable clinical candidates. Many of its partnered programs have succeeded in development, and none of its internal programs have failed clinically yet, although they are early.

238In areas like those, companies like Recursion or BenevolentAI have an edge. Thus, Schrödinger has largely tackled targets that are already genetically or biologically validated, such as MALT1 and WEE1, and optimized chemistry to achieve best-in-class molecules.

242

243No Schrödinger-originated drug has been approved yet, but the results in the near future could change that if partners like Nimbus/Takeda succeed in phase III trials. Schrödinger’s business model, featuring a profitable software arm and investments in drug discovery, also offers a sustainability that pure-play biotech startups lack. It essentially allowed the company to be patient and scientifically rigorous, without the same level of risk and pressure for immediate clinical success. The company frequently emphasizes maintaining “scientific leadership” and rigorous validation. For instance, it engages with regulators on advancing in silico methods, commenting on FDA initiatives for modeling in R&D.

233

242If so, it would validate not just the idea of AI speeding up drug discovery but also improving clinical success rates by crafting better drugs.

### F. Comparative summary

11

,

44

,

52

,71, 72, 73

,

76

,

77

,

165

,

212

,

213

,

244

,

245provides a side-by-side comparison of their platforms, achievements to date, and challenges.

| Company | Target/Mechanism | Clinical Trial Identifier | Discovery Speed | Cost Efficiency | Partnerships | Core AI Approach | Main Challenges | References |
|---|---|---|---|---|---|---|---|---|
| Exscientia (EXS-21546) | A2A receptor antagonist | NCT04727138/NCT05920408 | Reduced lead optimization cycle >10× faster than conventional | Estimated ∼70% cost reduction | Sanofi (2022 collaboration) | Active-learning reinforcement loop (AI-driven design) | Translational predictivity for immune oncology | 44,52 |
| BenevolentAI (BEN-2293) | TRK A/B/C inhibitor for atopic dermatitis | EUCTR 2020-003143-28-GB (phase IIa trial) | Hit-to-lead <18 mo | Moderate cost savings via knowledge graph | AstraZeneca AI collaboration | Biomedical knowledge graph + machine reasoning | Data integration and target validation depth | 212,213 |
| Insilico Medicine (INS018_055 (ISM001-055)) | TNIK inhibitor for IPF | NCT05938920/NCT05975983 | First AI-discovered drug to phase I in <18 mo | ∼50% reduction in early-stage cost | Fosun Pharma and EQRx | End-to-end generative biology and chemistry pipeline | Scalability of generative models for new targets | 11,244 |
| Recursion Pharmaceuticals (REC-2282 and REC-994) | HDAC inhibitor/superoxide scavenger | NCT04624794/NCT05010200 | Rapid phenotypic screening via BioHive-2 graphics processing unit | Reduced wet-lab iteration costs | Bayer (2020 partnership) | AI-enabled phenomics and image-based screening | High data volumes require advanced QC | 71, 72, 73,76,77,165 |
| Schrödinger (SGR-1505) | MALT1 inhibitor for B-cell malignancies | NCT05544019 | Hybrid physics–AI accelerated lead optimization | ∼2× cost saving vs traditional pipeline | BMS strategic partnership | FEP + ML for free-energy prediction | Model generalizability across target classes | 245 |

## II. Emerging players and global developments (2024–2025)

### A. Insitro (USA)

172

,

246

,

247The company generates high-throughput functional genomic data, for example, clustered regularly interspaced short palindromic repeats-edited induced pluripotent stem cell–derived cells modeling disease, and applies AI to identify targets predictive of patient outcomes.

168

,

248Insitro’s approach bridges in vitro models and in silico analysis, yielding insights into diseases like nonalcoholic steatohepatitis (NASH) and ALS.

249

,

250

168BMS (since 2020, a $25 million milestone in 2022 for discovering a novel ALS target),

168and most recently Eli Lilly (2023) to find targets for metabolic diseases including metabolic-associated fatty liver disease.

168

251The company’s significance lies in its methodological innovation, as it is a leader in phenotypic AI (like Recursion), but uses human-induced pluripotent stem cell models and genetics to ensure relevance. If Insitro’s collaborations yield drug candidates, for example

*,*Gilead has an Insitro-discovered NASH target advancing in preclinical studies,

168

,

251it will validate this data-driven target discovery approach. Insitro’s work underscores a broader trend of AI+lab integration and exemplifies the West Coast US influence that integrates Silicon Valley AI with cutting-edge biology. It is anticipated that Insitro will announce its first clinical candidate in the near future, potentially marking another milestone for AI in drug discovery.

### B. Isomorphic Labs (UK)

114

,252, 253, 254 Isomorphic Labs builds upon AlphaFold, the revolutionary protein-folding AI, and other advanced AI techniques such as deep and reinforcement learning to model biological problems.

114

,

168

168Rather than focusing on a single pipeline, Isomorphic Labs positions itself as a platform to solve “the toughest challenges in biology and chemistry” with AI. In early 2024, it announced 2 landmark collaborations (Eli Lilly and Novartis) that could be worth nearly $3 million in milestones.

168

,

255These deals involve Isomorphic’s AI working on de novo small-molecule discovery for targets selected by these pharmaceutical companies.

168

,

255Such hefty deals signal big pharma’s strong interest in Big Tech’s AI prowess. Isomorphic Labs is also notable for its global talent, including Demis Hassabis, the cofounder of DeepMind, who leads the strategic vision, as well as top computational biologists and medicinal chemists recruited from industry.

253Although Isomorphic has not disclosed specific drug compounds as yet, there are reports that it aims to have at least 1 AI-designed molecule in clinical trials by late 2025.

2

,

256If achieved, that would mark the entry of big technology companies directly into drug development.

### C. Atomwise (USA)

168

,

260

,

261

262After years of providing services and partnerships, Atomwise achieved a milestone in late 2023 by nominating its first internal development candidate, an AI-discovered TYK2 inhibitor for autoimmune disease.

168

,

263

,

264This orally bioavailable, allosteric TYK2 inhibitor demonstrated promise in preclinical models for systemic lupus erythematosus, psoriasis, and inflammatory bowel disease and is slated for clinical trials in 2024.

48

,

168In April 2024, the company published results of a study screening 318 targets with AtomNet, finding novel hits for 235 of them, showcasing AI’s breadth as an alternative to high-throughput wet screening.

168Atomwise’s progress is significant, as it validates the longevity of AI drug startups after a decade of R&D. It is finally entering the clinic, potentially achieving success by being among the first wave of AI-originated small molecules to be tested in humans. Its work also highlights the continuing importance of structure-based methods in the AI “toolkit” and discovering how combining AI with the enormous virtual chemical space can yield drug candidates that might be missed by human-led discovery.

### D. XtalPi and Chinese artificial intelligence biotech companies (China)

265

,

266It raised hundreds of millions of dollars, including investment from Tencent and SoftBank, and has struck deals with Western pharmaceutical companies.

267and in 2024, announced a landmark codevelopment partnership with a US pharma, DoveTree. The latter partnership was worth up to $6–$10 billion for multiple AI-designed drug candidates.

267

,

268Similarly, the Chinese pharma giant, China Shijiazhuang Pharmaceutical Group (CSPC), struck a deal worth more than US$5 billion with AstraZeneca in mid-2025, granting AstraZeneca access to CSPC’s AI-discovered oncology portfolio.

267These latter developments represent some of the largest AI–pharma deals on record.

267These developments signal a globalization of AI drug discovery with Chinese AI biotechnology companies now supplying innovative drug candidates to multinational pharmaceutical companies, not just generic agents. Factors such as fast timelines, lower costs, and strong national support make China an emerging AI powerhouse.

267In the first quarter of 2025, Chinese companies accounted for 32% of global biotech company licensing deal value (up from ∼21% in 2023), reflecting this momentum.

267The international implication is significant, whereas the US still leads in the number of AI drug startup companies and venture capital funding, China’s combination of talent, consisting of many AI scientists and its sheer scale, is positioning it as a major player. It also raises the competitive bar with collaborations like Pfizer-XtalPi, which was expanded in 2023,

267suggesting that Western pharmaceutical companies see their respective Chinese AI counterparts as equal partners. Thus, the global AI drug discovery ecosystem is becoming more interconnected, with cross-border deals and a race to claim first drug approvals.

### E. Big pharma’s internal efforts and smaller artificial intelligence startups

168

,

272In Europe, companies like Iktos (France) combine AI with robotics for automated discovery, recently securing EU grants and partnerships to validate a fully AI-driven, automated chemistry platform.

168

### F. Artificial intelligence in biologics and new therapeutic modalities

186

,

314By 2025, several AI-designed antibodies had entered phase I trials, such as Generate Biomedicines’ inhaled antibody for asthma and chronic obstructive pulmonary disease, which showed superior affinity and half-life compared with parent molecules, enabling dosing every 6 months instead of monthly.

114

,

188Chinese startup Helixon signed a landmark US$1.7 billion licensing deal with Sanofi in 2025 to deliver AI-generated antibodies, reflecting both technical maturation and global market interest.

315

316

,

317Its discovery used AI-assisted sequence optimization and structure-stability modeling to enhance catalytic efficiency and resilience in gastrointestinal conditions. SKYCovione (GBP510), a computationally designed protein nanoparticle COVID-19 vaccine developed by SK Bioscience in collaboration with the University of Washington’s Institute for Protein Design, received regulatory approval in South Korea and a WHO Emergency Use Listing.318, 319, 320 These cases highlight the growing clinical validation of AI-designed biologics.

321These advances extend AI’s impact beyond traditional chemistry, showing its expanding role in shaping the next generation of biologics. The key challenge remains translating computational designs into clinically validated therapies, but the progress of programs such as TAK-062, SKYCovione, and AI-designed antibodies suggests that biologics could soon rival small molecules in productivity and therapeutic reach.

322

### G. Global and non-Western pharmaceutical artificial intelligence innovation

114

,

323Sanofi’s $1.7 billion antibody licensing deal with Helixon underscores China’s strength in AI-designed biologics.

324

114

,

325

,

326Governments are also playing key roles; China’s state support has accelerated domestic AI biotech, whereas the UK and EU have backed public–private partnerships such as MELLODDY for data-sharing in ML. This geographic diversification shows that AI innovation is increasingly multipolar, with cross-border collaborations shaping the field’s trajectory.

## III. Regulatory and ethical considerations in artificial intelligence–driven drug discovery

130

,

327

,

328These efforts aimed to balance innovation with accountability, addressing concerns around transparency, bias, and explainability of AI systems.

### A. Regulatory guidance

329This guidance, titled “Considerations for the Use of AI to Support Regulatory Decision-Making,” outlines the FDA’s expectations for sponsors who incorporate AI-derived results in their submissions.

329A key element is a “risk-based credibility assessment framework,” where companies must demonstrate the reliability and credibility of an AI model for its intended context of use.

329In practice, this means providing detailed documentation of the model’s development, the source data used for its training, its performance metrics, and any limitations.

329Regulators want to know, for instance, if a model that prioritized a target was trained on comprehensive and unbiased data or if a predictive toxicology model was validated on the relevant chemical space. Transparency in data provenance is emphasized to build trust in AI outputs. The FDA also encourages early dialogue and invites companies to engage with the agency early when planning to use AI, given that this is “new territory for the FDA, too.”

329

330the EMA released a Reflection Paper in 2024 on AI in the medicinal product lifecycle. The EMA report similarly highlights principles like General Data Protection Regulation-compliant data handling, algorithmic transparency, and the need for human oversight in AI–driven processes.

330Additionally, the EU is moving forward with the broad EU AI Act, which could classify certain AI applications in drug development as “high risk” and impose requirements for traceability and risk management (although the Act is not finalized as of 2025). Both the FDA and EMA appear aligned in seeking clear documentation and justification for AI use. For instance, companies should explain how an AI model arrived at its recommendation (to the extent possible), and how they mitigated risks like model bias or drift.

### B. Transparency and explainability

329

329This approach helps assign accountability and ensures that AI suggestions undergo expert scrutiny. In the longer term, advances in explainable AI for life sciences may provide more interpretable models. For instance, algorithms that highlight which biological features or data points most influenced their output. Until then, rigorous validation and cross-checking of AI results with experimental data are the principal mechanisms to build confidence in the predicted drug molecules.

### C. Data bias and fairness

334For example, an AI trained primarily on European genomic data might overlook targets relevant to Asian or African populations. Regulators and ethicists have therefore raised concerns about ensuring adequate population diversity in training datasets.

335

336

,

337In response, companies are increasingly assembling diverse datasets, for example, Recursion is integrating patient data from multiple sources,

180or knowledge graph models incorporating global research literature to avoid parochial views. Some AI biotechnology companies have put in place internal “ethics boards” to review algorithmic choices. For instance, avoiding using socioeconomic or race variables in models unless clinically justified, to prevent algorithmic discrimination in issues like trial recruitment.

### D. Accountability and validation

338

,

339In drug discovery, consider an AI-recommended compound that later fails due to toxicity.

16In this case, is it the fault of the AI or the scientists who chose to trust it? Legally, the responsibility currently lies with the drug sponsor (the company) just as with any other drug. However, to uphold this, sponsors must maintain strict validation practices.

2In practice, most AI-driven companies already do this, as observed with BenevolentAI’s extensive lab work or Recursion’s phenotypic validations. The difference is volume and speed; AI can quickly generate many hypotheses, so ensuring quality control and focusing on the right ones is critical. Some ethicists have floated the idea of an AI “audit trail” keeping logs of how an AI system was used in decision making for a drug, so that if something goes wrong, for example, unforeseen toxicity, 1 can trace back whether any algorithmic signals were missed or misinterpreted. This could be part of regulatory submissions in the future that may include, for instance, providing model output logs.

### E. Another aspect of accountability is in clinical trials

329

### F. Intellectual property and privacy

340Boltz-1 (2024),

341and Chai-1 (2025).

342In parallel, frameworks such as DeepChem (2023)

343and RDKit (2024)

344exemplify the growing movement toward open science in AI–driven molecular discovery and cheminformatics. In contrast, black-box proprietary models might hide important scientific insights and stifle development. In the future, regulators might lean toward approaches that share results openly for collective learning on what experimental drugs work or fail.

2but maintaining rigorous oversight is essential to ensure that speed does not come at the cost of patient safety or scientific soundness.

329The task now is to implement those safeguards in a pragmatic way. We can expect continual refinement of guidelines as more AI-designed drugs enter late-stage trials and approvals. Each case will provide lessons on what level of transparency or evidence is needed. Ethically, the biopharmaceutical industry appears to be committed to using AI responsibly, recognizing that public and regulatory trust must be earned through openness and proven results.

## IV. Robotics artificial intelligence in pharmacology: From “Hands-On” to “Self-Driving” discovery

345

,

346Emerging initiatives exemplifying this convergence of AI and robotics are outlined below.

### A. AstraZeneca iLab (Gothenburg)

### B. Recursion (Salt Lake City)

### C. Insitro (South San Francisco)

350

### D. Emerald Cloud Lab

351

### E. Wyss Institute “Interrogator” (multi-organ-on-chips)

352

### F. Atinary and Chemspeed

### G. Autonomous mobile “robo-pharmacologist”

356The convergence of robotics and AI will redefine pharmacology by transforming experimentation into a closed-loop, data-driven process. Across industry and academia, autonomous platforms will, in the near future, compress the timescale needed for DMTA cycles, run reproducible experiments at scale, and generate high-fidelity datasets that fuel predictive models. These advances extend beyond the current high-throughput gains of AI to enable new capabilities such as remote-access discovery in cloud laboratories, translational insight from robotic multiorgan systems, and adaptive optimization through the integration of AI and robotics.

361These systems integrate computer vision, large language model (LLM) reasoning, and precision motion control to autonomously execute assays, maintain cell cultures, and handle reagents with minimal supervision.362, 363, 364, 365

370

## V. Conclusions and outlook

2

,

139However, we do not yet have evidence that AI-derived drugs have higher phase II/III success rates. Early phase II data are limited and similar to industry averages, namely ∼30%–40% success in phase II.

2It will take the next 3–5 years, as dozens of these programs reach proof-of-concept trials, to know if AI’s smarter choices translate into higher efficacy or lower late-stage attrition.

180This could accelerate innovation globally, and regulators might even encourage the use of validated open models to avoid duplication of effort. An excellent example is that AlphaFold for structural modeling is now standard.

131

,

371As AI-designed drugs enter patients, communicating how they were discovered and why they are believed to work will be important for public trust. Interestingly, AI’s entrance has reignited discussions on “mechanism versus empirical” drug discovery. Phenotypic AI might find a drug without a known mechanism, but will physicians and patients be comfortable using a treatment if “an AI found it,” but we are not entirely sure how it works? Historically, many drugs have been used effectively before their mechanisms were dissected (eg, aspirin), but the bar is higher now for explanation.

*Nature Medicine*,

11whereas Recursion and Exscientia scientists are publishing datasets and methods. This academic rigor and peer review will help validate AI approaches in the broader scientific community.

### A. Global implications

372

,

373with major contributions from the United States, United Kingdom, European Union, China, and other regions.

374Cross-collaboration between Western pharmaceutical companies and Eastern AI firms has created a more networked R&D ecosystem.

267Regulatory bodies such as the FDA and EMA are already coordinating on AI oversight, whereas Japan’s Pharmaceuticals and Medical Devices Agency

375and China’s National Medical Products Administration

376are closely following these developments. This convergence is laying the groundwork for international harmonization of AI-based regulatory standards.

#### 1. Near-term implications

377Strategic partnerships between established pharmaceutical companies and AI startups are likely to dominate this phase, expanding data-sharing frameworks and driving early regulatory adaptation. Developing countries could begin to “leapfrog” traditional R&D constraints by adopting open-source AI tools and cloud-based platforms, increasing their participation in global drug discovery.

#### 2. Long-term implications

378This evolution will depend on sustained investment in digital infrastructure, ethical data stewardship, and transparent validation practices across borders.

### B. Real-world impact and outcomes (2018–2025)

379Notable successes include Insilico Medicine’s TNIK inhibitor Rentosertib for IPF, which showed positive phase IIa efficacy signals, and Nimbus/Takeda’s TYK2 inhibitor, now in phase III, which may become the first AI-influenced approved drug.

11However, failures have also occurred, with BenevolentAI’s pan-Trk inhibitor (BEN-2293) failing in a phase IIa eczema trial,

186and Recursion’s cerebral cavernous malformation program (REC-994) showed limited efficacy in phase II.

74

380These outcomes suggest that AI is indeed accelerating early-stage discovery and improving efficiency, but it has not yet overcome the fundamental biological hurdles of later-stage development. The mixed record highlights both progress and remaining challenges, underscoring the importance of rigorous validation.

### C. Integration of large language models in drug discovery

381Insilico’s “ChatPandaGPT” exemplifies this trend, whereas academic initiatives like ChemCrow and Geneformer show that LLMs can propose synthetic routes, predict reaction outcomes, and uncover new therapeutic targets from genomic datasets.

186

,

187

382Although their outputs still require expert curation, the ability of LLMs to synthesize unstructured biomedical knowledge represents a paradigm shift. Moving forward, convergence of LLMs with multimodal AI (integrating omics, structure, and clinical data) could make them indispensable in discovery pipelines, supporting transparency, explainability, and speed.

383

,

384

## Financial support

## Data availability

## CRediT authorship contribution statement

**Mahendiran Dharmasivam:**Conceptualization, Software, Investigation, Figures, Writing – original draft, Writing – review and editing.

**Busra Kaya:**Writing – review and editing.

**Adedoyin Akinware:**Writing – review and editing.

**Mahan Gholam Azad:**Writing – review and editing.

**Des R. Richardson:**Supervision, Writing – review and editing.

## Cited by (5)

### The isoflavone metabolites, O-desmethylangolensin and (S)-equol, relax isolated arteries ex vivo and decrease arterial blood pressure in vivo

2026, Biochimica Et Biophysica Acta Molecular Basis of Disease### Artificial intelligence–assisted drug discovery in 2025: Faster, but is it better? The robots are coming, look out!

2026, Pharmacological Reviews### Novel Compounds as MALT1 Inhibitors for Treating Cancer

2026, ACS Medicinal Chemistry Letters