---
type: "corpus"
item_id: "2aae0b4a53508d5d"
title: "零成本！用 Google 表单 + Apps Script 搭建全自动独立分发码/优惠码系统"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1252447"
project_url: "https://cmder.aitobox.com/"
author: "aitobox"
published_at: "2026-10-28T02:29:06"
captured_at: "2026-10-29T20:50:17+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-29"
pub_day: "2026-10-28"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 零成本！用 Google 表单 + Apps Script 搭建全自动独立分发码/优惠码系统

> [!info] 一句话导读
> 在 V2EX 发码，是一个比较常见的场景，目前来看手工发邮件有点儿烦；自动化的方案就是 woobox,tally 等表单服务，但是它们的免费版有很多限制；最致命的就是发码数目太少了；

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1252447>
> 指标：回复=0
> 作者：aitobox　|　发布：2026-10-28T02:29:06
> 项目链接：<https://cmder.aitobox.com/>
> 采集：2026-10-29T20:50:17+08:00　|　id：`2aae0b4a53508d5d`

## 正文

在 V2EX 发码，是一个比较常见的场景，目前来看手工发邮件有点儿烦；自动化的方案就是 woobox,tally 等表单服务，但是它们的免费版有很多限制；最致命的就是发码数目太少了；

本来想自己写个轻量服务的，但是跟 AI 一通聊，发现用 Google Forms 也可以非常简单的做这件事；于是整理了下面这篇文档；这是我跟着 AI 一步一步做下来，跑通了，然后整理完成的；

供有发码需求的开发者们参考：



对于独立开发者而言，产品上架或大版本更新时，去各大垂直社区（如 Reddit 、V2EX 、MacRumors 、专属垂直论坛）做 Giveaway （免费赠码 / 兑换码活动） 是冷启动最高效的手段之一。

但在分发“一人一码”的兑换码（如 App Store 兑换码、独立激活码）时，通常会遇到以下尴尬痛点：

1. 人工私信发码：回帖量一旦破百，纯手动查收、复制、私信不仅累瘫，还极易错发、漏发。
2. 商业表单 SaaS 成本高：像 Typeform 、Jotform 这类工具，免费版每月通常只给 10 条提交额度；若要开启“填表后自动邮件发码”或连接 Zapier/Make ，每月至少要掏几十美元订阅费。
3. 明文贴码被爬虫截胡：直接在帖子里贴一批码，几分钟内就会被机器爬虫扫光，真实用户根本领不到。

本文分享一套 100% 免费、完全云端 Serverless 运行、支持防刷/防并发/每日限量自动关停 的自动化发码方案：基于 Google Forms + Google Sheets + Apps Script 搭建。

一、 系统架构与运转逻辑

整个自动化发码流水线完全基于 Google 免费生态，零服务器成本：

```

[用户提交表单 (填写邮箱)] 
         │
         ▼
[Google Forms 触发 Webhook]
         │
         ▼
[Google Apps Script 云端脚本]
   ├── 1. 获取分布式并发锁 (LockService ，防止两名用户同时分到同一个码)
   ├── 2. 统计今日发码数 (与 DAILY_LIMIT 校验，防止超额)
   ├── 3. 校验邮箱唯一性 (防脚本重复提交刷码)
   ├── 4. 从 Codes 码池取出第一个空闲码
   ├── 5. 写入该用户的邮箱与领取时间戳 (原子回写)
   ├── 6. 调用 GmailApp 自动发送包含兑换教程的邮件
   └── 7. 若触发单日限额，自动将表单设为“停止收集”并提示“明日再来”
         │
         ▼
[次日凌晨定时触发器 (Cron Trigger)]
   └── 自动将表单重新开启 (SetAcceptingResponses = true)

```

二、 详细搭建步骤

第一步：创建 Google 表单（用户端入口）

1. 访问 Google Forms 创建新表单。
2. 基础设置：
  ⚬ 题目中添加至少一个收集邮箱的字段，例如 Your Email （或者直接在表单“设置”中开启系统自带的“收集电子邮件地址”）。
  ⚬ （可选）添加一个题目如 Your Forum Username （论坛用户名），用于增加门槛、防止黑产批量机刷。
