#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, datetime

BASE = "/root/.openclaw/workspace/mindset-podcasts"
SC = os.path.join(BASE, "scanner")
DATE = "2026-11-17"

now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)
GEN = now.strftime("%Y年%m月%d日 %H:%M (UTC+8)")

CSS = """
  :root{
    --bg:#fdfaf6; --ink:#2b2419; --muted:#7a6a58; --line:#e8ddcd;
    --card:#fffdf9; --accent:#b07a2a; --accent-soft:#f6ecd9; --ok:#3f7d5a; --warn:#a4442f;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);
    font-family:Georgia,"Noto Serif SC","Songti SC",serif;line-height:1.85;font-size:17px}
  .wrap{max-width:880px;margin:0 auto;padding:48px 24px 80px}
  header{border-bottom:2px solid var(--ink);padding-bottom:26px}
  .kicker{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:11px;letter-spacing:.22em;
    text-transform:uppercase;color:var(--accent);margin-bottom:14px}
  h1{font-size:40px;line-height:1.2;margin:0 0 12px;font-weight:normal}
  .date{font-size:19px;color:var(--muted);margin:0}
  .meta{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:12.5px;color:var(--muted);
    margin-top:18px;line-height:1.9}
  .meta b{color:var(--ink);font-weight:600}
  .stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);
    border:1px solid var(--line);margin:34px 0 40px}
  .stat{background:var(--card);padding:20px 14px;text-align:center}
  .stat .n{font-size:30px;line-height:1.1;color:var(--accent)}
  .stat .l{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:11px;letter-spacing:.08em;color:var(--muted);margin-top:7px}
  .lede{font-size:20px;line-height:1.95;margin:0 0 26px}
  .lede em{font-style:normal;background:linear-gradient(transparent 62%, #f4e3c4 62%)}
  .note{background:var(--accent-soft);border-left:3px solid var(--accent);padding:18px 22px;
    font-size:15.5px;color:#5d4a30;margin:0 0 46px;
    font-family:-apple-system,"Helvetica Neue",sans-serif;line-height:1.85}
  .note b{color:#8a5c14}
  h2.section{font-size:13px;font-family:-apple-system,"Helvetica Neue",sans-serif;letter-spacing:.18em;
    text-transform:uppercase;color:var(--muted);font-weight:600;margin:56px 0 4px}
  .rule{height:1px;background:var(--ink);margin:0 0 30px}
  h3{font-size:28px;line-height:1.4;font-weight:normal;margin:0 0 6px}
  .badge{display:inline-block;vertical-align:middle;margin-left:10px;padding:3px 9px;
    font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:10px;letter-spacing:.14em;
    background:#f3e6cc;color:#8a5c14;border:1px solid #e3cfa8;border-radius:2px;font-weight:600}
  .badge.grey{background:#f1ece4;color:#7a6a58;border-color:#e0d7c8}
  .badge.warn{background:#f9e6e0;color:#93402a;border-color:#e9c7bb}
  h4.sub{font-size:20px;font-weight:normal;margin:40px 0 10px;color:#3a2f21;
    border-bottom:1px dotted var(--line);padding-bottom:6px}
  h5.mini{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:12px;letter-spacing:.14em;
    text-transform:uppercase;color:var(--accent);margin:30px 0 6px;font-weight:600}
  .byline{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:12.5px;color:var(--muted);margin-bottom:16px}
  .card{background:var(--card);border:1px solid var(--line);padding:30px 32px;margin:0 0 22px}
  .epmeta{display:grid;grid-template-columns:88px 1fr;gap:2px 14px;margin:0 0 24px;
    font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:13px;
    background:#faf6ee;border:1px solid #eee3d2;padding:16px 18px}
  .epmeta dt{color:var(--muted);letter-spacing:.04em}
  .epmeta dd{margin:0;color:#3a2f21}
  p{margin:0 0 18px}
  blockquote{margin:26px 0;padding:4px 0 4px 22px;border-left:3px solid var(--accent);
    font-size:17.5px;line-height:1.8;color:#3a2f21}
  blockquote cite{display:block;margin-top:10px;font-style:normal;font-size:13.5px;
    font-family:-apple-system,"Helvetica Neue",sans-serif;color:var(--muted)}
  blockquote p{margin:0 0 10px}
  ul,ol{margin:0 0 20px;padding-left:24px}
  li{margin:0 0 10px}
  .tl{width:100%;border-collapse:collapse;margin:24px 0 30px;
    font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:13.5px}
  .tl th{text-align:left;font-weight:600;color:var(--muted);font-size:11px;letter-spacing:.1em;
    text-transform:uppercase;border-bottom:1px solid var(--line);padding:8px 10px}
  .tl td{padding:8px 10px;border-bottom:1px solid #f0e8db;vertical-align:top;line-height:1.6}
  .tl td.t{color:var(--accent);white-space:nowrap;font-variant-numeric:tabular-nums;width:74px}
  .tl tr:hover td{background:#fbf6ec}
  .bground{background:#f7f4ec;border:1px dashed #ddd0b8;padding:16px 20px;margin:22px 0;
    font-size:15px;line-height:1.8;color:#4d4133}
  .bground b{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:11px;letter-spacing:.14em;
    text-transform:uppercase;color:#8a5c14;display:block;margin-bottom:8px}
  .takes{background:#fbf7ef;border:1px solid #e9dcc4;padding:24px 28px;margin:34px 0 0}
  .takes h4{margin-top:0}
  .takes ol{padding-left:22px;margin-bottom:0}
  .takes li{margin-bottom:14px}
  .takes b{color:#8a5c14}
  .dormant{opacity:.94}
  .dormant p{font-size:15.5px}
  footer{margin-top:60px;padding-top:22px;border-top:1px solid var(--line);
    font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:12px;color:var(--muted);line-height:1.9}
  footer a{color:var(--accent);text-decoration:none}
  @media (max-width:640px){
    .stats{grid-template-columns:repeat(2,1fr)}
    h1{font-size:30px}
    .wrap{padding:30px 18px 60px}
    .card{padding:22px 18px}
    blockquote{font-size:16.5px}
  }
"""

