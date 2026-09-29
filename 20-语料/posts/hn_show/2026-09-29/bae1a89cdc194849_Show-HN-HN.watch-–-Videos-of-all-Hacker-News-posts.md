---
type: "corpus"
item_id: "bae1a89cdc194849"
title: "Show HN: HN.watch – Videos of all Hacker News posts"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49879401"
project_url: "https://hn.watch/"
author: "mrborgen"
published_at: "2026-09-28T15:16:13Z"
captured_at: "2026-09-29T09:42:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-29"
pub_day: "2026-09-28"
tags:
  - 语料
  - hn_show
  - author_mrborgen
  - story_49879401
  - show_hn
  - front_page
metrics: {"points": 125, "comments": 81, "engagement_velocity": 125}
comments_count: 81
comments_total: 81
discovered_via: "hn:show_hn:3d"
---

# Show HN: HN.watch – Videos of all Hacker News posts

> [!info] 一句话导读
> Hi HN, I’m Per, founder of Scrimba (YC S20). We’ve spent the last decade teaching people how to code with an HTML-based video format. We’ve now plugged an LLM i…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49879401>
> 指标：点赞=125 · 评论=81 · engagement_velocity=125
> 作者：mrborgen　|　发布：2026-09-28T15:16:13Z
> 项目链接：<https://hn.watch/>
> 采集：2026-09-29T09:42:55+08:00　|　id：`bae1a89cdc194849`

## 正文

Hi HN, I’m Per, founder of Scrimba (YC S20). We’ve spent the last decade teaching people how to code with an HTML-based video format. We’ve now plugged an LLM into it, so that people can create explainer videos about anything. It’s called “Scrimba Explain”.To demo this technology for Hacker News, we built HN.watch. It’s like HN, but with explainer videos instead of articles. We create them on-the-fly the first time someone clicks on a link.While there are obvious visual drawbacks of using HTML instead of diffusion models, there are three big benefits: - Speed: Much faster to generate than pixel-based videos (just a few seconds from click to playback) - Cost: Our cost per video is ~$0.04. (Excluding image generation, which some videos utilize. Quickly blows up the cost) - Easy editing: the above benefits also make AI-assisted editing cheap & fastOur hypothesis is that if video creation goes from “dollars and minutes” to “cents and seconds”, a bunch of new use cases will be unlocked. Here are some we see already: - A video explanation of every single Pull Request (we do this internally) - Give every page in your internal/extrernal docs a video - Turn a complex article into a video in ~4 seconds (via our Chrome extension) - Course creators can quickly draft lessons before recording the real thing - People also create a lot of personal stuff stories for their kids, wedding invitations, birthdays, etcThe stack is based on an open-source programming language (Imba) created by our CTO, Sindre Aarsæther. It compiles to JavaScript, so it interoperates fully with the npm + node ecosystem. You can learn more here: https://imba.io/We’ve also built our own sync engine (OP), and a context management system for agents (Q). We feared this would make the LLMs struggle when writing code for us, as neither is in their training data (there’s very little Imba in there too). However, we’ve been pleasantly surprised to see that LLMs actually are really good at our stack. This is probably because the stack is extremely dense. Imba is compact, and so is OP, where a single declaration sets storage, sync, permissions, UI, and what the AI sees. This means there’s no translations between frontend, API, db and JSON where the model can get confused and get things wrong.Simply said, instead of using React.js, Express, Supabase, and LangChain, we built it all from scratch. Definitely suffering from the “not invented here” syndrome, lol! As for the models, we use Gemini, GPTs, Inworld, ElevenLabs, and a few others.If you want to try it out, just take your pick: - The Web UI (scrimba.com/explain) - MCP (add it to your coding agent) - ChatGPT Plugin - Chrome ExtensionYou can find a link to all of the above in our docs: https://docs.scrimba.com/explain/introductionAnd finally, a real pixel-based video of the tool: https://www.youtube.com/watch?v=k6rbHmBxSEsWould love to hear your feedback and if anyone has ideas for other use cases.PS: I expect quite a bit of pushback from HN for this launch, given how fan of text the HN crowd is. This kind of tool is not for everyone. But there are a lot of people today who prefer videos over text, especially in the younger generations.

## 评论（81/81）

