#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
BASE = '/root/.openclaw/workspace/mindset-podcasts'
style = open('/tmp/style.html', encoding='utf-8').read()

now_utc = '2026-10-11 09:53 UTC'
now_hkt = '2026-10-11 17:53'

def card(name, host, tag, last_title, last_date, dur, link, site, first_report, synopsis, note=''):
    tagcls = 'none'
    return f'''
<!-- ==================== {name} ==================== -->
<section class="pod">
  <div class="pod-head">
    <h2>{name}</h2>
    <span class="host">{host}</span>
    <span class="tag {tagcls}">{tag}</span>
  </div>
  <div class="callout">
    📭 本台今日（2026-10-11）比對 <code>state.json</code> 後<b>無新集數</b>。所有已發佈集數 GUID 均已掃過。<br>
    <b>最後已知劇集：</b>{last_title}（{last_date}{('，' + dur) if dur else ''}）
  </div>
  <div class="le-summary" style="margin-top:14px">
    <b>內容概要：</b>{synopsis}
  </div>
  <div class="le-link" style="margin-top:10px">🔗 <a href="{site}">{site}</a>{(' · 集數頁：<a href="' + link + '">連結</a>') if link else ''} · 首次完整拆解見 <a href="{first_report}">{first_report.replace('daily-report-','').replace('.html','')} 日報</a></div>
  {('<div class="callout" style="margin-top:12px">' + note + '</div>') if note else ''}
</section>
'''

cards = ''

cards += card(
    "Acquired", "Ben Gilbert &amp; David Rosenthal", "最近無更新",
    "The Home Depot", "2026-09-13", "3 小時 35 分（12,902 秒）",
    "https://www.acquired.fm/episodes/home-depot", "https://www.acquired.fm/episodes",
    "daily-report-2026-09-14.html",
    "Home Depot 創辦故事：Bernie Marcus 同 Arthur Blank 喺 48 歲同 35 歲畀人炒魷之後，聽咗紐約銀行家 Ken Langone（就係令佢哋被炒嗰個人）嘅一句話——「你哋係畀金馬蹄鐵踢中咗屁股」——然後寫下美國零售史上最強複利故事之一。官方描述形容成一個「Avengers 電影」：只要 Avengers 被炒、破產、再疊起十呎高嘅空油漆罐扮有貨。Sol Price 等傳奇人物陸續客串出場。",
    note="⚠️ Acquired 自 09-13 後未再有新集；本台更新節奏約每月 1–2 集（長篇研究型），下一集通常緊接大主題。")

cards += card(
    "Founders", "David Senra", "最近無更新",
    "#436 Ari Emanuel's Autobiography", "2026-10-05", "1 小時 9 分（4,185 秒）",
    "", "https://www.founderspodcast.com/",
    "daily-report-2026-10-06.html",
    "David Senra 讀 Ari Emanuel（Endeavor／WME 掌門人）自傳《Roll The Calls》（題目源自 Emanuel 家族格言「唔好等，主動打過去」）嘅讀書筆記。Senra 一貫做法：抽書中行動者嘅決策、野心同偏執，講一個經紀人點樣由收發室做到建立橫跨演藝、體育、時尚嘅娛樂帝國。本集由 Ramp、Applovin、Vanta 贊助。",
    note="ℹ️ Founders 為週更（多數星期一），#436 對應 10-05；下一集預料 10-12 左右。")

cards += card(
    "All-In", "Chamath · Jason · Sacks · Friedberg", "最近無更新",
    "Is Claude Conscious? Pope Rejects, Model Welfare Movement, OpenAI's Math Backlash, France Riots", "2026-10-10", "1 小時 33 分（01:33:15）",
    "https://allinchamathjason.libsyn.com/is-claude-conscious-pope-rejects-model-welfare-movement-openais-math-backlash-france-riots",
    "https://allin.com/", "daily-report-2026-10-10.html",
    "四大主題：（1）Anthropic 認為 Claude 可能具意識——新宗教？游說教廷、對齊風險、model welfare 運動；（2）OpenAI 數學突破引發社群反彈（Terry Tao、Scott Aaronson 等發聲）；（3）法國騷亂、Friedberg 嘅「社會主義指數」與債市；（4）Grok Bot 轉 headless、OpenAI 推 Dots、IP 是否一文不值。",
    note="ℹ️ 此集已於 10-10 日報完整拆解；All-In 一般週五／週六更新（美西時間），下一集預料 10-16 前後。")

cards += card(
    "My First Million", "Sam Parr &amp; Shaan Puri", "最近無更新",
    "The creative genius behind Squatty Potty &amp; Poo-Pourri reveals his marketing playbook", "2026-10-07", "1 小時 5 分（3,938 秒）",
    "", "https://www.mfmpod.com/episodes/",
    "daily-report-2026-10-08.html",
    "Episode 869：Shaan Puri 同 Angel Studios 創辦人 Jeff Harmon 對談，講「揾系統漏洞（glitches）」——由幫牙醫做嘅神級營銷案例（Squatty Potty、Poo-Pourri）講起，示範點樣捕捉注意力、19 分鐘廣告實驗、以及點解要揀自己真正頭痛嘅問題去創業。內含 HubSpot「$1M Attention Guide」推廣。",
    note="ℹ️ MFM 每週約 2–3 集（週一／週三／週五）；Shaan vs Sam 輪更主持。下一集預料 10-12 前後。")