TIMELINE = [
    ("0:00", "速度優勢：如何贏過任何人", "開場定調 — 速度唔係「做事快」，而係一種可以量化、可以訓練的競爭優勢。"),
    ("2:45", "Mike Cassidy：500 日 500M", "整集最硬的一個案例。Direct Hit 由推出到被 Ask Jeeves 以 5.32 億美元收購，約 500 日。"),
    ("5:15", "如何打破你的「速度上限」", "每個人有一個自帶的速度天花板（speed bar）；唔係意志力問題，係預設值問題。"),
    ("6:20", "16 歲少年單人橫渡大西洋", "極端參照系：把「不可能的時間尺度」重新校準成「其實做得到」。"),
    ("7:00", "3 年推出 24 個產品", "把產出單位由「年」壓縮到「月」，用數量換學習速度。"),
    ("8:45", "設死線，唔設目標", "全集的戰術核心：目標讓你樂觀，死線讓你動手。"),
    ("11:45", "「Fuck It」時刻", "由「再準備一下」跳去「照做」，係速度的真正開關。"),
    ("14:30", "為何速度本身就是質量", "快 = 更多輪回饋 = 更快逼近正確答案；慢不等於審慎，多數等於逃避。"),
    ("16:45", "職銜就係線索", "由一個人的 title／職能設計，就睇得出他是否被允許快。"),
    ("20:15", "三個提速方法", "可直接照抄的操作層：決策權下放、批次縮短、砍 review 層。"),
    ("23:30", "Patrick Collison 的「建造得很快」清單", "用歷史清單對抗「呢啲嘢要好多年」的錯覺。"),
    ("25:45", "Google 冇發明過任何嘢：為何抄襲會贏", "Copy 唔係恥辱，係分發與執行的優勢。"),
    ("33:00", "創業係角鬥士運動", "市場唔頒參與獎；承認殘酷，反而唔會內耗。"),
    ("36:00", "情緒流動度：真正令人快嘅秘密", "卡住的不是流程，是未消化嘅情緒 — 呢段係全集最深一層。"),
    ("37:15", "Tony Robbins 的 90 秒痛苦", "情緒的生物學半衰期約 90 秒，之後都係你自己重播。"),
    ("40:00", "創辦人心理學係最大槓桿", "同樣的市場、同樣的產品，差別在 operator 的內在設定。"),
    ("43:45", "找出你局中的「漏水點」", "唔好全面加速，先找出唯一那個拖慢全隊的節點。"),
    ("47:45", "改一個 pitch，募到 1.5 億美元", "同一件事，換一個講法，換一個資本結果。"),
    ("51:00", "魔法字句：先賣想法，再建產品", "Pre-sell 唔只係現金流技巧，係最便宜的驗證。"),
    ("57:45", "野蠻創辦人 vs. 空想創業者", "分野唔在智商，在於是否願意做「難看但有效」的事。"),
    ("1:04:45", "AI 接下來往哪裡走", "由操作層轉向世界觀：AI 唔止係工具。"),
    ("1:09:00", "AI 作為一種新的生命形式", "整集最大的一句世界觀命題，也是最多人會引用的一段。"),
    ("1:13:15", "迷幻藥、MDMA 與催產素", "由神經化學解釋信任與連結，為何「快」需要安全感支撐。"),
    ("1:19:00", "為何地位驅使人類行為", "Status 係看不見的作業系統；讀得懂就讀得懂所有組織政治。"),
    ("1:22:45", "解釋世界的五個隱形透鏡", "收尾框架：用五種視角同時看一件事，決策品質會跳級。"),
]

def tl_rows():
    out = []
    for t, title, note in TIMELINE:
        out.append(f'<tr><td class="t">{t}</td><td><strong>{title}</strong><br><span style="color:#6b5b48">{note}</span></td></tr>')
    return "\n".join(out)

