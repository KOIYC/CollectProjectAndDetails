---
type: "corpus"
item_id: "2d111b885d7f790b"
title: "Show HN: Capo-S3 – a typed, async-first S3 client for Python"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50293303"
project_url: "https://pypi.org/project/capo-s3"
author: "karpetrosyan"
published_at: "2026-10-29T18:02:03Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_karpetrosyan
  - story_50293303
  - show_hn
metrics: {"points": 11, "comments": 2, "engagement_velocity": 11}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Capo-S3 – a typed, async-first S3 client for Python

> [!info] 一句话导读
> Skip to main content

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50293303>
> 指标：点赞=11 · 评论=2 · engagement_velocity=11
> 作者：karpetrosyan　|　发布：2026-10-29T18:02:03Z
> 项目链接：<https://pypi.org/project/capo-s3>
> 采集：2026-10-30T09:46:09+08:00　|　id：`2d111b885d7f790b`

## 正文

Skip to main content
 Switch to mobile version
Search PyPI
 search-focus#focusSearchField"
 data-search-focus-target="searchField">
Search
Blog
Docs
Log in
Register
Blog
Docs
Log in
Register
Deutsch
English
español
Esperanto
français
português (Brasil)
Ελληνικά
русский
українська
עברית
中文 (简体)
中文 (繁體)
日本語
한국어
Search PyPI
Search
capo-s3 0.30.0
Typed, async Python SDK for Amazon S3.
pip install capo-s3
Copy PIP instructions
project-tabs#tabKeydown"
 aria-label="Project description. Focus will be moved to the description.">
Description
project-tabs#tabKeydown"
 aria-label="Metadata. Focus will be moved to the metadata panel.">
Metadata
project-tabs#tabKeydown"
 aria-label="Files. Focus will be moved to the project files.">
Release files
project-tabs#tabKeydown"
 aria-label="Release security. Focus will be moved to the security panel.">
Security
project-tabs#tabKeydown"
 aria-label="Release history. Focus will be moved to the release history panel.">
Release history
capo-s3: typed, async Python SDK for Amazon S3
capo-s3 is a typed Python SDK for Amazon S3 and S3-compatible storage such as RustFS, MinIO and Cloudflare R2. AsyncS3Client works with asyncio and trio, and S3Client has the same methods for sync code. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.
Beyond the S3 API it has a transfer manager for multipart uploads and downloads of large files, presigned URLs and presigned POST forms, paginators and waiters.
It is part of capo , a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: https://capo-sdk.dev/services/s3/
Install capo-s3
pip install capo-s3
Upload and download an S3 object in Python
from capo_s3 import AsyncS3Client
async def main ():
 async with AsyncS3Client () as s3 :
 # Upload an object
 await s3 . put_object ( "my-bucket" , "hello.txt" , body = b "Hello, World!" )
# Download it
 async with s3 . get_object ( "my-bucket" , "hello.txt" ) as response :
 async for chunk in response [ "body" ]:
 print ( chunk )
from capo_s3 import S3Client
def main ():
 with S3Client () as s3 :
 # The sync client: the same methods, without async and await
 s3 . put_object ( "my-bucket" , "hello.txt" , body = b "Hello, World!" )
with s3 . get_object ( "my-bucket" , "hello.txt" ) as response :
 for chunk in response [ "body" ]:
 print ( chunk )
Use RustFS, MinIO, Cloudflare R2 or other S3-compatible storage
from capo_s3 import AsyncS3Client , Credentials
async def main ():
 async with AsyncS3Client (
 region = "us-east-1" ,
 endpoint = "http://localhost:9000" ,
 credentials = Credentials ( access_key = "" , secret_key = "" ),
 # RustFS wants the bucket in the path, not in the host name
 force_path_style = True ,
 ) as s3 :
 # The same client, talking to RustFS
 await s3 . create_bucket ( "my-bucket" )
 await s3 . put_object ( "my-bucket" , "hello.txt" , body = b "Hello, RustFS!" )
