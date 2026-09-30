---
type: "corpus"
item_id: "6b1b1caec48fc851"
title: "Show HN: Binary Code Translator – free browser-based text↔binary converter"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49897350"
project_url: "https://binarycodetranslator.org/"
author: "liweipt"
published_at: "2026-09-29T17:45:07Z"
captured_at: "2026-09-30T18:57:07+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-30"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_liweipt
  - story_49897350
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Binary Code Translator – free browser-based text↔binary converter

> [!info] 一句话导读
> Binary Code Translator 01001000 01101001

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49897350>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：liweipt　|　发布：2026-09-29T17:45:07Z
> 项目链接：<https://binarycodetranslator.org/>
> 采集：2026-09-30T18:57:07+08:00　|　id：`6b1b1caec48fc851`

## 正文

01 BinaryTools
 Workbench
 Alphabet
 How to read
 Examples
◐
Binary Code Translator 01001000 01101001
Convert text ⇄ binary code. Switching views keeps your input, the encoding is always stated, and your data never leaves the browser.
INPUT
 Copy share link
Waiting
 Paste something and the type is detected automatically
Auto
 Text
 Binary
 Hex
 Number
0 characters
Clear
 Read QR…
 Read WAV…
 Read dot matrix…
Encoding & format (expand as needed)
Text encoding
UTF-8
 ASCII · 7-bit
 ASCII · 8-bit
Grouping
Every 8 bits
 Every 4 bits
 No grouping
Separator
Space
 None
 Comma
Paste tolerance: line breaks, commas and 0x prefixes are ignored; the output header always states the exact settings used.
Text
 Binary
 Bases
 Image
 Sound
 Bytes Later
 Music Planned
Byte map
 ⇄ ⇄ ⇄
TRY AN EXAMPLE
Hello → 40 bits
 你好 → 6 bytes
 42 → number
 48 69 → hex
 01001000 01101001 → bits
Text encoding vs number bases — two different things. The text "42" is two characters and encodes to 00110100 00110010 in ASCII/UTF-8 (a "4" glyph and a "2" glyph). The number 42 is a value, written 101010 in binary. The tool detects which one you mean; the Bases view converts numbers, the Binary view converts text.
ONE INPUT, THREE OUTPUTS — THE SAME "Hi" ( 01001000 01101001 )
QR code
Scanning returns exactly the chosen string — Hi with "Original text" selected, or the 0/1 characters with "Binary characters" selected. It encodes what you pick and never converts silently.
Open in the tool → Image · QR
Dot matrix
Black = 1, white = 0, read row by row, plus three corner markers so the grid can be located again. QR scanners cannot read it — bring it back with Read dot matrix… .
Open in the tool → Image · Dot matrix
Signal tone
An FSK-modulated tone (ggwave, about 4.3 s) you can play and download as WAV — then restore into the input box with Read WAV… . Microphone receiving is planned, not in this version.
Open in the tool → Sound
How to read binary code → Decode "Hi" step by step, plus what to do when bits are missing or the encoding doesn't match.
 Binary code alphabet → A–Z, a–z, 0–9 and symbols with ASCII values and 8-bit binary. Click a row to copy; convert your own name.
 Verified examples → Hi, Hello, I love you, Happy birthday, a Chinese character, and the number 42 vs the text "42".
How to read binary code, step by step
Reading binary text means undoing an encoding: the bits were produced by taking each character, turning it into a number, and writing that number in base 2. You reverse that in three steps.
The complete example: decode 01001000 01101001
Step What you do Result
1. Group into 8-bit bytes Split the bits into blocks of eight 01001000 | 01101001
2. Get each byte's value Read each byte as a base-2 number (place values 128 64 32 16 8 4 2 1) 01001000 = 72 · 01101001 = 105
3. Map values to characters Look the values up in the ASCII table 72 = H · 105 = i
Result Hi
Worked arithmetic for step 2: 01001000 → 0×128 + 1×64 + 0×32 + 0×16 + 1×8 + 0×4 + 0×2 + 0×1 = 72 .
Decode it yourself in the tool
01001000 01101001
Input type: binary · encoding: UTF-8 · grouped in 8-bit bytes
Open in the converter → Text view
 See it as bytes →
