---
type: "corpus"
item_id: "ec74da80b81873a3"
title: "Typst makes big strides"
source: "lobsters"
source_name: "Lobsters"
url: "https://lobste.rs/s/j4oyxa/typst_makes_big_strides"
project_url: "https://lwn.net/Articles/1092993"
published_at: "2026-09-18T08:14:17.568-05:00"
captured_at: "2026-09-20T09:20:20+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - lobsters
  - a11y
  - programming
metrics: {"score": 110, "comments": 19}
comments_count: 19
comments_total: 19
discovered_via: "lobsters:hottest"
archived: true
archived_at: "2026-09-20T09:21:33+08:00"
archive_reason: "渠道停用"
---

# Typst makes big strides

- **来源**：Lobsters　|　**kind**：post
- **原帖**：https://lobste.rs/s/j4oyxa/typst_makes_big_strides
- **指标**：得分=110 · 评论=19
- **作者**：—　|　**发布**：2026-09-18T08:14:17.568-05:00
- **项目链接**：https://lwn.net/Articles/1092993
- **采集**：2026-09-20T09:20:20+08:00　|　**id**：`ec74da80b81873a3`

## 正文

Typst makes big strides [LWN.net]

# Typst makes big strides

September 9, 2026

This article was contributed by Lee Phillips

 Typst is a system for typesetting documents into various formats: PDF, SVG, PNG, and, in progress, HTML. It is adept at handling technical material, and is often considered to be an eventual LaTeX replacement. We last looked in on Typst a year ago, when it had reached version 0.13. A new version, 0.15, was released in June with lots of new features, including support for variable fonts, MathML, multiple bibliographies, and more. Typst is free, Apache-2.0-licensed software, programmed in Rust. 

#### Variable Fonts

 Typst now has support for variable fonts. Most fonts are distributed in a set of files containing their glyphs in different weights, in variations such as italic, bold, and so on. A recent development in the world of typography is the advent of variable fonts, which can contain all their variations in a single file. This both saves space and can permit greater flexibility on the part of the author or designer. 

 Font features and variations are chosen by setting the value for an "axis"; each axis changes some aspect of the rendered glyphs. There are typically multiple axes that can have discrete values, for turning on and off various features, or continuous values lying between two limits. The latter can be used, for example, for choosing the weight of the font along a continuum. 

 To test the new Typst feature, I downloaded two open-source variable fonts: Roboto Flex, a general-purpose font with 13 axes, and Zycon, a font containing no letters but 17 small decorative pictures. Zycon's six continuous axes smoothly alter various aspects of the pictures, making the font useful in animations. 

 Here is a Typst document that uses both of these fonts, varying one of the axes for each of them: 

```
   #set text(font:"Roboto Flex")
   #for n in (-305, -200, -98) {
       set text(variations:("YTDE": n)) 
       [A penguin jumped quietly.
   
       ]
   }
   
   #set text(font:"Zycon")
   #for n in array.range(0, 10, inclusive:true) {
     set text(variations:("M1  ": n/10))
     str.from-unicode(127773)
   } 

```

 In Typst, a "

" character puts the document in "code mode", where the rest of the line or block is interpreted as code in Typst's built-in language. Within code mode, material enclosed in square brackets is interpreted as "text mode", or text to be typeset. 

 The code above contains two commands to 

set

 the fonts by name, using one of the options of the 

text()

 function. Next we have 

for

 loops, which operate as might be expected. Inside the loops we call the 

text()

 function to set the 

variations

 variable. The text to be used with the Roboto Flex font is entered directly, but the output using the Zycon font is a single character specified with the 

str.from-unicode()

 function. It could have been entered directly, but readers may not have been able to see it, depending on the coverage in their browser's font. 

 The axis that we manipulate in Roboto Flex is called 

YTDE

. As the figure below shows, this axis determines the length of the font's descenders, while leaving its other characteristics unchanged. This might be useful when typesetting tables, for example, to avoid collisions between the descenders and the table-cell boundaries. One of Zycon's six axes, called "

M1 

" (the two trailing spaces are part of the name; all axis names contain four characters), does different things to different characters. The effect on the Moon glyph is to change the lunar phase. 

 Compiling this document with 

typst compile vfont.typ

 produces a PDF in 

vfont.pdf

, which is shown in the screen shot below: 