Put, copy and delete S3 objects
from capo_s3 import AsyncS3Client
async def main ():
 async with AsyncS3Client () as s3 :
 # Upload with a content type and your own metadata
 await s3 . put_object (
 "my-bucket" ,
 "report.json" ,
 body = b '{"total": 3}' ,
 content_type = "application/json" ,
 metadata = { "author" : "me" },
 )
# Size, type and metadata, without downloading the object
 head = await s3 . head_object ( "my-bucket" , "report.json" )
 print ( head . get ( "content_length" ), head . get ( "content_type" ), head . get ( "metadata" ))
# Copy an object, here into another bucket
 await s3 . copy_object ( bucket = "other-bucket" , key = "report.json" , copy_source = "my-bucket/report.json" )
# Delete one object
 await s3 . delete_object ( "my-bucket" , "report.json" )
# Delete many in one request
 await s3 . delete_objects ( "my-bucket" , { "objects" : [{ "key" : "a.txt" }, { "key" : "b.txt" }]})
Create, check and delete S3 buckets
from capo_s3 import AsyncS3Client
async def main ():
 async with AsyncS3Client () as s3 :
 # Create a bucket; outside us-east-1 it has to name its region
 await s3 . create_bucket (
 "my-bucket" ,
 create_bucket_configuration = { "location_constraint" : "eu-central-1" },
 )
# Check that a bucket exists and that you may use it
 await s3 . head_bucket ( "my-bucket" )
# Delete a bucket, which has to be empty
 await s3 . delete_bucket ( "my-bucket" )
Upload a large file to S3 with the transfer manager
from capo_s3 import AsyncS3Client , AsyncTransferManager
async def main ():
 async with AsyncS3Client () as s3 :
 manager = AsyncTransferManager (
 s3 ,
 # A file of 16 MiB or more goes up as a multipart upload, in parts of 8 MiB.
 # S3 needs every part but the last to be at least 5 MiB
 target_part_size_bytes = 8 * 1024 * 1024 ,
 multipart_upload_threshold_bytes = 16 * 1024 * 1024 ,
 # Download the parts the object was uploaded in; "range" downloads
 # byte ranges of target_part_size_bytes instead
 multipart_download_type = "part" ,
 )
# Upload a file
 await manager . upload ( "video.mp4" , "my-bucket" , "video.mp4" )
# Download it into another file
 await manager . download ( "my-bucket" , "video.mp4" , "copy.mp4" )
from capo_s3 import AsyncS3Client , AsyncTransferManager
async def main ():
 async with AsyncS3Client () as s3 :
 manager = AsyncTransferManager (
 s3 ,
 target_part_size_bytes = 8 * 1024 * 1024 ,
 multipart_upload_threshold_bytes = 16 * 1024 * 1024 ,
 multipart_download_type = "part" ,
 )
# upload takes the keywords of put_object
 await manager . upload (
 "video.mp4" ,
 "my-bucket" ,
 "video.mp4" ,
 content_type = "video/mp4" ,
 checksum_algorithm = "CRC32" ,
 )
# download takes the keywords of get_object
 await manager . download ( "my-bucket" , "video.mp4" , "copy.mp4" , version_id = "3HL4kqtJlcpXroDTDmJ" )
# Bigger parts, for this upload only
 await manager . upload (
 "video.mp4" ,
 "my-bucket" ,
 "video.mp4" ,
 transfer_config_overrides = { "target_part_size_bytes" : 64 * 1024 * 1024 },
 )
# Byte ranges, for this download only
 await manager . download (
 "my-bucket" ,
 "video.mp4" ,
 "copy.mp4" ,
 transfer_config_overrides = { "multipart_download_type" : "range" },
 )
from capo_s3 import AsyncS3Client , AsyncTransferManager
async def main ():
 async with AsyncS3Client () as s3 :
 manager = AsyncTransferManager (
 s3 ,
 target_part_size_bytes = 8 * 1024 * 1024 ,
 multipart_upload_threshold_bytes = 16 * 1024 * 1024 ,
 multipart_download_type = "part" ,
 )