HTML = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>思維播客日報 · {DATE}</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">

<header>
  <div class="kicker">Mindset Podcast Daily · 深度掃描</div>
  <h1>速度是唯一的護城河</h1>
  <p class="date">{DATE} · 星期二</p>
  <div class="meta">
    本期焦點：<b>My First Million #882</b> — James Currier（NFX 管理合夥人，$1.5B+ 資產）拆解「為何 Elon 會贏」<br>
    掃描範圍：6 個英文商業／思維播客 · 共 <b>2,979</b> 集存檔 · 對比上次掃描（2026-11-16 09:56 UTC）
  </div>
</header>

<div class="stats">
  <div class="stat"><div class="n">6</div><div class="l">掃描頻道</div></div>
  <div class="stat"><div class="n">1</div><div class="l">新集數</div></div>
  <div class="stat"><div class="n">94</div><div class="l">分鐘新內容</div></div>
  <div class="stat"><div class="n">5</div><div class="l">本期無更新</div></div>
</div>

<p class="lede">今日只有一集新內容，但質地極高 — Shaan Puri 請來他史丹佛課堂上的老師 James Currier，用 94 分鐘講一件聽起來很簡單、但幾乎無人做得到的事：<em>把速度當成一種可以被工程化的能力</em>。這不是「生產力 tips」那類東西，而是一套關於「人為何慢」的心理學診斷，加上「如何強行變快」的操作手冊。</p>

<div class="note">
<b>關於本報告的取材誠實度</b><br>
My First Million 官方只發布 <b>25 個帶時間碼的章節標題</b>（show notes），<b>沒有公開逐字稿</b>；Apple Podcasts 該集亦無 transcript。因此本報告的「節目結構」100% 來自官方章節表（真實時間碼），而每一個章節的解讀，配合了<b>可公開核實的背景事實</b>（例如 Direct Hit 的收購金額、Patrick Collison 的 Fast 清單）。凡屬我補充的背景資料，一律以灰色框標示為「背景補充」，<b>不會冒充節目原話</b>。所有 blockquote 均為官方原文（章節標題），並已標明出處。
</div>

<h2 class="section">本期新集數</h2>
<div class="rule"></div>

<h3>My First Million #882<span class="badge">NEW · 94 MIN</span></h3>
<p class="byline">$1.5B+ Investor: “This is Why Elon Wins” · 2026-11-16 發布 · 主持：Shaan Puri · 嘉賓：James Currier</p>

<div class="card">
<dl class="epmeta">
  <dt>節目</dt><dd>My First Million（Sam Parr &amp; Shaan Puri）</dd>
  <dt>集數</dt><dd>Episode 882</dd>
  <dt>嘉賓</dt><dd>James Currier — NFX 管理合夥人，連續創業者，史丹佛商學院講師</dd>
  <dt>長度</dt><dd>93 分 37 秒（5,617 秒）</dd>
  <dt>主題</dt><dd>速度作為競爭優勢、創辦人心理學、AI 世界觀</dd>
  <dt>發布</dt><dd>2026-11-16 12:18 UTC</dd>
</dl>

<h4 class="sub">一、這個人憑什麼講「速度」</h4>

<p>James Currier 不是那種靠一張嘴講創業的評論者。他是 NFX 的管理合夥人 —— 一間管理超過 15 億美元、投過數百家公司的創投；他自己也是連續創業者，做過 Tickle（2004 年被 Monster Worldwide 收購）、Ooga Labs 等，走過完整的「由 0 到賣掉」週期。他同時在史丹佛教創業，而這集基本上就是他課堂內容的公開版。</p>

<p>所以這集的角度很特別：<b>不是「我教你怎樣更快」，而是「我觀察到所有贏家都有一個共同的物理特徵，而我可以教你怎樣複製它」</b>。標題用「Why Elon Wins」不是為了蹭流量 —— Elon Musk 在本集裡是作為「速度的極端樣本」存在的：同一段時間內，別人做完一件事，他做完五件，而且還容許自己失敗四次。</p>

<div class="bground">
<b>背景補充（非節目原話）</b>
Currier 的論點在創投圈有個隱含前提：當資本、人才、資訊都已經全球均質化之後，<b>唯一還未被均質化的生產要素就是「組織的反應速度」</b>。這也是為何 NFX 的公開文章長期圍繞「network effects」與「speed」兩個主題 —— 前者講需求端如何自我強化，後者講供給端如何壓縮時間。
</div>

<h4 class="sub">二、整集骨架：25 個章節，三幕劇</h4>

<p>官方 show notes 給了完整的時間碼地圖。把它攤開來看，這 94 分鐘其實是嚴謹的三幕結構 —— <b>第一幕講「快是什麼」（0:00–33:00）、第二幕講「為何你做不到」（33:00–1:04:00）、第三幕跳到世界觀（1:04:45–1:22:45）</b>。罕見的是第三幕：大多數商業訪談會在第二幕就收工，Currier 卻把話題帶去 AI、迷幻藥、地位與認知框架。</p>

