---
type: "corpus"
item_id: "9197aef575ee69e1"
title: "Show HN: ZeroPoint – CPU-only decision model that can answer 'none of these'"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50429147"
project_url: "https://github.com/Javihaus/zeropoint"
author: "jhausmaval"
published_at: "2026-11-09T18:06:06Z"
captured_at: "2026-11-10T09:49:42+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_jhausmaval
  - story_50429147
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: ZeroPoint – CPU-only decision model that can answer 'none of these'

> [!info] 一句话导读
> GitHub - Javihaus/zeropoint: CPU-first, energy-based decision model. Picks the option that fits, or says none does, without being told that none is an option

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50429147>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：jhausmaval　|　发布：2026-11-09T18:06:06Z
> 项目链接：<https://github.com/Javihaus/zeropoint>
> 采集：2026-11-10T09:49:42+08:00　|　id：`9197aef575ee69e1`

## 正文

GitHub - Javihaus/zeropoint: CPU-first, energy-based decision model. Picks the option that fits, or says none does, without being told that none is an option · GitHub

## About

CPU-first, energy-based decision model. Picks the option that fits, or says none does, without being told that none is an option

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| .github | .github | | |
| assets | assets | | |
| benchmarks | benchmarks | | |
| docs | docs | | |
| fuzz | fuzz | | |
| requirements | requirements | | |
| scripts | scripts | | |
| src/ zeropoint | src/ zeropoint | | |
| tests | tests | | |
| tools | tools | | |
| training | training | | |
| .gitattributes | .gitattributes | | |
| .gitignore | .gitignore | | |
| BENCHMARK.md | BENCHMARK.md | | |
| CHANGELOG.md | CHANGELOG.md | | |
| CODE_OF_CONDUCT.md | CODE_OF_CONDUCT.md | | |
| CONTRIBUTING.md | CONTRIBUTING.md | | |
| LANGUAGES.md | LANGUAGES.md | | |
| LICENSE | LICENSE | | |
| NOTICE | NOTICE | | |
| README.md | README.md | | |
| SECURITY.md | SECURITY.md | | |
| mkdocs.yml | mkdocs.yml | | |
| pyproject.toml | pyproject.toml | | |
| View all files | | | |

# ZeroPoint: a CPU-first, energy-based decision model

Picks the option that fits,

or says none does,

without being told that none is an option

ZeroPoint is a small energy-based model. It measures how well each option fits the text and compares it with a fixed level, zero, that stands for none of these. An option that fits no better than zero gets almost no probability, so ZeroPoint can answer none with confidence.

How to read the numbers. Half of the cases have no right option. A random guess, with none counted as one more option, gets about 13% right. Always answering none gets 50% on the first row and 0% when one option is right.

| | ZeroPoint | Strands Decider 2B ¹ | Clef-flash ² | Semantic Router | Zero-shot NLI |
| --- | --- | --- | --- | --- | --- |
| Accuracy: right answer, none included | 53.6% | 58.6% | 53.3% | 19.4% | 20.7% |
| Same answer whatever the order: decisions that change when the same options are listed in another order. Lower is better | 0% | 7.3% | 0% | 0.6% | 0% |
| Accuracy when one option is right | 43.8% | 58.4% | 56.2% | 38.9% | 41.3% |
| Silent mistakes: no option fits, yet it answers with ≥ 90% confidence. Lower is better | 7.8% | 0.0% | 5.8% | – ³ | 22.2% |
| Confident when right: right answers stated with ≥ 90% confidence. Higher is better, and it is what makes the row above comparable: a model that never states 90% cannot make a silent mistake | 66% | 37% | ⟨Clef⟩% | – ³ | ⟨NLI⟩% |
| Latency, median on a CPU (on a GPU) | 42 ms | 6,770 ms (93 ms)⁴ | + 20,000 ms (156 ms)⁵ | 17 ms | 1,697 ms |
| Model size | 89 MB | 4.8 GB | 19 GB | 91 MB | 369 MB |
| Runs on | CPU | GPU | GPU | CPU | CPU or GPU |

 Measured on the three tests no model is likely to have seen in training: a 2,000-case test and two support-ticket tests, 300 cases of each, 900 in all, half of them with no right option. ZeroPoint, Semantic Router and zero-shot NLI on a 2-core CPU with 2 threads, one case at a time. Semantic Router 1.1.1 with its default encoder; zero-shot NLI with DeBERTa-v3-base. ¹ AWS, Apache 2.0, and ² Cloudflare, Apache 2.0, each with "None of these" added to every list as one more option, so that it can answer none. ³ Semantic Router gives similarities, not probabilities. ⁴ On a CPU: measured on another 2-core CPU, on 118 cases of the 2,000-case test, where ZeroPoint takes 18 ms. On a GPU: an NVIDIA L4, on the 900 cases. ⁵ On a CPU: not measured, because Clef-flash needs about 19 GB of memory; a lower bound estimated from its size, 4.5 times that of Strands Decider. On a GPU: an NVIDIA L4, on the 900 cases. Per-test results, other confidence thresholds and the scripts to run it all again: BENCHMARK.md.