# Upload with progress. Leaving the block before everything is sent,
 # or with an error, aborts the multipart upload
 async with manager . upload_iter ( "video.mp4" , "my-bucket" , "video.mp4" ) as upload :
 async for event in upload :
 print ( f " { event . transferred_bytes } of { event . total_bytes } bytes sent" )
# Download into memory, with progress: each event has its data
 # and the offset it belongs at
 data = bytearray ()
 async for event in manager . download_iter ( "my-bucket" , "video.mp4" ):
 data [ event . offset : event . offset + len ( event . data )] = event . data
 print ( f " { event . transferred_bytes } of { event . total_bytes } bytes received" )
from capo_s3 import S3Client , TransferManager
def main ():
 with S3Client () as s3 :
 # TransferManager does the same for the sync client
 manager = TransferManager (
 s3 ,
 target_part_size_bytes = 8 * 1024 * 1024 ,
 multipart_upload_threshold_bytes = 16 * 1024 * 1024 ,
 multipart_download_type = "part" ,
 )
manager . upload ( "video.mp4" , "my-bucket" , "video.mp4" )
 manager . download ( "my-bucket" , "video.mp4" , "copy.mp4" )
List objects in an S3 bucket
from capo_s3 import AsyncS3Client
async def main ():
 async with AsyncS3Client () as s3 :
 # Every bucket, however many pages that takes
 async for bucket in s3 . iter_list_buckets ():
 print ( bucket . get ( "name" ))
# Every object under a prefix, a page at a time
 async for page in s3 . iter_list_objects_v2 ( "my-bucket" , prefix = "photos/" ):
 for obj in page . get ( "contents" , []):
 print ( obj . get ( "key" ), obj . get ( "size" ))
# The "folders" right under a prefix
 async for page in s3 . iter_list_objects_v2 ( "my-bucket" , prefix = "photos/" , delimiter = "/" ):
 for folder in page . get ( "common_prefixes" , []):
 print ( folder . get ( "prefix" ))
# A single page, without the iterator
 page = await s3 . list_objects_v2 ( "my-bucket" , max_keys = 10 )
 print ( page . get ( "key_count" ), page . get ( "is_truncated" ))
Stream S3 objects and file uploads
from capo_s3 import AsyncS3Client , Body
async def main ():
 async with AsyncS3Client () as s3 :
 # A file from disk: its length is read from the file, and it is opened
 # again on every retry. Body.from_path does the same for S3Client
 await s3 . put_object ( "my-bucket" , "hello.txt" , body = Body . async_from_path ( "hello.txt" ))
# Your own chunks, with their total length. They can be sent only once,
 # so a request that fails after its body went out is not retried
 async def chunks ():
 yield b "Hello, "
 yield b "World!"
await s3 . put_object ( "my-bucket" , "hello.txt" , body = chunks (), content_length = 13 )
from capo_s3 import AsyncS3Client
async def main ():
 async with AsyncS3Client () as s3 :
 # Read the whole object into memory
 async with s3 . get_object ( "my-bucket" , "hello.txt" ) as response :
 data = b "" . join ([ chunk async for chunk in response [ "body" ]])
 print ( data )
# Only its first hundred bytes
 async with s3 . get_object ( "my-bucket" , "hello.txt" , range = "bytes=0-99" ) as response :
 data = b "" . join ([ chunk async for chunk in response [ "body" ]])
 print ( data )
Wait for an S3 bucket or object
from capo_s3 import AsyncS3Client
 from capo_s3.errors import WaiterTimeoutError
async def main ():
 async with AsyncS3Client () as s3 :
 # Create a bucket and wait until it is there
 await s3 . create_bucket ( "my-bucket" )
 await s3 . wait_until_bucket_exists ( "my-bucket" , max_wait_time = 60 )