#### MathML

 HTML export is still an experimental feature of Typst, but this release shows significant progress. The main new HTML feature is the translation of mathematics into MathML. The previous article on Typst showed the markup for a certain definite integral and displayed its output when rendered into a PDF by Typst. The same Typst code, when rendered into HTML, produces a long string of MathML markup that almost all reasonably current web browsers know how to interpret. The result appears like this: 

 $∫01(arcsin𝑥)2d𝑥𝑥21−𝑥2=𝜋ln2$ 

 If you don't see an equation above, your browser does not support MathML. If you do see it, a comparison with the typeset equation from the previous article shows that the PDF and HTML results are essentially identical. The ability to use Typst to produce TeX-quality mathematics in web browsers, without requiring a JavaScript library such as MathJax or having to resort to images, is a boon for scientific communication. 

 To enable the experimental HTML output, Typst requires a special flag: 

```
   typst c --features html integral.typ integral.html  

```

 That is the command used to typeset the equation markup in a file called 

integral.typ

 into HTML. 

#### "Bundle" output

 The typical use case for software such as Typst is the creation of single files, usually papers or books in the form of PDFs. The new "bundle" feature allows the author to specify a collection of output files, in any of the formats that Typst supports, in a single source file. These files can share data and contain both intra-document and inter-document links. 

 The feature is ideal for the creation of web sites, which consist of an interlinked network of HTML files. It should also be of interest to academics who might want to generate a slide deck for a conference talk along with the associated preprint from a single source file. 

 Here is a simple example of a Typst file that creates three interlinked documents, two HTML pages and a PDF, sharing a fragment of text: 

```
   #let text = ['Twas brillig, and the slithy toves
         Did gyre and gimble in the wabe:]
   
   #document("poems.html", title: [Famous Poems])[
     #link(<jabberwocky>)[Here] is a famous nonsense poem.
   ]<home>
   
   #document("jabberwocky.html", title: [Jabberwocky by Lewis Carroll])[
   This famous poem begins like this:
   
   #text
   
   The #link(<jabberwockyPDF>)[rest] of the poem.
   
   Go #link(<home>)[home].
   ]<jabberwocky>
   
   #document("jabberwocky.pdf", title: [Jabberwocky: the Complete Poem])[
   #text ....
   
   Go #link(<home>)[home].
   ]<jabberwockyPDF>   

```

 The command for processing this code, if it is saved in a file called 

bundle.typ

, is: 

```
   typst c --features html,bundle --format bundle bundle.typ   

```

 In my tests, the bundle feature worked as advertised, but since it, along with HTML output, is still considered a work in progress, the compiler requires the 

--features

 flag. 

 The command above creates a new directory called "bundle" containing the three files defined in the 

#document()

 functions. They all contain the two initial lines of the poem saved in the 

 variable. There are hyperlinks between the HTML pages, from one of those to the PDF, and from the latter back to the two-page website. The links are targeted using the labels, contained within angle brackets, following each document function. 

#### Multiple bibliographies

 Typst now permits multiple bibliographies in a single document, which was an eagerly awaited feature. Its canonical application is for books that may need a separate reference section for each chapter. The feature is best introduced with a toy example: 

```
   #show bibliography: set text(size: 8pt)
   
   = Chapter I
   
   According to @smith, Smith is uncommonly smart.
   
   #bibliography("works.bib",
   title: "References for Chapter I",
   group: none)
   
   = Chapter II
   
   Jones@jones has a different view. The issue was
   finally put to rest in the following year
   in @mergutroid.
   
   #bibliography("works.bib",
   title: "References for Chapter II",
   group: none)   

```

 Here the first line specifies that the bibliographies should use a font size smaller than the default used in the main text. In that text, the "

@

" prefixes create a citation using the default number-in-brackets style. At the end of each chapter, the 

bibliography()

 function is called. Its first argument specifies which database should be used for the bibliographic information; each bibliography section can use a different database, or collection of databases, if desired (see our recent article on Pandoc for a description of these text-file databases). The 

group

 argument controls how the citations are numbered. The value of 

none

 causes the numbering to begin with one for each section; numbering can alternatively be continuous for the entire work, or be grouped arbitrarily. 

 The figure below shows the output of the listing as it appears in PDF form: 