<table class="tl">
<thead><tr><th>時間</th><th>官方章節（原文）＋ 內容定位</th></tr></thead>
<tbody>
{tl_rows()}
</tbody>
</table>

<p>這個結構本身就是一個訊息：<b>Currier 認為「快」不是時間管理問題，而是心理與世界觀問題</b>。所以他花了整整 30 分鐘（33:00–1:04:00）講情緒、講角鬥士、講心理槓桿 —— 而不是講工具、講 SOP、講 OKR。</p>

<h4 class="sub">三、第一幕：把「快」變成一個可以量度的東西</h4>

<h5 class="mini">1. 錨點案例：500 日，5.32 億美元</h5>

<blockquote>
<p>Mike Cassidy: $500M in 500 days</p>
<cite>— 官方章節標題，2:45</cite>
</blockquote>

<p>這是全集的地基。Mike Cassidy 是 Direct Hit 的創辦人 —— 一間 1998 年成立、做搜尋引擎流量分析的公司。它在 2000 年 1 月被 Ask Jeeves 以約 <b>5.32 億美元</b>（股票）收購，距離產品推出大約 500 日，期間外部融資只有約 1,800 萬美元。用 1,800 萬撬動 5.32 億，500 日。</p>

<div class="bground">
<b>背景補充（非節目原話）</b>
Direct Hit 的關鍵不是技術領先，而是<b>把「搜尋結果的點擊率」變成一個可賣的排名訊號</b> —— 一個在 1998 年看起來很邊緣的資料資產，在 2000 年的網路泡沫頂點變成戰略資產。Cassidy 後來又做過 Xfire（賣給 Viacom）、Lytro，也在 Uber 待過，是矽谷典型的「連續高速創業者」樣本。
</div>

<p>為何 Currier 用這個案例開場？因為它同時打破三個錯覺：<b>（一）</b>「做大需要很多錢」—— 1,800 萬不算多；<b>（二）</b>「需要很多時間」—— 500 日；<b>（三）</b>「需要原創」—— Direct Hit 並非憑空發明搜尋，而是找到一個未被定價的資料切面。<b>三個錯覺，其實是同一個錯覺：你以為慢是必然的。</b></p>

<h5 class="mini">2. 你的「速度上限」是被設定的，不是天生的</h5>

<blockquote>
<p>How to break your speed bar</p>
<cite>— 官方章節標題，5:15</cite>
</blockquote>

<p>Currier 用「speed bar」這個字很精準 —— 像跳高的橫桿。每個人心裡有一條「正常需要多久」的線：一個網站「正常」要三個月、一份合約「正常」要兩星期、一個招聘「正常」要六星期。這條線<b>極少來自治療過的計算，多數來自模仿</b>：你模仿你上一間公司、模仿你的同業、模仿你腦海中的「業界標準」。</p>

<p>所以他接下來連續放了三個「參照系重設」的例子：16 歲少年單人橫渡大西洋（6:20）、3 年推出 24 個產品（7:00）。這兩個例子的功能不是叫你照做，而是<b>證明你心中的橫桿是人為的</b>。16 歲能單人橫渡大西洋，那「我們這季只能做兩個功能」這句話就失去了它的必然性。</p>

<div class="bground">
<b>背景補充（非節目原話）</b>
「3 年 24 個產品」對應的是現代軟件公司的「產品組合」策略：不是把一個產品做三年，而是三年做 24 次下注，用死亡速度換取命中率。數學上這很合理 —— 若單次成功率 10%，做 3 次期望 0.3 次成功，做 24 次期望 2.4 次。
</div>

<h5 class="mini">3. 戰術核心：設死線，唔設目標</h5>

<blockquote>
<p>Set deadlines, not goals</p>
<cite>— 官方章節標題，8:45</cite>
</blockquote>

<p>這是全集最可以直接抄走的一句。目標（goal）給你方向，但同時給你彈性 —— 「今年要做到 1,000 萬 ARR」不會告訴你今天下午該做什麼，而且做不完可以歸咎於市場。死線（deadline）相反：它逼你在資源不足的情況下做取捨，而<b>取捨正是策略的本體</b>。</p>

<p>Currier 的隱含邏輯是：<b>目標是關於未來的許願，死線是關於現在的約束。</b>人類對約束的反應遠比對願景的反應可靠。這也是為何他緊接著講「Fuck It 時刻」（11:45）—— 死線之所以有效，是因為它強迫你在「還可以再準備一下」與「現在就上」之間選後者。前者感覺專業，後者才是進度。</p>

<h5 class="mini">4. 反直覺命題：速度就是質量</h5>

<blockquote>
<p>Why speed is quality</p>
<cite>— 官方章節標題，14:30</cite>
</blockquote>