# Delete an object and wait until it is gone
 await s3 . delete_object ( "my-bucket" , "hello.txt" )
 await s3 . wait_until_object_not_exists ( "my-bucket" , "hello.txt" , max_wait_time = 60 )
# After max_wait_time seconds the waiter gives up
 try :
 await s3 . wait_until_object_exists ( "my-bucket" , "hello.txt" , max_wait_time = 10 )
 except WaiterTimeoutError :
 print ( "still not there" )
Generate a presigned S3 URL in Python
from capo_s3 import AsyncS3Client
async def main ():
 async with AsyncS3Client () as s3 :
 # Whoever has this URL can download the object, without credentials,
 # for the next ten minutes
 url = await s3 . presigned_get_object ( "my-bucket" , "hello.txt" , expire_in = 600 )
 print ( url )
# The same, saved by the browser under another name
 url = await s3 . presigned_get_object (
 "my-bucket" ,
 "hello.txt" ,
 expire_in = 600 ,
 response_content_disposition = 'attachment; filename="greeting.txt"' ,
 )
 print ( url )
# A URL to upload to: PUT the bytes to it
 url = await s3 . presigned_put_object ( "my-bucket" , "upload.txt" , expire_in = 600 )
 print ( url )
Handle S3 errors
from capo_s3 import AsyncS3Client
 from capo_s3.errors import NoSuchKey , NotFound , ServiceError
async def main ():
 async with AsyncS3Client () as s3 :
 # An error the API describes has its own class
 try :
 async with s3 . get_object ( "my-bucket" , "missing.txt" ) as response :
 print ( response . get ( "content_length" ))
 except NoSuchKey as e :
 print ( e . code , e . message )
# Is the object there? head_object raises NotFound when it is not
 try :
 await s3 . head_object ( "my-bucket" , "missing.txt" )
 except NotFound :
 print ( "no such object" )
# Any error S3 returns; one without a class of its own is an UnknownServiceError
 try :
 await s3 . delete_bucket ( "my-bucket" )
 except ServiceError as e :
 print ( e . code , e . message )
Configure S3 retries
from capo_s3 import AsyncS3Client
async def main ():
 async with AsyncS3Client ( retry_max_attempts = 5 ) as s3 :
 # Throttling, server errors and network failures are retried. Every call
 # of this client gets five attempts instead of the default three
 await s3 . head_object ( "my-bucket" , "hello.txt" )
from capo_s3 import AsyncS3Client
async def main ():
 async with AsyncS3Client () as s3 :
 # Five attempts for this call
 await s3 . head_object ( "my-bucket" , "hello.txt" , config_overrides = { "retry_max_attempts" : 5 })
# No retries for this call
 await s3 . head_object ( "my-bucket" , "hello.txt" , config_overrides = { "retry_max_attempts" : 1 })
Project links
Data verified by PyPI on Oct 28, 2026
Data provided by the project maintainers, verified at the time the release was uploaded to PyPI.
Changelog
Repository
Documentation
Homepage
Key dates
PyPI data
 Data sourced directly from PyPI's database.
Released:
 Oct 28, 2026
Latest release
1 maintainer
PyPI data
 Data sourced directly from PyPI's database.
karosis88
GitHub Statistics
Data verified by PyPI on Oct 28, 2026
 The GitHub source repository was provided by the project maintainers and verified by PyPI at the time of upload. Stars, forks, and open issues/PRs are derived from that repository and have not been independently verified.
Repository
Stars:
Forks:
Open issues:
Open PRs:
License
MIT License
Requires
Python >=3.10
Provides Extra
crc32c
 xxhash
 sso
Classifiers
Development Status
4 - Beta
Intended Audience
Developers
License
OSI Approved :: MIT License
Operating System
OS Independent
Programming Language
Python :: 3
Python :: 3.10
Python :: 3.11
Python :: 3.12
Python :: 3.13
Python :: 3.14
Topic
Software Development :: Code Generators
Typing
Typed
Metadata
Project links
Data verified by PyPI on Oct 28, 2026
Data provided by the project maintainers, verified at the time the release was uploaded to PyPI.
Changelog
Repository
Documentation
Homepage
Key dates
PyPI data
 Data sourced directly from PyPI's database.
