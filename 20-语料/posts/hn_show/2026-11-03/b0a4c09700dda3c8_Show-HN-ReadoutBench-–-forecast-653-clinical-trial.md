---
type: "corpus"
item_id: "b0a4c09700dda3c8"
title: "Show HN: ReadoutBench – forecast 653 clinical trials before they report"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50343521"
project_url: "https://readoutbench.com/"
author: "lhein"
published_at: "2026-11-02T20:50:38Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_lhein
  - story_50343521
  - show_hn
metrics: {"points": 3, "comments": 3, "engagement_velocity": 3}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: ReadoutBench – forecast 653 clinical trials before they report

> [!info] 一句话导读
> Why How it differs Trials Leaderboard Questions Paper

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50343521>
> 指标：点赞=3 · 评论=3 · engagement_velocity=3
> 作者：lhein　|　发布：2026-11-02T20:50:38Z
> 项目链接：<https://readoutbench.com/>
> 采集：2026-11-03T09:40:36+08:00　|　id：`b0a4c09700dda3c8`

## 正文

ReadoutBench
 Why How it differs Trials Leaderboard Questions Paper
Round 1 · open until 15 November 2026
Forecast clinical trials before they read out.
653 company-run phase 2 and 3 trials, randomized, completing between July 2026 and March 2027. Forecast whether each one works, by how much, and whether a result comes out at all. Entries are scored as the results arrive, over the next fourteen months.
Enter the round
 Download the trials
 Read the rules
 Read the paper