> **DANmode** · 2026-09-28T17:28:42.000Z　
> Thanks, I hate it.Kidding, I already sent it to a friend with ADHD who has been struggling to remain anchored to the tech world in any way besides Shorts.But, culturally, I definitely hate the trend it implies!Neat. Thank you for sharing.

---

> **alentodorov** · 2026-09-28T17:31:28.000Z　
> loved scrimba. thanks for building that. was anout to pushback bc of the torrent of show hn sloppy pists but this one is fun.

---

> **babu_mick** · 2026-09-28T17:34:45.000Z　
> yo this is wild

---

> **mgxplyr** · 2026-09-28T17:35:36.000Z　
> It's actually very good...

---

> **harvey9** · 2026-09-28T17:36:52.000Z　
> Please, nobody click on the link to this hn item within hn.watch as it would be even more dangerous than typing 'google' into Google

---

> **simbas** · 2026-09-28T17:41:34.000Z　
> I'm an instructional designer, and I think this is awesome!I'm going to be looking to reproduce this.

---

> **scosman** · 2026-09-28T17:42:02.000Z　
> These AI explainers are taking over. I tried getting this working back in May. The models were okay but not quite there and it was a ton of effort. Opus 5.5 seems like the tipping point.I made an OSS framework for these for when you want to go beyond one-shoting it: https://github.com/scosman/videowright- Voiceovers: aligns animations to the voiceover, can generate voiceover with elevenlabs, or will transcribe and timestamp a real voiceover- can reorder scenes both in code, and using ffmpeg for audio.- interactive controls during authoring, can ask for micro edits or re-builds- MP4 export/encoder- Generates a video from a prompt (obvs)

---

> **Vaslo** · 2026-09-28T17:42:58.000Z　
> This is great - many of us who are technical but not working in hardcore tech probably scroll by quickly on stuff we have never heard of. Getting a quick synopsis like this may drive more traffic and understanding.Thanks!

---

> **dverlaeckt80** · 2026-09-28T18:02:30.000Z　
> This is actually quite impressive from an engineer viewpoint. I just have the feeling that the videos quickly become very monotonous and rather boring due to the monotonous AI voices. If somehow you could bring dynamic variation in these videos that would be fantastic.

---

> **goshx** · 2026-09-28T18:04:40.000Z　
> This is awesome!

---

> **daok** · 2026-09-28T18:04:49.000Z　
> I like it! I bookmarked it. But I wouldn't pay for it.

---

> **1970-01-01** · 2026-09-28T18:11:12.000Z　
> This feels like when a decent book is made into a movie, and then the movie does well so someone will take the movie and summarize the plot in a YouTube video. TLDR: this is TLDR for TLDR. Just read more from the source.

---

> **j45** · 2026-09-28T18:11:54.000Z　
> This is pretty cool, I'd want to see the visualizations a little different but that's a personal preference.

---

> **fishtoaster** · 2026-09-28T18:19:12.000Z　
> Because we all contain multitudes, I can simultaneously accept that:1. I hate everything about this because I vastly prefer text over video for the same content, especially AI generated video2. There are a lot of people for whom video is their preferred medium and so this will be valuable to them.It's a technically cool project and your cost-per-video is impressively low. Best of luck!

---

> **mlaretallack** · 2026-09-28T18:38:27.000Z　
> Did not think I would like that, but really good, simple and easy summary.

---

> **ProofHouse** · 2026-09-28T18:41:50.000Z　
> I would stick with this. There's huge potential here. I'm not going to lie, I did a video of this, and it was pretty slop. Some of it didn't even make sense and was super irrelevant. That being said, refined, there's really actually some major potential with this idea.

---

> **customguy** · 2026-09-28T18:58:44.000Z　
> > And finally, a real pixel-based video of the tool: https://www.youtube.com/watch?v=k6rbHmBxSEs"a compressor uses three main organs" @ 2:97I don't dislike that it's video (because I know people who won't read can't be "made to read" by there not being "nice enough explainer videos"), but this is the kind of stuff that bothers me in both video and text, and greatly. I don't want to rant about it here because it's not specific to your product at all, it's not even specific to LLM, the internet and especially youtube is full of stuff that neither speakers/authors nor audience seem to ever parse. And if you're just downstream of big models you probably can't really influence that. But since you are NIH enjoyers, maybe you could train your own at some point? I don't want to consume such videos, but I do want those who do to have nicer ones, because that'd be good for me, too.