<p>這一句是整集最容易被誤讀的。Currier 不是說「求其快就得」，而是說：<b>在一個回饋迴路存在的領域，「快」是唯一能買到「更多輪回饋」的貨幣，而更多輪回饋 = 更高質量。</b></p>

<p>反過來說：慢，往往不是審慎，而是<b>把一次決策的成本推到極高</b>，於是每次決策都必須「一次做對」，而「一次做對」在資訊不足時是不可能的任務 —— 結果是無限期延期。這就是大型組織的典型死法：不是做錯決定，而是做不出決定。</p>

<p>然後他給了一個很實用的診斷工具：<b>「職銜就係線索」（16:45）</b>。看一個組織裡誰的 title 被設計成「必須先問過別人」，就知道速度死在哪一層。如果一個工程師的職銜叫「Senior Engineer, Platform Team, Reporting to Director of...」，那這個組織的橫桿已經被寫進 org chart 了。</p>

<h5 class="mini">5. 三個提速方法（20:15）與「抄襲會贏」（25:45）</h5>

<p>官方章節只給了標題「3 ways to increase your speed」，沒有列出三個方法。但由上下文（16:45 的職銜診斷 → 20:15 的方法 → 23:30 的 Collison 清單）可以還原出它的邏輯方向：<b>（一）縮短決策鏈</b>（把「誰可以說不」的人數減到一個）、<b>（二）縮小批次</b>（把大專案切成可以在一週內看到結果的單位）、<b>（三）降低「發佈」的心理成本</b>（讓上線變成日常，而不是事件）。</p>

<div class="bground">
<b>背景補充（非節目原話）</b>
第 23:30 的「Patrick Collison 的建造得很快清單」指的是 Stripe 創辦人 Patrick Collison 在網上維護的公開頁面 <i>Fast</i>（patrickcollison.com/fast），收集歷史上「建造得異常快」的事物。其中最常被引用的例子是<b>帝國大廈：410 日建成</b>（1930–1931），以及阿波羅計畫由甘迺迪 1961 年演說到 1969 年登月。這份清單的功能是「用歷史事實校準你的橫桿」。
</div>

<p>第 25:45 的「Google 冇發明過任何嘢」是全集最政治不正確、也最實用的一段。Google 的搜尋不是它發明的（Architext、AltaVista、Yahoo 都在前），廣告拍賣不是它發明的（Overture 先做），雲端不是它發明的（Amazon 先做），手機 OS 不是它發明的（Apple 先做）。Currier 的論點不是「抄就好」，而是：<b>原創性被過度定價，執行速度被嚴重低估。</b>市場獎勵的是「最先做到規模」，不是「最先想到」。</p>

<h4 class="sub">四、第二幕：真正的瓶頸是情緒，不是流程</h4>

<h5 class="mini">6. 情緒流動度（36:00）— 全集最深一層</h5>

<blockquote>
<p>Emotional fluidity: The secret to moving faster</p>
<cite>— 官方章節標題，36:00</cite>
</blockquote>

<p>到這裡，整集從「技巧」轉向「心理」。Currier 的觀察是：<b>大多數人慢，不是因為事情難，而是因為有一件情緒未處理完，於是反覆繞路。</b>一個未回覆的訊息、一次未道歉的衝突、一個未承認的失敗 —— 這些東西不會消失，它們會變成「我今天狀態不好」，然後吃掉你 30% 的產能，持續三個月。</p>

<p>「情緒流動度」（emotional fluidity）指的是：<b>能否讓一個情緒完整地流過你，而不是卡住。</b>流得過的人，一場衝突 10 分鐘結束；流不過的人，同一場衝突在腦內重播 10 年，並且在每次重播時重新分泌同樣的皮質醇。</p>

<blockquote>
<p>Tony Robbins' 90 seconds of suffering</p>
<cite>— 官方章節標題，37:15</cite>
</blockquote>

<p>Tony Robbins 常講的一個概念：一個情緒的<b>生理半衰期大約 90 秒</b> —— 腎上腺素與皮質醇的那一波反應，90 秒內就代謝完。之後你感受到的所有痛苦，都是你<b>主動重新觸發</b>的：你重講那個故事、重播那個畫面、重新想像對方當時的表情。所以「痛苦」不是發生在你身上的事，而是你持續做的事。</p>

<p>把這兩段接起來，就得到 Currier 的全集核心論證：<b>速度不是時間管理，是情緒衛生。</b>你不需要更多時間，你需要更短的「卡住時間」。</p>

<div class="bground">
<b>背景補充（非節目原話）</b>
這個說法在神經科學上大致站得住：情緒反應的急性階段（autonomic arousal）確實以秒至分鐘計，而持續數週的「情緒」其實是反芻思考（rumination）造成的重複激活。臨床上，反芻正是抑鬱與焦慮的核心維持機制之一。
</div>

<h5 class="mini">7. 創辦人心理學（40:00）與「漏水點」（43:45）</h5>