653 trials in the round
548 with a p_met question
15 Nov submissions close, 23:59:59 UTC
30 Jun 2027: the ranked result
Why
A woman whose lung cancer has come back after two lines of treatment is offered a place in a phase 3 trial. Half the patients get a new antibody-drug conjugate, half get docetaxel, a chemotherapy approved in 1996. Whether the new arm does better is what the trial is there to find out, and until it reads out, everyone involved works from some estimate of the odds. How good are those estimates? When 148 cancer specialists forecast 25 ongoing trials, their Brier score was 0.22, a little better than the 0.25 you get by saying 50% every time ( Doussau et al. 2023 ). Investigators forecasting their own trials did no better than that coin ( Benjamin et al. 2022 ).
I think AI models will be asked to make that kind of estimate, and an estimate is only worth as much as its track record. ReadoutBench builds one at the level of trials: hundreds of real trials, forecast before they report and scored when they do.
The obvious guess is strong. About 64% of the reported trials the registry model learned from met their primary endpoint, so saying yes to everything already scores well. Beating that takes judgement about this drug and this design (and sometimes about a company's habit of describing a miss as a success).
If the best model cannot beat a logistic regression on seven registry fields, that is worth knowing.
How it differs
Most medical AI benchmarks are exams with an answer key: MedQA and its relatives. Answer keys end up in training data, and a score on a test that has leaked says little. A question about a trial that has not reported has no key to leak. The closest benchmark to this one is CT Open , a live clinical-trial outcome challenge, and it is worth a look. The differences are deliberate:
CT Open ReadoutBench
What you give A class per outcome measure: did it reach statistical significance A probability per trial, plus the control-arm value and the effect size, subgroups, safety, whether a result comes out at all, and trial operations
Scoring Macro-F1 and balanced accuracy Brier score, a proper scoring rule: a confident miss costs more than a hedged one. Calibration shown for every entry
The bar Language models next to classical models Ranked in tiers against a published registry model; three frontier-model references are hashed before opening and published at the close
How results are read An automated, model-based pipeline over reported results Two independent labelling agents per trial that never see a forecast, reading press releases, filings, congress abstracts, papers and posted registry results; disagreements settled by the organiser, every label published with its sources
Who enters Any method Two boards: one model with the round's instructions unchanged, or anything at all
Press releases matter here: a company often announces a readout months before it posts results on ClinicalTrials.gov, and the first public statement is what a forecast is scored against.
Three of the 653
NCT06662383 Phase 3 Eli Lilly and Company
A Study of Retatrutide (LY3437943) Compared to Tirzepatide (LY3298176) in Adults Who Have Obesity
Experimental Retatrutide (dose not stated) (n = 400)
 Control Tirzepatide (dose not stated) (n = 400)
 Primary endpoint Percent change in body weight from baseline to week 80
 Design superiority; primary completion 2026-11
You forecast: the probability it meets its primary objective; the mean percent change in body weight from baseline to week 80 in the tirzepatide arm; the difference in mean percent change in body weight, experimental minus control, each as a median and an 80% range; plus whether a result comes out by each deadline.
Two drugs from the same company, head to head. The control arm is itself one of the strongest obesity drugs there is.
NCT05757869 Phase 3 Janssen Research & Development, LLC
A Study of Milvexian Versus Apixaban in Participants With Atrial Fibrillation
Experimental Milvexian, oral factor XIa inhibitor (dose not stated), with apixaban-matching placebo (n = 10,142)
 Control Apixaban (dose not stated), with milvexian-matching placebo (n = 10,142)
 Primary endpoint Time to first stroke or non-CNS systemic embolism in atrial fibrillation, over up to 4 years of follow-up
 Design non-inferiority; primary completion 2026-12-08
You forecast: the probability it meets its primary objective; the annualized event rate of stroke or non-CNS systemic embolism in the apixaban arm; the hazard ratio, experimental vs control, each as a median and an 80% range; plus whether a result comes out by each deadline.
Twenty thousand patients. Factor XIa inhibitors promise less bleeding; the question is whether they prevent as many strokes.
NCT06356311 Phase 3 Merck Sharp & Dohme LLC
A Study to Evaluate Sacituzumab Tirumotecan (MK-2870) in Advanced/Metastatic Gastroesophageal Adenocarcinoma (MK-2870-015)
Experimental Sacituzumab tirumotecan (MK-2870) (n = 237)
 Control Treatment of physician's choice (trifluridine-tipiracil, irinotecan, paclitaxel or docetaxel) (n = 236)
 Primary endpoint Overall survival (time from randomization to death from any cause), up to about 31 months
 Design superiority; primary completion 2026-10-19
You forecast: the probability it meets its primary objective; the median overall survival in the treatment of physician's choice arm, in months; the hazard ratio for death, experimental vs control, each as a median and an 80% range; plus whether a result comes out by each deadline.
Overall survival, the hardest endpoint there is, against chemotherapy of the physician's choice.
Browse all 653 trials
All trials With a p_met question Operations only
How it works
Download
 Each trial has a packet: its ClinicalTrials.gov record as pulled for the round, a question card fixing the endpoint and arms, and its operations questions.
Forecast
 One line per trial: probabilities, and for most efficacy trials the control-arm value and the effect. forecast_instructions.md is the prompt the Models board uses.
Upload
 Sign in with Hugging Face and upload on the round's page. The file is checked at once. Up to three entries per account; each upload is logged in public.
Get scored
 Two independent labelling agents read each result as it comes out, and every label is published with its sources. Scores at 31 March 2027 (early look), 30 June 2027 (ranked) and 31 December 2027 (supplementary).
Two boards
Models
 One model, answering from the packet alone with the round's instructions unchanged. It compares models.
Open
 Anything else: any harness, tools, web access or several models. It shows how far a system can go.
What is scored
Trials Will it work? p_met Numbers Will a result be out? Operations
536 superiority and non-inferiority trials yes 509 (control and effect; subgroups on 275) yes yes
12 equivalence trials yes: equivalence shown no yes yes
105 trials with no efficacy goal no no no yes
Two rankings, both in tiers: p_met against the registry model, and the number score against the Opus reference entry. Everything else (safety, key secondary, next step, timing, operations) is shown on each entry's scorecard and never ranked.
Leaderboard
First scores on 31 March 2027; the ranked result on 30 June 2027. Until then the board holds the five reference entries. The two baselines are in the dataset with their forecasts, training table and code. The three model entries are sealed until submissions close, so nobody can copy the Opus reference that scales the number score; their SHA-256 hashes are in the paper , so they cannot be changed in the meantime.
Entry Board What it is Brier, p_met Tier
B1 · registry model reference Logistic regression on seven registry fields, fitted on reported trials. The bar for the ranking pending the reference
B0 · base rate reference The same probability for every trial pending pending
Claude Opus 5.5 Models Packet only, the round's instructions unchanged. The reference for the number score pending pending
Claude Sonnet 5.5 Models Same rules pending pending
Claude Haiku 5.5 Models Same rules pending pending
Are the answers really unknown?
Before launch, every trial was searched for a public result, an announced stop or a statement on its primary outcome: PubMed, the web in the sponsor's language, congress abstracts, and sponsors' pipeline documents and quarterly reports. Each check, with its searches and pages, is in the repository .
The checks cannot be perfect, so the scoring does not depend on them. When each trial is labelled, its first public statement is dated. Any trial with a result public before the round closed (a missed one from before launch, or one that came out during the two open weeks) is dropped from scoring and listed. Only results that appear after the close count.
85 trials are marked below the bar : the pre-launch checks could not search them as deeply as the rest. They are scored, and the leaderboard also shows each entry without them.
Questions
Can I use web search, tools or several models? On the Open board, yes: any model, prompt, tools, retrieval, web access and people in the loop, declared with the entry. The Models board is one model answering from the packet alone, with the round's instructions unchanged.
Can people enter, not only AI systems? Yes, on the Open board, with human_in_the_loop set. A forecast for every trial with a p_met question is required (548), so a 50-trial hand-picked subset is not an entry; a spreadsheet and a lot of evenings is.
What counts as "met"? The trial meets its primary objective as registered and fixed on its question card. "Positive" or "encouraging" with no statement on the primary endpoint keeps the question open; if nothing clearer comes by the deadline, it counts as not met. The rules list every case.
What if a trial never reports? It is not scored for p_met at that deadline. Whether a result comes out at all is its own question ( p_public ), scored separately.
What if a result was already out? Any trial whose first public statement on its primary result came before the round closed is dropped from scoring and listed, whether the checks before launch missed it or it came out during the two open weeks.
Can I change my entry? Upload again before the close; the last upload counts. Every upload is logged in a public list with its time and file fingerprint. Up to three entries per Hugging Face account, each a different harness.
Why only company-run trials? Companies announce readouts fast, often by press release within weeks of the primary analysis. Academic trials can take years to publish, which would leave most of the round unscored.
Does it cost anything? No. Entries report their own cost per trial (compute and API), shown with the entry.
Dates
1 Nov 2026 Round opens. Trial files, rules and the two baseline entries published; the paper, with the hashes of all five reference entries, deposited on Zenodo.
15 Nov 2026 Submissions close at 23:59:59 UTC (00:59:59 CET on 16 November). The three model entries are published and can be checked against their hashes.
31 Mar 2027 Early look: results public by this date.
30 Jun 2027 Ranked result: results public by this date.
31 Dec 2027 Final, unranked pass, which also covers slower reporters.
ReadoutBench is a research benchmark about forecasting trial results from public information. It is not medical advice and not a tool for decisions about individual patients, and nothing on it is investment advice.
ReadoutBench is run by Lucas Heinrich. Contact: contact@readoutbench.com · Code and checks: GitHub (MIT) · Paper

## 评论（3/3）

> **jchaselubitz** · 2026-11-02T20:53:53.000Z　
> This is very cool!

---

> **jchaselubitz** · 2026-11-02T20:58:45.000Z　
> Are there other projects like this? Also, what results have you been able to find on historical data?

---

> **lhein** · 2026-11-02T21:08:47.000Z　
> Most similar is CT Open, which is also a trial outcome predictor. ForecastBench does the same but for general questions.For 111 trials reported after the cutoff date, Opus/Sonnet/Haiku was too pessimistic (~59% expected vs. 73% observed) and was beaten by a plain regression on the registry features. Their ordering of the trials was good though, and combining with the regression got them 8% accuracy increase. Small sample size; thus, the online version

## 导航

- 项目页：[[10-项目/readoutbench.com_0974e065]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