---

> **russellbeattie** · 2026-09-28T19:11:07.000Z　
> I just tried it out - it's pretty cool. The postscript was actually noted in the generated video about this topic, which I find amusing.I have to say, if HN were to add an AI generated paragraph summary about each link at the top of each comments page, it would probably go a long way to improving the discussions about a lot of topics. The number of people who comment based on the title of a link alone is pretty high, and I'd bet the vast majority of commenters only skim the linked pages anyways. Might as well get everyone on the same page with a quick overview.

---

> **vbernat** · 2026-09-28T19:25:21.000Z　
> This looks a good idea to let people choose their preferred medium. I am not into video either, but I turned one of my latest blog article into a video using Claude, since I thought it would be “easy.” I asked it to build the video by screencasting a browser presenting the interactive diagrams of the article and add some titles. It build some kind of recording app for me. It still took me many hours, but I think I would be faster if I redid it. I would pay to have it done faster, but I want to keep control of the text, not have a summary.The article: https://vincent.bernat.ch/en/blog/2026-spanning-tree-videoThe tool built by Claude to make the video: https://github.com/vincentbernat/vincent.bernat.ch/tree/2808...

---

> **kristopolous** · 2026-09-28T19:29:21.000Z　
> you know what might be interesting? The "HN 10 minute" -- 20 seconds per front page hn story as a podcast, daily.

---

> **eleventen** · 2026-09-28T19:35:55.000Z　
> Now I want to watch the comments as a video too.

---

> **bobajeff** · 2026-09-28T19:42:45.000Z　
> I like the concept and these explainers. It sounds like this is using a HTML based format to be similar to like a Flash / Shockwave animation to keep data size down.I wonder what the challenge would be of making these videos more interactive would be? Also I do wonder if there is any research happening in making AI explainers more trustable.

---

> **adrianwaj** · 2026-09-28T19:42:52.000Z　
> Great. Wordpress plugin would work. Get publishers to embed these videos at the top of their own articles. Allow them to tweak/fix/fine-tune them. Accept micropayments and on-demand generation. Readers can pay for better videos or "deep-dives."This will work for young readers too, illiterates, sensory-impaired and foreigners. All four!!

---

> **nonethewiser** · 2026-09-28T19:47:27.000Z　
> You guys are going to hate this but next up: Each thread in a 10 second explainer and it just autoplays

---

> **wewewedxfgdf** · 2026-09-28T20:02:27.000Z　
> How does this capture the video?

---

> **popey** · 2026-09-28T20:06:38.000Z　
> I can see vertical versions of these doing well on YT shorts or TikTok.

---

> **george_max** · 2026-09-28T20:22:39.000Z　
> Nice concept, but why not generate one video per post rather than re-generating the video for each click per user? The result is going to be the same, and it will be significantly cheaper to run.

---

> **ElijahLynn** · 2026-09-28T20:28:00.000Z　
> Love this! I've already used it a bunch to go through some HN posts that I might not have otherwise read.It's definitely a form of TLDR, but for watching?!This feels like some kind of parallel to Jev in that. If it is super fast, what other use cases may be unlocked it, as you suggest.Also, I love the simple, easy to remember domain name, HN.watch!

---

> **mrborgen** · 2026-09-28T20:30:18.000Z　
> Btw, we are hiring a new developer to join us in Oslo, Norway. We pay well and give a lot of freedom wrt working from home or at the office (hybrid solution). If getting HTML-based video generation down to 1 cent for 1 minute with 1 second delay, then please email me: per@scrimba.com.

---

> **OutOfHere** · 2026-09-28T20:47:19.000Z　
> How does this even reliably read the webpages, since so many of them block bots?

---

> **OutOfHere** · 2026-09-28T20:50:37.000Z　
> I don't see an RSS feed.

---

> **wewewedxfgdf** · 2026-09-28T21:52:24.000Z　
> I don't really see why a new programming language is needed to make explainer pages (they are not actually videos).Seems like over engineering - why not just make JavaScript/HTML?

---

> **indigodaddy** · 2026-09-28T22:37:04.000Z　
> This is super cool.Not affiliated but trymyrepo.com is very neat as well. Seems similar space.Also I had Muse agent create a skill that can do videos. Worked pretty well. Things are getting wild.Lastly, this might fun to those who like this space: (my thing)https://github.com/jgbrwn/mst3k-anything