Important

Hosted LLMs, through an API, are right in 57–60% of these cases, a few points more than ZeroPoint, and take 18 to 55 times longer. See the details here.

## ZeroPoint at a glance

| Size | Latency | Deterministic | Multilingual |
| --- | --- | --- | --- |
| 89 MB, no GPU The model ships inside the package: nothing is downloaded at run time. Strands Decider needs 4.8 GB and a GPU; Clef-flash 19 GB. | 42 ms on a CPU Median on the tests above, on 2 CPU cores. On another 2-core CPU, ZeroPoint takes 18 ms per decision and Strands Decider 6.8 s. | Same input, same answer The order of the options never changes the decision; Strands Decider's changes in 7% of cases, and in 13% of support tickets whose own queue is not on the list. Same decisions on Linux, macOS and Windows, tested on every change. | 25 languages EU languages in the Latin script, plus Catalan, Basque and Galician. Which ones, and why. |

Routing a support ticket, finding the intent behind a request, sending a document to the right process: each means picking one option from a list. A classifier always picks something, even when the right option is not on the list or the text has nothing to do with the task. ZeroPoint can answer none, and the probability of none comes out of the same calculation as the probability of each option.

## Quick start

```
pip install zeropoint
```

```
from zeropoint import ZeroPoint

zp = ZeroPoint()
zp.decide("Can you move 200 euros from my savings to my checking account?",
          ["transfer", "balance", "pay bill"])
```

```
transfer  0.77  ███████████████·····
balance   0.02  ····················
pay bill  0.01  ····················
none      0.20  ████················
→ transfer · 12 ms

```

When none of the options fits, ZeroPoint says so:

```
zp.decide("Set an alarm for 6:30 tomorrow morning", ["transfer", "balance", "pay bill"])
```

```
pay bill  0.00  ····················
transfer  0.00  ····················
balance   0.00  ····················
none      1.00  ████████████████████
→ none · 12 ms

```

The options can be any short text, in any of the supported languages:

```
zp.decide("Me han cobrado dos veces la suscripción de marzo, ¿podéis devolverme el duplicado?",
          ["facturación", "soporte técnico", "recursos humanos"])
```

```
facturación       0.76  ███████████████·····
soporte técnico   0.00  ····················
recursos humanos  0.00  ····················
none              0.24  █████···············
→ facturación · 16 ms

```

See the Docs: javihaus.github.io/zeropoint.

## Integration

ZeroPoint runs in your process: one call per decision, no network, no GPU, no service to run. In a routing pipeline, gate on confidence: auto-route above your threshold and escalate the rest to human review.

```
d = zp.decide(text, ["transfer", "balance", "pay bill"])

if d.choice is None or d.confidence < 0.8:
    send_to_person(text)        # no option fits, or ZeroPoint is not sure enough
else:
    route(text, d.choice)       # e.g. "transfer"
```

The right threshold depends on what a wrong action costs you; pick it on a few hundred of your own labelled texts.

| Attribute | Description |
| --- | --- |
| `choice` | the chosen option, or `None` when none is the most probable answer |
| `confidence` | probability of `choice` (of none when `choice` is `None`) |
| `p_none` | probability that none of the options fits |
| `probabilities` | probability of each option, in the order you gave them; with `p_none` they add up to 1 |
| `depths` | how strongly the text belongs to each option (near 0: not at all) |
| `text_truncated` | `True` if the text was longer than ZeroPoint reads (192 word pieces) and its end was ignored |
| `options_truncated` | options longer than 16 word pieces, whose end was ignored |
| `blocks` | how many reads of 20 options the list needed |
| `latency_ms` | time the decision took |

