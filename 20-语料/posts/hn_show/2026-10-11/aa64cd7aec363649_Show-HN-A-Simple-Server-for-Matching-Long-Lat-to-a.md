---
type: "corpus"
item_id: "aa64cd7aec363649"
title: "Show HN: A Simple Server for Matching Long/Lat to a Timezone"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50035690"
project_url: "https://github.com/LittleGreenViper/LGV_TZ_Lookup"
author: "ChrisMarshallNY"
published_at: "2026-10-10T18:27:00Z"
captured_at: "2026-10-11T09:54:15+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-11"
pub_day: "2026-10-10"
tags:
  - 语料
  - hn_show
  - author_ChrisMarshallNY
  - story_50035690
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: A Simple Server for Matching Long/Lat to a Timezone

> [!info] 一句话导读
> LittleGreenViper/LGV_TZ_Lookup

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50035690>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：ChrisMarshallNY　|　发布：2026-10-10T18:27:00Z
> 项目链接：<https://github.com/LittleGreenViper/LGV_TZ_Lookup>
> 采集：2026-10-11T09:54:15+08:00　|　id：`aa64cd7aec363649`

## 正文

# LittleGreenViper/LGV_TZ_Lookup

Server for Matching Long/Lat to Timezone

- Stars: 47
- Forks: 2
- Watchers: 47
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2023-06-13T14:20:06Z

## Languages

- PHP

## Top Contributors

- ChrisMarshallNY (61 contributions)

---

## README

# LGV_TZ_Lookup
A Server for Matching Long/Lat to Timezone

## Overview
This project is a fairly simple PHP project, designed to accept the GeoJSON output of the Timezone Boundary Builder Project, and provide a simple API, for matching longitude/latitude locations with timezones.

Send in a long/lat, and get back a string, with the standard TZ time zone designator of the timezone that covers that point.

This is the GitHub repo for this project

## What Problem Does This Solve?
Unfortunately, time zones are not a simple "I'm at this longitude, so it must be this time." They are political constructs.

Here's why we can't just do a simple longitude match:

Time Zones Of the World
_Image Source: Wikimedia Commons_

We address this by using the rendered result of this great project, which is an effort to build a "living document" map of all the world timezones, as a shapefile (a file that can project polygons over a digital map), and locating a geographic point, within those shapes.

## How This Works
We provide a very basic PHP server that builds a simple database from the data in the massive shapefile (The GeoJSON variant that results from the timezone boundary builder. It can be found in any of the project releases). The database is deliberately "dumb," with a view towards making the project as flexible as possible, and lookups fast and easy.

Each timezone is described in a GeoJSON polygon (or multipolygon).

> NOTE: We are making _huge_ assumptions about the file. We assume that the polygons are very basic, "closed" polygons, and that multipolygons are simply aggregations of simple polygons (as opposed to making "holes," and whatnot).

We build a database of polygons (breaking up multipolygons), with what we term a "domain rect." This is a rectangle that encloses the entire polygon, regardless of the shape of the polygon.

The "domain rect" is used for a fast "triage" lookup. Its vertices are indexed in the database, so comparisons are zippy. We can quickly find the timezones that may contain our location, and ignore the rest.

In some cases, the domain rect "triage" may return only one result, so we got it in one. In other cases, we can then do a simple "Winding Number" lookup of the location, using the un-indexed polygon data for that timezone, and figure out which polygon actually has it. We return the first one.

From a usage standpoint, you simply send in a longitude/latitude pair, as a simple HTTP GET, and you will receive a "raw" string response, with the TZ name of the timezone that applies to the location.

`http`_[_`s`_]_`://`_[_`/index.php`_]_`?ll=`,

`https://tz.example.com?ll=-73.123,44.456`

The long/lat is sent as a comma-separated pair of floating-point numbers that represent degrees of longitude and latitude.

## Dependencies
This is a server project, designed for your classic "LAMP" hosting, so you'll need to have a standard PHP/MySQL host.

This project uses the streaming JSON parser, in order to parse this file (a current release, at the time of this writing), which is a GeoJSON file, containing the calculated timezones, and is created by this project.

Otherwise, it is a very basic PHP project (tested against PHP 8.2, at the time of this writing).

The initial release is built for MySQL (tested against MySQL 5.7), but uses PHP PDO, and has an absurdly simple database schema, so it can be expanded to other databases fairly easily.

Other than a Composer link to the streaming JSON parser, there are no other dependencies.

### Batteries Not Included
Well...that's not _strictly_ true. You'll need to download the GeoJSON file from the Timezone Boundary Builder Project releases. It's a big file, and may be updated, as timezones change. You can use either of the files (with or without oceans), but the project tests against the oceans variant.