3. 配置提交成功提示语：
  ⚬ 点击 设置（ Settings ）-> 演示文稿（ Presentation ）-> 确认消息（ Confirmation message ） 点击编辑。
  ⚬ 建议文案（说明网络延迟和垃圾邮件检查，降低客诉）：
  
```
    🎉 Thank you for participating!
    Your Lifetime Pro Promo Code is being processed and sent to your email address.
    
    Please keep in mind:
    • Email delivery might experience slight delays depending on your provider.
    • If you don't see it immediately, please check your Spam / Junk / Promotions folder.
    • Still can't find it? Please wait 10 minutes and check again.

```

4.生成关联电子表格：
  ⚬ 切换到 回复（ Responses ） 标签页，点击绿色的 关联到表格（ Link to Sheets ），创建一个新的 Google 表格。

第二步：配置 Google Sheet 数据表（码池 DB ）

打开刚刚自动生成的电子表格：

1. 默认的工作表是 Form Responses 1 （记录用户填写的答案）。
2. 在底部点击 + 新建一个工作表，重命名为 Codes （注意大小写，代码严格依赖该名称）。
3. 在 Codes 工作表的第一行设置表头：

  ⚬ A1：Code

  ⚬ B1：AssignedTo

  ⚬ C1：AssignedAt

4.把准备好的几百或一千个兑换码，依次粘贴到 A 列（从 A2 开始往下排），B 列和 C 列保持空白。

第三步：部署 Apps Script 核心后端代码

1. 在电子表格菜单栏，点击 扩展程序（ Extensions ）-> Apps Script 。
2. 清空编辑器中的原有代码，粘贴以下完整的脚本：
```

// ============================================================
// Configuration: Daily Quota
// Note: Google's free Gmail quota is 100 emails/day.
// ============================================================
const DAILY_LIMIT = 100;

function sendPromoCode(e) {
  // 1. 获取分布式锁，防止高并发下多个请求分配同一个码（最长等待 20 秒）
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
  } catch (err) {
    console.error("Lock timeout: " + err);
    return;
  }

  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const codeSheet = ss.getSheetByName("Codes");
    const data = codeSheet.getDataRange().getValues();
    const timeZone = Session.getScriptTimeZone();
    const todayStr = Utilities.formatDate(new Date(), timeZone, "yyyy-MM-dd");

    // 2. 统计今日已发码数量
    let todaySentCount = 0;
    for (let i = 1; i < data.length; i++) {
      const assignedAt = data[i][2]; // Column C: AssignedAt
      if (assignedAt instanceof Date) {
        const assignedDateStr = Utilities.formatDate(assignedAt, timeZone, "yyyy-MM-dd");
        if (assignedDateStr === todayStr) {
          todaySentCount++;
        }
      }
    }

    // 3. 超过今日配额，立即关停表单并截断
    if (todaySentCount >= DAILY_LIMIT) {
      closeFormForToday(ss);
      console.warn(`Daily quota reached (${DAILY_LIMIT}). Form closed for today.`);
      return;
    }

    // 4. 双重保底提取用户邮箱（中英文表头兼容 + 正则表达式兜底）
    const namedValues = e.namedValues || {};
    let recipientEmail = "";

    // 逻辑 A：关键词匹配表头
    for (let key in namedValues) {
      const lowerKey = key.toLowerCase();
      if (lowerKey.includes("email") || lowerKey.includes("mail") || key.includes("邮件") || key.includes("邮箱")) {
        if (namedValues[key] && namedValues[key][0]) {
          recipientEmail = namedValues[key][0].trim();
          break;
        }
      }
    }

    // 逻辑 B：正则表达式全局扫描匹配
    if (!recipientEmail) {
      const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      for (let key in namedValues) {
        const val = (namedValues[key][0] || "").trim();
        if (emailPattern.test(val)) {
          recipientEmail = val;
          break;
        }
      }
    }

    if (!recipientEmail) {
      console.error("No valid email address found in submission. Keys: " + JSON.stringify(Object.keys(namedValues)));
      return;
    }

    // 5. 校验该邮箱是否已经领过码（防刷防重复领）
    for (let i = 1; i < data.length; i++) {
      if (data[i][1] && data[i][1].toString().toLowerCase() === recipientEmail.toLowerCase()) {
        console.warn("Email already claimed a code. Skipping: " + recipientEmail);
        return;
      }
    }

    // 6. 从码池中查找第一个未被占用的码
    let promoCode = null;
    let targetRow = -1;

    for (let i = 1; i < data.length; i++) {
      const code = data[i][0];
      const assignedTo = data[i][1];

      if (code && (!assignedTo || assignedTo.toString().trim() === "")) {
        promoCode = code;
        targetRow = i + 1; // Google Sheets 行号从 1 开始
        break;
      }
    }

    // 7. 处理总码池耗尽的情况
    if (!promoCode) {
      closeFormPermanently(ss);
      console.warn("All promotional codes have been claimed. Form closed permanently.");
      return;
    }

    // 8. 标记该码为已使用（回写邮箱与时间戳）
    codeSheet.getRange(targetRow, 2).setValue(recipientEmail);
    codeSheet.getRange(targetRow, 3).setValue(new Date());
    SpreadsheetApp.flush(); // 强制即时落盘

    // 9. 调用 Gmail 发送包含激活码及指引的邮件
    const subject = "Your Lifetime Pro Code for ATBCmder (Mac App Store)";
    const body = `Hi there,