Note

For many texts, `zp.decide_many(texts, options)` takes one list of options for all texts, or one list per text. Each text is computed on its own, so every result is exactly what `decide` gives for that text alone. Lists can be of any length. ZeroPoint reads the options in blocks of 20 together with the text, and every option's probability comes from one distribution over the whole list.

The option `ZeroPoint(threads=2)` sets how many CPU threads the encoder uses. The decisions do not depend on it.

## Calibration

You can calibrate ZeroPoint on your own labelled data, on a CPU.

```
pip install torch --index-url https://download.pytorch.org/whl/cpu   # optional: CPU-only PyTorch, without the GPU libraries
pip install "zeropoint[fit]"        # adds PyTorch and onnx; deciding never needs them
```

```
mine, report = zp.fit(texts, labels)   # labels: the right option for each text, or None for "none of these"
print(report["before"], report["after"])
mine.save("my-model")

zp = ZeroPoint("my-model")
```

Note

`fit` keeps 20% of your examples apart and reports how the model does on them before and after. Same data, same seed and same number of threads give the same model, bit for bit. On the support-ticket tests above, 300 labelled tickets raised the share of right queues from 24% to 36% when the queue is on the list, and from 29% to 46% against unrelated texts. Confident answers when the ticket's own queue is missing went from 20% to 0%. A fit is 200 steps and takes about 4 to 12 minutes on 2 CPU threads, depending on the CPU.

Warning

With few examples the held-out part is small, and the report's numbers move a lot by chance. `fit` and `recalibrate` warn when fewer than 50 examples are held out.

Tip

If your labels are already the ones ZeroPoint knows and you only want to move the balance between acting and answering none, `zp.recalibrate(texts, labels)` refits just two numbers, in seconds, without PyTorch.

## How it works

ZeroPoint is an energy-based model, in the sense of LeCun et al. (2006) ¹. It does not write an answer. It gives each option an energy: a number that measures how compatible the option is with the text, low when they fit and high when they do not. Training shapes these energies, pushing down the energy of the right option and pushing up the energy of the others. The text and all the options are read together, in one pass of a small multilingual encoder, so each option is measured against the text and against the other options.

Energies become probabilities with Boltzmann’s rule, the rule physics uses for a system in equilibrium: the lower the energy of a state, the more probable it is. A classifier applies the rule to the options alone, so one of them always wins, even when the text has nothing to do with any of them. ZeroPoint adds one more state, none of the options, with its energy fixed at zero: the flat ground around the wells the options form. Each option counts only by how far it falls below that ground. An option that does not fall below it gets nothing, however many such options there are, and none gets its probability in the same step as every option.

 ¹ Y. LeCun, S. Chopra, R. Hadsell, M. Ranzato and F. J. Huang, A Tutorial on Energy-Based Learning, in Predicting Structured Data, MIT Press, 2006.

## Citation

```
@software{marin_zeropoint_2026,
  author = {Marín, Javier},
  title  = {ZeroPoint: a CPU-first, energy-based decision model},
  year   = {2026},
  url    = {https://github.com/Javihaus/zeropoint}
}
```

## License

ZeroPoint was trained only on data whose licence allows commercial use:

| Data | Licence |
| --- | --- |
| CLINC150 | CC BY 3.0 |
| Banking77, MASSIVE (English and Spanish) | CC BY 4.0 |
| Bitext customer support, banking, insurance and telco | CDLA-Sharing 1.0 |
| 5,000 examples written for this project | Apache 2.0 |

No data with a non-commercial licence was used for training, and none of the test texts above is in the training data. Details, with the criteria used to write the 5,000 examples, in docs/training-data.md.

The code is Apache 2.0. The model is built on multilingual-e5-small (MIT licence); the notices are in NOTICE.

## About

CPU-first, energy-based decision model. Picks the option that fits, or says none does, without being told that none is an option

### Code of conduct

Code of conduct

# Dodaios/ste80-humanizer

## 关联链接

- https://download.pytorch.org/whl/cpu
- https://github.com/Javihaus/zeropoint}

## 导航

- 项目页：[[10-项目/github.com_d9a8076e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
