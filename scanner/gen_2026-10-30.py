#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime, os

now = datetime.datetime.now(datetime.timezone.utc)
hk = now + datetime.timedelta(hours=8)
STAMP = now.strftime("%Y-%m-%d %H:%M UTC")
HKT = hk.strftime("%Y-%m-%d %H:%M")

HEAD = r'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>思維播客日報 · 2026-10-30</title>
<style>
  :root{
    --bg:#fdfaf6; --ink:#2b2419; --muted:#7a6a58; --line:#e8ddcd;
    --card:#fffdf9; --accent:#b07a2a; --accent-soft:#f6ecd9; --ok:#3f7d5a; --warn:#a4442f;
  }
  *{box-sizing:border-box}
  body{
    margin:0; background:var(--bg); color:var(--ink);
    font-family:Georgia,"Noto Serif SC","Songti SC",serif;
    line-height:1.85; font-size:17px;
  }
  .wrap{max-width:860px;margin:0 auto;padding:48px 24px 80px}
  header{border-bottom:2px solid var(--ink);padding-bottom:26px;margin-bottom:8px}
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
  .stat .l{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:11px;letter-spacing:.08em;
    color:var(--muted);margin-top:7px}
  .lede{font-size:20px;line-height:1.9;margin:0 0 26px}
  .lede em{font-style:normal;background:linear-gradient(transparent 62%, #f4e3c4 62%)}
  .note{background:var(--accent-soft);border-left:3px solid var(--accent);padding:18px 22px;
    font-size:15.5px;color:#5d4a30;margin:0 0 46px;font-family:-apple-system,"Helvetica Neue",sans-serif;line-height:1.85}
  h2.section{font-size:13px;font-family:-apple-system,"Helvetica Neue",sans-serif;letter-spacing:.18em;
    text-transform:uppercase;color:var(--muted);font-weight:600;margin:56px 0 4px}
  .rule{height:1px;background:var(--ink);margin:0 0 30px}
  h3{font-size:26px;line-height:1.4;font-weight:normal;margin:0 0 6px}
  .byline{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:12.5px;color:var(--muted);margin-bottom:14px}
  .card{background:var(--card);border:1px solid var(--line);padding:28px 30px;margin:0 0 22px}
  .badge{display:inline-block;font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:10.5px;
    letter-spacing:.1em;padding:3px 9px;border-radius:2px;vertical-align:middle;margin-left:8px}
  .badge.none{background:#efe7db;color:#8a755c}
  .badge.new{background:#e6f0e9;color:var(--ok)}
  .badge.early{background:#f7e6d6;color:#a4632a}
  .badge.rep{background:#f3e2e2;color:var(--warn)}
  .ep{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:13.5px;color:var(--muted);
    padding:12px 0;border-top:1px dotted var(--line);border-bottom:1px dotted var(--line);margin:16px 0}
  .ep b{color:var(--ink)}
  .why{font-size:15.5px;color:#4c3f30;background:#faf5ec;padding:14px 18px;margin-top:6px;
    font-family:-apple-system,"Helvetica Neue",sans-serif;line-height:1.8}
  .why b{color:var(--accent)}
  table{width:100%;border-collapse:collapse;font-family:-apple-system,"Helvetica Neue",sans-serif;
    font-size:13.5px;margin:8px 0 18px}
  th{text-align:left;font-weight:600;color:var(--muted);font-size:11px;letter-spacing:.08em;
    text-transform:uppercase;border-bottom:1px solid var(--ink);padding:8px 10px 8px 0}
  td{border-bottom:1px solid var(--line);padding:11px 10px 11px 0;vertical-align:top}
  td.n{color:var(--accent);white-space:nowrap}
  blockquote{margin:18px 0;padding:2px 0 2px 20px;border-left:2px solid var(--accent);
    font-style:italic;color:#4a3d2d}
  blockquote .src{display:block;font-style:normal;font-family:-apple-system,"Helvetica Neue",sans-serif;
    font-size:11.5px;color:var(--muted);margin-top:8px;letter-spacing:.04em}
  .kickerline{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:12px;letter-spacing:.1em;
    text-transform:uppercase;color:var(--accent);margin:26px 0 6px;font-weight:600}
  .three{background:#fff;border:1px solid var(--line);padding:22px 26px;margin:0 0 30px}
  .three h4{margin:0 0 12px;font-size:15px;font-family:-apple-system,"Helvetica Neue",sans-serif;
    letter-spacing:.1em;text-transform:uppercase;color:var(--accent);font-weight:600}
  .three ol{margin:0;padding-left:20px;font-size:16px}
  .three li{margin-bottom:10px}
  .chapter{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:13px;color:#5d4a30;
    columns:2;column-gap:28px;line-height:2}
  .chapter span{display:block;break-inside:avoid}
  .chapter b{color:var(--accent);font-weight:600;display:inline-block;min-width:56px}
  .verdict{border-top:2px solid var(--ink);border-bottom:1px solid var(--line);padding:18px 0;margin:26px 0}
  .verdict p{margin:0;font-size:16.5px}
  .foot{margin-top:56px;padding-top:22px;border-top:1px solid var(--line);
    font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:12.5px;color:var(--muted);line-height:1.9}
  a{color:var(--accent);text-decoration:none;border-bottom:1px solid #e3cfa9}
  .num{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:12px;color:var(--accent);
    letter-spacing:.1em;font-weight:600}
  .flag{background:#fdf0ef;border-left:3px solid var(--warn);padding:14px 18px;margin:16px 0;
    font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:14.5px;color:#7d3122;line-height:1.8}
  @media(max-width:620px){
    .wrap{padding:32px 18px 60px} h1{font-size:30px} .stats{grid-template-columns:repeat(2,1fr)}
    .card{padding:22px 20px} body{font-size:16px} .chapter{columns:1}
  }
</style>
</head>
<body>
<div class="wrap">
'''

BODY = r'''
<header>
  <div class="kicker">Mindset Podcasts · Daily Deep Scan</div>
  <h1>每日思維播客深度掃描</h1>
  <p class="date">2026 年 10 月 30 日，星期五</p>
  <div class="meta">
    報告生成時間：<b>%%STAMP%%（香港時間 %%HKT%%）</b><br>
    掃描方式：6 條 RSS feed 並行抓取 XML，逐集比對 GUID 去重（<b>HTTP 200 × 6</b>）<br>
    Repo：<a href="https://github.com/JMOKSZ/mindset-podcasts">JMOKSZ/mindset-podcasts</a> · 本輪新增 GUID：<b>2</b><br>
    上一個掃描點：2026-10-29 09:56 UTC
  </div>
</header>

<div class="stats">
  <div class="stat"><div class="n">6</div><div class="l">掃描播客</div></div>
  <div class="stat"><div class="n">2</div><div class="l">新集數</div></div>
  <div class="stat"><div class="n">6/6</div><div class="l">Feed 正常</div></div>
  <div class="stat"><div class="n">84<span style="font-size:16px">分</span></div><div class="l">可量時長合計</div></div>
</div>

<p class="lede">今日兩集，表面一集講生意、一集講婚姻，但其實係同一件事：<em>默認規則（default）永遠唔會站在你嗰邊。</em>WHOOP 唔接受「硬件公司就係每 12 個月賣一次機」嘅默認，改成訂閱制；Sexton 唔接受「婚姻嘅財產規則由州議會寫」嘅默認，改成自己寫。<em>兩個人都係喺「未有事之前」就把規則定好——呢個就係佢哋真正賣嘅嘢。</em></p>

<div class="note">
  <b>今日覆蓋率：</b>2 / 6 有新集數。<b>六條 feed 全部 HTTP 200</b>，冇抓取失敗。<br>
  <b>一個要講清楚嘅 caveat：</b>Diary of a CEO 呢集 <b>唔係新訪談</b>，係 2026 年 2 月 12 日 James Sexton 完整集數嘅「Most Replayed Moment」重播剪輯（28 分 16 秒）。我照樣做完整萃取，但會明確標示邊啲係原集內容、邊啲係剪輯包裝——唔會當成新料賣你。<br>
  <b>本日最值錢嘅一句：</b>Sexton 講婚前協議——「你已經有一份婚前協議，問題只係由州議會寫，定由你同佢寫。」呢句搬去生意，就係<p style="margin:8px 0 0">「你已經有一套商業規則，問題只係由平台、房東、大客寫，定由你寫。」</p>
</div>

<h2 class="section">Ep.1 · All-In Interview</h2>
<div class="rule"></div>

<div class="card">
  <h3>WHOOP CEO, Will Ahmed: 50B Hours of Health Data, a 4 Million Member Data Moat, &amp; the FDA Fight<span class="badge new">NEW</span></h3>
  <div class="byline">All-In with Chamath, Jason, Sacks &amp; Friedberg · 主持 Jason Calacanis · 嘉賓 Will Ahmed（WHOOP 創辦人兼 CEO）</div>

  <div class="ep">
    <b>上線：</b>2026-10-29 21:26 UTC（香港 10/30 05:26）　<b>時長：</b>55 分 39 秒　<b>形式：</b>單人深度訪談（非週五四人 roundtable）
  </div>

  <p><b>主題：</b>呢集唔係「運動手環評測」，而係一份<b>硬件公司轉訂閱制嘅完整帳簿</b>：點解要放棄 $500 一次性收入、點樣令 400 萬人平均每日戴 23.6 小時、50 億小時生理數據可以換到咩、以及一間 private company 點樣同 FDA 打一場「呢個究竟係 wellness 定 medical device」嘅定義戰。</p>

  <p><b>嘉賓：</b>Will Ahmed，WHOOP 創辦人兼 CEO。2012 年創立，哈佛本科生時期做咗大量心率變異度（HRV）研究——當時學界知道 HRV 有意義，但冇辦法 24/7 量度，呢個空隙就係 WHOOP 嘅起點。公司做咗 14 年，現時約 <b>1,200 名員工</b>、<b>400 萬會員</b>；Jason 喺節目入面用自己的說法形容公司「估值 100 億美元、年收入約 10 億」——<b>呢兩個數字係主持人口徑，唔係財報數字</b>，我照樣標示出處，唔當事實。</p>

  <div class="kickerline">核心論點 · 順住章節走</div>

  <p><span class="num">01</span> <b>Growth curve：12 年、18 個月、6 個月（01:54）</b>——Ahmed 自己講：「用咗大約 12 年到 100 萬會員，然後大約 18 個月到 200 萬，大約 6 個月到 300 萬，今年底預計 400 萬。」呢條曲線嘅重點唔係「爆發」，而係<b>爆發之前嘅 12 年</b>。一款要 24/7 戴住嘅產品，前十年基本上係喺度等「佩戴率」呢個變數發酵——而佩戴率係冇得買嘅。</p>

  <p><span class="num">02</span> <b>$500 硬件 → 訂閱制（03:12）</b>——2017 年面向消費者時係一次性 $500。一年後觀察到兩件事：<b>買咗嘅人戴得好耐</b>（穿戴業最難嘅留存，佢哋反而係強項），但<b>買嘅人唔夠多</b>。於是 2018–19 年改成 $15–$30/月、硬件成本內含。呢個決定嘅真正影響唔係收入模型，而係<b>公司 DNA</b>：一旦你係訂閱公司，你 obsession 嘅對象由「新客」變成「現有會員」，指標由出貨量變成 churn、engagement、同「有冇真係改變到行為」。</p>

  <p><span class="num">03</span> <b>硬件公司嘅隱藏激勵（05:08）</b>——全集最值得抄落嚟嘅一段。Ahmed 講：硬件公司<b>被激勵每 12 個月出一代新機，無論有冇真正創新</b>，因為你總要收下一筆硬件錢；而且你冇誘因喺舊機上面加功能，因為你要說服人買新機。訂閱公司啱啱相反：<b>硬件要 step function 咁好先出，其餘時間全部用軟件更新舊機</b>。所以一個 18 個月前入會嘅會員，之後陸續得到 ECG、AFib 偵測、advanced labs（驗血）、healthspan（WHOOP age）、blood pressure insights。呢個就係「同一件硬件，不斷升值」嘅結構。</p>

  <p><span class="num">04</span> <b>23.6 小時／日，50 億小時（06:59 &amp; 19:28）</b>——平均每位會員每日戴 <b>23.6 小時</b>，累積<b>超過 500 億小時連續生理數據</b>，「one of the largest health data sets in the world」。呢個數字嘅意義唔係大，而係<b>連續</b>：14 日電量 + 滑蓋充電（戴住叉電），令佢哋拿到嘅係一條唔斷嘅時間序列，而唔係每日幾十個 sample。所有後面嘅 baseline、trend、異常偵測，都建基於呢一點。</p>

  <p><span class="num">05</span> <b>由「量度」升級到「預測」（19:31–20:54）</b>——佢哋自己訓練 foundation models（唔係租 frontier model），而且開始出現一個好關鍵嘅訊號：<b>有跡象可以透過生理訊號，預測某個 biomarker 超標，而唔需要直接量度嗰個 biomarker</b>。例如估你皮質醇高，就叫你去驗某一項。呢個係由「wearable」跳去「triage layer」——唔係取代醫生，而係決定你應該去驗咩。呢個定位比「健康助手」值錢得多。</p>

  <p><span class="num">06</span> <b>Journal：100+ 行為，>50% 每日記錄（23:50）</b>——WHOOP Journal 有 100 幾種行為（酒精、水份、旅行、冥想、情緒、補充品…），超過一半會員每日填。加上 <b>80% 會員有用 AI coach</b>、<b>每日開 app 8 次</b>。Ahmed 嘅講法係：如果你要寫一個「預測一個人開唔開心」嘅演算法，你必須要有大量情緒標籤——而呢啲標籤係會員自己免費提供嘅。呢個就係佢口中嘅 data moat：<b>唔係感測器，係「人願意每日答問題」呢個習慣</b>。</p>

  <p><span class="num">07</span> <b>Behavioral insights 嘅實際數字（26:16–29:35）</b>——Jason 即場讀自己嘅 report：暖水浴 <b>+7% recovery</b>、酒精 <b>−9%</b>、遲食（睡前 3 小時內）係全體會員最傷睡眠嘅行為之一、一日入面高壓力區間佔比 +1% 就 <b>−9% recovery</b>、strain +5 就 recovery −5。Ahmed 亦提醒：呢啲係<b>相關性</b>，唔係因果——例如「維他命 D −3」可能只係因為你旅行嗰幾日食咗。呢個誠實位好重要：一間賣數據洞察嘅公司，肯喺自己節目講「呢個可能係 false positive」。</p>

  <p><span class="num">08</span> <b>GLP-1 tracker（32:40）</b>——佢哋加咗 GLP-1 追蹤，原因唔係潮流，而係一個具體風險：<b>食 GLP-1 減重，大約一半係脂肪、一半係肌肉</b>，所以好多人瘦得快但變得虛弱。WHOOP 嘅介入係：知道你食 GLP-1 → 推你步行（例如 9,800 步）、每週兩次力量訓練、補水、蛋白質、creatine。呢個係「穿戴裝置做行為處方」嘅最好例子：<b>唔係話你知數據，而係因為數據而改你嘅行程。</b></p>

  <p><span class="num">09</span> <b>FDA 之戰：定義權就係產品權（34:57–41:00）</b>——血壓呢個 signal，傳統上被歸類為「必須係醫療器材」。WHOOP 認為血壓同時影響壓力、睡眠、整體健康，所以有一條清楚的 wellness lane。佢哋先做咗一個 <b>70,000 人</b>嘅 stress / sleep / blood pressure 研究（會員每日上傳血壓讀數），訓練出算法，然後推出 blood pressure insights。FDA 發 warning letter，公開爭議。結果：<b>FDA 後來更新指引，承認血壓可以有 wellness 應用</b>，feature 今日仍然在。同時，佢哋嘅 ECG 係正正經經走 510(k)  cleared。呢個「兩條腿走路」——有些產品走醫療審批、有些走 wellness——係醫療科技公司最實際嘅監管路線圖。</p>

  <p><span class="num">10</span> <b>Build vs Partner vs Buy（41:53）</b>——Jason 挑機：你 100 億估值、10 億收入，點解唔直接買 Omron、自己做血壓計同體重秤？Ahmed 答：血壓袖帶係相對商品化（commoditized）嘅技術，而且有醫療效力要求，所以佢哋選擇合作（用袖帶做 calibration，之後由 WHOOP 無袖帶量度），目標係<b>取代袖帶</b>，唔係賣袖帶。判斷標準好清楚：<b>呢樣嘢係我嘅核心 IP，定係我嘅 calibration 工具？</b>後者就唔應該自己造。</p>

  <p><span class="num">11</span> <b>「你唔係產品」（42:24）</b>——Ahmed 明講：「We do not sell data. You are not the product, Jason. The membership is the product.」呢句係同 Google / Apple 嘅商業模式直接對照：一邊賣廣告同賣硬件，一邊賣訂閱。佢嘅講法係「我哋 earned the right to accumulate this data，因為我哋有好強嘅 data policy」。你自己判斷呢句有幾多成係真、幾多成係 positioning——但至少佢肯喺節目上講到咁白。</p>

  <p><span class="num">12</span> <b>LeBron 同「唔付錢買運動員」（47:31–50:08）</b>——今日宣布 LeBron James 成為全球大使。關鍵細節：<b>LeBron 已經戴咗 11 年，係史上第一批 100 個用戶之一，而且一直冇正式合約</b>。Ahmed 嘅原則係：如果你未到做大眾廣告嘅階段，就唔應該付錢叫人用你產品——「You want people to love your product authentically」，更何況 24/7 佩戴，「冇任何金額可以令我說服一個唔喜歡嘅運動員戴住瞓覺」。呢個係一個好清楚嘅早期市場策略：<b>先要 ICP 真心用，之後才談 NIL（name, image, likeness）</b>。</p>

  <p><span class="num">13</span> <b>Lightning round（44:44–47:00）</b>——幾個可以直接抄嘅立場： podcast 影響力揀 <b>Huberman</b>（但 Bryan Johnson「推高咗大家對『應該量度咩』嘅想像」）；冷浴 vs 凍水涼，揀<b>凍水涼</b>，因為「accessible，人人每日做得到，30–60 秒就夠」；紅光治療 vs 桑拿，揀<b>桑拿</b>，並直說「紅光嗰樣係 marketing nonsense」；有氧 vs 重訓，對 40 歲以上，「<b>應該舉多啲鐵，少啲 elliptical</b>，因為肌肉量係長壽嘅重要指標」；咖啡，佢自己<b>即刻飲</b>，唔等 90 分鐘；三個分數入面最在意 <b>recovery</b>。</p>

  <div class="kickerline">關鍵引用（逐字，出自本集 transcript）</div>

  <blockquote>
    “It took about 12 years for us to get to a million members and then another 18 months or so to 2 million, about six months to 3 million and we expect to end the year around 4 million members.”
    <span class="src">— Will Ahmed，01:54</span>
  </blockquote>

  <blockquote>
    “When you're a hardware business, you're incentivized to ship new hardware every 12 months, whether or not it's actually innovative because you always need that next dollar from a hardware sale.”
    <span class="src">— Will Ahmed，05:38</span>
  </blockquote>

  <blockquote>
    “On average, a WHOOP member wears WHOOP 23.6 hours a day. And as a consequence, we have just over 50 billion hours of continuous physiological data.”
    <span class="src">— Will Ahmed，19:28</span>
  </blockquote>

  <blockquote>
    “Through physiological signals, we might be able to predict that a biomarker is out of range without actually measuring the biomarker itself.”
    <span class="src">— Will Ahmed，20:27</span>
  </blockquote>

  <blockquote>
    “We do not sell data. You are not the product, Jason. The membership is the product.”
    <span class="src">— Will Ahmed，42:24</span>
  </blockquote>

  <blockquote>
    “You want people to love your product authentically. … There's no amount of money I'm going to be able to pay an athlete to wear something 24-7 if they don't like it.”
    <span class="src">— Will Ahmed，49:16</span>
  </blockquote>

  <div class="kickerline">對 James 嘅意思</div>
  <div class="why">
    呢集有三樣可以直接搬去任何訂閱／服務型生意：<br>
    <b>① 檢查你嘅收入模型有冇偷偷獎勵「唔創新」。</b>一次性收費 → 你靠「出新版」賺錢；訂閱 → 你靠「令舊客繼續用」賺錢。同一個產品，兩種模型會養出兩種完全唔同嘅公司。你而家嘅收費方式，獎勵緊你做邊件事？<br>
    <b>② Data moat 唔係「你收集到幾多」，而係「人願唔願意繼續答你問題」。</b>WHOOP 最強嘅資產係 >50% 會員每日填 journal、80% 用 AI coach、一日開 8 次 app。呢個係習慣，唔係技術。你手上嘅客戶關係，有冇一個「每日／每週必答」嘅儀式？<br>
    <b>③ 監管／平台規則係可以談嘅，但你要有數據。</b>WHOOP 打得贏 FDA 嘅定義戰，靠嘅係 70,000 人研究數據 + 公開堅持，唔係靠公關。你同平台、房東、大客嘅「默認條款」有冇得談？有——但你要先有自己嘅數據同替代方案。
  </div>
</div>

<h2 class="section">Ep.2 · The Diary of a CEO</h2>
<div class="rule"></div>

<div class="card">
  <h3>Most Replayed Moment: Why You Need A Prenup And How To Avoid Divorce!<span class="badge rep">重播剪輯</span></h3>
  <div class="byline">The Diary of a CEO · Steven Bartlett · 嘉賓 James Sexton（紐約離婚律師）</div>

  <div class="ep">
    <b>上線：</b>2026-10-30 06:00 UTC（香港 14:00）　<b>時長：</b>28 分 16 秒　<b>原集：</b>2026-02-12 完整訪談
  </div>

  <div class="flag">
    <b>先講清楚：</b>呢集係「Most Replayed Moment」——DOAC 將 2 月完整集數入面最多人重播嘅婚前協議段落重新剪出嚟，加新包裝再上架。所以你會聽到 Steven 用「我朋友」舉例、Sexton 用 M&amp;M 糖果做示範，全部都係原集內容。以下萃取混合咗<b>剪輯描述</b>同<b>原集 transcript</b>，我逐句標明來源，唔會當成 10 月新訪談。
  </div>

  <p><b>主題：</b>婚前協議唔係「唔信任」嘅證明，而係<b>一份由你主動寫嘅規則集</b>。Sexton 嘅核心命題好簡單：你無論如何都會有一份婚前協議——問題只係由州議會寫（默認），定由你同伴侶寫（自訂）。而大部分人不願意談，唔係因為唔需要，而係因為<b>怕講出口等於承認可能會散</b>。</p>

  <p><b>嘉賓：</b>James Sexton，紐約執業超過 25 年嘅離婚律師，專門代表高資產客戶（運動員、企業家）。著作《If You're in My Office, It's Already Too Late》。佢喺原集講自己收費 <b>每小時 1,000 美元</b>，並直認「我終日喺法庭做嘅嘢，就係工程化（或防止被工程化）陪審團同法官嘅觀感」。</p>

  <div class="kickerline">核心論點</div>

  <p><span class="num">01</span> <b>婚前協議係「最唔賺錢」嘅業務（原集 24:xx）</b>——Steven 問：「你作為一個靠拆散人賺錢嘅律師，你覺得婚前協議令婚姻更長久？」Sexton 答：「係。因為呢個係我哋最唔賺錢嘅嘢做。婚前協議而家基本上自動化，我睇到一個未來：AI 就做得嚟。」呢個自白好關鍵——<b>賣預防嘅人，永遠賺得少過賣補救嘅人</b>。佢自己都係靠補救賺錢，所以佢嘅建議有對價關係，你要自己打折聽。</p>

  <p><span class="num">02</span> <b>你已經有一份婚前協議（原集 25:xx）</b>——「It'll either be written by the state legislature or it'll be written by you and she. Who do you trust more?」然後佢用 DMV 做比喻：你去監理處排隊，會唔會覺得「呢班人真係好，應該由佢哋管我段婚姻」？呢個比喻粗暴但有效：<b>默認規則係由一班你唔認識、而且會換人嘅人寫嘅。</b>你唔講，就等於默認接受。</p>

  <p><span class="num">03</span> <b>「怕講」本身就係答案（原集 25:xx）</b>——「If you'd be scared to mention a prenup to your partner, then you should definitely mention a prenup to your partner. Because what that means is I'm afraid to have a hard conversation.」呢句係全集最可操作嘅一句。佢嘅邏輯係：婚姻之後一定會拋大量「難對話」畀你（錢、小朋友、照顧父母、病、失業），如果連呢一個都講唔出口，你唔係唔需要協議，你係<b>未準備好結婚</b>。</p>

  <p><span class="num">04</span> <b>信任係雙向嘅（原集 26:xx）</b>——如果對方話「你唔信我」，Sexton 嘅反問係：「咁你係咪都唔信我？你係咪唔信我哋會對對方公平？」佢嘅結論：<b>你哋唔係互相防範，你哋係共同防範一個「規則由第三方設定」嘅未來。</b>呢個 reframing 好重要——把「我 vs 你」變成「我哋 vs 默認制度」。</p>

  <p><span class="num">05</span> <b>邊個真正找數（原集 27:xx）</b>——Steven 講朋友嘅個案：離婚打咗七年，兩邊律師對打，<b>佢仲要付前妻嘅律師費</b>。Sexton 確認：「有presumption（推定）——高收入一方要負責低收入一方嘅合理法律費用。」所以「唔簽協議」唔係「慳返律師費」，而係<b>將律師費變成一個你控制唔到嘅開放式負債</b>。佢自己都講：「我有客戶付過幾百萬。」</p>

  <p><span class="num">06</span> <b>專家估價戰爭（原集 28:xx）</b>——呢段係全集技術含量最高。離婚時如果涉及私人公司，雙方可以各自請「partisan expert」（有立場嘅估值專家），一邊負責<b>抬高</b>、一邊負責<b>壓低</b>。Sexton 嘅比喻：「煙草公司都請到醫生 testify 話吸煙有益。」玩法有兩種：<b>攻擊數據</b>（你用錯數據）或者<b>攻擊結論</b>（數據啱但結論錯）。而估值係 speculative——所以同一間公司可以有兩個天差地遠嘅價。如果法官信「值 10 億」，你要付 5 億，<b>即使你手上冇 5 億現金</b>——可以用「distributive award」分多年付。呢個就係「wealth can quietly vanish on paper」嘅真正機制：<b>唔係資產消失，而係估值被重新定義。</b></p>

  <p><span class="num">07</span> <b>律師嘅誘因（原集 29:xx）</b>——Steven 直接問：「咁樣唔係對你有利？拖長嚟做？」Sexton 答：「係。放大衝突、拖長、拉鋸。而且我終日操縱人嘅情緒——你以為我唔可以用呢個能力作惡？」但佢跟住補一個更真實嘅機制：<b>呢行係靠聲譽存活</b>。「最好嘅律師，係可以賺幾百萬但最後用一萬蚊律師費就 settle 咗單案。」因為一旦你被認定係「煽風點火」嗰種，市場會記住。<b>呢個係一個好好嘅商業課：短期可以靠資訊不对称賺錢，長期只能靠聲譽。</b></p>

  <p><span class="num">08</span> <b>M&amp;M 三個桶（原集 31:xx）</b>——Sexton 用糖果示範婚姻財產結構：<b>你嘅、我嘅、我哋嘅</b>。結婚前各自嘅嘢係 separate property；結婚後共同賺／共同買嘅入「we」桶；一旦「commingling（混同）」——例如將婚前物業嘅租金存入聯名戶口——就好難拆返。無婚前協議 = 所有嘢都有可能被納入「we」，然後要 identification、valuation、division 三重工程。</p>

  <p><span class="num">09</span> <b>時間懸崖（原集 33:xx–35:xx）</b>——佢講咗幾個「 cliff」：某些州（佢點名加州）有 7 年後資產性質改變嘅講法；紐約則係一旦 commingle 就麻煩；贍養費公式亦會隨婚姻年期跳級（例如 20 年）。結果係<b>人會計時</b>：有人等到 20 年先入紙，有人趕喺 6 年半就走。佢亦警告唔好喺協議入面寫 sunset clause（例如「10 年後自動失效」），因為嗰樣嘢會令你喺第 9 年半開始問「我係咪想賭落去」——<b>一個設計出嚟嘅 deadline，會反過來改變你嘅行為。</b>（法律細節各州不同，呢度係佢節目上嘅講法，唔係法律意見。）</p>

  <p><span class="num">10</span> <b>速限比喻（原集 35:xx）</b>——「政府一定要揀一個數字。55 咪合法，56 咪犯法。56 同 55 有好大分別咩？冇。但佢哋要揀一個數。」所以問題唔係「呢個數合唔合理」，而係<b>「你信唔信由佢哋幫你揀？」</b>呢個係一個通用嘅制度經濟學問題：所有默認規則都係任意嘅，但後果唔任意。</p>

  <p><span class="num">11</span> <b>真正嘅建議：每週三分鐘（原集 43:xx）</b>——被問「如果只做一個儀式，令伴侶最大機會留低」，Sexton 答：<b>每星期寫低／講三樣你欣賞對方嘅事，而且每星期都唔同。</b>進階版係花五分鐘講「呢三樣嘢點解令我覺得被愛」。然後佢用達賴喇嘛嘅故事收尾：「如果你想內心平靜，每日冥想 15 分鐘。」行政人員話「我冇 15 分鐘」。達賴喇嘛答：「咁你冥想一個鐘。」——<b>你唔肯花 5 分鐘維護關係，你將來要花幾百個鐘補救。</b></p>

  <p><span class="num">12</span> <b>最深一層：恐懼（原集 45:xx）</b>——講到點解人明知有用都唔做，Sexton 話：「我哋唔係怕關係嘅未來，我哋係怕自己唔值得被愛。最深嘅恐懼係：如果你睇到我真正嘅樣——所有軟弱、自私、黑暗——你唔可能愛我。所以你愛嘅只係我扮演嘅角色。」呢段係全集唯一離開法律、直插人心嘅位置，亦解釋咗為何「婚前協議」呢個話題咁易觸發情緒：<b>它逼你承認，你同對方都係有可能離開嘅人。</b></p>

  <div class="kickerline">關鍵引用（原集 transcript 逐字）</div>

  <blockquote>
    “You have a prenup. It’ll either be written by the state legislature or it’ll be written by you and she. Who do you trust more?”
    <span class="src">— James Sexton，原集「The Case for Prenuptial Agreements」段</span>
  </blockquote>

  <blockquote>
    “If you’d be scared to mention a prenup to your partner, then you should definitely mention a prenup to your partner. Because what that means is I’m afraid to have a hard conversation with my partner.”
    <span class="src">— James Sexton，同上</span>
  </blockquote>

  <blockquote>
    “A prenup is not a referendum on the likelihood of us breaking up. A prenup is not a commentary on how much we trust each other. … A prenup is a rule set.”
    <span class="src">— James Sexton，M&amp;M 示範段</span>
  </blockquote>

  <blockquote>
    “There’s a presumption that the higher earning individual should be responsible for the reasonable legal fees of the less earning spouse.”
    <span class="src">— James Sexton，講「邊個找數」</span>
  </blockquote>

  <blockquote>
    “The cigarette companies had doctors who were willing to testify that cigarettes are good for you. Like, you can find an expert to say almost anything if you pay them enough.”
    <span class="src">— James Sexton，講 dueling experts（估值專家對打）</span>
  </blockquote>

  <div class="kickerline">對 James 嘅意思</div>
  <div class="why">
    呢集表面講婚姻，實際上係一份<b>「默認條款審計」</b>，三樣可以直接搬：<br>
    <b>① 你身上有幾多份「別人幫你寫嘅合約」？</b>公司註冊章程、平台服務條款、租約、供應商合約、甚至你嘅僱傭合約。你冇談過嘅條款，就係默認條款。Sexton 嘅問題搬過去：「你信唔信由佢哋幫你揀個數？」<br>
    <b>② 「怕講」係一個診斷工具，唔係一個障礙。</b>如果你唔敢同某個人（伴侶、合夥人、大客）講某件事，嗰件事就係你最需要講嘅事。你而家避緊邊個對話？<br>
    <b>③ 估值可以被重新定義，所以「帳面富貴」唔等於「可支配」。</b>離婚只係其中一個場景；合夥拆伙、融資、稅務、遺產都一樣。真正嘅安全邊際係<b>現金流同結構</b>，唔係估值。
  </div>
</div>

<h2 class="section">最近無更新 · 四台狀態</h2>
<div class="rule"></div>

<div class="card">
  <h3>最近無更新<span class="badge none">NO UPDATE</span></h3>
  <p>以下四台今日 feed 正常（HTTP 200），但最新一集嘅 GUID 已在 <code>state.json</code> 記錄，即係<b>冇漏抓，只係真係冇新集</b>。</p>

  <table>
    <tr><th>播客</th><th>最後一集</th><th>日期</th><th>距今</th></tr>
    <tr>
      <td><b>Acquired</b></td>
      <td><a href="https://www.acquired.fm/episodes/seinfeld">Seinfeld</a><br><span style="color:#7a6a58">3 小時 50 分（13,820 秒）</span></td>
      <td class="n">10 月 18 日</td><td>12 日</td>
    </tr>
    <tr>
      <td><b>Founders</b></td>
      <td><b>#438 James Garfield’s Extraordinary Rise</b></td>
      <td class="n">10 月 26 日</td><td>4 日</td>
    </tr>
    <tr>
      <td><b>My First Million</b></td>
      <td><b>Ex-Amazon VP tells us what it’s really like working with Jeff Bezos</b></td>
      <td class="n">10 月 28 日</td><td>2 日</td>
    </tr>
    <tr>
      <td><b>Knowledge Project</b></td>
      <td><a href="https://fs.blog/knowledge-project-podcast/outliers-kc-irving/">[Outliers] K.C. Irving: How to Build an Empire on Your Own Terms</a></td>
      <td class="n">10 月 29 日</td><td>1 日</td>
    </tr>
  </table>

  <div class="why">
    <b>值得留意嘅節奏：</b>All-In 休息咗 6 日之後，噚日一次過出咗一集 55 分鐘嘅單人訪談（WHOOP），今日就輪到 DOAC 出重播。兩台同時「唔做常規節目」——All-In 由週五 roundtable 轉做 interview special，DOAC 由新訪談轉做 best-of。呢個通常係季中調整（美國選舉週＋感恩節前夕），唔係異常，但可以預期下週新內容密度會偏低。<br>
    <b>Knowledge Project 要記住：</b>K.C. Irving 嗰集仍然係會員優先，公開日期 <b>11 月 3 日</b>。你今日想聽就要入會；唔急就等下星期二。<br>
    <b>Acquired 12 日：</b>正常。佢一集做 3–4 小時研究，兩至三星期出一集係一貫節奏。
  </div>
</div>

<h2 class="section">兩集交叉 · 同一個命題</h2>
<div class="rule"></div>

<div class="three">
  <h4>默認規則與自訂規則</h4>
  <ol>
    <li><b>WHOOP（商業版）</b>——默認：硬件公司每 12 個月賣一次機。自訂：訂閱制，硬件只在 step function 時更新，其餘靠軟件令舊機升值。<b>結果：公司嘅激勵由「說服你買」變成「說服你留」。</b></li>
    <li><b>Sexton（關係版）</b>——默認：婚姻財產規則由州議會寫，離婚時由兩邊律師同專家估價對打。自訂：結婚前坐低寫一份「你嘅、我嘅、我哋嘅」規則集。<b>結果：衝突由「法庭上打」變成「餐桌上講」。</b></li>
    <li><b>共同結構</b>——兩者都係<b>喺未有事之前，用一個低成本嘅動作，換走一個高成本嘅未來</b>。WHOOP 用每月 $15–30 換走「買機焦慮」；Sexton 用幾千蚊律師費換走「幾百萬訴訟」。而兩者嘅阻力都一樣：<b>人唔願意為「唔會發生嘅事」付錢。</b></li>
  </ol>
  <p style="margin:14px 0 0;font-size:15.5px;color:#5d4a30"><b>拉遠一層：</b>呢個就係上一份報告（10 月 29 日）Paine 講嘅「負面目標」——政府最重要嘅工作因為冇發生，所以永遠冇人見到。今日兩集係同一個道理嘅微觀版：<b>你最好嘅決定，通常係一件「冇發生嘅災難」；而正因為冇發生，你永遠唔會知道自己慳咗幾多。</b></p>
</div>

<div class="verdict">
  <p><b>如果今日只聽一集：</b>聽 <b>All-In × WHOOP</b>（55 分鐘）。佢係一份完整嘅「訂閱制經濟學 + 數據護城河 + 監管策略」教材，而且有具體數字。<b>如果今日只想學一個概念：</b>記住 Sexton 嗰句——「你已經有一份婚前協議，問題只係邊個寫。」然後問自己：你生意入面，邊份合約係「州議會寫嘅」？</p>
</div>

<h2 class="section">今日一句</h2>
<div class="rule"></div>

<blockquote style="font-size:20px;line-height:1.95">
  “A prenup is a rule set.”
  <span class="src">— James Sexton。今日兩集都係講同一件事：你唔寫規則，規則就會寫你。WHOOP 寫咗訂閱制嘅規則，Sexton 叫你寫婚姻嘅規則——分別只在於，一個寫喺 term sheet，一個寫喺餐桌上。</span>
</blockquote>

<div class="foot">
  <b>報告生成：</b>%%STAMP%%（香港時間 %%HKT%%）<br>
  <b>掃描範圍：</b>6 條 RSS feed，全部 HTTP 200；本輪新增 2 集，新增 GUID 已寫入 <code>scanner/state.json</code>。<br>
  <b>新增 GUID：</b><br>
  　· All-In — <code>25ed3987-a02b-434e-8a71-ed74bad8e863</code><br>
  　· Diary of a CEO — <code>flightcast:01M4BFEBPEK1CKAKZ2BYPSHPK1</code><br>
  <b>資料來源：</b>各台 RSS（show notes 全文）、Apple Podcasts episode metadata（iTunes lookup API）、All-In 全集 transcript（podscripts.co 公開轉錄）、Diary of a CEO 原集 transcript（singjupost.com 公開轉錄，2026-02-12 集）。<br>
  <b>誠實標注：</b>① 所有引號內文字均出自上述公開 transcript 或官方 show notes，冇虛構對白；框架解釋與「對 James 嘅意思」屬分析，唔係嘉賓原話。② All-In 集數入面「100 億估值 / 10 億收入」係主持 Jason Calacanis 嘅口頭描述，唔係公司財報，報告內已標明。③ DOAC 呢集係 2 月完整訪談嘅重播剪輯，唔係新訪談，已於卡片頂部標示。④ Sexton 提到嘅「7 年 community property」「20 年贍養費跳級」等屬美國個別州嘅講法，各州法律不同，唔構成法律意見。<br>
  <b>前置過濾：</b>Jev（TypeSafe）評分：All-In <b>1.18</b>（business）、DOAC <b>0.25</b>。該 profile 按「新聞價值」設計，唔適用於用戶主動訂閱嘅播客；DOAC 低分正好對應「重播剪輯、非新訪談」呢個事實，已在報告內明確標示，兩集均保留。
</div>
</div>
</body>
</html>
'''

html = HEAD + BODY.replace("%%STAMP%%", STAMP).replace("%%HKT%%", HKT)
out = "/root/.openclaw/workspace/mindset-podcasts/daily-report-2026-10-30.html"
open(out, "w", encoding="utf-8").write(html)
print("wrote", out, len(html), "bytes")
