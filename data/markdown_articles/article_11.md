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

185Its comprehensive Pharma.AI platform comprises interconnected modules: PandaOmics for AI-powered target identification (mining omics and literature for novel disease drivers), Chemistry42 for generative molecule design, and InClinico for clinical trial outcome prediction (Table 3).

6

,

168

,

186

,

187Using this “toolkit,” Insilico seeks to both discover first-in-class targets and generate drug candidates against them, a “full-stack” AI approach.

| Category | Details |
|---|---|
| Platform | Pharma.AI suite: PandaOmics (target ID), Chemistry42 (generative design), InClinico (trial prediction); ChatPandaGPT (2023). Incorporates AlphaFold2 and quantum computing into workflows. |
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

## Conflict of interest

## Financial support

## Data availability

## CRediT authorship contribution statement

**Mahendiran Dharmasivam:**Conceptualization, Software, Investigation, Figures, Writing – original draft, Writing – review and editing.

**Busra Kaya:**Writing – review and editing.

**Adedoyin Akinware:**Writing – review and editing.

**Mahan Gholam Azad:**Writing – review and editing.

**Des R. Richardson:**Supervision, Writing – review and editing.

## References

- 1Role of artificial intelligence in cancer drug discovery and developmentCancer Lett, 627 (2025), Article 217821, 10.1016/j.canlet.2025.217821
- 2When will AI be creating all new drugs? AVEVAhttps://www.aveva.com/en/our-industrial-life/type/article/when-will-ai-be-creating-all-new-drugs/#:∼:text=molecules%20are%20substantially%20more%20successful,industry%20averages%20of%20around%2040 (Published June 17, 2025), Accessed 9th Aug 2025
- 3The contribution of artificial intelligence to drug discovery: current progress and prospects for the futureA. Khamparia, B. Pandey, D.K. Pandey, D. Gupta (Eds.), Microbial Data Intelligence and Computational Techniques for Sustainable Computing, Springer Nature Singapore (2024), pp. 1-23, 10.1007/978-981-99-9621-6_1
- 4Artificial intelligence revolutionizing drug development: exploring opportunities and challengesDrug Dev Res, 84 (8) (2023), pp. 1652-1663, 10.1002/ddr.22115
- 5The potential of artificial intelligence in pharmaceutical innovation: from drug discovery to clinical trialsPharmaceuticals (Basel), 18 (6) (2025), p. 788, 10.3390/ph18060788
- 6Artificial intelligence in drug development: reshaping the therapeutic landscapeTher Adv Drug Saf, 16 (2025), Article 20420986251321704, 10.1177/20420986251321704
- 7A small-molecule TNIK inhibitor targets fibrosis in preclinical and clinical modelsNat Biotechnol, 43 (1) (2025), pp. 63-75, 10.1038/s41587-024-02143-0
- 8AI-enabled drug discovery reaches clinical milestoneNat Med, 31 (8) (2025), pp. 2490-2491, 10.1038/s41591-025-03832-2
- 9Leveraging artificial intelligence and machine learning in kinase inhibitor development: advances, challenges, and future prospectsRSC Med Chem, 16 (10) (2025), pp. 4698-4720, 10.1039/D5MD00494B
- 10Current status of computational approaches for small molecule drug discoveryJ Med Chem, 67 (21) (2024), pp. 18633-18636, 10.1021/acs.jmedchem.4c02462
- 11A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trialNat Med, 31 (8) (2025), pp. 2602-2610, 10.1038/s41591-025-03743-2
- 12AI-Driven drug discovery for rare diseasesJ Chem Inf Model, 65 (5) (2025), pp. 2214-2231, 10.1021/acs.jcim.4c01966
- 13Artificial intelligence in drug discovery and developmentF.J. Hock, M.K. Pugsley (Eds.), Drug Discovery and Evaluation: Safety and Pharmacokinetic Assays, Springer International Publishing (2024), pp. 1461-1498, 10.1007/978-3-031-35529-5_92
- 14Applications of artificial intelligence in biotech drug discovery and product developmentMedComm, 6 (8) (2025), Article e70317, 10.1002/mco2.70317
- 15Human Edge in the AI Age: Eight Timeless Mantras for SuccessPenguin Random House India Private Limited (2025)
- 16Advanced AI applications for drug discoveryI.A. Shah, Q. Sial (Eds.), Advances in Computational Intelligence for the Healthcare Industry 4.0, IGI Global (2024), pp. 42-86, 10.4018/979-8-3693-2333-5.ch003
- 17AI/ML methodologies and the future-will they be successful in designing the next generation of new chemical entities?J Cheminform, 17 (1) (2025), p. 46, 10.1186/s13321-025-00995-5
- 18Evaluating the impact of ai and ml on modern drug discoveryJ Pharm Insight Res, 2 (4) (2024), pp. 67-72, 10.69613/8tckqp18
- 19Artificial intelligence and machine learning in drug discoveryR.K.P. Tripathi, S. Tiwari (Eds.), Converging Pharmacy Science and Engineering in Computational Drug Discovery, IGI Global Scientific Publishing (2024), pp. 54-75, 10.4018/979-8-3693-2897-2.ch003
- 20Artificial intelligence and machine learning-aided drug discovery in central nervous system diseases: state-of-the-arts and future directionsMed Res Rev, 41 (3) (2021), pp. 1427-1473, 10.1002/med.21764
- 21Drug discovery with explainable artificial intelligenceNat Mach Intell, 2 (10) (2020), pp. 573-584, 10.1038/s42256-020-00236-4
- 22State of AI report. London, UK.[Google Scholar]https://www.stateof.ai/2020 (October 1, 2020), Accessed 9th Aug 2025
- 23The role of big data in self-learning AI systemsJ Artif Intell Res, 9 (2021), pp. 1-10
- 24The AI Ladder: Accelerate Your Journey to AIO'Reilly Media (2020)
- 25An Introductory Guide to Artificial Intelligence for Legal ProfessionalsKluwer, Law International (2020)
- 26Mechanism of baricitinib supports artificial intelligence-predicted testing in patients with COVID-19EMBO Mol Med, 12 (8) (2020), Article e12697, 10.15252/emmm.202012697
- 27TNIK's emerging role in cancer, metabolism, and age-related diseasesTrends Pharmacol Sci, 45 (6) (2024), pp. 478-489, 10.1016/j.tips.2024.04.010
- 28Insilico eyes Q4 start for late-stage trials of IPF candidateGEN Edge, 7 (1) (2025), pp. 371-375, 10.1089/genedge.7.1.068
- 29Standigm ASK™: knowledge graph and artificial intelligence platform applied to target discovery in idiopathic pulmonary fibrosisBrief Bioinform, 25 (2) (2024), Article bbae035, 10.1093/bib/bbae035
- 30Harnessing AI and quantum computing for accelerated drug discovery: regulatory frameworks for in silico to in vivo validationJ Pharm, 2 (3) (2025), p. 11, 10.3390/jpbi2030011
- 31How generative AI is reducing drug discovery timelines by 70%. Mediumhttps://prajnaaiwisdom.medium.com/how-generative-ai-is-reducing-drug-discovery-timelines-by-70-e86d58f7c780 (Published April 28 2025), Accessed 9th Aug 2025
- 32Exploring the future of biopharmaceutical drug discovery: can advanced AI platforms overcome current challenges?Discov Artif Intell, 4 (1) (2024), p. 102, 10.1007/s44163-024-00188-3
- 33Artificial intelligence-driven innovations in oncology drug discovery: transforming traditional pipelines and enhancing drug designDrug Des Dev Ther, 19 (2025), pp. 5685-5707, 10.2147/DDDT.S509769
- 34AI comes to the Nobel Prize and drug discoveryJ Pharm Anal, 14 (11) (2024), Article 101160, 10.1016/j.jpha.2024.101160
- 35Insights into artificial intelligence utilisation in drug discoveryJ Med Econ, 27 (1) (2024), pp. 304-308, 10.1080/13696998.2024.2315864
- 36Artificial intelligence in drug developmentNat Med, 31 (1) (2025), pp. 45-59, 10.1038/s41591-024-03434-4
- 37Artificial intelligence for drug discovery: are we there yet?Annu Rev Pharmacol Toxicol, 64 (1) (2024), pp. 527-550, 10.1146/annurev-pharmtox-040323-040828
- 38Artificial intelligence in drug development: present status and future prospectsDrug Discov Today, 24 (3) (2019), pp. 773-780, 10.1016/j.drudis.2018.11.014
- 39Success stories of AI in drug discovery—where do things stand?Expert Opin Drug Discov, 17 (1) (2022), pp. 79-92, 10.1080/17460441.2022.1985108
- 40Machine learning in drug deliveryJ Control Release, 373 (2024), pp. 23-30, 10.1016/j.jconrel.2024.06.045
- 41Discovery Channels: watson health might have come up far short of expectations, but AI techniques remain poised to reinvent drug discoveryMed Mark Media, 57 (7) (2022), pp. 34-37
- 42Double dare: exscientia expands AI platform into antibody design: British pioneer of data-driven drug discovery eyes doubling the number of potential druggable sites, as well as a future move into more complex biologicsGEN Edge, 4 (1) (2022), pp. 896-902, 10.1089/genedge.4.1.151
- 43AI-Driven Pharma tech firm expands Its discovery platform into biologics: Exscientia intends to double the addressable target universe of its platform by combining generative AI design and virtual screeningGenet Eng Biotechnol News, 43 (1) (2023), pp. 10-11, 10.1089/gen.43.01.02
- 44Pipeline pruning: Exscientia cuts programs to sharpen precision oncology focus: founder and CEO Andrew Hopkins discusses the AI drug pioneer's plans to partner or end internal development of dozens of active drug candidates, and plans for 2024GEN Edge, 5 (1) (2023), pp. 889-897, 10.1089/genedge.5.1.170
- 45Defining activity and patient selection of a novel CDK7 inhibitor, GTAEXS-617, through AI-supported primary cancer tissue profilingEur J Cancer, 174 (1) (2022), pp. S44-S45, 10.1016/S0959-8049(22)00919-4
- 46From knowledge, drug power: an interview with Andrew HopkinsGEN Biotechnol, 1 (3) (2022), pp. 225-229, 10.1089/genbio.2022.29035.aho
- 472289P Determining anti-cancer efficacy of a reversible LSD1 inhibitor, EXS74539, in primary AML tissues with limited thrombocytopenic effectsAnn Oncol, 34 (2023), Article S1173, 10.1016/j.annonc.2023.09.1317
- 48Tapping into the drug discovery potential of AIBiopharmadealmakers (May 27, 2021), pp. B37-B39, 10.1038/d43747-021-00045-7https://www.nature.com/articles/d43747-021-00045-7, Accessed 27th Aug 2025
- 49Abstract 3930: AI-driven discovery and profiling of GTAEXS-617, a selective and highly potent inhibitor of CDK7Cancer Res, 82 (12 suppl) (2022), Article 3930–3930, 10.1158/1538-7445.AM2022-3930
- 50BMS Collaboration Paying Off for Exscientia: AI drug developer designs EXS4318, the I&I small molecule that has entered Phase I trials overseen by pharma giant in up-to-$1.3B+ partnershipGEN Edge, 5 (1) (2023), pp. 147-150, 10.1089/genedge.5.1.31
- 51Inside the Nascent Industry of AI-Designed DrugsNature Publishing Group (2023)
- 52A new paradigm for drug developmentLancet Digit Health, 2 (5) (2020), pp. e226-e227, 10.1016/S2589-7500(20)30088-1
- 53Integrating of artificial intelligence in drug discovery and development: a comparative studyPharmacophore, 14 (3) (2023), pp. 35-40, 10.51847/ANVMZrZ4X4
- 54A survey on computational methods in drug discovery for neurodegenerative diseasesBiomolecules, 14 (10) (2024), p. 1330, 10.3390/biom14101330
- 55Lighthouse illuminates therapeutics for a variety of diseases including COVID-19iScience, 25 (11) (2022), Article 105314, 10.1016/j.isci.2022.105314
- 56AI and machine learning in drug discoveryH. Yang (Ed.), Data Science, AI, and Machine Learning in Drug Development, Chapman and Hall/CRC (2022), pp. 63-93, 10.1201/9781003150886-4
- 57Rational design and identification of ISM7594 as a tissue-agnostic FGFR2/3 inhibitorJ Med Chem, 68 (13) (2025), pp. 13887-13906, 10.1021/acs.jmedchem.5c00928
- 58Oral ENPP1 inhibitor designed using generative AI as next generation STING modulator for solid tumorsNat Commun, 16 (1) (2025), p. 4793, 10.1038/s41467-025-59874-0
- 59Discovery of novel inhibitors for WD repeat-containing protein 5 (WDR5)-MYC protein-protein interactionChem Biol Drug Des, 105 (5) (2025), Article e70129, 10.1111/cbdd.70129
- 60A novel, covalent broad-spectrum inhibitor targeting human coronavirus MproNat Commun, 16 (1) (2025), p. 4546, 10.1038/s41467-025-59870-4
- 61Discovery of novel SIK2/3 inhibitors for the potential treatment of MEF2C+ acute myeloid leukemia (AML)J Med Chem, 68 (7) (2025), pp. 7518-7538, 10.1021/acs.jmedchem.4c03225
- 62Discovery of potent, highly selective, and orally bioavailable MTA cooperative PRMT5 inhibitors with robust in vivo antitumor activityJ Med Chem, 68 (2) (2025), pp. 1940-1955, 10.1021/acs.jmedchem.4c02732
- 63Tang QQ, Xiao DY, Veviorskiy A, et al. AI-driven robotics laboratory identifies pharmacological TNIK inhibition as a potent senomorphic agent.
*Aging Dis*. 2026;17(1):1–20.https://doi.org/10.14336/Ad.2024.1492. - 64Design, synthesis, and biological evaluation of novel orally available covalent CDK12/13 dual inhibitors for the treatment of tumorsJ Med Chem, 68 (4) (2025), pp. 4148-4167, 10.1021/acs.jmedchem.4c01616
- 65Discovery of pyrrolopyrazine carboxamide derivatives as potent and selective FGFR2/3 inhibitors that overcome mutant resistanceJ Med Chem, 68 (3) (2025), pp. 3886-3899, 10.1021/acs.jmedchem.4c03205
- 66Intestinal mucosal barrier repair and immune regulation with an AI-developed gut-restricted PhD inhibitorNat Biotechnol, 43 (11) (2024), pp. 1772-1777, 10.1038/s41587-024-02503-w
- 67Discovery of a novel macrocyclic noncovalent CDK7 inhibitor for cancer therapyJ Med Chem, 67 (22) (2024), pp. 20580-20594, 10.1021/acs.jmedchem.4c02098
- 68Chemistry42: an AI-driven platform for molecular design and optimizationJ Chem Inf Model, 63 (3) (2023), pp. 695-701, 10.1021/acs.jcim.2c01191
- 69Abstract 502: ISM3091, a novel selective USP1 inhibitor as a targeted anticancer therapyCancer Res, 83 (7 suppl) (2023), Article 502–502, 10.1158/1538-7445.Am2023-502
- 70PRT543, a methyl transferase inhibitor, has potent anti-tumor activity against adenoid cystic carcinoma of salivary glandsCancer Res, 83 (7) (2023), Article 4897–4897, 10.1158/1538-7445.Am2023-4897
- 71In the pipeline: recursion's approach to AI and machine learningGEN Biotechnol, 3 (5) (2024), pp. 269-273, 10.1089/genbio.2024.0049
- 72As pipeline advances, recursion expands AI focus to clinical trials: chief R&D and commercial officer Najat Khan, PhD, tells GEN Edge the company aims to improve design of studies, accelerate enrollment, and enhance evidence generationGEN Edge, 7 (1) (2025), pp. 63-69, 10.1089/genedge.7.1.012
- 73Recursion advances AI-based C. diff candidate to phase II: first patient dosed in ALDER trial assessing oral, non-antibiotic small molecule for recurrent form of infection with the bacteriumGEN Edge, 6 (1) (2024), pp. 887-890, 10.1089/genedge.6.01.168
- 74Recursion announces promising clinical data on lead ai-based drug candidate for brain disease: patients with cerebral cavernous malformation (CCM) treated with oral drug, REC-994, showed reduction in total cerebral and brainstem lesion volumeGEN Edge, 7 (1) (2025), pp. 84-89, 10.1089/genedge.7.1.015
- 75Clinical Pharmacology and tolerability of REC-994, a redox-cycling nitroxide compound, in randomized phase 1 dose-finding studiesPharmacol Res Perspect, 12 (3) (2024), p. e1200, 10.1002/prp2.1200
- 76Trans-Atlantic triumph: AI drug pioneers Recursion, Exscientia combine: company vows first- and best-in-class drug discovery based on artificial intelligence after joining forces to create a pipeline of 30+ programsGEN Edge, 6 (1) (2024), pp. 950-956, 10.1089/genedge.6.01.179
- 77Recursion halts four pipeline programs, sharpening cancer, rare disease focus: AI drug developer advances fourth Sanofi-partnered program, earns $7 million milestone paymentGEN Edge, 7 (1) (2025), pp. 302-309, 10.1089/genedge.7.1.055
- 78Artificial intelligence makes a splash in small-molecule drug discoveryBiopharm Deal, 2022 (2022), Article d43747-022, 10.1038/d43747-022-00104-7
- 79Advancing drug discovery via artificial intelligenceTrends Pharmacol Sci, 40 (8) (2019), pp. 592-604, 10.1016/j.tips.2019.06.004
- 80The Netflix of digital biology? Recursion is reimagining drug discovery: by applying a proprietary operating system to drug discovery, the Utah clinical-stage biotechnology company expects to turn drug discovery from sequential testing into a search problemGEN Edge, 4 (1) (2022), pp. 672-678, 10.1089/genedge.4.1.110
- 81Nvidia’s $50 million Recursion investment starts alliance to scale up in AI drug discovery. MedCity News. 12 July 2023
- 82Recursion's Fast-Track Road to Therapeutics Using AI-Based Maps of Biology: the company reflects on their latest IND approval, the evolution of their end-to-end drug discovery platform, and what's next for the fieldGEN Edge, 6 (1) (2024), pp. 836-840, 10.1089/genedge.6.01.159
- 83Artificial intelligence (AI) applications in drug discovery and drug delivery: revolutionizing personalized medicinePharmaceutics, 16 (10) (2024), p. 1328, 10.3390/pharmaceutics16101328
- 84Algorithm exploitation: humans are keen to exploit benevolent AIiScience, 24 (6) (2021), Article 102679, 10.1016/j.isci.2021.102679
- 85Cognitive technology addressing optimal cancer clinical trial matching and protocol feasibility in a community cancer practiceJ Clin Oncol, 35 (15 suppl) (2017), Article 6501–6501, 10.1200/JCO.2017.35.15_suppl.6501
- 86Discovery of a potent, selective, and brain-penetrant checkpoint kinase 1 inhibitor, BEN-28010, for the treatment of glioblastomaJ Med Chem, 68 (9) (2025), pp. 9101-9125, 10.1021/acs.jmedchem.5c00279
- 87AI isn't the magic bullet to simplify drug discovery: wet-lab biology and translational models are key to confirming AI-derived findingsGenet Eng Biotechnol News, 44 (6) (2024), pp. 20-21, 10.1089/gen.44.06.09
- 88The art of AI in drug discovery: vibrant field has a wealth of new algorithms, more data, and fresh fundingInside Precis Med, 11 (1) (2024), pp. 18-21, 10.1089/ipm.11.01.04
- 89Type I inhibitors of tropomyosin receptor kinase (Trk): a 2020–2022 patent updateExpert Opin Ther Pat, 33 (7–8) (2023), pp. 503-521, 10.1080/13543776.2023.2262136
- 90Legal and policy issues surrounding ai-assisted chemistry and drug discoveryAriz Law J Emerg Technol, 8 (1) (2024), pp. 1-20, 10.2458/azlawjet.7077
- 91Navigating the complexities of drug development for inflammatory bowel diseaseNat Rev Drug Discov, 23 (7) (2024), pp. 546-562, 10.1038/s41573-024-00953-0
- 92Integrating artificial intelligence for drug discovery in the context of revolutionizing drug deliveryLife (Basel), 14 (2) (2024), p. 233, 10.3390/life14020233
- 93Sgr-1505 is a potent MALT1 protease inhibitor with a potential best-in-class profileBlood, 142 (1 suppl 1) (2023), p. 2997, 10.1182/blood-2023-190985
- 94A Phase 1, open-label, multicenter, dose-escalation study of Sgr-1505 as monotherapy in subjects with mature B-cell malignanciesBlood, 142 (1 suppl 1) (2023), p. 3102, 10.1182/blood-2023-182838
- 95A phase 1/2 study of STP938, a first-in-class inhibitor of CTP synthase 1, in patients with relapsed/refractory B or T cell lymphomaJ Clin Oncol, 41 (16 suppl) (2023), Article TPS7591, 10.1200/JCO.2023.41.16_suppl.TPS7591
- 96Beyond trial and error: leveraging advanced software for Therapeutic discoveryChem Biol Lett, 12 (1) (2025), Article 1251–1251, 10.62110/sciencein.cbl.2025.v12.1251
- 97Abstract 3025: optimization of therapeutic index of SGR-3515, a first-in-class Wee1/Myt1 inhibitor through intermittent dosing for monotherapy and combination with chemotherapy in xenograft tumor modelsCancer Res, 85 (8 suppl 1) (2025), Article 3025–3025, 10.1158/1538-7445.Am2025-3025
- 98Abstract 4376: preclinical characterization of SGR-4174, a potent and selective SOS1 inhibitor for the treatment of pan KRAS mutant cancers in combination with KRAS pathway inhibitorsCancer Res, 85 (8 suppl 1) (2025), Article 4376–4376, 10.1158/1538-7445.Am2025-4376
- 99From model to molecule: Nvidia doubles down on AI drug discovery: GPU inventor partners with Schrödinger, AstraZeneca, UF health on computational approaches to therapy developmentGEN Edge, 3 (1) (2021), pp. 238-246, 10.1089/genedge.3.1.038
- 100Schrödinger's equation: physics+ machine learning= drug discovery: CEO Ramy Farid and Karen Akinsanya, Schrödinger's president of R&D, therapeutics discuss the company's AI formula with GEN EdgeGEN Edge, 5 (1) (2023), pp. 557-563, 10.1089/genedge.5.1.107
- 101Novel allosteric inhibitor to target drug resistance in EGFR mutant: molecular modelling and free energy approachMol Simul, 48 (9) (2022), pp. 801-811, 10.1080/08927022.2022.2055012
- 102Development of triple mutant T790M/C797S allosteric EGFR inhibitors: a computational approachJ Biomol Struct Dyn, 39 (15) (2021), pp. 5376-5398, 10.1080/07391102.2020.1786460
- 103Computational study on the mechanism of small molecules inhibiting NLRP3 with ensemble docking and molecular dynamic simulationsBMC Pharmacol Toxicol, 26 (1) (2025), p. 49, 10.1186/s40360-025-00851-0
- 104Repurposing FDA-approved drugs as NLRP3 inhibitors against inflammatory diseases: machine learning and molecular simulation approachesJ Biomol Struct Dyn, 43 (8) (2025), pp. 4327-4339, 10.1080/07391102.2024.2308072
- 105Identification of potent leucine-rich repeat kinase 2 inhibitors by virtual screening and biological evaluationChem Biol Drug Des, 105 (3) (2025), Article e70082, 10.1111/cbdd.70082
- 106Identification of novel LRRK2 inhibitors by structure-based virtual screening and alchemical free energy calculationPhys Chem Chem Phys, 26 (29) (2024), pp. 19775-19786, 10.1039/d4cp01762e
- 107KinDEL: DNA-encoded library dataset for kinase inhibitorsPreprint. Posted online October, 11 (2024)arXiv 2410.08938
- 108Pitfalls in performing genome-wide association studies on ratio traitsHGG Adv, 6 (2) (2025), Article 100406, 10.1016/j.xhgg.2025.100406
- 109EmbedGEM: a framework to evaluate the utility of embeddings for genetic discoveryBioinform AdV, 4 (1) (2024), Article vbae135, 10.1093/bioadv/vbae135
- 110Compositional deep probabilistic models of DNA-encoded librariesJ Chem Inf Model, 64 (4) (2024), pp. 1123-1133, 10.1021/acs.jcim.3c01699
- 111Machine learning across multiple imaging and biomarker modalities in the UK Biobank improves genetic discovery for liver fat accumulationmedRxiv, 2024 (Preprint. Posted January 07, 2024), Article 01.06.24300923, 10.1101/2024.01.06.24300923
- 112A pooled cell painting CRISPR screening platform enables de novo inference of gene function by self-supervised deep learningbioRxiv (Preprint. Posted August 27, 2023), Article 2023.08.13.553051, 10.1101/2023.08.13.553051
- 113An AI biotech hauls in $600 million, plus more funding highlights to closeMedCity News (April 1, 2025)
- 114Generative AI platforms drive drug discovery dealmakingBiopharmadealmakers (Nature). August, 16 (2024), 10.1038/d43747-024-00084-whttps://www.nature.com/articles/d43747-024-00084-w, Accessed 27th Aug 2025
- 115Purification of pharmaceuticals via retention time prediction: leveraging graph isomorphism networks, limited data, and transfer learningJ Sep Sci, 48 (6) (2025), Article e70178, 10.1002/jssc.70178
- 116Democratizing artificial intelligence in pre-clinical drug discovery: while ai-driven approaches tout increased speed and lower costs, commercial interests compromise scientific collaborationGenet Eng Biotechnol News, 45 (7) (2025), pp. 24-27, 10.1089/gen.45.07.10
- 117From molecules to medicines: the role of AI-driven drug discovery against Alzheimer's disease and other neurological disordersPharmaceuticals (Basel), 18 (7) (2025), p. 1041, 10.3390/ph18071041
- 118AlphaFold3: an overview of applications and performance insightsInt J Mol Sci, 26 (8) (2025), p. 3671, 10.3390/ijms26083671
- 119NGT: generative AI with synthesizability guarantees discovers MC2R inhibitors from a Tera-scale virtual screenJ Med Chem, 67 (21) (2024), pp. 19417-19427, 10.1021/acs.jmedchem.4c01763
- 120AI is a viable alternative to high throughput screening: a 318-target studySci Rep, 14 (1) (2024), p. 7526, 10.1038/s41598-024-70321-w
- 121Discovery of a cryptic pocket in the AI-predicted structure of PPM1D phosphatase explains the binding site and potency of its allosteric inhibitorsFront Mol Biosci, 10 (2023), Article 1171143, 10.3389/fmolb.2023.1171143
- 122AtomNet poseranker: enriching ligand pose quality for dynamic proteins in virtual high-throughput screensJ Chem Inf Model, 62 (5) (2022), pp. 1178-1189, 10.1021/acs.jcim.1c01250
- 123SPOP and OTUD7A control EWS-FLI1 protein stability to govern Ewing sarcoma growthAdv Sci (Weinh), 8 (14) (2021), Article e2004846, 10.1002/advs.202004846
- 124Templated nucleation of clotrimazole and ketoprofen on polymer substratesMol Pharm, 21 (9) (2024), pp. 4576-4588, 10.1021/acs.molpharmaceut.4c00491
- 125Tale of two polymorphs: investigating the structural differences and dynamic relationship between nirmatrelvir solid forms (Paxlovid)Mol Pharm, 21 (8) (2024), pp. 3800-3814, 10.1021/acs.molpharmaceut.3c01074
- 126Cocrystal synthesis through crystal structure predictionMol Pharm, 20 (7) (2023), pp. 3380-3392, 10.1021/acs.molpharmaceut.2c01098
- 127Effect of polymer additives on the crystal habit of metformin HClSmall Methods, 7 (6) (2023), Article e2201692, 10.1002/smtd.202201692
- 128Novel physics-based ensemble modeling approach that utilizes 3D molecular conformation and packing to access aqueous thermodynamic solubility: a case study of orally available bromodomain and extraterminal domain inhibitor lead optimization seriesJ Chem Inf Model, 61 (3) (2021), pp. 1412-1426, 10.1021/acs.jcim.0c01410
- 129Artificial intelligence in drug development and delivery: opportunities, challenges, and future directionsJ Angiotherapy, 8 (8) (2024), pp. 1-10, 10.25163/angiotherapy.8810326
- 130Harnessing the AI/ML in drug and biological products discovery and development: the regulatory perspectivePharmaceuticals (Basel), 18 (1) (2025), p. 47, 10.3390/ph18010047
- 131AI-powered clinical trials and the imperative for regulatory transparency and accountabilityHealth Technol, 14 (6) (2024), pp. 1071-1081, 10.1007/s12553-024-00904-0
- 132The illusion of safety: a report to the FDA on AI healthcare product approvalsPLoS Digit Health, 4 (6) (2025), Article e0000866, 10.1371/journal.pdig.0000866
- 133Explainable AI and federated learning in healthcare supply chain intelligence: addressing ethical constraints, bias mitigation, and regulatory compliance for global pharmaceutical distributionIJCATR, 14 (4) (2025), pp. 16-29, 10.7753/IJCATR1404.1002
- 134Transparency in Risk Regulation: the Case of the European Medicines AgencyKing's College, London (2017)
- 135Medicine, healthcare and the AI act: gaps, challenges and future implicationsEur Heart J Digit Health, 6 (4) (2025), pp. 833-839, 10.1093/ehjdh/ztaf041
- 136Medicines transparency at the European Medicines Agency (EMA) in the new information age: the perspectives of patientsJ Risk Res, 19 (9) (2016), pp. 1185-1215, 10.1080/13669877.2016.1200652
- 137Unveiling the black box: bringing algorithmic transparency to AIMasaryk Univ J Law Technol, 18 (1) (2024), pp. 93-122, 10.5817/MUJLT2024-1-4
- 138Ethical aspects in the use of artificial intelligence in the process of drug development [Aspecte etice în utilizarea inteligenței artificiale în procesul de dezvoltare a medicamentelor]J Med Braşov (2024), pp. 53-61, 10.31926/jmb.2023.2.8
- 139How successful are AI-discovered drugs in clinical trials? A first analysis and emerging lessonsDrug Discov Today, 29 (6) (2024), Article 104009, 10.1016/j.drudis.2024.104009
- 140These six biotechs are winning the race to get AI-designed drugs to the clinicInside Precis Med, 9 (4) (2022), pp. 40-42, 10.1089/ipm.09.04.10
- 141Revolutionizing drug development: the role of AI in modern pharmaceutical researchS. Agarwal, A.K. Dutta (Eds.), Bioinformatics and Beyond (1st ed.), CRC Press (2025), pp. 206-227
- 142AI3SD & MDC AI in Drug Discovery & Drug Safety Workshop Report 2019University of Southampton (2019), pp. 1-11, 10.5258/SOTON/P0008
- 143The rise of 'centaur' inventors: how patent law should adapt to the challenge to inventorship doctrine by human-AI inventing synergiesJ Pat Trademark Off Soc'y, 104 (2024), p. 71
- 144Application of artificial intelligence in drug discoveryCurr Pharm Des, 28 (33) (2022), pp. 2690-2703, 10.2174/1381612828666220608141049
- 145Efficacy and feasibility of pharmacoscopy-guided treatment for acute myeloid leukemia patients who have exhausted all registered therapeutic optionsHaematologica, 109 (2) (2024), pp. 617-621, 10.3324/haematol.2023.283224
- 146Functional precision medicine provides clinical benefit in advanced aggressive hematologic cancers and identifies exceptional respondersCancer Discov, 12 (2) (2022), pp. 372-387, 10.1158/2159-8290.CD-21-0538
- 147Exscientia signs AI-powered drug-discovery deal with CelgeneChem Eng News (March 21, 2019)https://cen.acs.org/business/informatics/Exscientia-signs-AI-powered-drug/97/web/2019/03, Accessed 9th Aug 2025
- 148AI drug hunter Exscientia chops down “rapidly emerging pipeline” to focus on two main oncology programsFierce Biotech. October, 3 (2023)
- 149AI in pharmacy: the transformative impact of artificial neural networks on pharmaceutical researchH. Roy, P.R. Bhavanam, S. Faizan Ali (Eds.), Proceedings of the International Symposium on Sustainable Drug Design and Nanoparticle Development: Quantum and Computational Perspectives (SDDNDQCP 2025), Atlantis Press International BV (2025), pp. 124-138, 10.2991/978-94-6463-813-4_10
- 150Applications of machine learning in drug discovery and developmentNat Rev Drug Discov, 18 (6) (2019), pp. 463-477, 10.1038/s41573-019-0024-5
- 151832P Characterisation of EXS73565: a potent and selective MALT1 inhibitor with low drug-drug interaction risk and potential in lymphomaAnn Oncol, 34 (2) (2023), pp. S546-S547, 10.1016/j.annonc.2023.09.696
- 152Abstract CT114: data from first-in-human study of EXS21546, an A2A receptor antagonist, now progressing into phase 1 in RCC/NSCLCCancer Res, 83 (8 suppl) (2023), Article CT114–CT114, 10.1158/1538-7445.AM2023-CT114
- 153Abstract 4150: enriching for adenosine antagonist patient responses through deep learningCancer Res, 82 (12 suppl) (2022), Article 4150–4150, 10.1158/1538-7445.AM2022-4150
- 15423P Enriching for response: patient selection criteria for A2AR inhibition by EXS-21546 through ex vivo modelling in primary patient materialImmuno-Oncol Technol, 16 (1) (2022), Article 100128, 10.1016/j.iotech.2022.100128
- 155Abstract 1731: EXS21546, a non-CNS penetrant A2AR-selective antagonist for anti-cancer immunotherapyCancer Res, 81 (13 suppl) (2021), Article 1731–1731, 10.1158/1538-7445.am2021-1731
- 156Merck KGaA doubles up on AI partners, tapping BenevolentAI and Exscientia for drug discovery pushFierce Biotech. September, 20 (2023)
- 157Understanding the company landscape in AI-Driven BioPharma R&DBiopharmadealmakers (Nature) (May 17, 2023)https://www.nature.com/articles/d43747-023-00020-4, Accessed 27th Aug 2025
- 158Several months after Exscientia merger, AI biotech outfit Recursion reworks pipelineFierce Biotech (May 5, 2025)
- 159Seven BioPharma trends to watch in 2025GEN Biotechnol, 4 (1) (2025), pp. 11-15, 10.1089/genbio.2025.0005
- 160Predict first: BMS executives discuss company's AI approach: Bristol Myers Squibb's Robert Plenge, MD, PhD, and Greg Meyers articulate how the pharma giant applies artificial intelligence and machine learningGEN Edge, 7 (1) (2025), pp. 211-219, 10.1089/genedge.7.1.039
- 161The potential applications of artificial intelligence in drug discovery and developmentPhysiol Res, 70 (4 suppl 4) (2021), pp. S715-S722, 10.33549/physiolres.934765
- 162Ai assistance in the drug development process: reaching for a regulatory frameworkSeton Hall L Rev, 54 (4) (2024), pp. 1239-1278, 10.60095/WBYZ9142
- 163A patent review of cyclin-dependent kinase 7 (CDK7) inhibitors (2018–2022)Expert Opin Ther Pat, 33 (2) (2023), pp. 67-87, 10.1080/13543776.2023.2195547
- 164Future of chemistry in the presence of artificial intelligenceS Afr J Chem, 77 (2023), pp. 150-156, 10.17159/0379-4350/2023/v77a19
- 165Recursion to acquire Exscientia, combining AI drug pioneersGEN Edge, 6 (1) (2024), pp. 699-703, 10.1089/genedge.6.1.134
- 166Recursion in secondary computer science education: a comparative study of visual programming approachesProceedings of the 55th ACM Technical Symposium on Computer Science Education V 1, Association for Computing Machinery (2024), pp. 1321-1327, 10.1145/3626252.3630916
- 167Recursion enhanced random forest with an improved linear model (RERF-ILM) for heart disease detection on the internet of medical things platformIEEE Access, 8 (2020), pp. 59247-59256, 10.1109/Access.2020.2981159
- 16812 AI drug discovery companies you should know aboutLabiotech. March, 27 (2025)http://labiotech.eu/best-biotech/ai-drug-discovery-companies/, Accessed 9th Aug 2025
- 169Edison to AI: Intellectual Property in AI-Driven Drug R&DThe Johns Hopkins University, Dissertation (2023), 10.26153/tsw/47191
- 170RecurTutor: an interactive tutorial for learning recursionACM Trans Comput Educ, 19 (1) (2018), pp. 1-25, 10.1145/3218328
- 171Learning representations for image-based profiling of perturbationsNat Commun, 15 (1) (2024), p. 1594, 10.1038/s41467-024-45999-1
- 172Image-based profiling for drug discovery: due for a machine-learning upgrade?Nat Rev Drug Discov, 20 (2) (2021), pp. 145-159, 10.1038/s41573-020-00117-w
- 173Drugs, dollars, and data: recursion eyes cost savings from AI drug discovery: recursion CEO Chris Gibson discusses Nvidia collaboration and the timeframe for artificial intelligence reining in sky-high treatment pricesGEN Edge, 6 (1) (2024), pp. 73-79, 10.1089/genedge.6.01.016
- 174Beyond the Hype of AI in Cancer R&DNature Publishing Group (2024)
- 175A phase 1 trial of the histone deacetylase inhibitor AR-42 in patients with neurofibromatosis type 2-associated tumors and advanced solid malignanciesCancer Chemother Pharmacol, 87 (5) (2021), pp. 599-611, 10.1007/s00280-020-04229-3
- 176Early phase clinical studies of AR-42, a histone deacetylase inhibitor, for neurofibromatosis type 2-associated vestibular schwannomas and meningiomasLaryngoscope Investig Otolaryngol, 6 (5) (2021), pp. 1008-1019, 10.1002/lio2.643
- 177The convergence of AI and pharma: recursion pharmaceuticals (RXRX), NVIDIA, and the next industrial revolutionMacrowise Newsletter (February 19, 2025)https://macrowise.substack.com/p/the-convergence-of-ai-and-pharma, Accessed 9th Aug 2025
- 178Recursion pharmaceuticals: an AI-powered drug discovery powerhouseKavout (December 4, 2024)
- 179Drug discovery, STAT! Nvidia, recursion speed pharma R&D with AI supercomputerNvidia Blog (May 13, 2024)https://blogs.nvidia.com/blog/drug-discovery-recursion-supercomputer/, Accessed 9th Aug 2025
- 180Recursion reports Q2 2025 with $7 million Sanofi milestone, announces clinical updatesBiopharmaTrend (August 5, 2025)
- 181CRISPR screening by AAV episome-sequencing (CrAAVe-seq): a scalable cell-type-specific in vivo platform uncovers neuronal essential genesNat Neurosci, 28 (10) (2025), pp. 2129-2140, 10.1038/s41593-025-02043-9
- 182Protein structure database predicted millions of 3D structures. AlphaFold Protein Structure Databasehttps://alphafold.ebi.ac.uk/, Accessed 7th Aug 2025
- 183Author correction: the AI drug revolution needs a revolutionnpj Drug Discov, 2 (1) (2025), p. 10, 10.1038/s44386-025-00022-5
- 184Researchers are betting that AI and automation can cut drug discovery from five years to six months: automating antiviralsIEEE Spectr, 57 (10) (2020), pp. 44-49, 10.1109/mspec.2020.9205548
- 185Harnessing AI to Accelerate Innovation in the Biopharmaceutical IndustryInformation Technology and Innovation Foundation (2024)
- 186Accelerating drug discovery, development, and clinical trials by artificial intelligenceMed, 5 (9) (2024), pp. 1050-1070, 10.1016/j.medj.2024.07.026
- 187PandaOmics: an AI-driven platform for therapeutic target and biomarker discoveryJ Chem Inf Model, 64 (10) (2024), pp. 3961-3969, 10.1021/acs.jcim.3c01619
- 188From lab to clinic: how artificial intelligence (AI) is reshaping drug discovery timelines and industry outcomesPharmaceuticals (Basel), 18 (7) (2025), p. 981, 10.3390/ph18070981
- 189Digital alchemy: the rise of machine and deep learning in small-molecule drug discoveryInt J Mol Sci, 26 (14) (2025), p. 6807, 10.3390/ijms26146807
- 190With $110 million financing complete, insilico eyes platform, pipeline progressGEN Edge, 7 (1) (2025), pp. 177-180, 10.1089/genedge.7.1.032
- 191Thinking on the use of artificial intelligence in drug discoveryJ Med Chem, 68 (5) (2025), pp. 4996-4999, 10.1021/acs.jmedchem.5c00373
- 192Study shows anti-aging potential for insilico's IPF candidate: company mulls expanding development of TNIK-targeting ISM001-055 after paper shows idiopathic pulmonary fibrosis drug reduces cellular senescenceGEN Edge, 7 (1) (2025), pp. 124-127, 10.1089/genedge.7.1.022
- 193Insilico details AI-designed IBD candidate's path to nomination: ISM5411 emerged in just 12 months from the start of design and engineering to selection of a preclinical prospect, which has since completed Phase I studiesGEN Edge, 6 (1) (2024), pp. 998-1003, 10.1089/genedge.6.01.188
- 194Insilico Medicine reports positive phase IIA results for ISM001-055, a novel first-in-class drug treatment for idiopathic pulmonary fibrosis (IPF) designed using generative AI. PR Newswire
- 195First AI-designed drug, rentosertib, named by USANDrug Target Review (March 14, 2025)
- 196Insilico Medicine sends first generative AI-designed drug for COVID-19 and variants to clinicEurekalert (insilico Medicine) (February 1, 2023)https://www.eurekalert.org/news-releases/980646, Accessed 9th Aug 2025
- 197Transform drug discovery and development with generative artificial intelligenceA. Khamparia, D. Gupta (Eds.), Generative Artificial Intelligence for Biomedical and Smart Health Informatics, John Wiley & Sons (2025), pp. 489-537, 10.1002/9781394280735.ch25
- 198SARS-CoV-2 infection and antiviral strategies: advances and limitationsViruses, 17 (8) (2025), p. 1064, 10.3390/v17081064
- 199Ubiquitin-specific protease inhibitors for cancer therapy: recent advances and future prospectsBiomolecules, 15 (2) (2025), p. 240, 10.3390/biom15020240
- 200Structural and biochemical insights into the mechanism of action of the clinical USP1 inhibitor, KSQ-4279J Med Chem, 67 (17) (2024), pp. 15557-15568, 10.1021/acs.jmedchem.4c01184
- 201AlphaFold accelerates artificial intelligence powered drug discovery: efficient discovery of a novel CDK20 small molecule inhibitorChem Sci, 14 (6) (2023), pp. 1443-1452, 10.1039/d2sc05709c
- 202Beyond boundaries: exploring the transformative power of AI in pharmaceuticalsDiscov Artif Intell, 4 (1) (2024), p. 82, 10.1007/s44163-024-00192-7
- 203First end-to-end generative AI-assisted drug ISM001-055 receives official generic name Rentosertib from USANEurekAlert (InSilico Medicine) (March 6, 2025)https://www.eurekalert.org/news-releases/1076031, Accessed 9th Aug 2025
- 204Clinical development success rates and contributing factors 2011–2021BIO, Informa Pharma Intelligence, and QLS Advisors (2021 Feb 12)https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf, Accessed 9th Aug 2025
- 205Embracing sustainable processes in the pharmaceutical industry with green chemistry and engineeringSustain Chem Process, 1 (1) (2025), pp. 1-10, 10.69709/SusProc.2025.133442
- 206Target-based screening for lead discoveryM. Rudrapal, J. Khan (Eds.), CADD and Informatics in Drug Discovery, Springer (2023), pp. 141-173, 10.1007/978-981-99-1316-9_7
- 207AI in small-molecule drug discovery: black box or crystal ball?Alacritya (2023)https://www.alacrita.com/whitepapers/ai-in-small-molecule-drug-discovery, Accessed 7th Aug 2025
- 208Artificial intelligence in drug discovery and development: transforming challenges into opportunitiesDiscov Pharm Sci, 1 (1) (2025), p. 7, 10.1007/s44395-025-00007-3
- 209Big data in drug discoveryS. Singh (Ed.), Machine Learning and Systems Biology in Genomics and Health, Springer (2022), pp. 17-48, 10.1007/978-981-16-5993-5_2
- 210AI-based personalized drug treatmentA. Khanna, M. El Barachi, S. Jain, M. Kumar, A. Nayyar (Eds.), Artificial Intelligence and Machine Learning in Drug Design and Development, John Wiley & Sons (2024), pp. 369-406, 10.1002/9781394234196.ch12
- 211Potential of artificial intelligence to accelerate drug development for rare diseasesPharmaceut Med, 38 (2) (2024), pp. 79-86, 10.1007/s40290-023-00504-9
- 212The AI-assisted identification and clinical efficacy of baricitinib in the treatment of COVID-19Vaccines, 10 (6) (2022), p. 951, 10.3390/vaccines10060951
- 213Baricitinib as potential treatment for 2019-nCoV acute respiratory diseaseLancet, 395 (10223) (2020), pp. e30-e31, 10.1016/S0140-6736(20)30304-4
- 214Current status of baricitinib as a repurposed therapy for COVID-19Pharmaceuticals (Basel), 14 (7) (2021), p. 680, 10.3390/ph14070680
- 215A systematic review on the contribution of artificial intelligence in the development of medicines for covid-2019J Pers Med, 11 (9) (2021), p. 926, 10.3390/jpm11090926
- 216Artificial intelligence in pharmaceutical industry: revolutionizing drug development and deliveryCurr Artif Intell, 2 (1) (2024), Article E051223224198, 10.2174/0129503752250813231124092946
- 217Generative AI in drug discovery and development: the next revolution of drug discovery and development would be directed by generative AIAnn Med Surg (Lond), 86 (10) (2024), pp. 6340-6343, 10.1097/MS9.0000000000002438
- 218Artificial intelligence and statistical methods for stratification and prediction of progression in amyotrophic lateral sclerosis: a systematic reviewArtif Intell Med, 142 (2023), Article 102588, 10.1016/j.artmed.2023.102588
- 219BenevolentAI pivots back to “TechBio” roots, causing more layoffsFierce Biotech. December, 11 (2024)
- 220Layoffs continued across biopharma in 2024BioSpace (December 31, 2024)https://www.biospace.com/biospace-layoff-tracker, Accessed 9th Aug 2025
- 221BenevolentAI lays off 30% of staff, exits US site as funding gap loomsFierce Biotech. April, 23 (2024)
- 222The impact of artificial intelligence on healthcare: a comprehensive review of advancements in diagnostics, treatment, and operational efficiencyHealth Sci Rep, 8 (1) (2025), Article e70312, 10.1002/hsr2.70312
- 223The emergence of baricitinib: a story of tortoises versus haresClin Infect Dis, 72 (7) (2021), pp. 1251-1252, 10.1093/cid/ciaa940
- 224Digital solutions and the role of AI in healthcare. Part 1: recent innovations in digital therapeuticsPharm Ind, 84 (12) (2022), pp. 1451-1458
- 225Naraghi A, Nourmohammadi R, Behravan I. Real-world applications of artificial intelligence and blockchain in healthcare. SSRN. Preprint. Posted online December 12, 2023. https://doi.org/10.2139/ssrn.4650201
- 226Discovery of selective GluN1/GluN3A NMDA receptor inhibitors using integrated AI and physics-based approachesActa Pharmacol Sin (Published online July 14, 2025), 10.1038/s41401-025-01607-6
- 227In silico chemical experiments in the age of AI: from quantum chemistry to machine learning and backAdv Mater, 36 (30) (2024), Article e2402369, 10.1002/adma.202402369
- 228Computer-aided drug discovery: from traditional simulation methods to language models and quantum computingCell Rep Phys Sci, 5 (12) (2024), Article 102334, 10.1016/j.xcrp.2024.102334
- 229In silico drug repurposing for inflammatory diseases: a systematic review of molecular docking and virtual screening studiesAm J Adv Technol Eng Solut, 2 (4) (2022), pp. 35-64, 10.63125/j1hbts51
- 230Discovery of a potent and selective tyrosine kinase 2 inhibitor: TAK-279J Med Chem, 66 (15) (2023), pp. 10473-10496, 10.1021/acs.jmedchem.3c00600
- 231Alchemical transformations and beyond: recent advances and real-world applications of free energy calculations in drug discoveryJ Chem Inf Model, 64 (19) (2024), pp. 7214-7237, 10.1021/acs.jcim.4c01024
- 232Takeda announces positive results in phase 2b study of investigational TAK-279, an oral, once-daily TYK2 inhibitor, in people with moderate-to-severe plaqueTakeda (March 18, 2023)
- 233Schrödinger reports 63% revenue growth in Q1 2025, prepares to share clinical data for SGR-1505MedPath (May 7, 2025)
- 234Sgr-2921, a potent CDC7 inhibitor, demonstrates significant anti-leukemic responses in patient-derived aml models representing difficult-to-treat diseaseBlood, 142 (suppl 1) (2023), p. 2801, 10.1182/blood-2023-181826
- 235A first-in-human, phase 1, dose escalation study of SGR-2921 as monotherapy in subjects with relapsed/refractory acute myeloid leukemia or myelodysplastic syndromeBlood, 142 (suppl 1) (2023), p. 1548, 10.1182/blood-2023-186036
- 236Schrödinger reports strong fourth quarter and full-year 2024 financial results. Bus Wirehttps://ir.schrodinger.com/press-releases/news-details/2025/Schrdinger-Reports-Strong-Fourth-Quarter-and-Full-Year-2024-Financial-Results/default.aspx (February 26, 2025), Accessed 9th Aug 2025
- 237Exploring marine-derived compounds: in silico discovery of selective ketohexokinase (khk) inhibitors for metabolic disease therapyMar Drugs, 22 (10) (2024), p. 455, 10.3390/md22100455
- 238Nonlinear schrödinger networkarXiv (Preprint. Posted July 19, 2024), Article 2407.14504, 10.48550/arXiv.2407.14504
- 239Computational predictive toxicology modeling for assessing human health risks of novel psychoactive substances (NPS): a case studyAfr J Drug Alcohol Stud, 23 (2) (2025), pp. 115-136, 10.4314/ajdas.v23i2.4
- 240A robust crystal structure prediction method to support small molecule drug development with large scale validation and blind studyNat Commun, 16 (1) (2025), p. 2210, 10.1038/s41467-025-57479-1
- 241Artificial intelligence meets drug discovery: a systematic review on ai-powered target identification and molecular designPreprint (2025)https://www.preprints.org/manuscript/202503.0912/v1, Accessed 9th Aug 2025
- 242Discovery of potential WEE1 inhibitors via hybrid virtual screeningFront Pharmacol, 14 (2023), Article 1298245, 10.3389/fphar.2023.1298245
- 243Advanced computational modeling accelerating small-molecule drug discovery: a growing track record of successX. Huang, R.G. Aslanian, W.H. Tang (Eds.), Contemporary Accounts in Drug Discovery and Development, John Wiley & Sons (2022), pp. 9-25, 10.1002/9781119627784.ch2
- 244Deep learning analysis on images of iPSC-derived motor neurons carrying fALS-genetics reveals disease-relevant phenotypesbioRxiv (Preprint. Posted January 6, 2024), Article 2024.01.04.574270, 10.1101/2024.01.04.574270
- 245Symmetry-based representations for artificial and biological general intelligenceFront Comput Neurosci, 16 (2022), Article 836498, 10.3389/fncom.2022.836498
- 246Plenary sessions Pl1 ELPAG award lectureEur J Hum Genet, 32 (S2) (2024), pp. 799-903, 10.1038/s41431-024-01732-6
- 247Artificial intelligence (AI) in drugs and pharmaceuticalsComb Chem High Throughput Screen, 25 (11) (2022), pp. 1818-1837, 10.2174/1386207325666211207153943
- 248Impact of artificial intelligence (AI) on drug discovery and product developmentInd J Pharm Edu Res, 56 (3s) (2022), pp. s387-s397, 10.5530/ijper.56.3s.146
- 249Companies recognized as innovators for 2021J Commer Biotechnol, 26 (2) (2021), pp. 13-19, 10.5912/jcb986
- 250The physics-AI dialogue in drug designRSC Med Chem, 16 (4) (2025), pp. 1499-1515, 10.1039/d4md00869c
- 251Strategic analysis of deepmind technologies limited: an exploratory case study of ai innovation, ethics, and business evolutionPoornaprajna Int J Teach Res Case Stud (PIJTRCS), 2 (1) (2025), pp. 108-147, 10.5281/zenodo.16811537
- 252Application of artificial intelligence large language models in drug target discoveryFront Pharmacol, 16 (2025), Article 1597351, 10.3389/fphar.2025.1597351
- 253Biopharma Deals Get Smaller and EarlierNature Publishing Group (2025)
- 254Isomorphic labs, an AI offshoot of deepMind, is preparing human trials for AI-designed drugs with the ambition to “solve all diseases.”Fortune (July 6, 2025)
- 255ELVIS lives: 20th century inspires drug developer's AI tools: microsoft-backed 1910 genetics draws on sickle-cell disease discovery and other blasts from the pastGEN Edge, 3 (1) (2021), pp. 259-267, 10.1089/genedge.3.1.041
- 256Small-molecule targeting AMPA-mediated excitotoxicity has therapeutic effects in mouse models for multiple sclerosisSci Adv, 9 (49) (2023), Article eadj6187, 10.1126/sciadv.adj6187
- 257Artificial Intelligence in Drug Development: Patenting and Regulatory AspectsSpringer Nature (2024), 10.1007/978-981-97-2954-8
- 258Discovery of novel trace amine-associated Receptor 5 (TAAR5) antagonists using a deep convolutional neural networkInt J Mol Sci, 23 (6) (2022), p. 3127, 10.3390/ijms23063127
- 259Artificial Intelligence-based computational screening and functional assays identify candidate small molecule antagonists of PTPMU-dependent adhesionInt J Mol Sci, 24 (5) (2023), p. 4274, 10.3390/ijms24054274
- 260Report on an NIH workshop on ultralarge chemistry databaseschemRxiv (Preprint. Posted May 11, 2021), Article 14554803.v1, 10.26434/chemrxiv.14554803.v1
- 261POS0463 a novel, oral, allosteric inhibitor of TYK2 demonstrates in vitro potency, selectivity, and in vivo efficacy in mouse models of psoriasisAnn Rheum Dis, 83 (2024), p. 1131, 10.1136/annrheumdis-2024-eular.2693
- 262AI-based drug discovery company Atomwise sets its sights on inflammatory disease marketGEN Edge, 5 (1) (2023), pp. 683-687, 10.1089/genedge.5.1.132
- 263Patsnap (Product Website) (2025)
- 264Pioneering AI drug discovery & automated researchXtalPi (2025)
- 265China’s AI drug discovery companies land huge deals with Big PharmaRest of World (August 6, 2025)
- 266XtalPi and DoveTree announce landmark $6 billion AI drug discovery collaborationPR Newswire (7 August 2025)
- 267Nvidia's venture arm raises stake in AI drug discoverer genesis therapeutics: NVentures invests further in Stanford spinout to accelerate development of platform designed to optimize molecules for complex targets in oncology, immunologyGEN Edge, 6 (1) (2024), pp. 1010-1016, 10.1089/genedge.6.01.190
- 268Litchfield K, Augustine M, Nene NR, et al. Immunotherapy drug target identification using machine learning and patient-derived tumour explant validation. Preprint. Posted online December 4, 2024. https://doi.org/10.21203/rs.3.rs-5499857/v1
- 269Graph-pMHC: graph neural network approach to MHC class II peptide presentation and antibody immunogenicityBrief Bioinform, 25 (3) (2024), Article bbae123, 10.1093/bib/bbae123
- 270Intelligence mission: berg finds a buyer: investor group BPGbio acquires company's AI platform, built with $400 million in investment, its drug and diagnostic pipelinesGEN Edge, 5 (1) (2023), pp. 151-155, 10.1089/genedge.5.1.32
- 271The potential of iron chelators of the pyridoxal isonicotinoyl hydrazone class as effective antiproliferative agentsBlood, 86 (11) (1995), pp. 4295-4306, 10.1182/blood.V86.11.4295.bloodjournal86114295
- 272The potential of iron chelators of the pyridoxal isonicotinoyl hydrazone class as effective antiproliferative agents III: the effect of the ligands on molecular targets involved in proliferationBlood, 94 (2) (1999), pp. 781-792, 10.1182/blood.V94.2.781
- 273The potential of iron chelators of the pyridoxal isonicotinoyl hydrazone class as effective antiproliferative agents, IV: the mechanisms involved in inhibiting cell-cycle progressionBlood, 98 (3) (2001), pp. 842-850, 10.1182/blood.v98.3.842
- 274The potential of iron chelators of the pyridoxal isonicotinoyl hydrazone class as effective antiproliferative agents II: the mechanism of action of ligands derived from salicylaldehyde benzoyl hydrazone and 2-hydroxy-1-naphthylaldehyde benzoyl hydrazoneBlood, 89 (8) (1997), pp. 3025-3038, 10.1182/blood.V89.8.3025
- 275Pyridoxal isonicotinoyl hydrazone and its analogs: potential orally effective iron-chelating agents for the treatment of iron overload diseaseJ Lab Clin Med, 131 (4) (1998), pp. 306-315, 10.1016/s0022-2143(98)90180-9
- 276Examination of the antiproliferative activity of iron chelators: multiple cellular targets and the different mechanism of action of Triapine compared with desferrioxamine and the potent pyridoxal isonicotinoyl hydrazone analogue 311Clin Cancer Res, 9 (1) (2003), pp. 402-414
- 277Dipyridyl thiosemicarbazone chelators with potent and selective antitumor activity form iron complexes with redox activityJ Med Chem, 49 (22) (2006), pp. 6510-6521, 10.1021/jm0606342
- 278Iron chelators with high antiproliferative activity up-regulate the expression of a growth inhibitory and metastasis suppressor gene: a link between iron metabolism and proliferationBlood, 104 (9) (2004), pp. 2967-2975, 10.1182/blood-2004-05-1866
- 279Antitumor activity of metal-chelating compound Dp44mT is mediated by formation of a redox-active copper complex that accumulates in lysosomesCancer Res, 71 (17) (2011), pp. 5871-5880, 10.1158/0008-5472.CAN-11-1218
- 280Design, synthesis, and characterization of new iron chelators with anti-proliferative activity: structure-activity relationships of novel thiohydrazone analoguesJ Med Chem, 50 (24) (2007), pp. 6212-6225, 10.1021/jm070839q
- 281Synthesis, characterization, and in vitro anticancer activity of copper and zinc bis(thiosemicarbazone) complexesInorg Chem, 58 (20) (2019), pp. 13709-13723, 10.1021/acs.inorgchem.9b01281
- 282Structure-activity relationships of novel iron chelators for the treatment of iron overload disease: the methyl pyrazinylketone isonicotinoyl hydrazone seriesJ Med Chem, 51 (2) (2008), pp. 331-344, 10.1021/jm7012562
- 283Di-2-pyridylketone 4,4-dimethyl-3-thiosemicarbazone (Dp44mT) overcomes multidrug resistance by a novel mechanism involving the hijacking of lysosomal P-glycoprotein (Pgp)J Biol Chem, 290 (15) (2015), pp. 9588-9603, 10.1074/jbc.M114.631283
- 284A mechanism for overcoming P-glycoprotein-mediated drug resistance: novel combination therapy that releases stored doxorubicin from lysosomes via lysosomal permeabilization using Dp44mT or DpCCell Death Dis, 7 (12) (2016), Article e2510, 10.1038/cddis.2016.381
- 285Novel di-2-pyridyl–derived iron chelators with marked and selective antitumor activity: in vitro and in vivo assessmentBlood, 104 (5) (2004), pp. 1450-1458, 10.1182/blood-2004-03-0868
- 286Structure-activity relationships of di-2-pyridylketone, 2-benzoylpyridine, and 2-acetylpyridine thiosemicarbazones for overcoming pgp-mediated drug resistanceJ Med Chem, 59 (18) (2016), pp. 8601-8620, 10.1021/acs.jmedchem.6b01050
- 287Zinc(II)-thiosemicarbazone complexes are localized to the lysosomal compartment where they transmetallate with copper ions to induce cytotoxicityJ Med Chem, 59 (10) (2016), pp. 4965-4984, 10.1021/acs.jmedchem.6b00238
- 288Iron chelators of the dipyridylketone thiosemicarbazone class: precomplexation and transmetalation effects on anticancer activityJ Med Chem, 52 (2) (2009), pp. 407-415, 10.1021/jm801012z
- 289Novel thiosemicarbazone iron chelators induce up-regulation and phosphorylation of the metastasis suppressor N-myc down-stream regulated gene 1: a new strategy for the treatment of pancreatic cancerMol Pharmacol, 80 (4) (2011), pp. 598-609, 10.1124/mol.111.073627
- 290Novel second-generation di-2-pyridylketone thiosemicarbazones show synergism with standard chemotherapeutics and demonstrate potent activity against lung cancer xenografts after oral and intravenous administration in vivoJ Med Chem, 55 (16) (2012), pp. 7230-7244, 10.1021/jm300768u
- 291Novel "hybrid" iron chelators derived from aroylhydrazones and thiosemicarbazones demonstrate selective antiproliferative activity against tumor cellsBlood, 100 (2) (2002), pp. 666-676, 10.1182/blood.v100.2.666
- 2922-acetylpyridine thiosemicarbazones are potent iron chelators and antiproliferative agents: redox activity, iron complexation and characterization of their antitumor activityJ Med Chem, 52 (5) (2009), pp. 1459-1470, 10.1021/jm801585u
- 293Novel thiosemicarbazones of the ApT and DpT series and their copper complexes: identification of pronounced redox activity and characterization of their antitumor activityJ Med Chem, 53 (15) (2010), pp. 5759-5769, 10.1021/jm100561b
- 294Design, synthesis, and characterization of novel iron chelators: structure-activity relationships of the 2-benzoylpyridine thiosemicarbazone series and their 3-nitrobenzoyl analogues as potent antitumor agentsJ Med Chem, 50 (15) (2007), pp. 3716-3729, 10.1021/jm070445z
- 295Synthesis and characterization of quinoline-based thiosemicarbazones and correlation of cellular iron-binding efficacy to anti-tumor efficacyBioorg Med Chem Lett, 22 (17) (2012), pp. 5527-5531, 10.1016/j.bmcl.2012.07.030
- 296A novel class of thiosemicarbazones show multi-functional activity for the treatment of Alzheimer's diseaseEur J Med Chem, 139 (2017), pp. 612-632, 10.1016/j.ejmech.2017.08.021
- 297Methemoglobin formation by Triapine, di-2-pyridylketone-4,4-dimethyl-3-thiosemicarbazone (Dp44mT), and other anticancer thiosemicarbazones: identification of novel thiosemicarbazones and therapeutics that prevent this effectMol Pharmacol, 82 (1) (2012), pp. 105-114, 10.1124/mol.112.078964
- 298Iron chelators of the pyridoxal isonicotinoyl hydrazone class. Relationship of the lipophilicity of the apochelator to its ability to mobilise iron from reticulocytes in vitroCan J Physiol Pharmacol, 72 (6) (1994), pp. 659-666, 10.1139/y94-093
- 299Advantages of novel anti-cancer selenosemicarbazones: preferential reactivity of their Fe(III), Cu(II), and Zn(II) complexes with key physiological reductants/ligands versus isosteric thiosemicarbazonesJ Med Chem, 68 (9) (2025), pp. 9594-9622, 10.1021/acs.jmedchem.5c00374
- 300Innovative N-acridine thiosemicarbazones and their Zn(II) complexes transmetallate with Cu(II): redox activity and suppression of detrimental oxy-myoglobin oxidationInorg Chem, 63 (43) (2024), pp. 20840-20858, 10.1021/acs.inorgchem.4c03642
- 301Isosteric replacement of sulfur to selenium in a thiosemicarbazone: promotion of Zn(II) complex dissociation and transmetalation to augment anticancer efficacyJ Med Chem, 67 (14) (2024), pp. 12155-12183, 10.1021/acs.jmedchem.4c00884
- 302Targeting lysosomes by design: novel N-acridine thiosemicarbazones that enable direct detection of intracellular drug localization and overcome P-glycoprotein (Pgp)-mediated resistanceChem Sci, 15 (37) (2024), pp. 15109-15124, 10.1039/d4sc04339a
- 303Differential transmetallation of complexes of the anti-cancer thiosemicarbazone, Dp4e4mT: effects on anti-proliferative efficacy, redox activity, oxy-myoglobin and oxy-hemoglobin oxidationChem Sci, 15 (3) (2024), pp. 974-990, 10.1039/d3sc05723b
- 304Steric blockade of oxy-myoglobin oxidation by thiosemicarbazones: structure-activity relationships of the novel PPP4pT seriesJ Med Chem, 66 (22) (2023), pp. 15453-15476, 10.1021/acs.jmedchem.3c01612
- 305Innovative thiosemicarbazones that induce multi-modal mechanisms to down-regulate estrogen-, progesterone-, androgen- and prolactin-receptors in breast cancerPharmacol Res, 193 (2023), Article 106806, 10.1016/j.phrs.2023.106806
- 306The thiosemicarbazone, DpC, broadly synergizes with multiple anti-cancer therapeutics and demonstrates temperature- and energy-dependent uptake by tumor cellsBiochim Biophys Acta Gen Subj, 1866 (8) (2022), Article 130152, 10.1016/j.bbagen.2022.130152
- 307Designing tailored thiosemicarbazones with bespoke properties: the styrene moiety imparts potent activity, inhibits heme center oxidation, and results in a novelJ Med Chem, 66 (2) (2023), pp. 1426-1453, 10.1021/acs.jmedchem.2c01600
- 308A class of iron chelators with a wide spectrum of potent antitumor activity that overcomes resistance to chemotherapeuticsProc Natl Acad Sci U S A, 103 (40) (2006), pp. 14901-14906, 10.1073/pnas.0604979103
- 309Breaking the cycle: targeting of NDRG1 to inhibit bi-directional oncogenic cross-talk between pancreatic cancer and stromaFASEB J, 35 (2) (2021), Article e21347, 10.1096/fj.202002279R
- 310Development of pyridyl thiosemicarbazones as highly potent agents for the treatment of malaria after oral administrationJ Antimicrob Chemother, 74 (10) (2019), pp. 2965-2973, 10.1093/jac/dkz290
- 311Multi-modal mechanisms of the metastasis suppressor, NDRG1: inhibition of WNT/
*β*-catenin signaling by stabilization of protein kinase C*α*J Biol Chem, 300 (7) (2024), Article 107417, 10.1016/j.jbc.2024.107417 - 312AI widens search spaces and promises more hits in drug discovery: AI platforms are enhancing discovery efforts across modalities—small-molecule drugs, RNA-based therapeutics, and protein-based therapeuticsGenet Eng Biotechnol News, 42 (4) (2022), pp. 34-3638
- 313Innovation in the Chinese BioPharma sector: from me-too to first-in-classBiopharma in China: Innovation, Trends and Dealmaking, Springer (2024), pp. 71-99, 10.1007/978-981-97-1471-1_4
- 314A study of TAK-062 in treatment of active celiac disease in participants attempting a gluten-free dietTakeda (August 20, 2025)https://clinicaltrials.gov/study/NCT05353985, Accessed 10th Oct 2025
- 315A study of TAK-062 in treatment of active celiac disease in participants attempting a gluten-free dietTakeda (August 19, 2025)https://www.guidelinecentral.com/clinical-trial/?id=NCT05353985, Accessed 30th Oct 2025
- 316Immunogenicity and safety study of SK SARS-CoV-2 recombinant nanoparticle vaccine adjuvanted with AS03 (COVID-19). SK Bioscience Co., Ltdhttps://clinicaltrials.gov/study/NCT05007951?tab=table (August 04, 2025), Accessed 30th Oct 2025
- 317Safety and immunogenicity study of SARS-CoV-2 nanoparticle vaccine (GBP510) adjuvanted with or without AS03 (COVID-19). SK Bioscience Co., Ltdhttps://clinicaltrials.gov/study/NCT04750343?utm_source=chatgpt.com (October 05, 2025), Accessed 9th Aug 2025
- 318Safety and immunogenicity of a SARS-CoV-2 recombinant protein nanoparticle vaccine (GBP510) adjuvanted with AS03: a randomised, placebo-controlled, observer-blinded phase 1/2 trialEClinicalmedicine, 51 (2022), Article 101569, 10.1016/j.eclinm.2022.101569
- 319Scratch that? de novo antibody design enters the AI drug discovery toolboxGEN Edge, 7 (1) (2025), pp. 345-351, 10.1089/genedge.7.1.063
- 320Revolutionizing drug development: AI-driven predictive modeling for accelerated small molecule and biologic therapeuticsWell Test J, 33 (suppl 2) (2024), pp. 668-691
- 321Delivering Innovation: 2020 Oncology Market OutlookMcKinsey & Company (2020)
- 322Biopharma licensing and M&A trends in the 21st-century landscapeJ Commer Biotechnol, 25 (3) (2020), p. 37, 10.5912/jcb943
- 323An 8-year prospective, observational, multi-centre post-marketing safety surveillance study conducted in South Korea (2014–2022) following the introduction of GSK's inactivated quadrivalent seasonal influenza vaccine (fluarix tetra) for subjects aged 6 months and olderDrug Saf, 47 (4) (2024), pp. 365-375, 10.1007/s40264-024-01395-8
- 324Public-Private-Partnerships in Drug Research and DevelopmentSpringer (2024), 10.1007/978-3-031-75806-5
- 325The first European Union approval of a new medicine to treat cardiovascular diseases in 2023: why is it important to collaborate with the European Medicines Agency?Eur Heart J, 45 (1) (2024), pp. 7-9, 10.1093/eurheartj/ehad426
- 326Regulatory science to 2025: an analysis of stakeholder responses to the European Medicines Agency's strategyFront Med (Lausanne), 7 (2020), p. 508, 10.3389/fmed.2020.00508
- 327How the FDA guidance on the use of AI will impact drug development PharmaLex
- 328European regulator clarifies guidance on the use of ai in the medicinal product lifecycleGoodLifeSci (Sidley Austin LLP) (October 22, 2024)
- 329A survey on bias and fairness in machine learningACM Comput Surv, 54 (6) (2021), pp. 1-35, 10.1145/3457607
- 330Bias in data-driven artificial intelligence systems–an introductory surveyWires Data Min Knowl, 10 (3) (2020), Article e1356, 10.1002/widm.1356
- 331Ethical considerations in AI addressing bias and fairness in machine learning modelsJ Knowl Learn Sci Technol, 1 (1) (2022), pp. 130-138, 10.60087/jklst.vol1.n1.p138
- 332The role of data bias in AI-driven healthcare decision-making: impacts and mitigation approachesAalto University (2025)https://urn.fi/URN:NBN:fi:aalto-202506154673, Accessed 9th Aug 2025
- 333The Ethical Implications of Artificial Intelligence: a Deep Dive into Bias, Fairness, and Transparency. Researchgatehttps://www.researchgate.net/profile/Lawrence-Emma/publication/386045670_The_Ethical_Implications_of_Artificial_Intelligence_A_Deep_Dive_into_Bias_Fairness_and_Transparency/links/6740946e6dedd318c8939a95/The-Ethical-Implications-of-Artificial-Intelligence-A-Deep-Dive-into-Bias-Fairness-and-Transparency.pdf (November 6, 2024), Accessed 9th Aug 2025
- 334Review of AI/ML applications in the medicines lifecycleHorizon Scanning Short Report. 9 July 2025
- 335Regulating the use of ai in drug development: legal challenges and compliance strategiesFood and Drug Law Institute (FDLI) (July 2025)
- 336AI-driven decision-making applications in pharmaceutical sciencesT.V.T. Nguyen, N.T.M. Vo (Eds.), Using Traditional Design Methods to Enhance AI-Driven Decision Making, IGI Global Scientific Publishing (2024), pp. 1-63, 10.4018/979-8-3693-0639-0.ch001
- 337Ethical and regulatory consideration in AI-assisted drug development2nd DMIHER International Conference on Artificial Intelligence in Healthcare, Education and Industry (IDICAIEI), IEEE (2024), pp. 1-6, 10.1109/idicaiei61867.2024.10842700
- 338Accelerating biomolecular modeling with atomworks and rf3bioRxiv (Posted August 14, 2025), Article 2025.08.14.670328, 10.1101/2025.08.14.670328
- 339Boltz-1 democratizing biomolecular interaction modelingbioRxiv (Posted November 20, 2024), Article 2024.11.19.624167, 10.1101/2024.11.19.624167
- 340Chai-1: decoding the molecular interactions of lifebioRxiv (Posted October 11, 2024), Article 2024.10.10.615955, 10.1101/2024.10.10.615955
- 341DeepChem. GitHub repositoryhttps://github.com/deepchem/deepchem?utm_source=chatgpt.com (April 3, 2025), Accessed 30th Oct 2025
- 342RDKit. GitHub
*repository*https://github.com/rdkit/rdkit?utm_source=chatgpt.com (2025), Accessed 30th Oct 2025 - 343Autonomous chemistry: navigating self-driving labs in chemical and material sciencesMatter, 7 (7) (2024), pp. 2382-2398, 10.1016/j.matt.2024.06.003
- 344A revolutionary paradigm in chemistry and materials science research: self-driving laboratoriesChem Commun (Camb), 61 (55) (2025), pp. 10026-10038, 10.1039/d5cc01959a
- 345Augmenting DMTA using predictive AI modelling at AstraZenecaDrug Discov Today, 29 (4) (2024), Article 103945, 10.1016/j.drudis.2024.103945
- 346The implementation and impact of chemical high-throughput experimentation at AstraZenecaACS Catal, 15 (7) (2025), pp. 5229-5256, 10.1021/acscatal.4c07969
- 347Advancing automation in high-throughput screening: modular unguarded systems enable adaptable drug discoveryDrug Discov Today, 27 (8) (2022), pp. 2051-2056, 10.1016/j.drudis.2022.03.010
- 348insitro to present at the 42nd Annual J.P. Morgan Healthcare Conferencehttps://www.businesswire.com/news/home/20231220789179/en/insitro-to-Present-at-the-42nd-Annual-J.P.-Morgan-Healthcare-Conference (Published January 2024), Accessed 9th Aug 2025
- 349How emerald cloud lab is revolutionizing the laboratory using AWShttps://aws.amazon.com/startups/learn/how-emerald-cloud-lab-is-revolutionizing-the-laboratory-using-aws (2025), Accessed 28th Aug 2025
- 350Robotic fluidic coupling and interrogation of multiple vascularized organ chipsNat Biomed Eng, 4 (4) (2020), pp. 407-420, 10.1038/s41551-019-0497-x
- 351Autonomous chemical experiments: challenges and perspectives on establishing a self-driving labAcc Chem Res, 55 (17) (2022), pp. 2454-2466, 10.1021/acs.accounts.2c00220
- 352Self-driving laboratories for chemistry and materials scienceChem Rev, 124 (16) (2024), pp. 9633-9732, 10.1021/acs.chemrev.4c00055
- 353Science acceleration and accessibility with self-driving labsNat Commun, 16 (1) (2025), p. 3856, 10.1038/s41467-025-59231-1
- 354Autonomous mobile robots for exploratory synthetic chemistryNature, 635 (8040) (2024), pp. 890-897, 10.1038/s41586-024-08173-7
- 355Ai-driven robotics and automation: the evolution of human-machine collaborationJ World Sci, 4 (4) (2025), pp. 422-437, 10.58344/jws.v4i4.1389
- 356AI-Powered Robotics and Automation: innovations, challenges, and pathways to the futureEJCSIT, 13 (1) (2025), pp. 33-44, 10.37745/ejcsit.2013/vol13n13344
- 357Zhang P, Zhang H, Xu H, et al. Autonomous generalist scientist: towards and beyond human-level scientific research with agentic and embodied AI and robots Preprint. Posted online August 2024. https://doi.org/10.13140/RG.2.2.35148.01923.
- 358AI in robotics: perception, planning, and human-robot interactionG.A. Kumar, K.C. Sreedhar, M. Swathi (Eds.), Artificial Intelligence:
*Foundations*,*Frontiers, and Future*, Quill Tech Publications (2025), pp. 258-262 - 359Scaling laws in scientific discovery with AI and robot scientistsarXiv (Preprint. Posted March 28, 2025), Article 2503.22444, 10.48550/arXiv.2503.22444
- 360Large language models for chemistry roboticsAuton Robots, 47 (8) (2023), pp. 1057-1086, 10.1007/s10514-023-10136-2
- 361Innovating robot-assisted surgery through large vision modelsNat Rev Electr Eng, 2 (5) (2025), pp. 350-363, 10.1038/s44287-025-00166-6
- 362Large language models for robotics: a surveyarXiv (Preprint. Posted November 13, 2023), Article 2311.07226, 10.48550/arXiv.2311.07226
- 363Foundation models in robotics: applications, challenges, and the futureInt J Robot Res, 44 (5) (2025), pp. 701-739, 10.1177/02783649241281508
- 364Humanoid robotics in material and chemistry experimentsSci China Mater, 68 (7) (2025), pp. 2240-2245, 10.1007/s40843-025-3384-9
- 365Robotics and automation: revolutionizing Research and DevelopmentD. Datta, V. Jain, B. Halder, U. Raychaudhuri, S. Kumar (Eds.), Evolving Landscapes of Research and Development: Trends, Challenges, and Opportunities, IGI Global Scientific Publishing (2025), pp. 313-338, 10.4018/979-8-3693-7101-5.ch014
- 366Humanoid robots like tesla optimus and the future of supply chains: enhancing efficiency, sustainability, and workforce dynamicsAutomation, 6 (1) (2025), p. 9, 10.3390/automation6010009
- 367Robotic automation of pharmaceutical and life science industriesV.A. Saharan (Ed.), Computer Aided Pharmaceutics and Drug Delivery: an Application Guide for Students and Researchers of Pharmaceutical Sciences, Springer (2022), pp. 381-414, 10.1007/978-981-16-5180-9_12
- 368Artificial intelligence and robotics: a step forward towards drug discoveryNeuroQuantology, 20 (10) (2022), pp. 250-284, 10.14704/nq.2022.20.10.NQ55020
- 369Ethical considerations and regulatory compliance in AI driven diagnosticsA. Kumar, F. Ortiz-Rodriguez, J.B. De Vasconcelos, P. Kumar Dutta, H.K. Saini, P.S. Rathore (Eds.), Adversarial Deep Generative Techniques for Early Diagnosis of Neurological Conditions and Mental Health Practises: Theoretical Insights with Practical Applications, Springer (2025), pp. 91-113, 10.1007/978-3-031-91147-7_5
- 370Artificial intelligence in natural product drug discovery: current applications and future perspectivesJ Med Chem, 68 (4) (2025), pp. 3948-3969, 10.1021/acs.jmedchem.4c01257
- 371AI-driven drug discovery and repurposing for neurodegenerative disordersMachine Learning for Neurodegenerative Disorders, CRC Press (2024), pp. 80-124
- 372Artificial intelligence (AI) provided early detection of the coronavirus (COVID-19) in China and will influence future Urban health policy internationallyAI, 1 (2) (2020), pp. 156-165, 10.3390/ai1020009
- 373Efforts of the Pharmaceuticals and Medical Devices Agency of Japanese regulatory agency in supporting biosimilar development and disseminate informationNaunyn-Schmiedebergs Arch Pharmacol, 398 (7) (2025), pp. 9357-9365, 10.1007/s00210-025-03874-w
- 374Innovative drugs approved in China after registration classification reform: current status, disparities, and challengesClin Pharmacol Ther (Published online October 11, 2025), 10.1002/cpt.70084
- 375Artificial intelligence in small-molecule drug discovery: a critical review of methods, applications, and real-world outcomesPharmaceuticals (Basel), 18 (9) (2025), p. 1271, 10.3390/ph18091271
- 376Lousqui D. AI regulation and the new geography of influence. SSRN. Preprint. Posted online January 13, 2025.
- 377Value of artificial intelligence in neuro-oncologyLancet Digit Health, 7 (9) (2025), Article 100876, 10.1016/j.landig.2025.100876
- 378Revolutionizing new drug discovery: harnessing AI and machine learning to overcome traditional challenges and accelerate targeted therapiesArtif Intell Health, 2 (2) (2024), pp. 29-40, 10.36922/aih.4423
- 379Large language model-driven knowledge discovery for designing advanced micro/nano electrocatalyst materialsCMC, 84 (2) (2025), pp. 1921-1950, 10.32604/cmc.2025.067427
- 380From pixels to generalization: ensuring information security and model performance with design principles for synthetic image data in deep learningS. Kuehnel, I. Nastjuk, S. Sackmann, S. Trang (Eds.),
*Proceedings of the 3rd International Workshop on Current Information Security and Compliance Issues in Information Systems Research (CIISR 2023), Co-located with the 18**th**International Conference on Wirtschaftsinformatik (WI 2023), Paderborn, Germany, September 18, 2023*, CEUR Workshop Proceedings (2023), pp. 49-61 - 381Multimodal large language models in health care: applications, challenges, and future outlookJ Med Internet Res, 26 (2024), Article e59505, 10.2196/59505
- 382Large language models in genomics-a perspective on personalized medicineBioengineering (Basel), 12 (5) (2025), p. 440, 10.3390/bioengineering12050440
- 383Sanofi signs US $1.2 billion AI drug discovery deal with Insilico medicinePharm Deals Rev, 2022 (11) (2022), p. 11
- 384A novel highly selective allosteric inhibitor of tyrosine kinase 2 (TYK2) can block inflammation- and autoimmune-related pathwaysCell Commun Signal, 21 (1) (2023), p. 287, 10.1186/s12964-023-01299-7

## Cited by (5)

### The isoflavone metabolites, O-desmethylangolensin and (S)-equol, relax isolated arteries ex vivo and decrease arterial blood pressure in vivo

2026, Biochimica Et Biophysica Acta Molecular Basis of Disease### Artificial intelligence–assisted drug discovery in 2025: Faster, but is it better? The robots are coming, look out!

2026, Pharmacological Reviews### Novel Compounds as MALT1 Inhibitors for Treating Cancer

2026, ACS Medicinal Chemistry Letters