#### Multiple PDF standards

 Avoiding the use of proprietary extensions is normally sufficient to ensure that the PDFs created with Typst, LaTeX, or any other competent software will fulfill the promise of the format: documents will be openable and appear identical in all readers, now and in the future. At a deeper level, however, a PDF is not just a PDF. There are various PDF versions and, on top of these, dozens of formal standards relating to archivability and accessibility. The standards for archivability are meant to ensure that the document really does work across a wide variety of reader software and that it will do so forever. The accessibility standards relate to the usability of a PDF for people with disabilities of various sorts. 

 Typst already had the ability to target various PDF versions and standards for archiving or accessibility. The new feature is the option to target more than one when compiling a document. This is useful, because one may want to generate a PDF that has both archival and accessibility attributes. The implementation of the feature helps the author to navigate the forest of PDF standards by issuing warnings or errors in the cases of incompatible combinations or failure to follow best practices for the standards targeted. 

 As an example, here is a command that attempts to compile the "book" document from the previous section, requesting both PDF version 1.7 and the A-1b archive standard: 

```
   typst c --pdf-standard 1.7,a-1b book.typ  

```

 The Typst compiler responds with this error message: 

```
   error: PDF 1.7 is not compatible with PDF/A-1b
   hint: PDF/A-1b requires version PDF 1.4   

```

 PDF version 1.7 is compatible with A-2b, so this will work: 

```
   typst c --pdf-standard 1.7,a-2b book.typ   

```

 If, however, we add the UA-1 accessibility standard, as in this command: 

```
   typst c --pdf-standard 1.7,a-2b,ua-1 book.typ    

```

 We again get an error: 

```
   error: PDF/UA-1 error: missing document title
    = hint: set the title with `set document(title: [...])`   

```

 Normally the Typst compiler doesn't insist on anything beyond correct syntax, but if we specify a particular accessibility standard, the document must conform to that standard. UA-1 requires, among other things, a document title. 

 The foregoing is not merely arcana, although it may seem to be of little relevance to the typical author of a scientific paper or textbook. These details are important to archivists and publishers; in addition to helping disabled users, producing accessible PDFs is a legal requirement applying to state and federal governments in the US and many other countries. Typst's advanced handling of multiple PDF standards makes it a useful tool in these contexts. 

#### Conclusion

 Typst 0.15 has other enhancements that are not described in detail in this article. Some of these are support for spot colors, detailed diagnostics that explain any failure of convergence during the compilation process, and new map and filter functions in the built-in scripting language. The documentation, which is updated to cover the new version, is now available in a 26MB PDF. 

 Typst is developed on GitHub, where it has 460 contributors. The creators of the project have written a guide for new contributors where they describe what a PR should look like and warn that any code or description generated by an LLM will be rejected. They are also forthright about the fact that Typst is a company as well as an open-source project, and that decisions about the direction of the project, as well as the suitability of individual contributions, will take the needs of the company into account. This is a factor that prospective contributors and users should keep in mind. 

 Progress in the development of the system is impressive. The community of users is enthusiastic; their participation has expanded the Typst ecosystem to over 1500 packages. 

 However, network effects in the publishing world are preventing Typst from fulfilling the potential that we saw for it in our previous article. Although users have devised templates to match the style specifications of several journals, those that require source submissions (rather than just PDFs) still insist on LaTeX, Word, or some other format. Very few accept manuscripts marked up in Typst. This is not likely to change while Typst remains in a pre-1.0 status (which is probably still a ways off) and is in danger of requiring significant, possibly breaking changes to documents. 

 Despite this, Typst is an immensely useful tool today. For example, I recently had to create an SVG logo and found that writing a textual description using Typst's built-in graphics commands was quicker and easier than reaching for a drawing program. It's impossible to say whether Typst's advantages will lead to it becoming a "LaTeX replacement", as many of its admirers describe it. But, if development continues at the current pace, it is a distinct possibility, although one that may take a decade or two to come to fruition. 