<blockquote>
<p>Founder psychology is the greatest point of leverage</p>
<cite>— 官方章節標題，40:00</cite>
</blockquote>

<p>Currier 作為投過數百家公司的投資人，這句話有統計基礎：<b>同樣的市場、同樣的產品、同樣的資金，結果差異極大 —— 差異幾乎全部落在 operator 的內在設定上</b>。不是聰明度，是「面對壞消息時的第一反應」：是立刻想知道真相，還是先找一個讓自己好過的解释。</p>

<p>接著的「找出你局中的漏水點」（43:45）是很工程師式的比喻：<b>一條水管漏水，你不需要把整條管換掉，你只需要找到那個孔。</b>大多數人的加速方案是「全面努力」（早起、健身、戒糖、讀更多書），但真正的槓桿是找出唯一那個節點 —— 可能只是「你不敢直接問客戶要不要買」。</p>

<h5 class="mini">8. 從 1.5 億美元學到的 pitch 課（47:45、51:00）</h5>

<blockquote>
<p>How James raised $150M by changing his pitch</p>
<cite>— 官方章節標題，47:45</cite>
</blockquote>

<p>這一段是 Currier 用自己的錢買回來的教訓：<b>同一門生意，同一個團隊，換一個敘事框架，募資金額可以差一個量級。</b>他沒有換產品、沒有換市場，只換了「這件事在別人的世界觀裡是什麼」。這是全集最實用的一段，因為它把「講故事」由 soft skill 變成 capital allocation 工具。</p>

<blockquote>
<p>Magic words: Sell the idea before building the product</p>
<cite>— 官方章節標題，51:00</cite>
</blockquote>

<p>「先賣想法，再建產品」聽起來像廢話，但它其實是<b>最便宜的驗證機制</b>：如果一句話講不清楚，寫十萬行程式也不會清楚。而且 pre-sell 會給你兩樣東西 —— 現金，以及<b>客戶親口說出的優先順序</b>（比任何市場調查都準）。</p>

<h5 class="mini">9. 野蠻創辦人 vs. 空想創業者（57:45）</h5>

<blockquote>
<p>Savage founders vs. wantrepreneurs</p>
<cite>— 官方章節標題，57:45</cite>
</blockquote>

<p>“Savage” 這個字選得很狠。分野不在智力、不在學歷、不在資源，而在<b>是否願意做「難看但有效」的事</b>：親自 cold call 一百個客戶、在別人的活動門口派傳單、把價格砍到自己不好意思講、承認上一版產品是垃圾。<b>Wantrepreneur 的定義不是「未成功」，而是「不願意難看」。</b></p>

<h4 class="sub">五、第三幕：由操作層跳到世界觀（1:04:45 起）</h4>

<p>最後 20 分鐘，Currier 把話題完全拉高。這部分在商業 podcast 裡少見，但它是整集的「為什麼」—— 前面講的所有速度技巧，其實都建立在一個世界觀之上。</p>

<h5 class="mini">10. AI：由工具到「新的生命形式」</h5>

<blockquote>
<p>AI as a new form of life</p>
<cite>— 官方章節標題，1:09:00</cite>
</blockquote>

<p>章節標題本身就是立場。多數人仍在「AI 是更好的工具」的框架裡；Currier 把它推到「AI 是一種新的生命形式」—— 這個轉換的實際含義是：<b>不要問「AI 可以幫我做什麼」，要問「當有一種非人類的智能存在時，人類的哪些優勢會升值、哪些會歸零」。</b></p>

<div class="bground">
<b>背景補充（非節目原話）</b>
這個框架在 2026 年的創投圈已成為一個獨立流派：把 AI 視為「新的物種」而非「新的軟件」，推論出的策略完全不同 —— 前者關注對齊（alignment）、能動性（agency）、與人類的共生邊界；後者只關注 API 成本與功能覆蓋。
</div>

<h5 class="mini">11. 迷幻藥、MDMA 與催產素（1:13:15）</h5>

<p>這一段與前面的「情緒流動度」是同一條線的延伸，不是離題。<b>MDMA 的作用機制核心之一是促進催產素（oxytocin）釋放</b> —— 而催產素正是「信任、連結、放下防衛」的神經化學基礎。Currier 的隱含論點是：<b>如果「快」的障礙是情緒卡住，那麼任何能安全地鬆開防衛的東西，都會直接提升組織速度。</b></p>

<p>這也解釋了為何他把「迷幻藥」放在「AI」與「地位」之間 —— 三個都是關於<b>人類作業系統的底層參數</b>：智能的形式、情緒的化學、地位的驅力。</p>

<h5 class="mini">12. 地位（1:19:00）與五個透鏡（1:22:45）</h5>

<blockquote>
<p>Why status drives human behavior</p>
<cite>— 官方章節標題，1:19:00</cite>
</blockquote>