Released:
 Oct 28, 2026
Latest release
1 maintainer
PyPI data
 Data sourced directly from PyPI's database.
karosis88
GitHub Statistics
Data verified by PyPI on Oct 28, 2026
 The GitHub source repository was provided by the project maintainers and verified by PyPI at the time of upload. Stars, forks, and open issues/PRs are derived from that repository and have not been independently verified.
Repository
Stars:
Forks:
Open issues:
Open PRs:
License
MIT License
Requires
Python >=3.10
Provides Extra
crc32c
 xxhash
 sso
Classifiers
Development Status
4 - Beta
Intended Audience
Developers
License
OSI Approved :: MIT License
Operating System
OS Independent
Programming Language
Python :: 3
Python :: 3.10
Python :: 3.11
Python :: 3.12
Python :: 3.13
Python :: 3.14
Topic
Software Development :: Code Generators
Typing
Typed
Release files for capo-s3 0.30.0
For a detailed explanation of source distributions (sdists) and built distributions (wheels), please see the package formats documentation .
Source distribution (sdist)
Source distribution for capo-s3 0.30.0
File
 Size
 Uploaded
 Provenance
capo_s3-0.30.0.tar.gz
657.1 kB
Oct 28, 2026
Without provenance
Details
Built distribution (wheel)
Table of built distributions (wheels) for capo-s3 0.30.0
File
Interpreter
ABI
Platform
Reset
capo_s3-0.30.0-py3-none-any.whl
1.2 MB
Oct 28, 2026
Without provenance
Python 3
none
any
Details
Total release size: 1.9 MB
Release files
 / capo_s3-0.30.0.tar.gz
Download URL
capo_s3-0.30.0.tar.gz
Size
 657.1 kB
Tags
Source
SHA-256 checksum
How to use checksums
8bfd4a2d6f93d8b051e3f71ff0d180a11415dde2ba61a498f5b71e4e5969fac0
BLAKE2b-256 checksum
How to use checksums
2b643cf6f6f6b6f4d0f647ff1c28ac639c2c10a9117c9a0be7f18b1a1c00b118
Upload date
Oct 28, 2026
Uploaded using Trusted Publishing?
What is trusted publishing?
Yes
Uploaded via
uv/0.13.6 {"installer":{"name":"uv","version":"0.13.6","subcommand":["publish"]},"python":null,"implementation":{"name":null,"version":null},"distro":{"name":"Ubuntu","version":"24.04","id":"noble","libc":null},"system":{"name":null,"release":null},"cpu":null,"openssl_version":null,"setuptools_version":null,"rustc_version":null,"ci":true}
Release files
 / capo_s3-0.30.0-py3-none-any.whl
Download URL
capo_s3-0.30.0-py3-none-any.whl
Size
 1.2 MB
Tags
Python 3
SHA-256 checksum
How to use checksums
b2f241904299ac2d78b9f516aa256897f268cde1b65b498adafd0244ceedc325
BLAKE2b-256 checksum
How to use checksums
cacf2382329f1e95110d480808d19fc07a5a38de67b35914655ffd0a9b5c4f68
Upload date
Oct 28, 2026
Uploaded using Trusted Publishing?
What is trusted publishing?
Yes
Uploaded via
uv/0.13.6 {"installer":{"name":"uv","version":"0.13.6","subcommand":["publish"]},"python":null,"implementation":{"name":null,"version":null},"distro":{"name":"Ubuntu","version":"24.04","id":"noble","libc":null},"system":{"name":null,"release":null},"cpu":null,"openssl_version":null,"setuptools_version":null,"rustc_version":null,"ci":true}
Security for capo-s3 0.30.0
Report project as malware
Provenance
Provenance describes where a file came from. On PyPI, provenance is shared via attestations , which provide a verifiable record of the build or publishing details. View details, limitations and caveats.
No provenance found
None of the files in this release were uploaded with provenance metadata.
A note on package security
PyPI is a repository for distributing packages, not a service for auditing them. While third-party security researchers and our staff do their best to detect and remove malicious packages, PyPI cannot guarantee the quality, security or suitability of any given package.
To learn more about protecting yourself from malicious actors, visit our package security documentation .
Release history
Release notifications |
 RSS feed