PDF accessibility Posted Sep 9, 2026 16:43 UTC (Wed) by jasonjgw (subscriber, #52080) [Link] (4 responses) 

 It is encouraging that support for PDF accessibility has been implemented relatively early in the development of the project. Although this feature is useful, it is always best to publish an HTML version of a document alongside the PDF, as there are PDF reading applications that do not support the structure tree (tagged PDF), and a person who is blind or vision-impaired using a screen reader would not benefit from the accessibility features in that case. 

 Under Linux, the PDF reader in Firefox is the only consumer-side implementation that I have encountered which offers any support for tagged PDF via the Orca screen reader. Now that Typst is moving toward mature support for both tagged PDF and HTML, I'll consider using it for some writing projects, although the lack of acceptance by scholarly publishing venues noted in the article remains an obstacle. At least the included, first-class HTML support should make it easier for me to proofread a rendered version of my own work using a screen reader (braille and speech output), which is possible with LaTeX if external HTML conversion tools are used. 

 Reply to this comment 

 

PDF accessibility Posted Sep 9, 2026 18:19 UTC (Wed) by leephillips (guest, #100450) [Link] (1 responses) 

 Good points. Typst’s new bundle feature makes publishing an HTML version automatically alongside a PDF much more convenient. 

 Reply to this comment 

 

PDF accessibility Posted Sep 10, 2026 21:48 UTC (Thu) by azumanga (subscriber, #90158) [Link] 

 How good is the quality nowadays? Last time it really wasn’t acceptable, many things didn’t appear in the HTML. It’s really not accessible to have a modern system which isn’t accessible. I certainly can’t use it. 

 Reply to this comment 

 

PDF accessibility Posted Sep 15, 2026 14:37 UTC (Tue) by mathstuf (subscriber, #69389) [Link] 

Has there been any noise on pandoc supporting conversions? That might help with the scholarly publishing angle.

 Reply to this comment 

 

PDF accessibility Posted Sep 19, 2026 15:00 UTC (Sat) by mrugiero (guest, #153040) [Link] 

> Although this feature is useful, it is always best to publish an HTML version of a document alongside the PDF, as there are PDF reading applications that do not support the structure tree (tagged PDF), and a person who is blind or vision-impaired using a screen reader would not benefit from the accessibility features in that case.

Wouldn't a vision-impaired user pick a PDF reading application that supports tagged PDFs? Not opposing giving out more options, but one would think people are likely to use applications that are accessible to whatever abilities and disabilities they have, provided the option exists.

 Reply to this comment 

 

An impressive set of features, but… Posted Sep 18, 2026 7:03 UTC (Fri) by callegar (guest, #16148) [Link] (3 responses) 

Typst has an impressive and growing set of features, as well as remarkable speed. When I first learned about it a few versions ago, I immediately looked into it, trying to get accustomed to its different way of doing things compared to TeX/LaTeX, and evaluating what would be needed to port some of my existing document classes.

However, I quickly backed off and put adoption on hold, as the quality of its typesetting has so far been rather disappointing.

If Donald Knuth originally designed TeX because he was deeply frustrated by the declining quality of digital typography, then things haven't improved much here. Typst still lacks features that one would nowadays take for granted—such as italic correction (the automatic insertion of kerning space when transitioning from an italic face back to an upright one, which prevents the impression of non-uniform word spacing caused by character slants).

Phrases like " odd function" end up looking terrible, as the height of the "d" and the "f" amplifies the visual impact of the missing correction.

In many cases, you even get complete collisions, as seen here: https://private-user-images.githubusercontent.com/18075640/241815141-f9dd1b11-5281-4b45-9fb4-537a1916e01a.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODk3MTQwOTAsIm5iZiI6MTc4OTcxMzc5MCwicGF0aCI6Ii8xODA3NTY0MC8yNDE4MTUxNDEtZjlkZDFiMTEtNTI4MS00YjQ1LTlmYjQtNTM3YTE5MTZlMDFhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWYLTQTUzUFFLNFpBJTJGMjAyRzA5MTglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwOTE4VDA2NDMxMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVjYThiOGE4ZmY0NTFjYzVmZDlmNjdkYzNmMTVhZGRlMzM1ZTA3YjIyNDA2ZjU3MWQxNzE1ZjhlOGRkYWZkNWQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.neg4OKbcgHlQ3OalxBWAszef0E5iVPvCbDi83DyvgNc

This problem is especially systematic when using footnotes: https://private-user-images.githubusercontent.com/10307457/529865105-c391bd78-e905-44c4-9080-48f683b508f5.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODk3MTQzMjEsIm5iZiI6MTc4OTcxNDAyMSwicGF0aCI6Ii8xMDMwNzQ1Ny81Mjk4NjUxMDUtYzM5MWJkNzgtZTkwNS00NGM0LTkwODAtNDhmNjgzYjUwOGY1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWYLTQTUzUFFLNFpBJTJGMjAyRzA5MTglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwOTE4VDA2NDcwMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTIwMThmZGY0Yzc1OTZmNDVhNTE1MjBiMzlkMDE1ODhjNzdmNWY4MjE2NhNhNDIyNWIwNmEwYzkwYTY1ZWU5OTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.I6OuNqw5sEVdVurxpLFtzlwij-mILzRzaPRovVfA3kY

This leaves many Typst-produced documents looking unprofessional, often giving the impression of a sloppy author. Almost every other typesetting program—traditional TeX engines, modern variants like LuaTeX, SILE, Glu, Patoline—seems to handle this better or offer some form of automatic italic correction, and even MS Word seems to score better here.

The fact that this isn't directly supported by standard OpenType text fonts shouldn't hold developers back from implementing a "good enough" heuristic on top of OpenType, as other tools do.

And yes, while you can implement the correction manually, there are two major drawbacks:

- The manual insertion of kerning makes the source document far harder to read.
- A primary advantage of tools like TeX and Typst is the ability to generate documents programmatically, a workflow where manual kerning adjustments become virtually impossible.

 Reply to this comment 

 

An impressive set of features, but… Posted Sep 18, 2026 7:12 UTC (Fri) by callegar (guest, #16148) [Link] (2 responses) 

Just noticed the ugly long links to images in github issues broke in my previous comment when it got published. Trying again:

Clashing

Footnotes

 Reply to this comment 

 

An impressive set of features, but… Posted Sep 18, 2026 17:07 UTC (Fri) by mathstuf (subscriber, #69389) [Link] (1 responses) 

They're still returning 404.

 Reply to this comment 

 

An impressive set of features, but… Posted Sep 19, 2026 12:27 UTC (Sat) by callegar (guest, #16148) [Link] 

You are right, they work in my browser, but just because they are cached.

Here are the links to the individual comments in the bug thread:

- too thin spacing
- clash
- footnote flags

And also a comparison of different engines

 Reply to this comment 

 

On trust, companies and infrastructure Posted Sep 19, 2026 15:06 UTC (Sat) by mrugiero (guest, #153040) [Link] (1 responses) 

 I find it a tiny bit troubling that people aim to replace latex with a product of what's openly a company first. Haven't we've been burned before by relying on companies and expecting them to keep software free (as in speech and beer)? Do we want to build our scientific publishing infrastructure on more of that? 

 Reply to this comment 

 

On trust, companies and infrastructure Posted Sep 19, 2026 15:11 UTC (Sat) by dskoll (subscriber, #1630) [Link] 

Yes, I agree and I continue to use LaTeX. However, it is a bit frustrating to produce decent epub output from LaTeX input. That may not matter too much for scientific papers, but it does for textbooks or reference books. 

I have a workflow that "works" using `tex4ebook` but the result is a bit messy. 

 Reply to this comment 



# Saving another 100TB of RAM with math (and Rust) | Cloudflare Blog

## 评论（19/19）

**snej**（37 分） · 2026-09-18T09:59:13.047-05:00：

Most fonts are distributed in a set of files containing their glyphs in different weights, in variations such as italic, bold, and so on. A recent development in the world of typography is the advent of variable fonts, which can contain all their variations in a single file.

Font nerd here. That’s true, but omits the big deal, which is that the variations can be continuous. So a variable font with “weight” as an axis has not just one or two bold variants but an infinite number, as the glyphs smoothly interpolate their control points.

**chrismorgan**（5 分） · 2026-09-18T11:34:32.565-05:00：

Yeah, we already had a widely-deployed way of grouping variations into a single file for 25–30 years, TrueType Collections.

**5d22b**（0 分） · 2026-09-18T11:12:02.908-05:00：

This "recent development" sounds, in effect, like Metafont, something TeX had 40–50 years ago. I'm not claiming Metafont is practical to use, and LWN says variable fonts "saves space", which I think is an advantage over Metafont, but the lack of mention of Metafont makes me wonder whether Typst are familiar with what they're trying to supplant.

**trenchant**（29 分） · 2026-09-18T11:33:52.337-05:00：

Variable fonts do not come from Typst. They are supported in the browser and descend from OpenType, while Metafont is bitmap only and seems to be dead / LaTeX only.

**5d22b**（1 分） · 2026-09-18T12:23:11.320-05:00：

To clarify, I didn't mean to suggest otherwise.

**isuffix**（16 分） · 2026-09-18T12:19:49.484-05:00：

That's still a bit condescending. Typst didn't create variable fonts, nor is it particularly interested in redefining font technologies or file formats. Implementing variable font support was mostly about supporting a technology users were asking for. The variable font issue got to 147 upvotes before it was completed; only two open issues still have more. No one yet has posted an issue asking for MetaFont support.

**5d22b**（5 分） · 2026-09-18T12:28:53.727-05:00：

No one yet has posted an issue asking for MetaFont support.

I don't think using Metafont would be practical or suitable for a modern project such as Typst, but I would have been reassured to see it mentioned as prior art.

**p0llard**（11 分） · 2026-09-18T11:32:49.785-05:00：

The author of the article isn’t affiliated with Typst as far as I can tell, so I don’t think the lack of any mentions of Metafont in this article is any indication as to whether the Typst authors are familiar with Metafont or not.

**colindean**（16 分） · 2026-09-18T17:33:12.189-05:00：

I really have to give a shout out to Typesetter as an excellent, simple Typst editor for Linux. I've had to write a surprising number of simple correspondence letters in the last 18 months since moving for the first time in almost 15 years. This simple editor made that process so nice and quick, to be able to produce a templated letter with automatic date updates and some light markup beyond what I would do in just a boring plain text editor.

**videah**（11 分） · 2026-09-19T02:06:37.821-05:00：

I recently rewrote my personal website entirely in Typst, it’s on the cusp of becoming really good for blogging

**proctrap**（2 分） · 2026-09-19T09:39:18.156-05:00：

uuh any additional war stories here ? are there sources ? I resonated deeply with the just need one more html inject part.

**valdemar**（4 分） · 2026-09-19T10:38:57.935-05:00：

I did it a bit over a year ago, but since then they have made strides in using it as a fully static generator as well and various stuff in this post is now outdated https://erk.dev/2025/04/19/bureaucracy

My custom stuff is here: https://git.sr.ht/~erk/hs/tree/main/item/posts/govuk.tpl

And the posts are here: https://git.sr.ht/~erk/hs/tree/main/item/posts

**cyberia**（9 分） · 2026-09-18T19:39:41.419-05:00：

I wrote my master's thesis in Typst. Good stuff.

**near**（4 分） · 2026-09-19T05:44:06.451-05:00：

I recently used Typst when updating my CV, and I didn't like the look of the ModernCV LaTeX template anymore. It's pretty nice! I was able to pick up enough of it to have a pleasant result in roughly an hour (using one of the provided templates). I went on to see more and found that it's super useful to create small a6-sized zines as well.

The language looks pretty well thought out, and I'm happy they are working on MathML output and I think this will provide a good foundation for accessible mathematics on the web. I don't quite understand why it comes with an entirely different language for expressing mathematical formulas when compared to TeX though, and I wouldn't be surprised if quite a few academics in fields where TeX is the default (like mathematics and physics) will be reluctant to adopt Typst just because of this.

**chrismorgan**（9 分） · 2026-09-19T08:26:55.382-05:00：

TeX math mode uses TeX syntax, namespaces and semantics. It’s tightly integrated.

Typst math mode uses Typst syntax, namespaces and semantics. It’s tightly integrated.

Various other libraries and programs have implemented an approximation of TeX math mode, but it’s an imitation of some of it, like Vim modes tend to be in other editors (though evil-mode is reputed to be very good, and Zed’s Vim mode is well on its way to being very good).

Typst using TeX syntax for math mode would be terrible, badly out of place in its language. What’s really very nice about Typst is that you can use things like MiTeX as a Typst package for such compatibility.

**near**（2 分） · 2026-09-19T09:54:24.839-05:00：

I didn't know about any efforts to provide compatibility layers, thanks for sharing! MiTeX does look quite nice.

**rustybolt**（3 分） · 2026-09-19T10:01:07.929-05:00：

I wouldn't be surprised if quite a few academics in fields where TeX is the default (like mathematics and physics) will be reluctant to adopt Typst just because of this.

I'm not even an academic but this is exactly why I didn't switch to Typst. I'm trying to get shit done, I don't want to learn a new math typesetting system. I probably would do it if I was a student but I have a full-time job, two kids, a girlfriend and a dog and zero spare time and energy to spend on this.

**rustybolt**（3 分） · 2026-09-19T12:54:04.017-05:00：

Oh god I just looked into Typst again and it does really nice, I really ought to look into it whenever I have time in like 3 years.

**bgs_**（3 分） · 2026-09-19T06:13:30.084-05:00：

Typst is going in the right direction

## 关联链接

- https://lwn.net/Articles/1092993/