---

> **totallygeeky** · 2026-09-28T23:52:41.000Z　
> Clicked on the demo "What caused the fall of the Roman Empire?" and immediately saw the same inadequacies I've seen in every other system like this: any attempt at visualizing a point ends up being absolute nonsense. Graphics and charts that confuse more than help, or even contradict what is being said.It ends up being a hurdle I don't think these services can surpass, given these systems understand nothing, and have no spatial reasoning. Any of these systems that claim to help explain things visually end up being a huge liability for the learner and I would never recommend them to someone.

---

> **bmau5** · 2026-09-29T01:18:37.000Z　
> As a non-technical and oft confused reader, this is very helpful! Also a very happy Scrimba user :)

---

> **spmartin823** · 2026-09-29T01:30:27.000Z　
> You should talk to the Editory guys, they did this for local news.

---

> **chimneychanga** · 2026-09-29T01:32:04.000Z　
> This is actually really useful to me, thanks! I often skip reading interesting articles because it's either too technical or because my eyes have had enough for the day. Listening to a summary video like this is a great solution!

---

> **nxc18** · 2026-09-28T19:00:55.000Z　
> Leaning into brainrot is not going to unrot your brain, even - especially - if you have ADHD.I watched the videos and confirmed they are worse than brainrot.

---

> **mrborgen** · 2026-09-28T21:13:32.000Z　
> Hahah! Thanks.We've always gotten a ton of positive comments from people with ADHD who've used our HTML videos to learn to code. Despite it not being in our target group at all when we started out.Hope your friend finds it helpful!

---

> **mrborgen** · 2026-09-28T21:06:58.000Z　
> Thank you!

---

> **nonethewiser** · 2026-09-28T19:06:18.000Z　
> I found that video to be one of the clearest. TBH they are all pretty good.This is pretty crazy. It's not hard to imagine something like Reddit deploying this as a first party feature.

---

> **mrborgen** · 2026-09-28T20:03:06.000Z　
> We have a free MCP so you are free too use our tool if you'd like to use it in your courses as well :)

---

> **mrborgen** · 2026-09-28T19:52:42.000Z　
> That video in the README is amazing! Will definitely dig into this project.We're not using Opus 5.5 btw, as it would be too expensive. Our goals is to eventually get the cost down to 1 cent for a 1 minute video, and with 1 second delay from submit to playback. For that, we need dirt cheap and lightning fast models.

---

> **jonplackett** · 2026-09-28T19:10:16.000Z　
> The thing I like about an explainer video is the personality and insight of the person giving it.Like Marquise Brownlee just has opinions I care about and I watch his videos for this reason.If a video just explains something I could just read all I’m getting is a layer of obfuscation.

---

> **itomato** · 2026-09-28T19:27:24.000Z　
> 0:04 for the first , 0:02 for the second. I'm personally all done with that.

---

> **mrborgen** · 2026-09-28T20:01:17.000Z　
> Thanks! And I agree. We're getting tons of requests for more nuance in voice selection from our users. You're currently able to say i.e. "Australian English female" in your prompts today, but you should also ideally be able to describe the voice characteristic (i.e. like a funny grandpa, engaged news reporter).What Gemini 3.8 Flash TTS is doing with generative voice design in this area super interesting.

---

> **redhed** · 2026-09-28T19:16:40.000Z　
> Yeah I feel like this would be better as summaries of textbook chapters or information rich sources, a lot of HN posts are already basically text summaries of a complex topic that it doesn't really make sense to further summarize them.

---

> **mrborgen** · 2026-09-28T20:06:10.000Z　
> We are not particularly pleased with the state of our visualizations, so I totally agree. If you have any examples of how you'd like to see the visualizations, please share them!

---

> **jonplackett** · 2026-09-28T19:08:24.000Z　
> I concur with only #1.

---

> **mrborgen** · 2026-09-28T19:44:18.000Z　
> Thanks! Several people on our team are actually exactly like you: they don't really use videos themselves for learning, but see the utility for others, and enjoy the technical challenges around building a high-performant video format.

---

> **abalashov** · 2026-09-28T20:27:15.000Z　
> Indeed. In much the same vein, I simultaneously accept that:1. I loathe video with the white-hot glow of a thousand angry suns, and loathe LLM slop-digests of things more still.2. I spend tremendous amounts of time in situations where I can listen but not read, whether driving or on my bike, and this is a legitimately useful way to catch up on HN in those situations.