This release
0.30.0
 This release
Oct 28, 2026
2 release files
No provenance
0.29.0
Oct 26, 2026
2 release files
No provenance
0.28.0
Oct 24, 2026
2 release files
No provenance
0.27.0
Oct 19, 2026
2 release files
No provenance
0.26.0
Oct 17, 2026
2 release files
No provenance
0.25.0
Oct 17, 2026
2 release files
No provenance
0.24.0
Oct 12, 2026
2 release files
No provenance
0.23.0
Oct 10, 2026
2 release files
No provenance
0.22.0
Oct 9, 2026
2 release files
No provenance
0.21.0
Oct 6, 2026
2 release files
No provenance
0.20.0
Oct 4, 2026
2 release files
No provenance
0.19.0
Oct 2, 2026
2 release files
No provenance
0.17.0
Sep 24, 2026
2 release files
No provenance
0.16.0
Sep 18, 2026
2 release files
No provenance
0.15.0
Aug 26, 2026
2 release files
No provenance
0.14.0
Aug 22, 2026
2 release files
No provenance
0.13.0
Aug 20, 2026
2 release files
No provenance
0.12.0
Aug 19, 2026
2 release files
No provenance
0.11.0
Aug 18, 2026
2 release files
No provenance
0.10.0
Aug 18, 2026
2 release files
No provenance
0.9.0
Aug 15, 2026
2 release files
No provenance
0.8.0
Aug 14, 2026
2 release files
No provenance
0.7.0
Aug 2, 2026
2 release files
No provenance
0.6.0
Jul 26, 2026
2 release files
No provenance
0.1.0
Jul 26, 2026
2 release files
No provenance
PyPI
Developed and maintained by the Python Software Foundation and Python community, for the Python community.
Status: all systems operational
Donate today!
Help
PyPI documentation
Getting help
Installing packages
Uploading packages
Packaging user guide
About PyPI
PyPI blog
Infrastructure dashboard
Statistics
Logos & trademarks
Our sponsors
Contributing to PyPI
Bugs and feedback
Contribute on GitHub
Translate PyPI
Sponsor PyPI
Development credits
Using PyPI
Terms of Service
Report security issue
Code of conduct
Privacy Notice
Acceptable Use Policy
Switch to desktop version
Anthropic, PBC
 Visionary sponsor
Bloomberg
 Visionary sponsor
Hudson River Trading
 Visionary sponsor
Meta
 Visionary sponsor
NVIDIA
 Visionary sponsor
Microsoft
 Sustainability sponsor
Depot
 Continuous Integration
AWS
 Cloud computing and Security Sponsor
Datadog
 Monitoring
Fastly
 CDN
Google
 Download Analytics
Sentry
 Error logging
StatusPage
 Status page
"PyPI", "Python Package Index", and the blocks logos are registered trademarks of the Python Software Foundation .
© 2026 Python Software Foundation
Site map
Deployed from 1ac4057

## 评论（2/2）

> **karpetrosyan** · 2026-10-29T18:34:52.000Z　
> Author is here. Capo also has SDKs for all 400+ AWS services, in idiomatic python: https://capo-sdk.dev/

---

> **bompus** · 2026-10-29T18:58:38.000Z　
> Very awesome. It's nice to see alternatives and modern solutions.

## 关联链接

- http://localhost:9000
- https://capo-sdk.dev/services/s3/

## 导航

- 项目页：[[10-项目/pypi.org_0cc9e457]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