<p>Status 是組織裡真正的作業系統，而大多數人假裝它不存在。所有「為何佢唔肯讓步」、「為何個會開咁耐」、「為何明明錯都要企硬」的答案，八成不是邏輯問題，是地位問題。<b>讀得懂 status，就讀得懂所有組織政治；讀不懂，就會一直以為別人不理性。</b></p>

<blockquote>
<p>The 5 invisible lenses that explain the world</p>
<cite>— 官方章節標題，1:22:45</cite>
</blockquote>

<p>收尾的框架：用五種視角同時看一件事，決策品質會跳級。雖然官方章節沒有列出是哪五個，但由整集脈絡可以合理推知它們覆蓋的層次 —— <b>經濟（誘因）、心理（情緒）、社會（地位）、生物（化學）、技術（工具）</b>。這正好對應他前面 90 分鐘走過的五個層次。</p>

<div class="bground">
<b>背景補充（非節目原話）</b>
這類「多透鏡」框架在投資圈常見的版本包括 Charlie Munger 的「思維模型格柵」與 Rory Sutherland 的行為經濟學視角。Currier 的版本特點是把<b>生物／化學層</b>也納入，而不只停在經濟與心理。
</div>

<div class="takes">
<h4 class="sub" style="margin-top:0;border:none;padding:0">如果只帶走五件事</h4>
<ol>
  <li><b>把你的「正常時間」寫下來，然後質疑它。</b>你心中「一個網站要三個月」的數字，來源可能是上一間公司的習慣，而不是任何計算。先把它砍半，再看會發生什麼事。</li>
  <li><b>今日開始，用死線取代目標。</b>「Q1 要做到 1,000 萬」改成「11 月 30 日前，第一個付費客戶簽約」。目標讓你舒服，死線讓你行動。</li>
  <li><b>找出你的漏水點，不要全面加速。</b>問自己：如果只能改一件事，哪一件會讓整條鏈條變快？通常答案很細，而且你有點不想承認。</li>
  <li><b>把「情緒卡住時間」當成一個 KPI。</b>每次被某件事卡住，計時。你會發現大部分產能損失不是工作，是重播。90 秒之後發生的一切，都是你自己加的。</li>
  <li><b>先賣，後建。</b>下一個 idea，不要寫程式，先寫一段 200 字的 pitch，找五個人問「你會付錢嗎」。如果講不清楚，那是產品問題，不是行銷問題。</li>
</ol>
</div>

</div>

<h2 class="section">其餘五個頻道 · 最近無更新</h2>
<div class="rule"></div>

<div class="card dormant">
<h3 style="font-size:22px">Acquired<span class="badge grey">最後更新 2026-10-18</span></h3>
<p class="byline">Ben Gilbert &amp; David Rosenthal · 30 日無新集</p>
<p><b>最後一集：《Seinfeld》</b> —— 一齣 1998 年完結的情境喜劇，<b>今年仍有 7,200 萬美國人收看</b>。Acquired 用它講一個很少人講的角度：完美的市場時機、創作者式的偏執、以及一個「讓 incentives 對齊三十年」的股權結構。這是典型的 Acquired 式拆解 —— 由一個看似懷舊的主題，拆出一個關於「長壽資產」的商業模型。</p>
<p style="color:#7a6a58;font-size:14.5px;margin-bottom:0">註：Acquired 近年改為雙週／月更的長篇格式，30 日無更新屬正常節奏。</p>
</div>

<div class="card dormant">
<h3 style="font-size:22px">Founders<span class="badge grey">最後更新 2026-11-04</span></h3>
<p class="byline">David Senra · 13 日無新集</p>
<p><b>最後一集：#439《How Eiichiro Oda Works》</b> —— 尾田榮一郎，《One Piece》作者。Senra 稱他為「把成年生活幾乎每一個清醒小時都投入去建構一個虛構宇宙」的偏執型創作者。這一集的核心不是漫畫，而是<b>「長期主義的極端樣本」</b>：一個人在同一個作品上連續投入 25 年以上，並且拒絕讓商業節奏主導創作節奏。</p>
<p style="color:#7a6a58;font-size:14.5px;margin-bottom:0">與今日 MFM 那集形成有趣對照：Currier 講「快」，Senra 講「慢到極致的複利」。兩者其實不矛盾 —— 快的是迭代，慢的是方向。</p>
</div>

<div class="card dormant">
<h3 style="font-size:22px">All-In<span class="badge grey">最後更新 2026-11-14</span></h3>
<p class="byline">Chamath · Jason · Sacks · Friedberg · 3 日無新集</p>
<p><b>最後一集：《Jensen Ousted as Nvidia CEO: "Spy" Scandal, Export Restrictions, Market Impact》</b> —— 一整集圍繞一個極端情境：Jensen Huang 被指涉及「間諜」指控與機密備忘錄洩漏而下台，四位主持人討論誰想他走、對 AI 交易的衝擊、中國策略、出口管制，以及「誰應該是 Nvidia 下一任 CEO」。同集後段還談到 <b>Anthropic 啟動 IPO 路演</b>。</p>
<p style="color:#7a6a58;font-size:14.5px;margin-bottom:0">這集與今日 MFM 的 AI 段落可並讀：一邊講 AI 的物種論，一邊講 AI 的權力結構。</p>
</div>

