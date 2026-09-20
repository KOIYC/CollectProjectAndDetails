---
type: "corpus"
item_id: "b0de47b82e09f0d8"
title: "GPT-6 Astra Solves a WWI German Radio Cipher"
source: "lobsters"
source_name: "Lobsters"
url: "https://lobste.rs/s/ywnsld/gpt_6_astra_solves_wwi_german_radio_cipher"
project_url: "https://prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio"
published_at: "2026-09-19T03:44:38.517-05:00"
captured_at: "2026-09-20T03:31:09+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - lobsters
  - cryptography
  - vibecoding
metrics: {"score": 11, "comments": 8}
comments_count: 8
comments_total: 8
discovered_via: "lobsters:hottest"
archived: true
archived_at: "2026-09-20T09:21:33+08:00"
archive_reason: "渠道停用"
---

# GPT-6 Astra Solves a WWI German Radio Cipher

- **来源**：Lobsters　|　**kind**：post
- **原帖**：https://lobste.rs/s/ywnsld/gpt_6_astra_solves_wwi_german_radio_cipher
- **指标**：得分=11 · 评论=8
- **作者**：—　|　**发布**：2026-09-19T03:44:38.517-05:00
- **项目链接**：https://prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio
- **采集**：2026-09-20T03:31:09+08:00　|　**id**：`b0de47b82e09f0d8`

## 正文

Published: 2026-09-17
Author: prinz

GPT-6 Astra Solves a WWI German Radio Cipher - prinz

# GPT-6 Astra Solves a WWI German Radio Cipher

prinz

Sep 17, 2026

Scienceblogs.de, a German science blogging portal, includes a relatively famous list of 50 unsolved ciphers, which range from cryptograms published by serial killers to the famous Voynich manuscript.

Among these ciphers is a set of German radio messages from World War I that were encoded using the ADFGVX method.

This method is illustrated by the following example using the word “HOUSE” as the key:

```
    A D F G V X
A   H O U S E A
D   B C D F G I
F   J K L M N P
G   Q R T V W X
V   Y Z 0 1 2 3
X   4 5 6 7 8 9
```

As you can see, ADFGVX is used both horizontally and vertically to give each “cell” in the table a value. For example, in this text, “AA” corresponds to the letter H, “AD” corresponds to the letter O, “DA” corresponds to the letter B, and so on. And so, the word “PRINZ” would be encoded as:

FX GD DX FV VD

Using an encryption word other than “HOUSE” would result in a completely different table.

There is a list of known keys used by the Germans to encrypt these radio.messages, and hundreds of these messages have already been decoded, including by codebreaking expert George Lasry. Still, over a dozen have thus far eluded efforts to solve them, including (to my knowledge) this one, originally transmitted on November 27, 1918 (pg. 217):

GPT-6 Astra solved this cipher, and believes that the original message was as follows:

```
EIN ENGLISCHER KREUZER EINLIEG X SEWASTOPOL X S4STEN X EIN GESCHWADER DER X ALLIIERTEN FOLGT 26STEN X
```

Or, in English:

```
AN ENGLISH CRUISER ARRIVED AT SEVASTOPOL ON THE ?4TH AN ALLIED SQUADRON FOLLOWS ON THE 26TH
```

The model used “TRUPPENVERSCHIEBUNG” as the encryption word, as described on pgs. 214-215 of J. Rives Childs's “The History and Principles of German Military Ciphers, 1914–1918”. This encryption word yields the following table:

Before even using this table, the word “TRUPPENVERSCHIEBUNG” is required to be rearranged, so that the letters in the word are in an alphabetical order (e.g., T is 16th and R is 13th). 

Then, the same “TRUPPENVERSCHIEBUNG” is written out horizontally, with letters from the encrypted message written under it, in rows of 19 (resulting in 8 rows of 19 symbols each, plus 1 row of 18 symbols, since there are 170 characters total). This also means that we have 18 columns with 9 symbols each and 1 column with 8 symbols (column “G”). From here, because T is the 16th column, it has 14 9-symbol columns before it, plus 1 8-symbol G column; 9×14 + 1×8 = 134, so “T” will correspond to the following, 135th, symbols in the message, which is “A”. Similarly, the jext letter, “R”, corresponds to the letter “V” (because R is the 13th letter alphabetically and thus has 11×9 + 1×8 = 107 symbols before it; the 108th symbol in the message is “V”).

In the table above, “AV” corresponds to “E”, the first letter in “EIN”. We repeat this process until we decode the entire message.

(Wow.)

Astra's hypothesis for why this particular message was previously unsolved is that “TRUPPENVERSCHIEBUNG” was used as the key starting on December 9, 1918 - whereas, as noted above, this message was transmitted earlier, on November 27, 1918. The reason for this discrepancy is unknown.

Astra felt compelled to check its work and found that, in fact, the English cruiser HMS Canterbury arrived in Sevastopol on November 24, 2018, based on its original logs:

… and an allied squadron did follow on November 26 (see right below line 11, which says that an allied squadron arrived):

I am not aware of this particular message having ever been decoded before, so sharing it here as a minor (but I think really cool) result and illustration of the capabilities of this model.

# Write while learning | purplesyringa's blog

## 评论（8/8）

**simonw**（19 分） · 2026-09-19T07:57:25.763-05:00：

This article would be a lot more interesting if it included the prompts, transcript, and generated code from the session with the LLM.

**dallen**（15 分） · 2026-09-19T08:24:31.880-05:00：

It is irresponsible to misattribute these accomplishments to the AI agents. Every time, at least one person is involved in prompting and guiding the process. The headlines should be "[human] solves [challenge] using [tool]." The article author's use of anthropomorphizing phrases like "Astra's hypothesis for" and "Astra felt compelled" do not leave a good impression on me. I agree with @simonw that without seeing the prompts this is uninteresting.

**chrismorgan**（5 分） · 2026-09-19T08:11:28.215-05:00：

Astra's hypothesis for why this particular message was previously unsolved is that “TRUPPENVERSCHIEBUNG” was used as the key starting on December 9, 1918 - whereas, as noted above, this message was transmitted earlier, on November 27, 1918. The reason for this discrepancy is unknown.

I don’t know how such keys were managed (how/when distributed, how often rotated, &c.) but it sounds like a tired transmitter might have just accidentally used the next key in the book by mistake?

I presume this also makes the solving of the cipher rather less impressive—that it was probably just trying all the known keys and found a plausible match. It wasn’t solving a cipher, it was decoding a specific cipher text for which the key was not known.

**npiazza**（1 分） · 2026-09-19T11:45:54.484-05:00：

Yeah, the title makes it sound much more impressive than key reuse.

Could be a good avenue to check for some other encrypted messages though.

**cr**（4 分） · 2026-09-19T09:01:00.125-05:00：

To me an interesting example of storing all encrypted messages for a long time and then some day you’ll be able to crack and decipher them

**olegkovalov**（1 分） · 2026-09-19T04:08:11.835-05:00：

So..what??? I don't get this type of posts. Still not AGI and never-ish will be, AI;DR as always.

**sdt**（18 分） · 2026-09-19T05:22:15.451-05:00：

I don't get this type of comment.

I like old ciphers and while I would probably enjoy reading about it more if it had been a (team of) people, I still think it's interesting to read about.

I've so far refused to use LLMs for anything generative, still write code by hand, and am terrified of what lies ahead. But I still think it's interesting to see what these models are used for and how well (or not) they work.

**patchunwrap**（2 分） · 2026-09-19T05:11:42.865-05:00：

(to be clear I agree with you)

What makes you so confident?

## 关联链接

- https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio
