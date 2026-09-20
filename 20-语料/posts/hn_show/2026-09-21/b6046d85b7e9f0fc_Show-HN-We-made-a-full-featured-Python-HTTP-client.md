---
type: "corpus"
item_id: "b6046d85b7e9f0fc"
title: "Show HN: We made a full-featured Python HTTP client work inside WASI"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49122806"
author: "mesahm"
published_at: "2026-07-31T13:21:37Z"
captured_at: "2026-09-21T03:11:07+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_mesahm
  - story_49122806
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:83d"
---

# Show HN: We made a full-featured Python HTTP client work inside WASI

> [!info] 一句话导读
> Auto light/dark, in light mode

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49122806>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：mesahm　|　发布：2026-07-31T13:21:37Z
> 项目链接：—
> 采集：2026-09-21T03:11:07+08:00　|　id：`b6046d85b7e9f0fc`

## 正文

Menu
Expand
Light mode
Dark mode
Auto light/dark, in light mode
Auto light/dark, in dark mode
Skip to content
⭐ Niquests 3.21 is out! Native WASI support.
Niquests Documentation – Drop-in replacement for Requests – HTTP/1.1, HTTP/2, and HTTP/3.
Installation of Niquests
Quickstart
Advanced usage
Authentication
Requests → Niquests guide
HTTPX → Niquests guide
Niquests extension ecosystem
Frequently asked questions
Support
Vulnerability disclosure
Release process and rules
Community updates
Release History
Developer interface
Contributor’s guide
Authors
Back to top
View this page
Edit this page
Quickstart ¶
Eager to get started? This page gives a good introduction to getting started
with Niquests.
First, make sure that:
Niquests is installed
Niquests is up-to-date
Let’s get started with some simple examples.
Note
Standalone async examples must be enclosed in an async function and started
with asyncio.run . Short async snippets below may be pasted into the
body of the documented main() wrapper.
import asyncio
 import niquests
async def main () -> None :
 """Paste the example code here."""
if __name__ == "__main__" :
 asyncio . run ( main ())
Make a request ¶
Making a request with Niquests is very simple.
Begin by importing the Niquests module:
import niquests
Now, let’s try to get a webpage. For this example, let’s get GitHub’s public
timeline.
🔂 Sync
 r = niquests . get ( 'https://api.github.com/events' )
🔀 Async
 r = await niquests . aget ( 'https://api.github.com/events' )
Now, we have a Response object called r . We can
get all the information we need from this object.
Niquests’ simple API makes all forms of HTTP requests straightforward. For
example, this is how you make an HTTP POST request:
🔂 Sync
 r = niquests . post ( 'https://httpbingo.org/post' , data = { 'key' : 'value' })
🔀 Async
 r = await niquests . apost ( 'https://httpbingo.org/post' , data = { 'key' : 'value' })
Nice, right? What about the other HTTP request methods: PUT, PATCH, DELETE,
HEAD, OPTIONS, and QUERY? These are all just as simple:
🔂 Sync
 r = niquests . put ( 'https://httpbingo.org/put' , data = { 'key' : 'value' })
 r = niquests . patch ( 'https://httpbingo.org/patch' , data = { 'key' : 'value' })
 r = niquests . delete ( 'https://httpbingo.org/delete' )
 r = niquests . head ( 'https://httpbingo.org/get' )
 r = niquests . options ( 'https://httpbingo.org/get' )
 r = niquests . query ( 'https://httpbingo.org/anything' , json = { 'key' : 'value' })
🔀 Async
 r = await niquests . aput ( 'https://httpbingo.org/put' , data = { 'key' : 'value' })
 r = await niquests . apatch ( 'https://httpbingo.org/patch' , data = { 'key' : 'value' })
 r = await niquests . adelete ( 'https://httpbingo.org/delete' )
 r = await niquests . ahead ( 'https://httpbingo.org/get' )
 r = await niquests . aoptions ( 'https://httpbingo.org/get' )
 r = await niquests . aquery ( 'https://httpbingo.org/anything' , json = { 'key' : 'value' })
QUERY , standardized by RFC 10008 , carries a query in the request body.
Like GET , it is safe and idempotent; unlike GET , it can carry content.
Use Session.query() or
 AsyncSession.query() when working with a session.
That’s all well and good, but it’s also only the start of what Niquests can
do.
Passing parameters in URLs ¶
You often want to send some sort of data in the URL’s query string. If
you were constructing the URL by hand, this data would be given as key/value
pairs in the URL after a question mark, e.g. httpbingo.org/get?key=val .
Niquests allows you to provide these arguments as a dictionary of strings,
using the params keyword argument. As an example, if you wanted to pass
 key1=value1 and key2=value2 to httpbingo.org/get , you would use the
following code:
🔂 Sync
 payload = { 'key1' : 'value1' , 'key2' : 'value2' }
 r = niquests . get ( 'https://httpbingo.org/get' , params = payload )
🔀 Async
 payload = { 'key1' : 'value1' , 'key2' : 'value2' }
 r = await niquests . aget ( 'https://httpbingo.org/get' , params = payload )
You can see that the URL has been correctly encoded by printing the URL:
print ( r . url ) # 'https://httpbingo.org/get?key1=value1&key2=value2'
Note that any dictionary key whose value is None will not be added to the
URL’s query string.
You can also pass a list of items as a value:
🔂 Sync
 payload = { 'key1' : 'value1' , 'key2' : [ 'value2' , 'value3' ]}
 r = niquests . get ( 'https://httpbingo.org/get' , params = payload )
print ( r . url ) # 'https://httpbingo.org/get?key1=value1&key2=value2&key2=value3'
🔀 Async
 payload = { 'key1' : 'value1' , 'key2' : [ 'value2' , 'value3' ]}
 r = await niquests . aget ( 'https://httpbingo.org/get' , params = payload )
print ( r . url ) # 'https://httpbingo.org/get?key1=value1&key2=value2&key2=value3'
Response content ¶
We can read the content of the server’s response. Consider the GitHub timeline
again:
🔂 Sync
 import niquests
r = niquests . get ( 'https://api.github.com/events' )
 print ( r . text ) # '[{"repository":{"open_issues":0,"url":"https://github.com/...
🔀 Async
 import niquests
r = await niquests . aget ( 'https://api.github.com/events' )
 print ( r . text ) # '[{"repository":{"open_issues":0,"url":"https://github.com/...
Niquests automatically decodes content from the server. Most Unicode character
sets are decoded seamlessly.
When you make a request, Niquests makes educated guesses about the encoding of
the response based on the HTTP headers. The text encoding guessed by Niquests
is used when you access r.text . You can inspect and
change it through the r.encoding property:
print ( r . encoding ) # 'utf-8'
r . encoding = 'ISO-8859-1' # Force a specific encoding.
Warning
If Niquests cannot decode the content to a string with confidence,
it returns None .
If you change the encoding, Niquests will use the new value of
 r.encoding whenever you access
 r.text . You might do this when
you can apply special logic to work out what the encoding of the content will
be. For example, HTML and XML can specify their encoding in their bodies. In
situations like this, use r.content to find the
encoding, and then set r.encoding . This will let
you use r.text with
the correct encoding.
Niquests will also use custom encodings if you need them. If
you have created your own encoding and registered it with the codecs
module, you can simply use the codec name as the value of
 r.encoding and
Niquests will handle the decoding for you.
Binary response content ¶
You can also access the response body as bytes, for non-text requests:
>>> r . content
 b'[{"repository":{"open_issues":0,"url":"https://github.com/...
The gzip and deflate content codings are automatically decoded for you.
The br content coding is automatically decoded for you if a Brotli library
like brotli or brotlicffi is installed.
The zstd content coding is automatically decoded on Python 3.14 and later using
the standard-library compression.zstd module. On older Python versions, install
the zstandard library or the niquests[zstd]
extra to enable it.
For example, to create an image from binary data returned by a request, you can
use the following code:
>>> from PIL import Image
 >>> from io import BytesIO
>>> i = Image . open ( BytesIO ( r . content ))
JSON response content ¶
There’s also a built-in JSON decoder for JSON data:
🔂 Sync
 import niquests
r = niquests . get ( 'https://api.github.com/events' )
 print ( r . json ()) # [{'repository': {'open_issues': 0, 'url': 'https://github.com/...
🔀 Async
 import niquests
r = await niquests . aget ( 'https://api.github.com/events' )
 print ( r . json ()) # [{'repository': {'open_issues': 0, 'url': 'https://github.com/...
In case the JSON decoding fails, r.json() raises an exception. For example, if
the response gets a 204 (No Content), or if the response contains invalid JSON,
attempting r.json() raises
 JSONDecodeError . This wrapper exception
provides interoperability for multiple exceptions that may be thrown by different
Python versions and JSON serialization libraries.
 Response.json() attempts
to parse the response body regardless of its Content-Type header.
The success of a call to r.json() does not
indicate the success of the response. Some servers may return a JSON object in a
failed response (e.g. error details with HTTP 500). Such JSON will be decoded
and returned. To check that a request is successful, use
 r.raise_for_status() or check that
 r.status_code is what you expect.
Note
Since Niquests 3.2,
 r.raise_for_status() is chainable because it
returns the response when no error is raised.
Tip
Niquests supports using orjson instead of the json standard
library. To use that feature, install orjson or niquests[speedups] .
This can dramatically improve performance.
Tip
For typed JSON deserialization (e.g. with msgspec , pydantic , or cattrs ),
use r.content directly instead of
 r.json() for significantly better performance.
For example, msgspec.json.decode(r.content, type=list[User]) decodes bytes into typed
objects in a single pass, avoiding the intermediate dict. This is 2-5x faster than
 msgspec.convert(r.json(), list[User]) .
Raw response content ¶
In the rare case that you’d like to get the raw socket response from the
server, you can access r.raw . If you want to do this,
make sure you set
 stream=True in your initial request. Once you do, you can do this:
🔂 Sync
 r = niquests . get ( 'https://api.github.com/events' , stream = True )
r . raw
 #
r . raw . read ( 10 )
 # b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
🔀 Async
 r = await niquests . aget ( 'https://api.github.com/events' , stream = True )
r . raw
 #
await r . raw . read ( 10 )
 # b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
In general, however, you should use a pattern like this to save what is being
streamed to a file:
🔂 Sync
 with open ( filename , 'wb' ) as fd :
 for chunk in r . iter_content ( chunk_size = 128 ):
 fd . write ( chunk )
🔀 Async
 with open ( filename , 'wb' ) as fd :
 async for chunk in await r . iter_content ( chunk_size = 128 ):
 fd . write ( chunk )
Warning
Consider aiofiles or a similar library to avoid blocking
file I/O in async code.
Using Response.iter_content will handle a lot
of what you would otherwise have to handle when using
 Response.raw directly. When streaming a
download, the above is the preferred and recommended way to retrieve the
content. Note that chunk_size can be freely adjusted to a number that
may better fit your use cases.
Note
An important note about using
 Response.iter_content versus
 Response.raw .
 Response.iter_content will automatically
decode the gzip and deflate content codings.
 Response.iter_raw is a raw stream of bytes; it does not
transform the response content. If you really need access to the bytes as they
were returned, use Response.iter_raw .
Custom headers ¶
To add HTTP fields to a request, pass a dictionary to the
 headers parameter.
For example, we didn’t specify our user-agent in the previous example:
🔂 Sync
 url = 'https://api.github.com/some/endpoint'
 headers = { 'user-agent' : 'my-app/0.0.1' }
r = niquests . get ( url , headers = headers )
🔀 Async
 url = 'https://api.github.com/some/endpoint'
 headers = { 'user-agent' : 'my-app/0.0.1' }
r = await niquests . aget ( url , headers = headers )
Custom headers have lower precedence than more specific sources of information.
For example:
Authorization headers set with headers= will be overridden if credentials
are specified in .netrc , which in turn will be overridden by the auth=
parameter. Niquests searches for the netrc file at ~/.netrc , ~/_netrc ,
or at the path specified by the NETRC environment variable.
Authorization headers will be removed if you get redirected off-host.
Proxy-Authorization headers will be overridden by proxy credentials provided in the URL.
Content-Length headers will be overridden when we can determine the length of the content.
Furthermore, Niquests does not change its behavior based on which custom
headers are specified. The headers are passed into the final request.
All header values must be a string or bytes-like value. Although Unicode values
are permitted, header values should generally be representable in Latin-1.
More complicated POST requests ¶
Typically, you want to send form-encoded data, much like an HTML form.
To do this, simply pass a dictionary to the data argument. Your
dictionary of data will automatically be form-encoded when the request is made:
🔂 Sync
 payload = { 'key1' : 'value1' , 'key2' : 'value2' }
 r = niquests . post ( 'https://httpbingo.org/post' , data = payload )
 print ( r . json ()[ 'form' ]) # {'key1': ['value1'], 'key2': ['value2']}
🔀 Async
 payload = { 'key1' : 'value1' , 'key2' : 'value2' }
 r = await niquests . apost ( 'https://httpbingo.org/post' , data = payload )
 print ( r . json ()[ 'form' ]) # {'key1': ['value1'], 'key2': ['value2']}
The data argument can also have multiple values for each key. This can be
done by making data either a list of tuples or a dictionary with lists
as values. This is particularly useful when the form has multiple elements that
use the same key:
🔂 Sync
 payload_tuples = [( 'key1' , 'value1' ), ( 'key1' , 'value2' )]
 r1 = niquests . post ( 'https://httpbingo.org/post' , data = payload_tuples )
 payload_dict = { 'key1' : [ 'value1' , 'value2' ]}
 r2 = niquests . post ( 'https://httpbingo.org/post' , data = payload_dict )
 assert r1 . json ()[ 'form' ] == r2 . json ()[ 'form' ]
🔀 Async
 payload_tuples = [( 'key1' , 'value1' ), ( 'key1' , 'value2' )]
 r1 = await niquests . apost ( 'https://httpbingo.org/post' , data = payload_tuples )
 payload_dict = { 'key1' : [ 'value1' , 'value2' ]}
 r2 = await niquests . apost ( 'https://httpbingo.org/post' , data = payload_dict )
 assert r1 . json ()[ 'form' ] == r2 . json ()[ 'form' ]
There are times that you may want to send data that is not form-encoded. If
you pass in a string instead of a dictionary, that data will be posted directly.
For example, to encode JSON manually:
🔂 Sync
 import json
url = 'https://httpbingo.org/post'
 payload = { 'some' : 'data' }
 r = niquests . post ( url , data = json . dumps ( payload ))
🔀 Async
 import json
url = 'https://httpbingo.org/post'
 payload = { 'some' : 'data' }
 r = await niquests . apost ( url , data = json . dumps ( payload ))
The code above does not add a Content-Type: application/json header.
If you need that header set and do not want to encode the dictionary yourself,
you can pass the object directly using the json parameter, and it will be
encoded automatically:
🔂 Sync
 r = niquests . post ( url , json = payload )
🔀 Async
 r = await niquests . apost ( url , json = payload )
The json parameter is ignored if non-empty data or files is passed.
Custom JSON serialization ¶
Use json_encoder to customize request-side JSON serialization. The encoder
is synchronous, even with async APIs, and must return str or bytes . For
example, msgspec can serialize supported
objects directly to bytes:
🔂 Sync
 import msgspec
 import niquests
class User ( msgspec . Struct ):
 name : str
 active : bool
payload = User ( name = "Lina" , active = True )
 encoder = msgspec . json . encode
 url = "https://httpbingo.org/post"
 r = niquests . post ( url , json = payload , json_encoder = encoder )
with niquests . Session ( json_encoder = encoder ) as session :
 r = session . post ( url , json = payload )
🔀 Async
 import msgspec
 import niquests
class User ( msgspec . Struct ):
 name : str
 active : bool
payload = User ( name = "Lina" , active = True )
 encoder = msgspec . json . encode
 url = "https://httpbingo.org/post"
 r = await niquests . apost ( url , json = payload , json_encoder = encoder )
async with niquests . AsyncSession ( json_encoder = encoder ) as session :
 r = await session . post ( url , json = payload )
Top-level calls create a temporary session, so json_encoder can be passed directly
to post() , query() ,
 apost() , or aquery() . A session-level
encoder applies to every request made through that session.
POST multipart form data without a file ¶
Since Niquests 3.1.2, you can override the default
 application/x-www-form-urlencoded encoding and submit multipart form data
without a file:
🔂 Sync
 r = niquests . post (
 url , data = payload , headers = { 'Content-Type' : 'multipart/form-data' }
 )
🔀 Async
 r = await niquests . apost (
 url , data = payload , headers = { 'Content-Type' : 'multipart/form-data' }
 )
Note
You can specify a boundary in the header value. Niquests reuses that
boundary; otherwise, it generates one.
POST a multipart-encoded file ¶
Niquests makes it simple to upload multipart-encoded files:
🔂 Sync
 with open ( 'report.xls' , 'rb' ) as report :
 r = niquests . post ( url , files = { 'file' : report })
🔀 Async
 with open ( 'report.xls' , 'rb' ) as report :
 r = await niquests . apost ( url , files = { 'file' : report })
Warning
Opening a local file is blocking. Use an async file library
when blocking file I/O is unsuitable for your application.
You can set the filename, content type, and headers explicitly:
🔂 Sync
 with open ( 'report.xls' , 'rb' ) as report :
 files = {
 'file' : (
 'report.xls' , report , 'application/vnd.ms-excel' , { 'Expires' : '0' }
 )
 }
 r = niquests . post ( url , files = files )
🔀 Async
 with open ( 'report.xls' , 'rb' ) as report :
 files = {
 'file' : (
 'report.xls' , report , 'application/vnd.ms-excel' , { 'Expires' : '0' }
 )
 }
 r = await niquests . apost ( url , files = files )
You can also send strings as files:
🔂 Sync
 files = { 'file' : ( 'report.csv' , 'some,data,to,send \n another,row,to,send \n ' )}
 r = niquests . post ( url , files = files )
🔀 Async
 files = { 'file' : ( 'report.csv' , 'some,data,to,send \n another,row,to,send \n ' )}
 r = await niquests . apost ( url , files = files )
In the event you are posting a very large file as a multipart/form-data
request, you may want to stream the request. By default, Niquests does not
provide a multipart streaming encoder, but a separate package does:
 requests-toolbelt . You should read the toolbelt’s documentation for more details about how to use it.
For information about sending multiple files in one request, see the advanced
section.
Response status codes ¶
We can check the response status code:
>>> r = niquests . get ( 'https://httpbingo.org/get' )
 >>> r . status_code
 200
Niquests also comes with a built-in status code lookup object for easy
reference:
>>> r . status_code == niquests . codes . ok
 True
If a request returns a 4xx client error or 5xx server error response, we can
raise an exception with
 Response.raise_for_status() :
>>> bad_r = niquests . get ( 'https://httpbingo.org/status/404' )
 >>> bad_r . status_code
 404
>>> try :
 ... bad_r . raise_for_status ()
 ... except niquests . exceptions . HTTPError :
 ... print ( 'The response was unsuccessful' )
 The response was unsuccessful
Because the status_code for r is 200 ,
 raise_for_status returns
the response itself:
>>> r . raise_for_status () is r
 True
All is well.
Response headers ¶
We can view the server’s response headers through a dictionary-like object:
>>> r . headers
 {
 'content-encoding': 'gzip',
 'transfer-encoding': 'chunked',
 'connection': 'close',
 'server': 'nginx/1.0.4',
 'x-runtime': '148ms',
 'etag': '"e1ca502697e5c9317743dc078f67693f"',
 'content-type': 'application/json; charset=utf-8'
 }
The dictionary is special: it is designed for HTTP fields. According to
 RFC 9110 , HTTP field names are case-insensitive.
So, we can access the headers using any capitalization we want:
>>> r . headers [ 'Content-Type' ]
 'application/json; charset=utf-8'
 >>> r . headers . get ( 'content-type' )
 'application/json; charset=utf-8'
The server can send some fields multiple times with different values. Niquests
combines fields whose grammar permits comma-separated values so they can be
represented in one mapping. Fields such as Set-Cookie , which cannot be
safely combined this way, are handled separately by the underlying response and
cookie APIs.
In most cases, you may want to access a specific structured field quickly.
The oheaders property exposes parsed headers as objects:
>>> r . oheaders . content_type . charset
 'utf-8'
 >>> r . oheaders . report_to . max_age
 '604800'
 >>> str ( r . oheaders . date )
 'Mon, 02 Oct 2023 05:34:48 GMT'
 >>> from kiss_headers import get_polymorphic , Date
 >>> h = get_polymorphic ( r . oheaders . date , Date )
 >>> repr ( h . get_datetime ())
 datetime.datetime(2023, 10, 2, 5, 39, 46, tzinfo=datetime.timezone.utc)
To explore possibilities, visit the kiss-headers documentation at https://jawah.github.io/kiss-headers/
Cookies ¶
If a response contains cookies, you can quickly access them:
>>> url = 'https://httpbingo.org/cookies/set?example_cookie_name=example_cookie_value'
 >>> r = niquests . get ( url , allow_redirects = False )
>>> r . cookies [ 'example_cookie_name' ]
 'example_cookie_value'
To send your own cookies to the server, you can use the cookies
parameter:
>>> url = 'https://httpbingo.org/cookies'
 >>> cookies = dict ( cookies_are = 'working' )
>>> r = niquests . get ( url , cookies = cookies )
 >>> r . json ()[ 'cookies' ]
 {'cookies_are': 'working'}
Cookies are returned in a RequestsCookieJar ,
which acts like a dictionary but also offers a more complete interface,
suitable for use over multiple domains or paths. Cookie jars can
also be passed in to requests:
>>> jar = niquests . cookies . RequestsCookieJar ()
 >>> jar . set ( 'tasty_cookie' , 'yum' , domain = 'httpbingo.org' , path = '/cookies' )
 >>> jar . set ( 'gross_cookie' , 'blech' , domain = 'httpbingo.org' , path = '/elsewhere' )
 >>> url = 'https://httpbingo.org/cookies'
 >>> r = niquests . get ( url , cookies = jar )
 >>> r . json ()[ 'cookies' ]
 {'tasty_cookie': 'yum'}
The same response and request cookie APIs are available asynchronously:
r = await niquests . aget ( url , cookies = cookies )
 print ( r . cookies )
Note
Response.cookies ,
 Session.cookies and
 AsyncSession.cookies are always typed as
 RequestsCookieJar . This means you can use them directly as a mapping
(e.g. session.cookies.set(...) or response.cookies['name'] ) without first asserting or
casting the type, which static type checkers like mypy used to require.
This is not a runtime-breaking change. Any
 CookieJar (or plain mapping) you pass in is still
accepted: a plain CookieJar is silently coerced to a
 RequestsCookieJar , while a custom subclass (such as
 MozillaCookieJar and
other file-backed jars) is left untouched at the request level so it keeps its behavior.
The only trade-off is that assigning a non- RequestsCookieJar jar directly to the attribute,
for instance:
session . cookies = MozillaCookieJar ( "cookies.txt" ) # type: ignore[assignment]
will now be flagged by type checkers. The assignment keeps working at runtime; add a
 # type: ignore[assignment] (or a cast ) if you rely on that pattern.
By default, sessions merge cookies received through Set-Cookie into their
cookie jar. Set allow_incoming_cookies=False to prevent that merge. Response
cookies remain available, and cookies you set explicitly are still sent:
🔂 Sync
 with niquests . Session ( allow_incoming_cookies = False ) as session :
 session . cookies . set ( 'outgoing' , 'yes' )
 r = session . get ( 'https://httpbingo.org/cookies/set?incoming=no' )
 assert 'incoming' not in session . cookies
🔀 Async
 async with niquests . AsyncSession ( allow_incoming_cookies = False ) as session :
 session . cookies . set ( 'outgoing' , 'yes' )
 r = await session . get ( 'https://httpbingo.org/cookies/set?incoming=no' )
 assert 'incoming' not in session . cookies
Redirection and history ¶
By default, Niquests follows redirects for all methods except HEAD.
We can use the history property of the response object to track redirects.
The Response.history list contains the
 Response objects that were created in order to
complete the request. The list is sorted from the oldest to the most recent
response.
For example, GitHub redirects all HTTP requests to HTTPS:
>>> r = niquests . get ( 'http://github.com/' )
 >>> r . url
 'https://github.com/'
 >>> r . status_code
 200
 >>> r . history
 []
If you’re using GET, OPTIONS, POST, PUT, PATCH, DELETE, or QUERY, you can disable
redirection handling with the allow_redirects parameter:
>>> r = niquests . get ( 'http://github.com/' , allow_redirects = False )
 >>> r . status_code
 301
 >>> r . history
 []
If you’re using HEAD, you can enable redirection as well:
>>> r = niquests . head ( 'http://github.com/' , allow_redirects = True )
 >>> r . url
 'https://github.com/'
 >>> r . history
 []
The redirect controls and history property are identical in async code:
r = await niquests . aget ( 'http://github.com/' , allow_redirects = False )
 assert r . status_code == 301
 assert r . history == []
r = await niquests . ahead ( 'http://github.com/' , allow_redirects = True )
 assert r . url == 'https://github.com/'
 assert len ( r . history ) == 1
Timeouts ¶
You can limit how long Niquests waits during network operations with the
 timeout parameter. Nearly all production requests should specify a timeout:
🔂 Sync
 try :
 niquests . get ( 'https://github.com/' , timeout = 0.001 )
 except niquests . exceptions . Timeout :
 print ( 'The request timed out' )
🔀 Async
 try :
 await niquests . aget ( 'https://github.com/' , timeout = 0.001 )
 except niquests . exceptions . Timeout :
 print ( 'The request timed out' )
Note
A scalar timeout applies to socket connection and read operations; it is
not a wall-clock limit on the entire response download. A read timeout is
raised when no response bytes arrive on the socket within that interval.
You can also pass a (connect, read) tuple. Top-level GET, HEAD, and
OPTIONS calls default to 30 seconds; write-oriented methods, including
QUERY, default to 120 seconds. A session’s timeout= value supplies its
default when individual session requests omit one.
Warning
Connection timeout behavior can be surprising when a host resolves to
multiple addresses. Connection attempts may apply the timeout to each
address in turn, so the elapsed wall-clock time can exceed the configured
value. For example, two unreachable addresses can take roughly twice the
connection timeout.
Tip
Set happy_eyeballs=True when constructing your Session to try all endpoints simultaneously.
This can reduce delays caused by unreachable addresses.
Warning
Python’s synchronous system resolver cannot always enforce this timeout if
system DNS is unresponsive. This limitation does not apply to async mode.
To avoid it, configure a custom resolver with resolver= ; see
 DNS Resolution below.
Errors and exceptions ¶
In the event of a network problem, such as a DNS failure or refused connection,
Niquests will raise a ConnectionError exception.
Response.raise_for_status() will
raise an HTTPError if the HTTP request
returned an unsuccessful status code.
If a request times out, a Timeout exception is
raised.
If a request exceeds the configured maximum number of redirects, a
 TooManyRedirects exception is raised.
All exceptions that Niquests explicitly raises inherit from
 niquests.exceptions.RequestException .
HTTP/3 over QUIC ¶
Niquests relies on urllib3.future and the semi-optional qh3 package for HTTP/3.
If qh3 is not installed, HTTP/3 and QUIC are unavailable, but HTTP/1.1 and
HTTP/2 continue to work. Installing qh3 may require a compilation toolchain.
Run python -m niquests.help to check whether the installed dependencies
support HTTP/3. You can inspect the protocol negotiated for a response:
🔂 Sync
 r = niquests . get ( 'https://1.1.1.1' )
 print ( r . http_version )
🔀 Async
 r = await niquests . aget ( 'https://1.1.1.1' )
 print ( r . http_version )
The underlying library understands the Alt-Svc header and looks for an
 h3 alternative service. Once a valid service is discovered, Niquests can
open a QUIC connection and caches that information in memory. Negotiation
depends on the peer, DNS and Alt-Svc information, cached state, network
conditions, and installed dependencies. Repeated calls do not guarantee a
particular HTTP/2-to-HTTP/3 sequence.
Note
With urllib3.future 2.4 or later, Niquests can negotiate HTTP/3 without
a preceding TCP connection when the peer advertises HTTP/3 in an HTTPS DNS
record.
Lazy responses and manual scheduling ¶
HTTP/2 and HTTP/3 multiplexing is automatic in Niquests and does not require
this option. The historically named multiplexed=True option instead enables
manual response scheduling.
In this mode, each request is submitted immediately, but its request method
returns a lazy, promise-backed response before waiting for the exchange to
complete. This lets you submit several requests before resolving any of their
responses.
When the peer supports HTTP/2 or HTTP/3, the outstanding exchanges can progress
concurrently as independent streams on the same connection. Leaving one
response unresolved does not prevent later requests from using that connection.
To benefit from this mode, submit multiple requests before accessing response
data. Resolve the resulting promises explicitly with
 Session.gather() or
through the other resolution mechanisms described below.
Note
The parameter name is historical. multiplexed=True does not enable
HTTP/2 or HTTP/3, and it does not change protocol negotiation. It enables
lazy responses and gives the caller control over response resolution.
Submit requests ¶
Request methods return public Response objects whose
 lazy property is initially True . Internally, each lazy response is
backed by a response promise.
🔂 Sync
 from niquests import Session
 with Session ( multiplexed = True ) as s :
 responses = [
 s . get ( "https://httpbingo.org/delay/3" ),
 s . get ( "https://httpbingo.org/delay/1" ),
 ]
 assert all ( response . lazy for response in responses )
s . gather () # Resolve pending responses before closing the session.
🔀 Async
 from niquests import AsyncSession
 async with AsyncSession ( multiplexed = True ) as s :
 responses = [
 await s . get ( "https://httpbingo.org/delay/3" ),
 await s . get ( "https://httpbingo.org/delay/1" ),
 ]
 assert all ( response . lazy for response in responses )
await s . gather () # Resolve pending responses before closing the session.
The final gather calls above are included for deterministic cleanup. The
following sections show how to choose which responses to resolve.
Resolve all responses ¶
Calling gather without response arguments resolves every response pending
on the session:
🔂 Sync
 s . gather ()
🔀 Async
 await s . gather ()
After resolution, response.lazy is False and response attributes, body
methods, and extension APIs are available normally.
Resolve selected responses ¶
Pass one or more lazy responses to gather to resolve only those promises:
🔂 Sync
 from niquests import Session
with Session ( multiplexed = True ) as s :
 responses = [
 s . get ( "https://httpbingo.org/delay/3" ),
 s . get ( "https://httpbingo.org/delay/1" ),
 ]
 s . gather ( responses [ 0 ])
 print ( responses [ 0 ] . status_code )
 assert responses [ 1 ] . lazy is True
s . gather ( responses [ 1 ])
🔀 Async
 from niquests import AsyncSession
async with AsyncSession ( multiplexed = True ) as s :
 responses = [
 await s . get ( "https://httpbingo.org/delay/3" ),
 await s . get ( "https://httpbingo.org/delay/1" ),
 ]
 await s . gather ( responses [ 0 ])
 print ( responses [ 0 ] . status_code )
 assert responses [ 1 ] . lazy is True
await s . gather ( responses [ 1 ])
This allows application code to choose the order in which promise-backed
responses are resolved.
Implicit resolution in synchronous code ¶
In synchronous code, directly accessing response data implicitly resolves that
response:
with Session ( multiplexed = True ) as s :
 response = s . get ( "https://httpbingo.org/delay/1" )
 print ( response . status_code ) # Resolves this response first.
This implicit behavior is intentionally unavailable for non-awaitable
attributes on a lazy AsyncResponse , because blocking there
would stall the event loop. Resolve it explicitly with await s.gather(...) .
Scheduling limits with max_fetch ¶
Both session types expose
 gather(*responses, max_fetch=None) .
 max_fetch limits how many available promises each mounted adapter resolves
during that call.
Here are some possible invocations:
🔂 Sync
 s . gather () # Resolve all pending responses.
 s . gather ( resp ) # Resolve only resp.
 s . gather ( max_fetch = 2 ) # Resolve up to two available responses per adapter.
 s . gather ( resp_a , resp_b , resp_c ) # Resolve these three responses.
 s . gather ( resp_a , resp_b , resp_c , max_fetch = 1 ) # Resolve one available response per adapter.
🔀 Async
 await s . gather () # Resolve all pending responses.
 await s . gather ( resp ) # Resolve only resp.
 await s . gather ( max_fetch = 2 ) # Resolve up to two available responses per adapter.
 await s . gather ( resp_a , resp_b , resp_c ) # Resolve these three responses.
 await s . gather ( resp_a , resp_b , resp_c , max_fetch = 1 ) # Resolve one available response per adapter.
Async session ¶
Niquests provides AsyncSession for awaitable HTTP requests.
Its request methods mirror Session and return coroutines.
Here is a basic example:
import asyncio
 from niquests import AsyncSession , Response
async def main () -> None :
 async with AsyncSession () as s :
 tasks = [ s . get ( "https://httpbingo.org/delay/1" ) for _ in range ( 10 )]
 responses = await asyncio . gather ( * tasks )
 print ( responses )
if __name__ == "__main__" :
 asyncio . run ( main ())
Warning
Niquests currently supports only asyncio as its async backend.
Note
Top-level async shortcuts are available with an a prefix, including
 aget() , apost() ,
 aput() , apatch() ,
 adelete() , aoptions() ,
 ahead() , aquery() , and
 arequest() . Each call uses
a temporary AsyncSession ; use your own session to reuse
connections.
Async lazy responses and manual scheduling ¶
AsyncSession(multiplexed=True) uses the same manual response scheduling
described above. It does not enable HTTP/2 or HTTP/3 multiplexing; protocol
negotiation remains automatic.
Each awaited request method submits its request and returns a lazy,
promise-backed response without waiting for that exchange to finish. Submit
several requests before resolving them so HTTP/2 or HTTP/3 streams can progress
concurrently on the underlying connection. Resolve the promises explicitly with
 await session.gather() .
Look at this basic sample:
import asyncio
 from niquests import AsyncSession
async def main () -> None :
 async with AsyncSession ( multiplexed = True ) as s :
 responses = [
 await s . get ( "https://httpbingo.org/delay/1" ) for _ in range ( 10 )
 ]
 assert all ( response . lazy for response in responses )
await s . gather ()
 assert all ( response . lazy is False for response in responses )
 print ( responses )
if __name__ == "__main__" :
 asyncio . run ( main ())
Unlike synchronous lazy responses, an asynchronous lazy response cannot resolve
itself while a non-awaitable attribute is being accessed, because doing so would
block the event loop. Gather it explicitly before that access.
Warning
Combining AsyncSession with multiplexed=True
and stream=True produces a lazy AsyncResponse . Call
 await session.gather() before directly accessing its non-awaitable
attributes or methods.
AsyncResponse for streams ¶
Delaying the content consumption in an async context can be easily achieved using:
import niquests
 import asyncio
async def main () -> None :
async with niquests . AsyncSession () as s :
 r = await s . get ( "https://httpbingo.org/get" , stream = True )