Thank you for participating in the community giveaway!

Here is your Mac App Store Lifetime Pro Promo Code:
--------------------------------------------------
Code: ${promoCode}
--------------------------------------------------

How to redeem on macOS:
1. Open the "App Store" app on your Mac.
2. Click your account name/profile icon in the bottom-left corner.
3. Click "Redeem Gift Card" in the top-right corner.
4. Enter the code above and confirm.
5. Launch ATBCmder, and your Lifetime Pro license will be unlocked!

Note: Apple promotional codes strictly expire in 28 days. Please redeem it as soon as possible.

Official Website & Manual: https://cmder.aitobox.com
If you encounter any issues or have feedback, feel free to reply directly to this email.

Best regards,
AIToBox Team`;

    GmailApp.sendEmail(recipientEmail, subject, body);
    todaySentCount++;
    console.log(`Code issued to ${recipientEmail}. Today's progress: ${todaySentCount}/${DAILY_LIMIT}`);

    // 10. 如果当前发放恰好达到当日配额，立刻关闭表单
    if (todaySentCount >= DAILY_LIMIT) {
      closeFormForToday(ss);
      console.log(`Daily limit reached (${DAILY_LIMIT}). Form is now closed.`);
    }

  } catch (error) {
    console.error("Execution error: " + error.toString());
  } finally {
    lock.releaseLock();
  }
}

// 辅助函数：当日用尽，关闭表单
function closeFormForToday(ss) {
  const formUrl = ss.getFormUrl();
  if (formUrl) {
    const form = FormApp.openByUrl(formUrl);
    form.setAcceptingResponses(false);
    form.setCustomClosedFormMessage(
      "Today's quota (100 Lifetime Pro codes) has been fully claimed!\n\n" +
      "The form will automatically reopen tomorrow at 00:00 UTC. Thank you for your patience!"
    );
  }
}

// 辅助函数：活动结束，永久关闭表单
function closeFormPermanently(ss) {
  const formUrl = ss.getFormUrl();
  if (formUrl) {
    const form = FormApp.openByUrl(formUrl);
    form.setAcceptingResponses(false);
    form.setCustomClosedFormMessage(
      "All promotional codes for this giveaway have been claimed. Thank you for your support!\n\n" +
      "You can still download ATBCmder with a full 90-day free trial on the Mac App Store."
    );
  }
}