Binary numbers vs encoded text — don't mix them up
The bit string 101010 and the text encoding of "42" are different things:
The number 42 is a value. In base 2 it is 101010 , in base 16 it is 2A . No character encoding involved.
The text "42" is two characters. Each character gets a byte: "4" → 00110100 , "2" → 00110010 , so the text is 00110100 00110010 .
If someone hands you bits and says "decode this", they almost always mean encoded text (8 bits per character). If they say "what's this number in binary", they mean the value. Our converter detects which case your input is and states its interpretation in the result header — you can override it with the type selector.
ASCII and UTF-8: how they relate
ASCII defines 128 characters (values 0–127) and fits in 7 bits; files store one character per byte, so a leading 0 is added ( H = 72 = 01001000 ). UTF-8 keeps every ASCII character at exactly the same byte value — English text looks identical in ASCII and UTF-8 — and uses 2–4 bytes per character for other scripts. For example the Chinese character 好 is 11100101 10100101 10111101 (3 bytes). That's why "each character is 8 bits" is only true for ASCII-range characters.
When decoding goes wrong — and what to do
1. Illegal characters in the bits
01001x00 contains an x . Nothing but 0, 1 and separators belongs in a bit string. Fix: remove or correct the character and check the source again — don't delete the position, replace it with the correct bit.
2. Incomplete length — bits don't divide by 8
01001000 0110100 has 15 bits. 15 is not a multiple of 8, so the byte boundaries cannot line up and any "decoding" is meaningless. What the remainder tells you: only that the length is wrong — e.g. 19 bits leaves remainder 3, so you are missing or have 3 extra bits somewhere . It cannot tell you which line lost them ; you have to compare against the source, line by line. Our converter refuses to decode in this case, reports the remainder, and flags lines whose length differs from the majority.
Common mistake: "remainder 2, so line 2 lost 2 bits." No — the remainder says nothing about the location. A length check is a detector, not a locator.
3. Encoding mismatch
Some messages use 7-bit ASCII (7 bits per character, no leading zero). Decoded as 8-bit, the boundaries land in the wrong places and you get garbage or a "not valid UTF-8" error. Fix: if the total bit count divides evenly by 7 but not by 8, try the 7-bit ASCII option (the converter offers it in the error message). Multi-byte UTF-8 that starts mid-character fails the same way — realign to the start of the message.
Practice with verified examples → · Look up characters in the alphabet table →
Binary code alphabet — A–Z, 0–9 and symbols in 8-bit binary
This table shows how ASCII characters are written in binary. Each character maps to a decimal ASCII value from 0–127, and that value is written with 8 bits (padded with leading zeros). Click any row to copy its 8-bit binary code.
Scope note: this is the ASCII representation. UTF-8 uses these same single-byte values for A–Z, a–z, digits and symbols, but other writing systems (e.g. Chinese) take multiple bytes — not every piece of text is a sequence of 8-bit ASCII codes. See How to read binary code for details.
The full table
Character Decimal (ASCII) Binary (8-bit) Hex
A 65 01000001 41
B 66 01000010 42
C 67 01000011 43
D 68 01000100 44
E 69 01000101 45
F 70 01000110 46
G 71 01000111 47
H 72 01001000 48
I 73 01001001 49
J 74 01001010 4A
K 75 01001011 4B
L 76 01001100 4C
M 77 01001101 4D
N 78 01001110 4E
O 79 01001111 4F
P 80 01010000 50
Q 81 01010001 51
R 82 01010010 52
S 83 01010011 53
T 84 01010100 54
U 85 01010101 55
V 86 01010110 56
W 87 01010111 57
X 88 01011000 58
Y 89 01011001 59
Z 90 01011010 5A
a 97 01100001 61
b 98 01100010 62
c 99 01100011 63
d 100 01100100 64
e 101 01100101 65
f 102 01100110 66
g 103 01100111 67
h 104 01101000 68
i 105 01101001 69
j 106 01101010 6A
k 107 01101011 6B
l 108 01101100 6C
m 109 01101101 6D
n 110 01101110 6E
o 111 01101111 6F
p 112 01110000 70
q 113 01110001 71
r 114 01110010 72
s 115 01110011 73
t 116 01110100 74
u 117 01110101 75
v 118 01110110 76
w 119 01110111 77
x 120 01111000 78
y 121 01111001 79
z 122 01111010 7A
0 48 00110000 30
1 49 00110001 31
2 50 00110010 32
3 51 00110011 33
4 52 00110100 34
5 53 00110101 35
6 54 00110110 36
7 55 00110111 37
8 56 00111000 38
9 57 00111001 39
space 32 00100000 20
! 33 00100001 21
? 63 00111111 3F
. 46 00101110 2E
, 44 00101100 2C
- 45 00101101 2D
: 58 00111010 3A
; 59 00111011 3B
' 39 00100111 27
" 34 00100010 22
( 40 00101000 28
) 41 00101001 29
+ 43 00101011 2B
/ 47 00101111 2F
= 61 00111101 3D
< 60 00111100 3C
> 62 00111110 3E
@ 64 01000000 40
# 35 00100011 23
$ 36 00100100 24
% 37 00100101 25
& 38 00100110 26
* 42 00101010 2A
Tip: a row is highlighted on hover — click it to copy the 8-bit binary code.
How to convert your own name
Take the name ANN and look up each letter:
A → ASCII 65 → 01000001
N → ASCII 78 → 01001110
N → ASCII 78 → 01001110
So ANN = 01000001 01001110 01001110 in 8-bit ASCII (3 bytes).
Try it with your own name
Type any text — the binary below is computed live in your browser with UTF-8, the same encoding the tool uses.
Copy binary
 Open "ANN" in the converter →