---

> **mrborgen** · 2026-09-28T21:14:30.000Z　
> Thanks. Definitely lots of work left to make this feel non-AI-slop.Think there's a ton of potential here too. So we're staying on course.

---

> **xp84** · 2026-09-28T19:31:53.000Z　
> For most articles these days, we'd have to first have a separate bot get the archive.is link for it!But I'm skeptical that people would embrace it. It's more about the optics, and it also relates to the old principle of "Read the article -- don't start opining based only on the headline." Many would probably say that you shouldn't offer an opinion if you've only read an AI distillation.It could be wrong - or more likely, the article acknowledges likely objections and refutes them well, but that part didn't make it into the summary, so everyone starts raising very un-insightful points as though the author was oblivious to them.

---

> **mrborgen** · 2026-09-28T20:17:57.000Z　
> Nice! Will check out that repo.You can use MCP to generate an Explainer video next time if you want. It's currently free, as the tokens for directing and scripting it is offloaded to your agent. And then we cover the TTS for the time being.

---

> **mrborgen** · 2026-09-28T20:02:16.000Z　
> Yes! We can set that up as a video quite easily. Don't have the infrastructure to push it as a podcast yet though.

---

> **mrborgen** · 2026-09-28T20:36:57.000Z　
> We usually include a section about the comments in the end of the video. But perhaps we should add a dedicated "Comments Video" as well.

---

> **jameshart** · 2026-09-28T19:51:44.000Z　
> And there’s no way to stop it

---

> **mrborgen** · 2026-09-28T20:18:31.000Z　
> It doesn't actually capture it as a video, it's just HTML with a voice over essentially.

---

> **mrborgen** · 2026-09-28T20:09:28.000Z　
> I hope so! We actually already support vertical videos when generated via the web ui (by clicking the mobile button).

---

> **mrborgen** · 2026-09-28T20:33:25.000Z　
> We do cache them like that! As I wrote:"We create them on-the-fly the first time someone clicks on a link."Though I realise it could have been said more explicitly. But the second time someone clicks the link we re-use the same explainer.

---

> **mrborgen** · 2026-09-28T20:34:36.000Z　
> Glad to hear that. Adding Jev as our "pre-planner" is very high on our todo list. It's the perfect tool for this kind of thing.

---

> **wewewedxfgdf** · 2026-09-28T20:32:27.000Z　
> >> getting HTML-based video generation down to 1 cent for 1 minute with 1 second delayHow would you do that?

---

> **mrborgen** · 2026-09-28T20:50:06.000Z　
> That was one of the challenges when building this. We ended up using Firecrawl. But even so there are a few pages we aren't able to read. In which case we use the Algolia API to get the HN comments and generate the video about the HN reaction on the article instead.

---

> **taneq** · 2026-09-29T00:29:10.000Z　
> They understand a heck of a lot more than they did. We’ve gone from “understands how to form a coherent sentence, mostly” to “understands enough about the world to generate a 20 minute infotainment video that you wouldn’t pick as AI unless you’re looking for the current tells” in, what, 5 years?It’s worth pondering what the world would be like if current AI methods don’t hit a glass ceiling, and get to the point where they can legitimately produce better, more creative, higher ‘nutritional value’ output than humans can. How do we spend our lives?

---

