---
type: "corpus"
item_id: "67a4355a563c60f0"
title: "Show HN: Put a Run Button on the SQL in Your Blog Posts"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49834998"
project_url: "https://seaquel.app/blog/run-sql-in-your-blog-posts"
author: "mikenikles"
published_at: "2026-09-24T18:37:16Z"
captured_at: "2026-09-25T13:42:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-25"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_mikenikles
  - story_49834998
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Put a Run Button on the SQL in Your Blog Posts

> [!info] 一句话导读
> Toggle theme svg]:px-2.5 gap-2" type="button" id="bits-s22" aria-haspopup="menu" aria-expanded="false" data-state="closed" data-dropdown-menu-trigger=""> Downlo…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49834998>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：mikenikles　|　发布：2026-09-24T18:37:16Z
> 项目链接：<https://seaquel.app/blog/run-sql-in-your-blog-posts>
> 采集：2026-09-25T13:42:25+08:00　|　id：`67a4355a563c60f0`

## 正文

Seaquel Product
 Learn SQL
 Pricing
 Compare
 Changelog
 Blog
 Docs
 GitHub
Toggle theme svg]:px-2.5 gap-2" type="button" id="bits-s22" aria-haspopup="menu" aria-expanded="false" data-state="closed" data-dropdown-menu-trigger=""> Download
svg]:px-2.5 -ml-2 gap-2" href="/blog"> All posts Blog Put a Run Button on the SQL in Your Blog Posts
 Put a Run Button on the SQL in Your Blog Posts
 A free embed that turns the SQL in your blog posts into real Postgres queries readers can edit and run without leaving the page.
 Mike Nikles
 · September 23, 2026 · 6 min read
On this page
 Adding it to a post
 Bring your own tables
 Several examples, one dataset
 Show the mistake, then the fix
 What your readers download
 Making it match your blog
 Where it works, and where it doesn't
 Why I'm giving it away
 Many SQL tutorial I’ve read have the same shape. Here’s a query, here’s the result, now imagine what happens when you change the WHERE clause.
 Why imagine it though?. I open a terminal, start a database, copy the schema out of the post (if the author included one), and by the time it’s all running I’ve forgotten what I was trying to learn.
 So I built a small thing for people who write about SQL. It looks like this:
SELECT p.name, sum(oi.quantity * oi.unit_price) AS revenue
FROM order_items oi
JOIN products p ON p.id = oi.product_id
GROUP BY p.name
ORDER BY revenue DESC
LIMIT 5
 Hit Run . Then change LIMIT 5 to LIMIT 3 , or DESC to ASC , and run it again. That’s real Postgres running in your browser tab. There’s no server behind it, no account, and nothing to install.
 It’s free, and you can put it in your own posts.
 Adding it to a post
 You need one script tag per page and one  element per example:
 < script type = " module " src = " https://seaquel.app/embed/seaquel-sql.js " > </ script >
< seaquel-sql >
 < pre > SELECT * FROM customers WHERE country = 'CA' </ pre >
 < a href = " https://seaquel.app " > Powered by Seaquel </ a >
 </ seaquel-sql >
 The  holds the starting query. If the script doesn’t load, or your platform strips it out, readers still see the query as plain text, so the post never breaks.
 Without any setup, queries run against a small sample shop with customers , products , orders and order_items . It’s the same data behind Learn SQL , in case you want to point readers somewhere to keep practicing.
 Bring your own tables
 Most posts need their own data. Put the schema and rows in a  inside the element. Readers don’t see it, but it runs before their first query.
 < seaquel-sql >
 < script type = " text/sql " >
 CREATE TABLE books ( id int PRIMARY KEY , title text , author text , published int ) ;
 CREATE TABLE reviews ( id int PRIMARY KEY , book_id int REFERENCES books ( id ) , stars int ) ;
 INSERT INTO books VALUES
 ( 1 , 'The Pragmatic Programmer' , 'Hunt, Thomas' , 1999 ) ,
 ( 2 , 'Designing Data-Intensive Applications' , 'Kleppmann' , 2017 ) ,
 ( 3 , 'SQL Antipatterns' , 'Karwin' , 2010 ) ,
 ( 4 , 'Database Internals' , 'Petrov' , 2019 ) ,
 ( 5 , 'The Art of PostgreSQL' , 'Fontaine' , 2017 ) ;
 INSERT INTO reviews VALUES
 ( 1 , 1 , 5 ) , ( 2 , 1 , 4 ) , ( 3 , 2 , 5 ) , ( 4 , 2 , 5 ) , ( 5 , 2 , 4 ) , ( 6 , 3 , 3 ) ;
 </ script >
 < pre >
 SELECT b . title
 FROM books b
 LEFT JOIN reviews r ON r . book_id = b . id
 WHERE r . id IS NULL
 </ pre >
 < a href = " https://seaquel.app " > Powered by Seaquel </ a >
 </ seaquel-sql >
 This gives you the books nobody has reviewed yet:
SELECT b.title
FROM books b
LEFT JOIN reviews r ON r.book_id = b.id
WHERE r.id IS NULL
 Several examples, one dataset
 A tutorial usually runs a handful of queries over the same tables. Instead of repeating the setup in every example, give it an id and point each widget at it:
 < script type = " text/sql " id = " library " >
 CREATE TABLE books ( . . . ) ;
 INSERT INTO books VALUES ( . . . ) ;
 </ script >
< seaquel-sql setup = " #library " >
 < pre > SELECT count ( * ) FROM books </ pre >
 </ seaquel-sql >
 Widgets that share a setup also share the tables, so the data only loads once. This one runs on the same books as the example above, and shows the average rating per title:
SELECT b.title, count(r.id) AS reviews, round(avg(r.stars), 1) AS avg_stars
FROM books b
LEFT JOIN reviews r ON r.book_id = b.id
GROUP BY b.title
ORDER BY avg_stars DESC NULLS LAST
 Every run happens inside a transaction that gets rolled back afterwards. Readers can DELETE FROM books or DROP TABLE reviews just to see what happens, and the next run still starts from your data. Go ahead and try it on the widget above.
 Show the mistake, then the fix
 A lot of writing about SQL starts with a query that doesn’t work. You show it failing, explain why, then show the version that does. Put two  elements in the widget and they become tabs:
 < seaquel-sql setup = " #library " >
 < pre title = " Broken query " data-result = " error " > . . . </ pre >
 < pre title = " Fixed query " data-result = " ok " > ... </ pre >
 </ seaquel-sql >
 The title is the tab’s label. data-result is optional: error puts a red cross on the tab and ok a green check. When an error tab fails the way it’s meant to, the widget offers to run the next tab. Each tab keeps its own edits, so readers can switch back and forth without losing anything. You’re not limited to two tabs, either.
 Here’s a mistake almost everyone makes with GROUP BY at some point:
SELECT b.author, b.title, count(r.id) AS reviews
FROM books b
LEFT JOIN reviews r ON r.book_id = b.id
GROUP BY b.author
ORDER BY reviews DESC
SELECT b.author, b.title, count(r.id) AS reviews
FROM books b
LEFT JOIN reviews r ON r.book_id = b.id
GROUP BY b.author, b.title
ORDER BY reviews DESC
 Postgres won’t pick a title for each author on its own, so every column you select has to be in the GROUP BY or inside an aggregate like count() . The SQL error pages on this site are built the same way, one tabbed widget per error.
 What your readers download
 The script is about 6 KB gzipped, and that’s all that loads with the page.
 Postgres itself is PGlite , a WebAssembly build of the real thing. It’s around 3.5 MB compressed, and it only downloads when a reader hovers over or clicks into a widget. A page with ten examples still loads it only once, and after that it comes from the browser cache. If you’ve written a tutorial that spans several posts, readers download it on the first one, and the rest load it from their cache.
 Queries never leave the reader’s tab. The script doesn’t set cookies, doesn’t run analytics, and doesn’t send anything back to me.
 Making it match your blog
 The widget follows the reader’s light or dark setting. To pin one, add theme="light" or theme="dark" to the element.
 Colors, corners and fonts are CSS variables you set on the element:
 seaquel-sql {
 --sq-accent : #6d28d9 ;
 --sq-accent-fg : #ffffff ;
 --sq-radius : 4px ;
 --sq-font : inherit ;
 }
 Variable What it controls
 --sq-bg , --sq-fg Background and main text
 --sq-muted Label, inactive tabs, status line and footer link
 --sq-subtle Toolbar and table header background
 --sq-border Borders and row dividers
 --sq-accent , --sq-accent-fg The Run button and focus ring
 --sq-error , --sq-error-bg Error messages
 --sq-danger , --sq-success The cross and check on tabs
 --sq-keyword , --sq-string , --sq-number , --sq-comment , --sq-function , --sq-operator Syntax highlighting
 --sq-radius Corner radius
 --sq-font , --sq-mono UI font and code font
 Your blog’s own CSS can’t reach inside the widget, which is on purpose. Plenty of blog themes style every table or * on the page, and without that wall the results table would end up unreadable on many sites. The variables are the way in.
 Where it works, and where it doesn’t
 You need a place where you can add a script tag. That covers Hugo, Jekyll, Astro, Eleventy, Next.js, Ghost (use an HTML card) and self-hosted WordPress (use a Custom HTML block).
 Medium, dev.to and Substack don’t allow scripts in posts, so the widget won’t run there. Thanks to the  fallback, the query still shows up as text, which is no worse than what you have today.
 One thing to watch for: MDX and some other blog engines read a bare < as the start of a tag, so WHERE price < 50 can break your build. Write it as WHERE price &lt; 50 instead. The widget turns it back into < before running it.
 Why I’m giving it away
 Mostly for the “Powered by Seaquel” link. Seaquel is the desktop SQL client I build, and people who write about SQL are exactly the people I’d like to know about it. That’s the trade. The widget is free, and since it runs on your readers’ machines there’s nothing for me to meter, so there are no usage limits. All I ask is that you leave the link in.
 If you use it, I’d love to see the post, so send it my way on Discord . Same if it breaks on your blog. I’ve tested it on a handful of setups, but yours may not be one of them.
Written by
 Mike Nikles Founder
Share
 svg]:px-2.5 justify-start gap-2" href="https://bsky.app/intent/compose?text=Put%20a%20Run%20Button%20on%20the%20SQL%20in%20Your%20Blog%20Posts%20" target="_blank" rel="noreferrer"> Share on Bluesky svg]:px-2.5 justify-start gap-2" href="https://x.com/intent/post?text=Put%20a%20Run%20Button%20on%20the%20SQL%20in%20Your%20Blog%20Posts&url=" target="_blank" rel="noreferrer"> Share on X svg]:px-2.5 justify-start gap-2" type="button"> Copy link svg]:px-2.5 justify-start gap-2" href="mailto:?subject=Put%20a%20Run%20Button%20on%20the%20SQL%20in%20Your%20Blog%20Posts&body="> Email a friend
Reading time
 6 min
 About 1,370 words
Keep reading
 April 18, 2026
 1 min read
Welcome to the Seaquel Blog
Why I'm starting a blog, what you can expect from it, and how it fits alongside the changelog.
 Mike Nikles Founder
Liked this? Get the next one.
 New writing from the Seaquel team, delivered once a week.
 svg]:px-3" type="submit"> Subscribe
 Send me new blog posts by email.
Seaquel
 The modern database client built for speed, efficiency, and
 intelligence. Open source.
Product
 Features
 All Features
 Learn SQL
 SQL Errors
 Pricing
 Download
 Changelog
Resources
 Blog
 GitHub
 Discord Community
 Report Issue
 Metrics
© 2026 Seaquel. MIT Licensed.
 Terms Privacy
svg]:px-2.5 gap-2" href="/download"> Download Seaquel

## 关联链接

- https://bsky.app/intent/compose?text=Put%20a%20Run%20Button%20on%20the%20SQL%20in%20Your%20Blog%20Posts%20
- https://seaquel.app
- https://seaquel.app/embed/seaquel-sql.js
- https://x.com/intent/post?text=Put%20a%20Run%20Button%20on%20the%20SQL%20in%20Your%20Blog%20Posts&url=

## 导航

- 项目页：[[10-项目/seaquel.app_4222ed2c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