Where the values come from
ASCII assigns 65–90 to A–Z , 97–122 to a–z and 48–57 to 0–9 . The lowercase letters are exactly 32 more than uppercase ( A =65, a =97), which flips one specific bit — that's why a is 01100001 while A is 01000001 .
Next: how to read a whole binary string →
Binary code examples you can verify
Every example below states the exact input, its type and encoding, and the correct result. Each was computed with standard UTF-8 encoding — not just by this site's own code — and every card opens the converter with that exact input and view preloaded.
One idea worth keeping: the number 42 and the text "42" are different inputs with different encodings. Both examples are below so you can compare them side by side.
Hi
01001000 01101001
2 bytes · UTF-8
Open in the converter → Binary Copy bits Decoded text view
Hello
01001000 01100101 01101100 01101100 01101111
5 bytes · UTF-8
Open in the converter → Binary Copy bits Decoded text view
I love you
01001001 00100000 01101100 01101111 01110110 01100101 00100000 01111001 01101111 01110101
10 bytes · UTF-8
Open in the converter → Binary Copy bits Decoded text view QR code → QR of the bits → Dot matrix → Signal tone →
Happy birthday
01001000 01100001 01110000 01110000 01111001 00100000 01100010 01101001 01110010 01110100 01101000 01100100 01100001 01111001
14 bytes · UTF-8
Open in the converter → Binary Copy bits Decoded text view Signal tone →
好
11100101 10100101 10111101
1 Chinese character · 3 bytes in UTF-8 (not 8-bit ASCII)
Open in the converter → Binary Copy bits Decoded text view
42
101010
The number 42 as a value (bases view): binary 101010 · hex 2A · octal 52
Open in the converter → Bases
"42"
00110100 00110010
The text "42" — two characters, 2 bytes. Compare with the number above: same input meaning, different encoding.
Open in the converter → Binary Copy bits Decoded text view
Check them yourself
For any English text you can verify by hand with the alphabet table : look up each character's value and write it as 8 bits. For characters beyond ASCII (like 好) the UTF-8 encoding takes multiple bytes — the tool states the byte count in its result header so you can tell at a glance which case you're in. See How to read binary code for the full method.
What does a QR code contain?
A QR code encodes exactly the string you choose: encode Hi and scanning returns Hi ; encode the binary characters 01001000 01101001 and scanning returns that string, which the receiver then decodes once more. In the Image view you pick between the two explicitly — the tool never converts silently.
Can signal tones be restored? What about dot matrices?
Signal tones use FSK modulation (ggwave, MIT license): the downloaded WAV can be restored to text with this tool's “Read WAV”. Live microphone receiving is planned and not in this version.
A dot matrix encodes the current bit string row by row with black = 1, white = 0. Matrices generated by this tool can be read back; QR scanners cannot read them, and restoring arbitrary images is not supported.
FAQ
Is my data uploaded? No. All conversion happens locally in your browser; QR codes, dot matrices and signal tones are generated on your device.
Why does it say “bits cannot be divided by 8”? The bit string is missing or has extra bits; decoding it anyway would only produce garbage. Check it against the source — this tool never pads silently.
Which bases are supported? Decimal, binary, octal and hexadecimal, with arbitrary precision and negative numbers (the view switches automatically based on the input type).
BinaryTools · Binary Code Translator
 Fully client-side — no backend, your data never leaves the browser
 Back to the tool

## 导航

- 项目页：[[10-项目/binarycodetranslator.org_5fce40da]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