async for chunk in await r . iter_content ( 16 ):
 print ( chunk )
if __name__ == "__main__" :
asyncio . run ( main ())
Or use iter_lines . It is an async generator, so iterate over it directly
without await :
import niquests
 import asyncio
async def main () -> None :
async with niquests . AsyncSession () as s :
 r = await s . get ( "https://httpbingo.org/get" , stream = True )
async for line in r . iter_lines ():
 print ( line )
if __name__ == "__main__" :
 asyncio . run ( main ())
Or simply by doing:
import niquests
 import asyncio
async def main () -> None :
async with niquests . AsyncSession () as s :
 r = await s . get ( "https://httpbingo.org/get" , stream = True )
 payload = await r . json ()
if __name__ == "__main__" :
asyncio . run ( main ())
When you specify stream=True with AsyncSession , the
returned object is an AsyncResponse . Its
 iter_content and
 iter_raw methods are awaitable and return async iterators, so use
 async for chunk in await response.iter_content() . In contrast,
 iter_lines is an async generator and is used as
 async for line in response.iter_lines() without await . The
 content , json ,
 text , and close
interfaces are also awaitable.
When enabling multiplexing in an async context, call await s.gather() before
direct access to non-awaitable response interfaces.
Here is a basic example of how you would do it:
import niquests
 import asyncio
async def main () -> None :
responses = []
async with niquests . AsyncSession ( multiplexed = True ) as s :
 responses . append (
 await s . get ( "https://httpbingo.org/get" , stream = True )
 )
 responses . append (
 await s . get ( "https://httpbingo.org/get" , stream = True )
 )
print ( responses )
await s . gather ()
print ( responses )
for response in responses :
 async for chunk in await response . iter_content ( 16 ):
 print ( chunk )
if __name__ == "__main__" :
asyncio . run ( main ())
Warning
Accessing a non-awaitable attribute or method of a lazy
 AsyncResponse without first calling await s.gather()
raises an error.
Scale your Session / pool ¶
By default, Niquests retains up to 10 origin pools and configures each pool with
a capacity of 10 connections. You can increase or decrease these values.
Set the following parameters in a session constructor:
Session(pool_connections=10, pool_maxsize=10)
pool_connections is the number of origin connection pools retained in the cache.
pool_maxsize is the configured connection capacity of each origin pool.
Tip
HTTP/2 and HTTP/3 can carry many concurrent streams over one
connection, subject to the peer’s advertised stream limit.
Note
These settings are most useful for multithreaded or async applications.
Pool connections ¶
After requests to three distinct origins, pool_connections=2 retains the two
most recently used origin pools, for host-b.tld and host-c.tld . The idle
pool for host-a.tld is evicted from the cache.
🔂 Sync
 import niquests
with niquests . Session ( pool_connections = 2 ) as s :
 s . get ( "https://host-a.tld/some" )
 s . get ( "https://host-b.tld/some" )
 s . get ( "https://host-c.tld/some" )
🔀 Async
 import niquests
async with niquests . AsyncSession ( pool_connections = 2 ) as s :
 await s . get ( "https://host-a.tld/some" )
 await s . get ( "https://host-b.tld/some" )
 await s . get ( "https://host-c.tld/some" )
Attention
For backward compatibility, this cache size applies per mounted adapter.
The default HTTP and HTTPS adapters each retain up to two origin pools when
 pool_connections=2 , so pools for up to four origins may be retained
across both schemes.
Pool maxsize ¶
Setting pool_maxsize=2 configures a capacity of two connections for the
 host-a.tld origin pool. This setting matters primarily in concurrent async
or threaded environments.
DNS resolution ¶
Niquests has built-in support for DNS over HTTPS, DNS over TLS, DNS over UDP,
and DNS over Q

## 评论（2/2）

> **syrusakbary** · 2026-07-31T15:20:23.000Z　
> Wait to see what Wasmer has in store... :P

---

> **mesahm** · 2026-07-31T16:48:43.000Z　
> it should work with Wasmer too, I presume, but I don't see anywhere compat with WASI p2/p3 sockets. I'll look into it asap.regards,

## 关联链接

- http://github.com/
- https://1.1.1.1
- https://api.github.com/events
- https://api.github.com/some/endpoint
- https://github.com/
- https://github.com/...
- https://host-a.tld/some
- https://host-b.tld/some
- https://host-c.tld/some
- https://httpbingo.org/anything
- https://httpbingo.org/cookies
- https://httpbingo.org/cookies/set?example_cookie_name=example_cookie_value
- https://httpbingo.org/cookies/set?incoming=no
- https://httpbingo.org/delay/1
- https://httpbingo.org/delay/3
- https://httpbingo.org/delete
- https://httpbingo.org/get
- https://httpbingo.org/get?key1=value1&key2=value2
- https://httpbingo.org/get?key1=value1&key2=value2&key2=value3
- https://httpbingo.org/patch
- https://httpbingo.org/post
- https://httpbingo.org/put
- https://httpbingo.org/status/404
- https://jawah.github.io/kiss-headers/

## 导航

- 项目页：[[10-项目/Show-HN-We-made-a-full-featured-Python-HTTP-clie_b6046d85]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