cards += card(
    "The Knowledge Project", "Shane Parrish", "最近無更新",
    "Ryan Serhant: How to Get People to Say Yes", "2026-10-08", "—（Members 先行；公開 10-08）",
    "https://fs.blog/knowledge-project-podcast/ryan-serhant/", "https://fs.blog/knowledge-project/",
    "daily-report-2026-10-09.html",
    "Ryan Serhant（SERHANT. 創辦人、《Million Dollar Listing New York》／Netflix《Owning Manhattan》主角）講「唔令人覺得被推銷」嘅銷售法：先建立連結、先幫人、賺到開口請求嘅資格。核心係信任與關係資本，而非話術。",
    note="ℹ️ KP 目前 RSS 只有 20 集（滾動 feed），週四更新；下一集預料 10-15 前後。")

cards += card(
    "The Diary of a CEO", "Steven Bartlett", "最近無更新",
    "Most Replayed Moment: AI Is Changing How Teams Work Forever", "2026-10-09", "20 分 41 秒（1,241 秒）",
    "", "https://thediaryofaceo.com/",
    "daily-report-2026-10-09.html",
    "DOAC「Most Replayed Moment」重播精華，剪自 2026-06-08 全集《Death of the Middle Class: Billionaire vs Entrepreneur DEBATE》嘅「AI 同未來工作」段落。對陣：Nick Hanauer（Amazon 首位非家族投資人，政策／分配派）vs Daniel Priestley（作家／創業者，適應派）。核心問題：當 AI 做得到原本只有人做得到嘅任務，係大規模失業，定係人類潛能新紀元？",
    note="ℹ️ DOAC 平日近乎每日更新（週一至週五 05:00 UTC 左右）；下一集預料 10-12。")

html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>思維播客日報 · 2026-10-11</title>
{style}
</head>
<body>
<div class="wrap">

<header class="top">
  <h1>思維播客日報 · 2026-10-11</h1>
  <div class="sub">6 個英文商業／思維播客 · 每日深度掃描 · 為 James 而設的「第二對耳仔」</div>
  <div class="meta">
    🕘 報告生成時間：<b>{now_utc}</b>（= 香港時間 {now_hkt}）<br>
    📡 掃描方式：6 條 RSS feed 直接抓取 XML，逐集比對 GUID 去重<br>
    🧮 Jev 前置過濾（TypeSafe System One, <code>news</code> profile）：本輪 <b>0 條候選</b> → 無需過濾（fail-open 正常）<br>
    🧑‍💻 Repo：<a href="https://github.com/JMOKSZ/mindset-podcasts">JMOKSZ/mindset-podcasts</a>
  </div>
</header>

<div class="summary">
  <b>今日重點：6 台全部無新集。</b>
  <ul>
    <li>📭 <b>Acquired、Founders、All-In、My First Million、Knowledge Project、Diary of a CEO</b>：本輪逐條比對後<b>均無未掃過嘅新 GUID</b>。</li>
    <li>📅 最近一次有更新：<b>All-In</b> 10-10（Claude 意識／OpenAI 數學／法國騷亂）、<b>DOAC</b> 10-09（AI 團隊重播高光）、<b>KP</b> 10-08（Ryan Serhant 銷售）、<b>MFM</b> 10-07（Squatty Potty 營銷）。三個台（Acquired／Founders）本身節奏較疏。</li>
    <li>ℹ️ 說明：6 條 feed 全部 HTTP 200 成功抓取；今日屬「無更新」日，各台最後已知劇集連內容概要列於下方卡片。</li>
  </ul>
</div>

<div class="stats">
  <div class="stat"><span class="n">6/6</span><span class="l">RSS 抓取成功</span></div>
  <div class="stat"><span class="n">0</span><span class="l">今日新集數</span></div>
  <div class="stat"><span class="n">2,978</span><span class="l">累計追蹤集數</span></div>
  <div class="stat"><span class="n">6</span><span class="l">播客台數</span></div>
</div>

{cards}

<footer class="bot">
  <div class="timeline">
    ⏱ <b>本輪掃描時序</b><br>
    <code>09:53Z</code> 讀 podcasts.json（6 台）/ state.json（2,978 個已掃 GUID）<br>
    <code>09:53Z</code> Fetch 6 條 RSS feed → 全部 HTTP 200（217 / 461 / 434 / 909 / 20 / 895 集）<br>
    <code>09:53Z</code> GUID 逐條比對 → <b>0 條新內容</b>（6 台最新集均已掃過）<br>
    <code>09:53Z</code> Jev triage 0 條（無候選；fail-open 健康）<br>
    <code>09:53Z</code> 生成「無更新」報告 → 更新 state.json lastScan → git push
  </div>
  <p>📬 本報告由 Vee Mok 為 James 自動生成 · 每日深度掃描 6 個英文商業／思維播客 · 所有內容基於真實 RSS／官方集頁，未經核實之數字與預測已標 ⚠️。</p>
  <p>🔗 <a href="https://jmoksz.github.io/mindset-podcasts/">jmoksz.github.io/mindset-podcasts</a> · <a href="https://github.com/JMOKSZ/mindset-podcasts">GitHub Repo</a></p>
</footer>

</div>
</body>
</html>
'''

open(BASE + '/daily-report-2026-10-11.html', 'w', encoding='utf-8').write(html)
print("written", len(html), "bytes")