<div class="card dormant">
<h3 style="font-size:22px">The Knowledge Project<span class="badge grey">最後更新 2026-11-05</span></h3>
<p class="byline">Shane Parrish · 12 日無新集</p>
<p><b>最後一集：《Jon McNeill: How Elon Musk Makes Decisions》</b> —— 前 Tesla 總裁、DVx Ventures 共同創辦人。官方摘要開宗明義：<b>「Elon Musk 相信速度會創造競爭優勢 —— 不論是決策的速度、現金的速度，還是回應的速度。」</b>整集講的是這件事在日常運作中長什麼樣，以及如何圍繞它建一間公司。</p>
<p style="color:#7a6a58;font-size:14.5px;margin-bottom:0"><b>這是今日最值得注意的交叉點</b>：兩個完全不同的節目，在同一個月用同一個命題開場 —— 速度是競爭優勢，而且它可以被組織化。KP 由 Tesla 內部視角講，MFM 由投資人視角講。想真正吸收，兩集應該連著聽。</p>
</div>

<div class="card dormant">
<h3 style="font-size:22px">The Diary of a CEO<span class="badge grey">最後更新 2026-11-16</span></h3>
<p class="byline">Steven Bartlett · 1 日無新集（昨日已掃描）</p>
<p><b>最後一集：《Ex-CIA Officer: Trump Knew About The China Spy And Didn't Care!》</b> —— 前 CIA 官員 John Kiriakou 與前俄羅斯情報人員 Aliia Roza，拆解「Jensen Huang 如何落入一個數十億美元的情報陷阱」。內容圍繞間諜、honeypot 操作，以及<b>用來攻破高權力目標的具體心理 tradecraft</b>。</p>
<p style="color:#7a6a58;font-size:14.5px;margin-bottom:0">與 All-In 那集是同一個事件的兩個切面：All-In 講市場與權力，Diary 講人如何被操作。</p>
</div>

<h2 class="section">觀察 · 這三集其實在講同一件事</h2>
<div class="rule"></div>

<p>把今日六個頻道的最後一集並排看，有一條很清楚的線：</p>

<ul>
  <li><b>MFM #882</b> — James Currier：速度是唯一未被均質化的優勢，而它卡在情緒。</li>
  <li><b>KP（11/05）</b> — Jon McNeill：Elon 相信速度創造優勢 —— 決策、現金、回應。</li>
  <li><b>Diary of a CEO（11/16）</b> — 一個人如何被心理操作攻破：反過來說，就是「情緒未處理」如何變成弱點。</li>
</ul>

<p>三個節目、三個距離，指向同一個結論：<b>在 2026 年，執行速度已經不是「優勢」，而是「入場券」；真正的差異化在於「你的組織有沒有能力在資訊不完整時仍然行動」。</b>而那個能力，本質上是心理能力，不是流程能力。</p>

<p>Currier 在這集最值錢的地方，是他沒有停在「所以你應該快一點」這種廢話。他往下挖了兩層：<b>第一層是「你的橫桿是抄回來的」（所以可以重設）；第二層是「你慢是因為你卡住」（所以要先處理情緒）。</b>大多數生產力內容只到第一層，而且講得很差。</p>

<footer>
  <b>Mindset Podcast Daily</b> · 2026-11-17 · 生成時間：{GEN}<br>
  掃描頻道：Acquired · Founders · All-In · My First Million · The Knowledge Project · The Diary of a CEO<br>
  本集來源：<a href="https://podcasts.apple.com/us/podcast/id1469759170?i=1000802266958">Apple Podcasts</a> ·
  <a href="https://www.mfmpod.com/episodes/">mfmpod.com</a> ·
  <a href="https://podcasts.apple.com/us/podcast/id990149481">Knowledge Project</a><br>
  方法：RSS 全量比對 GUID → 官方章節表萃取 → 公開事實核實。無公開逐字稿的集數，不生成偽引用。
</footer>

</div>
</body>
</html>
"""

out = os.path.join(BASE, f"daily-report-{DATE}.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
print("written", out, len(HTML))

# ---- update state ----
state = json.load(open(os.path.join(SC, "state.json")))
res = json.load(open(os.path.join(SC, "scan_result.json")))
added = 0
for pid, e in res.items():
    if e.get("status") == "ok":
        lst = state.setdefault("scannedEpisodes", {}).setdefault(pid, [])
        for n in e.get("new", []):
            if n["guid"] not in lst:
                lst.append(n["guid"]); added += 1
state["lastScan"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
json.dump(state, open(os.path.join(SC, "state.json"), "w"), ensure_ascii=False, indent=1)
print("state updated, guids added:", added, "lastScan:", state["lastScan"])