> **dd8601fn** · 2026-09-28T21:36:00.000Z　
> I gave it a fair shake (10 or so).
> I'll say this... it does the job of "I can't spend 45 minutes on a journal article that's already over my head, or get through 20 pages of blog slop, so please give me the summary version of this".The select comment/conversation slide is a nice touch, though it's sure making some choices there.Main problem seems to be that the sameness of the format (it's clearly following a strict template) and voice do make it feel very repetitive, real fast. I'm not sure how you get consistent results AND solve for that, though.

---

> **simbas** · 2026-09-28T22:36:34.000Z　
> Thanks!

---

> **scosman** · 2026-09-28T19:56:27.000Z　
> honestly it's horrible compared to some of the Opus 5.5 ones. But yeah, at the latency/speed you're looking for it's a different ballpark. Let Opus write the style and reference screens/animations, let your small fast model assemble it from parts.

---

> **xp84** · 2026-09-28T19:26:12.000Z　
> All of what you said is great, and I especially detest the proliferation of slop videos on YouTube, where it makes no sense to drown out the ample supply of such personalities and insights with AI voices summarizing wikipedia or Reddit threads over AI imagery slideshows.But given how good a job this seemed to do at giving me more than just headlines, I'd love to have maybe even just an audio podcast feed of the top 10 stories like this compiled a few times a day. I would listen while I'm doing things when reading isn't practical.tl;dr agree that we don't need this to replace reading, but I see that it can be a useful tool.

---

> **nonethewiser** · 2026-09-28T19:28:34.000Z　
> Presumably you also like that they are explaining things right? I mean that seems like the more critical step. Otherwise if it's just Marquise Brownlee, you could just watch Marquise Brownlee say the same sequence of random words for 3 minutes a few times per day.

---

> **xp84** · 2026-09-28T19:36:34.000Z　
> To me, the use case is to go from an often opaque headline ("Using Nix and containerd with Jev on macOS") to a paragraph which hopefully gives some strong hints as to what those things are and why it's interesting, because the articles often are written for an audience already deeply into all the topics. Because often a few of those terms I might have no clue about and thus scroll on by, but with a brief "why you should care" explanation, I might realize it's actually something cool.

---

> **kekebo** · 2026-09-28T19:41:39.000Z　
> I have ocd so I concur with only #2 for equilibrium.

---

> **itomato** · 2026-09-29T00:44:55.000Z　
> Is it a legit summary? Does it derail you?

---

> **kristopolous** · 2026-09-28T20:18:39.000Z　
> just ffmpeg it -vn and post it as an rss xml ... the audio sans video is a fine first step.

---

> **fragmede** · 2026-09-28T20:26:23.000Z　
> Post them to YouTube as shorts and capture view revenue.

---

> **samplifier** · 2026-09-28T20:04:43.000Z　
> And one has no eyelids.
> And I must blink.
> And not topple over.
> And out.

---

> **mrborgen** · 2026-09-28T20:42:13.000Z　
> We currently spend ~$0.4 on a video (without images) and a have a few seconds of delay before playback. So it's a matter of turning every stone in order to optimize it further. We're going to add Jev asap, as it's an obvious improvement along both axes.

---

> **OutOfHere** · 2026-09-29T00:03:48.000Z　
> Instead of using HN comments which can be a gross distortion of an article, it is better to ask the user to upload a PDF of the full text of the article. It is easy for the user to create such a PDF. Thereafter, subsequent users should have an opportunity to upload a new PDF if they so desire.

---

> **jonplackett** · 2026-09-28T19:34:28.000Z　
> Yeah I do see your point. And for some reason making it into audio does seem less offensive to me. Maybe it’s because it at least transforms it into something I can do while doing something else. Whereas a video is basically the same mode of operation: staring at a screen.I’m still basically against this though. I consider it slop.

---

> **TomGarden** · 2026-09-28T20:31:56.000Z　
> I just had opus make me a tts mobile app that grabs the top 20 HN stories and the top 5 comments for each and read them out to me (using one of the higher quality built in TTS voices on my pixel). The summarization is the worst part of this imo, so pure TTS wins

---

> **taneq** · 2026-09-29T00:24:14.000Z　
> Yeah, there’s been an explosion of that guff over the past few weeks. “POV: You are a $x who $y”. “Every level of being a $x”. “$x explainer”.The quality is getting very smooth but that just makes it worse because you can’t quite trust anything any more. It’s like the mental equivalent of HFCS.

---

> **jonplackett** · 2026-09-28T19:31:13.000Z　
> I feel I need to explain beyond just a whine.I think this is exactly the opposite of what AI should be used for. It is going to make people dumb.Watching a video instead of engaging your own brain makes you feel like you learned something without actually trying and I would bet it works much less well.If someone is there adding something beyond what is already there - ie someone like Maruqise. Then it makes sense for them to be there.If not it is just brain rot.People already have issues with concentration. Allowing them to further allow that muscle to atrophy will not be good.

## 关联链接

- https://docs.scrimba.com/explain/introductionAnd
- https://imba.io/We’ve
- https://www.youtube.com/watch?v=k6rbHmBxSEsWould

## 导航

- 项目页：[[10-项目/hn.watch_aae1d6f2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