// 定时任务函数：每日凌晨自动重开表单
function resetAndReopenFormDaily() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const formUrl = ss.getFormUrl();
  if (formUrl) {
    const form = FormApp.openByUrl(formUrl);
    form.setAcceptingResponses(true);
    console.log("Form is reopened for the new day.");
  }
}
```

3.按 Cmd + S （或 Ctrl + S ）保存代码。

第四步：配置自动化触发器（ Triggers ）

为了让系统全自动运转，需要配置两个触发器：

在 Apps Script 页面左侧边栏，点击闹钟图标 Triggers （触发器）-> 右下角 “+ Add Trigger”：

触发器 1：用户提交表单时即时发码

⚬ Choose which function to run：选择 sendPromoCode

⚬ Select event source：选择 From spreadsheet （来自电子表格）

⚬ Select event type：选择 On form submit （提交表单时）

⚬ 点击 Save （此时 Google 会弹出权限授权提示，点击 Advanced -> Go to Project (unsafe) -> Allow 即可）。

触发器 2：次日凌晨自动重开表单

⚬ 再次点击右下角 + Add Trigger

⚬ Choose which function to run：选择 resetAndReopenFormDaily

⚬ Select event source：选择 Time-driven （基于时间）

⚬ Select type of time based timer：选择 Day timer （按日定时器）

⚬ Select time of day：选择 Midnight to 1am （午夜至凌晨 1 点）

⚬ 点击 Save 。

三、 独立开发者的实战“避坑总结”

这套方案看似简单，但在实际落地中如果不注意以下几个细节，很容易遇到故障：

1.语言与表头不匹配的“静默失败”

⚬ 陷阱：如果你的 Google Forms 后台是中文界面，开启“收集电子邮件”时，传入 Sheets 的表头叫“电子邮件地址”。如果脚本里写死了判断 key.includes("email")，脚本会找不到邮箱而静默退出，用户收不到邮件。
⚬ 解法：上述代码中采用了“中文/英文关键词 + 全局邮箱格式正则扫描”的双保险匹配，无论表单换成什么语言、列名叫什么，只要用户填入的内容符合邮箱格式，就能精准抓取。

2.免费版 Gmail 的 100 封/天硬限制

⚬ 陷阱：Google 个人账号（@gmail.com ）通过脚本发送邮件的额度是 严格的 100 封/24 小时。如果活动突然被大 V 转发瞬间涌入几百人，一旦超额，后续邮件全都会抛出 Email quota exceeded 异常，甚至导致发信功能被封禁。
⚬ 解法：代码中内置了 DAILY_LIMIT = 100 。一旦当天计数达到上限，脚本会直接调用 form.setAcceptingResponses(false) 物理关停表单并提示用户明日再来，次日再通过 Cron 定时器自动放行，完美闭环。

3.多人并发填表的“撞码”事故

⚬ 陷阱：当多个用户在同一秒点击提交时，两个云端线程读取到的表格最新状态相同，极有可能把同一个激活码发给两个人。
⚬ 解法：代码开头必须使用 LockService.getScriptLock() 获取互斥锁。只有前一个请求写完表格落盘（ SpreadsheetApp.flush()）并释放锁后，后一个请求才能读取，彻底杜绝发重码。

4.时区校准

⚬ 在 Apps Script 左侧齿轮图标 Project Settings 中，务必检查 Time zone 。若活动面向全球，推荐设置为 (GMT+00:00) UTC ，确保每天的 00:00 截断与重开时间和文案严格对应。

四、 总结

这套方案的最大优势在于：

⚬ 零财务成本：不用购买第三方表单会员，不消耗自建服务器流量。
⚬ 完全免维护：放进 1,000 个码后，依靠每日限额与定时器自动开关，无需人工值守。
⚬ 交付体验良好：通过正规邮件投递，自带激活教程与官网链接，给用户非常正规的技术感与品牌信任度。

## 关联链接

- https://cmder.aitobox.com

## 导航

- 项目页：[[10-项目/cmder.aitobox.com_d453696a]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