## Implementation

### Initial Installation
Once you have a server available, install the contents of the `src` subdirectory into a place of your choosing, accessible via HTTP. You should have a URI that points to the `index.php` file in the `src` directory.

### Database Setup
You will need to set up a MySQL database, with a user with basic full permissions.

### Config File
A requirement for the server is a configuration file. It should generally be placed outside the HTTP-accesible directory tree, and you will need to modify the line in the `index.php` file that looks like this:

`define("__CONFIG_FILE_", __DIR__.'/../../../../TZInfo/config.php');`

To point to the configuration file.

The contents of the configuration file will look like this:

```
<?php 
    $g_dbName = "<DATABASE NAME>";
    $g_dbUserName = "<DATABASE USERNAME>";
    $g_dbPassword = "<DATABASE USER PASSWORD>";
    $g_dbType = "<DATABASE TYPE>";
    $g_dbHost = "<DATABASE HOST>";
    $g_dbPort = "<DATABASE PORT>";
    $g_server_secret = "<SERVER SECRET>";
```

with each of the strings changed to match the configuration. Here's an example:

```
<?php 
    $g_dbName = "HostingHash_TZDB";
    $g_dbUserName = "tzUser";
    $g_dbPassword = "swordfish";
    $g_dbType = "mysql";
    $g_dbHost = "127.0.0.1";
    $g_dbPort = "3306";
    $g_server_secret = "Shh-Dont-Tell-Anyone";
```

That `$g_server_secret` is important, if you don't want "just anyone" accessing the server. If it is set to a string, then every call to the server (including the command line) will need to have a `secret= ` query argument added to the regular query, like so:

#### HTTP Request:
`https://tz.example.com/index.php?secret=Shh-Dont-Tell-Anyone&ll=-73.123,44.456`

#### Command Line:
`?> php`_&lt;PATH TO THE src DIRECTORY>_`/index.php secret=Shh-Dont-Tell-Anyone load`

### Composer
Once the directory is in place, you'll need to update composer, to bring in the dependency.

```(bash)
$> cd <YOUR src DIRECTORY>
$> composer update
```

That will set up a `vendor` subdirectory. Just ignore it, after that. The server knows where to get it.

>NOTE: The dependency is only required for the load and setup. It is not required for subsequent queries.

### The Data File
You'll need to fetch the GeoJSON data file from the Boundary Builder Project Releases Directory. Get the latest release, and look for files named `timezones.geojson.zip`, or `timezones-with-oceans.geojson.zip`.

They are pretty big files.

Unzip the file into the `src` directory.

>NOTE: We have the project initially set up for the `combined-with-oceans.json` file. If you want to use the `combined.json` file, instead, then you should edit the `index.php` file at the line that looks like this:

```(php)
    $stream = fopen("$path/combined-with-oceans.json", 'r');

```

so that it looks like this:

```(php)
    $stream = fopen("$path/combined.json", 'r');

```

>CAUTION: If you do this, some of the tests won't pass!

### The Initial Load and Database Setup
You don't need to "prime" the database. The server will take care of creating the table.

However, the initial load can only be done via command-line, so you'll need to SSH into the server, and run the load from there. You use the syntax indicated above:

```(bash)
$> php <YOUR src DIRECTORY>/index.php secret=<SERVER SECRET> load
```

This can take a while.

Upon success, the script emits a simple `1`. If there was a problem, it emits a `0`.

Once that's done. the server is ready to go. You can even delete the JSON file and the vendor directory, if you want, but they will need to be back, before you can load.

You won't need to run `load` very often, so it shouldn't be in a `cron` job, or anything.

All interactions from then on, are done via HTTP.

### Testing
We have a set of simple tests that can be run. They send in known coordinates, and ensure that the server returns the proper response.

You run the tests, like so:

`https://tz.example.com`_[_`/index.php`_]_`?`_[_`secret=``&`_]_`test`

You will get a simple HTML page, with each of the tests, listed. If the test passes, the title will be green. If it fails, the title will be red, and there will be a list of links to failures, at the top of the page.

Everything should be green (unless you swapped out the JSON file, in which case, you'll need to look for the failures, and validate the tests).

## License
This is an MIT-Licensed project.

## 关联链接

- https://tz.example.com/index.php?secret=Shh-Dont-Tell-Anyone&ll=-73.123,44.456`
- https://tz.example.com?ll=-73.123,44.456`
- https://tz.example.com`_[_`/index.php`_

## 导航

- 项目页：[[10-项目/github.com_700f1358]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
