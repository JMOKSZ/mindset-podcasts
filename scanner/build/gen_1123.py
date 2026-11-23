# -*- coding: utf-8 -*-
import io, os

OUT = "/root/.openclaw/workspace/mindset-podcasts/daily-report-2026-11-23.html"

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
  blockquote p:last-child{margin:0}
  table{width:100%;border-collapse:collapse;margin:26px 0 34px;
    font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:13.5px}
  th{text-align:left;padding:11px 10px;border-bottom:2px solid var(--ink);font-size:11px;
    letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600}
  td{padding:12px 10px;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.55}
  td.num{font-variant-numeric:tabular-nums;white-space:nowrap}
  .pill{display:inline-block;padding:2px 8px;border-radius:10px;font-size:11px;
    font-family:-apple-system,"Helvetica Neue",sans-serif;letter-spacing:.06em}
  .pill.ok{background:#e7f0e9;color:#33684b}
  .pill.warn{background:#f8e6e1;color:#8f3a26}
  .pill.due{background:#fdf0d8;color:#8a5c14}
  ul,ol{margin:0 0 20px;padding-left:24px}
  li{margin-bottom:9px;line-height:1.75}
  .ts{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:13px;color:var(--accent);
    font-variant-numeric:tabular-nums}
  .ts b{color:#3a2f21;font-weight:600}
  .closing{border-top:2px solid var(--ink);margin-top:58px;padding-top:24px}
  .closing p{font-size:16.5px}
  footer{margin-top:60px;padding-top:20px;border-top:1px solid var(--line);
    font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:11.5px;color:var(--muted);line-height:1.9}
  a{color:#8a5c14}
  strong{font-weight:600}
  .kicker2{font-family:-apple-system,"Helvetica Neue",sans-serif;font-size:11px;letter-spacing:.2em;
    text-transform:uppercase;color:var(--accent);margin:0 0 8px;font-weight:600}
  @media(max-width:640px){
    .stats{grid-template-columns:repeat(2,1fr)}
    h1{font-size:31px} .card{padding:22px 20px} .wrap{padding:32px 18px 60px}
    table{font-size:12.5px} th,td{padding:9px 7px}
  }
"""

BODY = r"""
<div class="wrap">
<header>
  <div class="kicker">Mindset Podcast Daily · 六台深掃</div>
  <h1>思維播客日報</h1>
  <p class="date">2026 年 11 月 23 日 · 星期一</p>
  <div class="meta">
    掃描時間 <b>2026-11-23 09:54 UTC</b> · 六個 RSS feed 全部 HTTP 200 · 新增集數 <b>1</b><br>
    上一份報告 <b>2026-11-22</b>（全體零新集）· 今日唯一新集：Diary of a CEO × Steve Eisman（1:34:16）<br>
    萃取方式：官方 VTT 逐字稿全文 1,522 段逐段核對，數據與引文均出自原話，非節目簡介改寫
  </div>
</header>

<div class="stats">
  <div class="stat"><div class="n">6</div><div class="l">FEEDS 掃描</div></div>
  <div class="stat"><div class="n">1</div><div class="l">新增集數</div></div>
  <div class="stat"><div class="n">94</div><div class="l">新集分鐘</div></div>
  <div class="stat"><div class="n">35</div><div class="l">ACQUIRED 靜默日數</div></div>
</div>

<p class="lede">今日只有一台開閘，但呢一集抵得上一個星期。《The Diary of a CEO》搵嚟 <em>Steve Eisman</em>——2008 年次貸爆煲前做空、被寫入《The Big Short》嗰個人。佢今次唔係講「AI 有泡沫」咁簡單，而係直接指控 Anthropic 同 OpenAI 高層<b>合謀製造「世界末日」恐慌，去換取監管護城河</b>，順手把中國嘅 open-weight 模型擋在國門外。呢個講法喺主流財經媒體幾乎冇人敢用「conspiracy」呢個字。</p>

<div class="note">
<b>今日一句話：</b>Eisman 嘅框架唔係「AI 會唔會爆」，而係<b>「AI 已經大到不能倒，所以佢嘅生與死由政治決定，唔由市場決定」</b>。佢自己講：<b>如果 Anthropic 同 OpenAI 聽日破產，美國後日就衰退</b>——而美國 GDP 增長有一半以上就係 AI 資本開支。同一集裡面，佢仲順手拆咗 crypto 對沖論、買樓致富論，同埋「AI 會消滅所有工」嘅恐嚇。呢集係今年六台入面<b>反共識密度最高</b>嘅一集。
</div>

<h2 class="section">Tonight's main feature · 今晚主菜</h2>
<div class="rule"></div>

<div class="card">
  <p class="kicker2">The Diary of a CEO · Episode 5656</p>
  <h3>Financial Crash Expert: Biggest Money Mistake You'll Make, Everyone Gets This Wrong!</h3>
  <div class="byline">主持 Steven Bartlett · 嘉賓 Steve Eisman（前 FrontPoint 基金經理、現 Substack／YouTube 財經教育）</div>

  <dl class="epmeta">
    <dt>發佈</dt><dd>2026-11-23 06:00 UTC（香港時間 14:00）</dd>
    <dt>時長</dt><dd>1 小時 34 分 16 秒</dd>
    <dt>體裁</dt><dd>長篇對談 + 3 段廣告（約 6 分鐘，已標示）</dd>
    <dt>核心</dt><dd>AI 泡沫的集中度風險 · 監管護城河陰謀論 · 普通人理財</dd>
    <dt>連結</dt><dd><a href="https://podcasts.apple.com/us/podcast/financial-crash-expert-biggest-money-mistake-youll/id1291423644?i=1000803534789">Apple Podcasts</a></dd>
  </dl>

  <h4 class="sub">一句話總結</h4>
  <p>一個靠「睇穿誘因」起家的人，用同一副眼鏡看 2026 年的 AI：<b>唔係睇技術，係睇邊個收錢、幾時收、收完之後邊個埋單。</b>佢嘅結論有兩個層次——短線，他覺得泡沫味很濃但唔敢肯定（中期選舉令他改了口）；長線，他覺得 AI 係真技術，但 <b>2026 年嘅 AI 交易同 1999 年嘅互聯網交易，句式一模一樣</b>。</p>

  <h4 class="sub">嘉賓係邊個，為什麼要聽他講</h4>
  <p>Eisman 1990 年代在 Oppenheimer 做金融服務分析師，2000 年代初轉去 FrontPoint Partners 管理對沖基金。2007 年他研究次貸證券化，發現整條產業鏈（貸款仲介、投行、CDO 經理）全部按「量」而非「質」收費，於是用信用違約互換（CDS）做空。2008 年爆煲，基金賺約 10 億美元，他個人分到約 1 億。這段經歷被 Michael Lewis 寫進《The Big Short》，電影裡由 Steve Carell 飾演。</p>
  <p>但今日這一集之所以有重量，唔係因為「他預言過一次」。而係因為他<b>把 2008 年的方法論完整搬過來用了一遍</b>，包括：先找出誘因錯位在哪、再問「損失幾時才出現」、最後才問價格。他在節目中段明講：「次貸嘅教訓對今日冇咁重要，達康泡沫才是更重要的教材。」這是一個很刻意的選擇——他要講的是<b>泡沫的形狀</b>，不是銀行的形狀。</p>

  <h4 class="sub">全集骨架（帶時間碼，可直接跳聽）</h4>
  <table>
  <thead><tr><th style="width:74px">時間</th><th>段落</th><th>重點</th></tr></thead>
  <tbody>
  <tr><td class="ts">00:00</td><td>開場暴擊</td><td>三句定調：破產即衰退、史上最大單一行業、Sam Altman 的末日論「utter nonsense」</td></tr>
  <tr><td class="ts">02:20</td><td>我們在泡沫裡嗎</td><td>「我傾向是」→ 但中期選舉後「我唔肯定咗」</td></tr>
  <tr><td class="ts">04:13</td><td>拉斯維加斯那頓飯</td><td>次貸鏈條全貌：FICO 650 以下、年發 6,000 億、CDO「冇嘢好管理」</td></tr>
  <tr><td class="ts">09:36</td><td>Big Short 到底做咗乜</td><td>用買保險解釋 CDS：7 億名義、3% 成本、賺 10 億</td></tr>
  <tr><td class="ts">14:08</td><td>達康泡沫才是真教材</td><td>Henry Blodget 與「王朝級財富」；第一代全死、第二代收割基建</td></tr>
  <tr><td class="ts">17:05</td><td>AI 公司真的賺錢嗎</td><td>拆 ARR、token maxing、Uber 三個月燒完 AI 預算</td></tr>
  <tr><td class="ts">20:48</td><td>整個鏈只靠兩間公司</td><td>Nvidia 70% 收入來自五個客戶；Oracle 後台 50% 來自 OpenAI</td></tr>
  <tr><td class="ts">26:01</td><td>市場有幾多綁在 AI</td><td>Infotech 佔 S&P 40%（史無前例）→ 廣義 65%</td></tr>
  <tr><td class="ts">30:31</td><td>中期選舉改變了什麼</td><td>政治接管：數據中心審批變成逐鎮逐州的政治</td></tr>
  <tr><td class="ts">41:43</td><td>AI 公司沒有護城河</td><td>「唔需要開奔馳去買餸，踩單車得」</td></tr>
  <tr><td class="ts">43:38</td><td>末日論是不是合謀</td><td>核心指控：製造恐慌 → 換監管 → 用監管排除中國模型</td></tr>
  <tr><td class="ts">57:41</td><td>現在買什麼</td><td>四個月的 short-against-the-box；持股清單</td></tr>
  <tr><td class="ts">59:29</td><td>一千美元怎麼用</td><td>買指數、定期買、然後假裝忘記密碼</td></tr>
  <tr><td class="ts">01:00:36</td><td>永不碰 crypto 與黃金</td><td>論證：資產走勢與自己的論點完全相反</td></tr>
  <tr><td class="ts">01:09:12</td><td>現在該不該買樓</td><td>「Don't buy that house」；租 + 投入股市</td></tr>
  <tr><td class="ts">01:14:01</td><td>投資原則</td><td>管理層不誠實就跑；CoreWeave 創辦人減持 30 億</td></tr>
  <tr><td class="ts">01:20:21</td><td>給 18 歲的自己</td><td>能力傾向（aptitude）> 行業光環</td></tr>
  <tr><td class="ts">01:24:33</td><td>喪子與憤怒</td><td>1996 年 Max 之死；憤怒如何變成做空華爾街的燃料</td></tr>
  <tr><td class="ts">01:30:44</td><td>妻子 Valerie 的信</td><td>全場最靜的 40 秒</td></tr>
  </tbody>
  </table>

  <h4 class="sub">論點一：泡沫的形狀——達康，唔係次貸</h4>
  <p>Eisman 明確拒絕用 2008 年類比今日。理由很技術：2008 年是<b>銀行體系</b>的問題（擠兌、槓桿、連鎖違約），監管者被迫救；2026 年如果是 AI 泡沫爆破，<b>銀行唔會有事</b>——他講得很白：「銀行會好好，因為監管好得多、槓桿低得多。我完全唔擔心銀行。」所以殺傷力不同：一次是金融系統心臟病，一次是某個行業的深度衰退。</p>
  <p>他搬出的是 1995–2002 年。當年所有關於互聯網的樂觀句子，今天可以逐句套用在 AI 上；結果是大部分第一代公司破產，但<b>基建留了下來</b>，由 Google 這批第二代公司免費用。他的原話是：「他們唔需要為基建付錢，因為錢已經有人付過。」這句話是整集的樞紐：如果你同意，你就會得出「AI 技術會贏，但這批 AI 公司未必」的結論。</p>
  <blockquote>
    <p>“Everything that is being said about AI — just line up all the sentences of the people who are very positive — they are the exact same sentences that people said about the internet when it was going crazy.”</p>
    <cite>— Steve Eisman，約 <span class="ts">00:15:21</span></cite>
  </blockquote>
  <p>他同時修正了一個流行的錯覺：達康爆煲對普通人影響其實不大，因為那時消費者信貸一直健康，「消費者一次都冇失手」，NASDAQ 科技股則平了五六年。言下之意——<b>今次不同，因為今次綁住的是 GDP 同實體建設</b>，唔止是股價。</p>

  <h4 class="sub">論點二：整個產業鏈只靠兩間公司（集中度風險）</h4>
  <p>這一段是全集的數據心臟，也是他認為最被市場低估的地方。邏輯鏈是這樣：</p>
  <ol>
    <li><b>Nvidia</b> 是全球市值最大公司，最近一季收入同比增長超過 100%——「你同我講一間十億市值公司增長 100%，我會話唔錯；你話地球上最大嘅公司增長超過 100%，我會話難以置信。」但同一份 10-Q 寫明：<b>70% 收入來自五個客戶</b>，而這五個客戶就是超大規模雲商。</li>
    <li>反過來，<b>Microsoft、Amazon、Google 目前產生的 AI 收入中，70% 來自 Anthropic 同 OpenAI</b>——即這兩間初創在「付錢給」雲商。</li>
    <li>換算下來，這相當於三間雲商<b>雲端收入的 25–30%</b>，而雲端是他們最重要的業務之一。</li>
    <li>再看 Oracle：總後台訂單 <b>6,000 億美元，其中 50% 來自 OpenAI 一間</b>。他補了一個非常具體的市場事故：Oracle 去年公布後台由近乎零跳到 3,500 億，股價由 230 升至 330；幾日後有人發現全部來自 OpenAI 的（幾張）訂單，股價跌回 230，現在 130，至今未復原。</li>
  </ol>
  <p>然後是那個令他「瞪大眼」的數字：Anthropic 在 S-1 招股書裡披露，公司已作出 <b>8,950 億美元的承諾</b>（主要給晶片與雲端供應商）。他的反應是：「這間公司幾年前根本不存在。」</p>
  <blockquote>
    <p>“If Anthropic and OpenAI went bankrupt tomorrow, the U.S. would go into a recession the next day.”</p>
    <cite>— Steve Eisman，約 <span class="ts">00:29:04</span>，全集第一句與此段重複強調</cite>
  </blockquote>
  <p>他自己也知道這句話聽起來太戲劇化，所以補了機制：這兩間一旦違約，承諾消失 → 雲商與 Nvidia 減少訂單 → 數據中心建設停 → 相關 GDP 直接扣減。<b>「如果是一千億，唔係大問題；但這是一兆。」</b></p>

  <h4 class="sub">論點三：Infotech 佔 S&P 40%，史無前例</h4>
  <p>他給了一個很紮實的橫截面：S&P 500 分 11 個行業，<b>單單 Infotech 就佔 40%</b>；「美國歷史上從來冇任何一個行業這麼大，之前最高大約 25%。」</p>
  <p>但真正可怕的是他接著做的加法——因為 2010 年代 GICS 重新分類，Amazon 被移到非必需消費、Google 同 Meta 被移到通訊服務，所以「科技」的真實敞口被系統性低估：</p>
  <table>
  <thead><tr><th>加總層</th><th class="num">佔 S&P 比重</th><th>說明</th></tr></thead>
  <tbody>
  <tr><td>Infotech（官方分類）</td><td class="num">40%</td><td>Nvidia、Dell、Salesforce 等</td></tr>
  <tr><td>＋ Google／Amazon／Meta</td><td class="num">≈ 50%</td><td>被移出科技分類的三巨頭</td></tr>
  <tr><td>＋ 公用事業</td><td class="num">＋3%</td><td>為數據中心供電的主力</td></tr>
  <tr><td>＋ 投行／另類資管</td><td class="num">—</td><td>為整條鏈融資</td></tr>
  <tr><td>＋ 工業（GE Vernova、Eaton）</td><td class="num">—</td><td>發電與電氣化設備</td></tr>
  <tr><td><b>廣義 AI 敞口</b></td><td class="num"><b>≈ 65%</b></td><td>只剩醫療保健與必需消費「同 AI 完全無關」</td></tr>
  </tbody>
  </table>
  <p>他那句收尾很刻薄也很準：「換句話講，藥同廁紙同 AI 冇任何關係。」而這 65% 的估值，全部立在同一個故事上。</p>

  <h4 class="sub">論點四：資本強度逆轉——雲商由「現金機器」變成「要集資」</h4>
  <p>這是我認為全集最容易被忽略、但對估值影響最大的一段。Eisman 指出：Amazon、Microsoft、Google 本來是「地球史上最賺錢的公司，賺現金賺到唔知點算」。但因為 AI 數據中心建設太貴：</p>
  <ul>
    <li><b>Google 現金流已經轉負</b>；<b>Amazon 現金流轉負</b>；<b>Microsoft 處於臨界</b>。</li>
    <li>所以他們要集資，而且不只發債，還<b>發股票</b>：Google 幾個月前增發 <b>850 億美元</b>股權——「你知道 Google 上一次增發股票係幾時？2005 年上市嗰次。」</li>
    <li>這代表定價權由企業轉移到<b>固定收益市場</b>手裡。他的原話：「你絕對唔想完全受制於固定收益市場，因為固定收益市場好善變。」</li>
  </ul>
  <p>他舉 CoreWeave 做例子：這類 neocloud 只做「借債 → 建數據中心 → 出租」，債務成本由 <b>9% 升到 15%</b>。「15 厘，你根本建唔起數據中心。」於是股票市場突然發現：這些公司不再掌握自己命運。</p>
  <p>但這裡有一個反直覺的推論，也是他今日最有趣的一個判斷：<b>如果 AI 數據中心建設放慢 10–20%，對某些公司反而是重大利好。</b>因為支出由一兆降到 2,500 億，他們會遲几年到達終點，但<b>現金流會重新轉正</b>，不再依賴債市。所以他說：「我覺得慢一點，其實更健康。唔係瘋狂地慢，係慢一點。」</p>

  <h4 class="sub">論點五：沒有護城河——「唔需要開奔馳去買餸」</h4>
  <p>他先定義護城河：一種是監管壁壘（小鎮唯一雜貨店，叫市長立法禁止第二家），一種是商業壁壘（Google 的演算法橫掃全球——「世界史上最大的護城河」）。然後他說，AI 模型公司兩種都沒有：</p>
  <ul>
    <li>中國的 open-weight 模型便宜得多，「你唔需要開奔馳去買餸，踩單車得」。</li>
    <li>用戶毫無忠誠度：「你用開 Claude，隔離有人出咗個新嘅，你就會試。」模型之間<b>可替換</b>。</li>
    <li>結果：Anthropic 的 S-1 裡，收入環比由 Q2 的 <b>+150%</b> 掉到 Q3 的 <b>+45%</b>。「大家睇 Q2 就話 wow，但你睇到 Q3 就知慢咗。」</li>
  </ul>
  <p>他因此說自己唔會買兩間公司的 IPO。但這裡有一個他自己也承認的張力：如果冇護城河，為什麼他仍然相信 AI 是真技術？他的答案是——<b>技術會贏，但利潤會被拉平</b>。這正是達康的劇本：基建與技術留下，第一批公司死掉。</p>

  <h4 class="sub">論點六：那個「陰謀論」——全集最高爭議度的 8 分鐘</h4>
  <p>Bartlett 問得直接：「你覺得這是合謀？」Eisman 答得更直接：「我腦海裡冇一絲懷疑。」</p>
  <p>他的推理是純粹的誘因分析，分五步：</p>
  <ol>
    <li>中國 open-weight 模型品質接近、成本約十分一。</li>
    <li>Anthropic 同 OpenAI 都在虧錢，打不起價格戰。</li>
    <li>所以他們需要一個<b>非價格</b>的壁壘。</li>
    <li>於是放話「世界會終結」→ 引發恐慌 → 迫使監管進場 → 再遊說監管者把中國模型排除在美國市場外。</li>
    <li>這就是<b>監管護城河</b>：在美國境內獨佔整個 AI 世界。</li>
  </ol>
  <blockquote>
    <p>“If I was Dario Amodei and I seriously thought that what I'm doing is going to end planet Earth, the next sentence out of my mouth would not be, how much of an allocation for my IPO can I give you?”</p>
    <cite>— Steve Eisman，約 <span class="ts">00:50:49</span></cite>
  </blockquote>
  <p>他拿出兩件具體證據支撐：第一，今年一眾 CEO（Sundar Pichai、Dario Amodei、Mark Zuckerberg、Greg Brockman、Elon Musk、Jensen Huang）到白宮與特朗普簽了一份文件，內容全部是「內部控制、外部審計、董事會監督委員會」——<b>他說這份文件「同世界終結完全無關」，只是公司治理</b>。第二，業界曾寫過一封叫「Pacing the Frontier」的聯署，但「寫完就冇跟進，寫封信，好大件事咩」。</p>
  <p>他的核心測試很簡單，也值得記住：<b>看行為，不看說話（watch what I do, not what I say）</b>。如果你真心相信自己在毀滅地球，你嘅下一個動作唔會是「IPO 配售可以給我幾多」。</p>

  <h4 class="sub">主持人三次反駁（這段是全集最好的張力）</h4>
  <table>
  <thead><tr><th style="width:38%">Bartlett 的反駁</th><th>Eisman 的回應</th></tr></thead>
  <tbody>
  <tr><td>他們仍在互相廝殺，對 Google 而言更是存亡之戰；搜尋眼見在崩。</td><td>讓步一半：搜尋並非崩盤，但增長由 Q1 的 19% 降到 12%；而且 AI 業務<em>遠不如</em>搜尋賺錢（「你唔可以在裡面放廣告」）。所以他同意 Google 需要救生艇，但補一句：「呢件事唔由得佢決定，係政治問題。」</td></tr>
  <tr><td>如果懷俄明州唔批，微軟就去佛州建，反正仍然會建。</td><td>接受這個反駁，但指出後果：機會變得更稀缺 → 更貴；而且 OpenAI 都要搶同一個佛州。「你啱啱損失咗兩年同好多錢。」他認為這是「慢」的來源，而慢是好事。</td></tr>
  <tr><td>你會唔會錯？錯在哪？</td><td>「會。」條件是<b>真正達到 AGI</b>。「我唔覺得我們接近。這些模型，以目前形態，係極優秀的詞語檢索模型，但連『思考』都稱唔上。」連 Hugging Face 的 agent 逃出沙盒事件，他都歸類為「詞語檢索，唔係思考」。</td></tr>
  </tbody>
  </table>

  <h4 class="sub">關鍵數據一覽（全部出自本集原話）</h4>
  <table>
  <thead><tr><th>指標</th><th class="num">數值</th><th>意義</th></tr></thead>
  <tbody>
  <tr><td>Infotech 佔 S&P 500</td><td class="num">40%</td><td>史上最大單一行業；之前峰值約 25%</td></tr>
  <tr><td>廣義 AI 相關敞口</td><td class="num">≈ 65%</td><td>加三巨頭、公用、金融、工業後</td></tr>
  <tr><td>Nvidia 前五大客戶佔收入</td><td class="num">70%</td><td>集中度極高</td></tr>
  <tr><td>三朵雲 AI 收入來自 A／O</td><td class="num">70%</td><td>等於其雲端收入 25–30%</td></tr>
  <tr><td>Oracle 後台訂單</td><td class="num">$6,000 億</td><td>50% 來自 OpenAI</td></tr>
  <tr><td>Anthropic S-1 承諾金額</td><td class="num">$8,950 億</td><td>公司成立僅數年</td></tr>
  <tr><td>Anthropic 收入環比</td><td class="num">+150% → +45%</td><td>Q2 → Q3 明顯減速</td></tr>
  <tr><td>美國 AI 資本開支</td><td class="num">≈ $1 兆／年</td><td>佔 GDP 增長一半以上</td></tr>
  <tr><td>Google 股權增發</td><td class="num">$850 億</td><td>2005 年 IPO 後首次</td></tr>
  <tr><td>CoreWeave 債務成本</td><td class="num">9% → 15%</td><td>「15 厘建唔起數據中心」</td></tr>
  <tr><td>CoreWeave 創辦人減持</td><td class="num">&gt; $30 億</td><td>公司市值僅 $240 億</td></tr>
  <tr><td>次貸年發行量</td><td class="num">$750 億 → $6,000 億</td><td>2002 → 高峰，靠不斷放寬審批</td></tr>
  <tr><td>Big Short 名義規模／成本</td><td class="num">$7 億 / 3%</td><td>約 $2,100 萬／年保費</td></tr>
  <tr><td>該基金獲利／他個人</td><td class="num">$10 億 / $1 億</td><td>20% 分成，摩根士丹利再分一半</td></tr>
  <tr><td>供樓總成本 vs 五年前</td><td class="num">+50%</td><td>按揭、保險、稅、雜費合計</td></tr>
  <tr><td>回購市場規模</td><td class="num">$3.5 兆</td><td>只用短期美債，是美債需求的底層理由</td></tr>
  </tbody>
  </table>

  <h4 class="sub">七句原文（可直接引用）</h4>
  <blockquote>
    <p>“All these people — the lenders, Wall Street, this guy — they were all incentivized on volume, not on quality. And so they were going to originate loans until planet Earth literally burned, which is exactly what they did.”</p>
    <cite>— 論次貸，約 <span class="ts">00:07:37</span>。他把這條總結成一句格言：<b>incentives trump ethics every time</b>（誘因永遠壓過道德）。</cite>
  </blockquote>
  <blockquote>
    <p>“I believe in AI as a technology, but I also believed in the internet as a technology. That didn't stop the dot-com bubble.”</p>
    <cite>— 約 <span class="ts">00:25:09</span>。這句是他整個立場的鑰匙：技術判斷與投資判斷是兩件事。</cite>
  </blockquote>
  <blockquote>
    <p>“As Senator Patrick Moynihan once said: facts change, I change.”</p>
    <cite>— 約 <span class="ts">00:25:56</span>，解釋為何中期選舉後他改了口。</cite>
  </blockquote>
  <blockquote>
    <p>“You don't need to take a Mercedes-Benz to the grocery store. You could take a bike.”</p>
    <cite>— 約 <span class="ts">00:43:15</span>，講中國廉價模型如何侵蝕付費模型的定價權。</cite>
  </blockquote>
  <blockquote>
    <p>“I have a great believer in watch what I do, not what I say.”</p>
    <cite>— 約 <span class="ts">00:51:25</span>，整集方法論的總結。</cite>
  </blockquote>
  <blockquote>
    <p>“You don't need to beat the market. Just if the market does really well, you'll be fine. People lose too much money looking for an edge.”</p>
    <cite>— 約 <span class="ts">01:12:48</span>，對普通投資者最實用的一句。</cite>
  </blockquote>
  <blockquote>
    <p>“When you're in the throes of grief, it's the first thing you think about every morning. And you know when it's starting to change is that one morning you wake up and it's the second.”</p>
    <cite>— 約 <span class="ts">01:27:44</span>，講 1996 年喪子之後的十幾年。</cite>
  </blockquote>

  <h4 class="sub">對普通人的四個結論（他自己給的，不是我的演繹）</h4>
  <ol>
    <li><b>一千美元怎麼用：</b>買 S&amp;P 500 指數，之後每隔一至三個月有餘錢就再買，然後「忘記佢」。「唔好試圖擇時，唔好賣出再買返，唔好交易，唔好掂期權。」如果承受得起波動，可以一半 S&amp;P、一半 NASDAQ 100。</li>
    <li><b>唔好買樓（現在）：</b>「Don't buy that house.」理由不是情緒，是算術——供樓總成本（按揭、保險、稅、雜費）比五年前貴約 50%，而五年前利率是零。加上鎖死的市場：現有業主背 3% 按揭，買家要付 7%，交易唔會發生。他認為未來幾年美國樓價<b>下跌的可能性大於上升</b>。他自己租樓：「有問題我打給大樓，他們修，唔使我錢。」</li>
    <li><b>唔好碰 crypto 同黃金：</b>crypto 的標準論點是「對沖法幣貶值／系統崩潰」，但如果論點成立，通脹差、利率升、NASDAQ 跌的日子，crypto 應該升。實際完全相反——Nvidia 升它升，Nvidia 跌它跌。「你有一個論點，而你嘅資產走勢同論點完全相反，咁即係 A：你嘅論點係 nonsense；B：呢個只係對 speculation 再 speculation。」他唯一讓步：穩定幣在支付系統可能有價值。</li>
    <li><b>如果要買 AI，買「鏟和鎬」：</b>網絡（Cisco、Arista）、伺服器（Dell、Supermicro）、電力（GE Vernova、Quanta）、電氣化（Eaton）、冷卻（Vertiv）。「我唔需要擔心邊個模型最好。」</li>
  </ol>

  <h4 class="sub">我聽完之後的三個觀察（分析，不是他的話）</h4>
  <p><b>一、他的「陰謀論」其實是一個可證偽的命題，但佢講得太滿。</b>可證偽的部分是：如果監管最終真的針對中國模型設限，而限制的受益者正好是兩間美國前沿實驗室，那他的誘因解釋就得到支持。但他把「所有 CEO 都真心相信末日」一筆勾銷，這一步是信念飛躍——他自己也承認「團隊裡有些人真的相信」。聽的時候要把這兩層分開：<b>誘因分析可以參考，動機審判要打折</b>。</p>
  <p><b>二、集中度那組數字，比「泡沫」兩個字有用得多。</b>因為它提供了一個具體的監測儀：Nvidia 的五大客戶佔比、三朵雲 AI 收入中 A／O 的佔比、Anthropic 承諾金額 vs 實際收入。當這三個數字任何一個開始惡化，就是鏈條鬆動的第一聲。這比預測「幾時爆」實際得多。</p>
  <p><b>三、他今天的立場其實已經從「看空」變成「看政治」。</b>注意他反覆說的是「我改了口」、「我唔肯定咗」、「關鍵是建設會慢幾多」。這不是一個做空者的語言，是一個<b>風險管理者</b>的語言——他四個月前已把大部分科技持倉做 short-against-the-box 對沖（因為直接賣要付 30–35% 稅），並且必須在明年一月底前平倉。換句話說，他已經把觀點落實成一個有到期日的倉位，而不是一個永久的預言。</p>

  <h4 class="sub">與本週其他集數的交叉點</h4>
  <p>11 月 20 日 All-In 那集（已掃）標題就叫「Anthropic Goes Public, Nvidia in Crisis, Markets Tank, Open Source Crackdown?」——同 Eisman 今日講的 three things 幾乎逐項對應：Anthropic 上市、Nvidia 的客戶集中、以及「open source crackdown」（即他所講的用監管排除中國模型）。<b>兩集放在一起聽，會得到一個相當完整的 2026 年 11 月 AI 資本市場橫切面</b>：All-In 講的是參與者視角（他們在局內），Eisman 講的是旁觀者兼做空者視角（他在局外收保費）。分歧點只有一個：All-In 認為集中度是「護城河與需求證明」，Eisman 認為是「單點故障」。</p>
</div>

<h2 class="section">Other shows · 其餘五台</h2>
<div class="rule"></div>
<p style="font-family:-apple-system,'Helvetica Neue',sans-serif;font-size:13.5px;color:#7a6a58;margin-bottom:24px">以下五台今日無新集。列出最後已知劇集，並附上真實發佈節奏（以最近 24 條間距計算中位數），方便你判斷下次幾時再開機。</p>

<div class="card">
  <h3>All-In <span class="badge grey">最近無更新</span></h3>
  <div class="byline">Chamath · Jason · Sacks · Friedberg · 每 2–3 日一更（中位 2.1 日）</div>
  <dl class="epmeta">
    <dt>最後一集</dt><dd>Anthropic Goes Public, Nvidia in Crisis, Markets Tank, Open Source Crackdown?</dd>
    <dt>發佈</dt><dd>2026-11-20（UTC 22:14）· 靜默 3 日</dd>
    <dt>下次預計</dt><dd>11/23–11/24（今日或明日）</dd>
    <dt>狀態</dt><dd><span class="pill due">已到期</span></dd>
  </dl>
  <p>三日靜默剛好壓在中位數上，加上今日是星期一，通常週末錄、週日／週一上架，所以今日之內出新集的機率不低。上一集主題與 Eisman 今日的論述高度重疊（見上文「交叉點」），若你只聽一集，建議先聽 Eisman（結構較完整），再回去聽 All-In 補參與者視角。</p>
</div>

<div class="card">
  <h3>My First Million <span class="badge grey">最近無更新</span></h3>
  <div class="byline">Sam Parr &amp; Shaan Puri · 每 2–3 日一更（中位 2.9 日）</div>
  <dl class="epmeta">
    <dt>最後一集</dt><dd>A recovering awkward person's guide to undeniable charisma</dd>
    <dt>發佈</dt><dd>2026-11-20 · 靜默 3 日</dd>
    <dt>下次預計</dt><dd>11/23–11/24</dd>
    <dt>狀態</dt><dd><span class="pill due">已到期</span></dd>
  </dl>
  <p>呢集係「魅力／社交能力」主題，屬 MFM 近期偏 soft-skill 的一條線（之前 11/18 前後亦有類似題材）。節奏上 MFM 幾乎逢星期一、四出貨，所以今日很大機會有新集。呢類題材與今日主菜的硬財經形成很好的配搭——一小時聽資本結構，一小時聽人際操作。</p>
</div>

<div class="card">
  <h3>Founders <span class="badge grey">最近無更新</span></h3>
  <div class="byline">David Senra · 每 7–9 日一更（中位 8.2 日）</div>
  <dl class="epmeta">
    <dt>最後一集</dt><dd>#440 The Most Inspiring Autobiography I've Ever Read: Born of This Land — Chung Ju-yung</dd>
    <dt>發佈</dt><dd>2026-11-17 · 靜默 6 日</dd>
    <dt>下次預計</dt><dd>11/24–11/27</dd>
    <dt>狀態</dt><dd><span class="pill ok">節奏正常</span></dd>
  </dl>
  <p>鄭周永（現代集團創辦人）自傳。呢集係 Senra 典型嘅「一手傳記 + 生平決策點」格式：由北韓農村少年走到造船、汽車、高速公路。節奏正常，未到期。如果你要補課，Founders 最值錢嘅從來唔係故事，而係他反覆問嘅那條問題——<b>這個人在資源匱乏時，選擇了什麼、放棄了什麼</b>。</p>
</div>

<div class="card">
  <h3>The Knowledge Project <span class="badge grey">最近無更新</span></h3>
  <div class="byline">Shane Parrish · 每 7–14 日一更（中位 8.8 日）</div>
  <dl class="epmeta">
    <dt>最後一集</dt><dd>Bing Gordon: Learning From Bezos, Jobs, and Spielberg</dd>
    <dt>發佈</dt><dd>2026-11-19 · 靜默 4 日</dd>
    <dt>下次預計</dt><dd>11/26 前後（多數星期四）</dd>
    <dt>狀態</dt><dd><span class="pill ok">節奏正常</span></dd>
  </dl>
  <p>Bing Gordon 是 Kleiner Perkins 前合夥人、EA 前 CCO，亦是 Amazon 早期董事——所以他同時見過 Bezos、Jobs、Spielberg 的工作方式。這集對「如何判斷創辦人」這個題目有直接參考價值，與今日 Eisman 講「管理層不誠實就跑」可以對照讀：一個講怎麼看人，一個講看到什麼就該走。</p>
</div>

<div class="card">
  <h3>Acquired <span class="badge grey">最近無更新</span></h3>
  <div class="byline">Ben Gilbert &amp; David Rosenthal · 月更（中位 31.4 日）</div>
  <dl class="epmeta">
    <dt>最後一集</dt><dd>Seinfeld</dd>
    <dt>發佈</dt><dd>2026-10-19（美西 10/18 21:00）· 靜默 35 日</dd>
    <dt>時長</dt><dd>3 小時 50 分</dd>
    <dt>狀態</dt><dd><span class="pill due">已超出中位</span></dd>
  </dl>
  <p>35 日靜默，略微超出 31.4 日的中位數（最近十個間距：35 / 35 / 49 / 35 / 15 / 1 / 19 / 41 / 35 / 43 日）。以 Acquired 的習慣，這種長度通常代表正在做大型研究集（他們過去做 Nvidia、Costco 這類集數時，間距也會拉到 40 日以上）。<b>所以這不是停擺，而是在煮大菜</b>。3 小時 50 分的 Seinfeld 一集仍未聽的話，這是全六台最長的單集，適合分段。</p>
</div>

<h2 class="section">Cadence board · 六台節奏</h2>
<div class="rule"></div>
<table>
<thead><tr><th>節目</th><th>最後一集</th><th class="num">日期</th><th class="num">靜默</th><th class="num">中位間距</th><th>下次預計</th></tr></thead>
<tbody>
<tr><td><b>Diary of a CEO</b></td><td>Steve Eisman</td><td class="num">11-23</td><td class="num">0 日</td><td class="num">3.0 日</td><td><span class="pill ok">11/26</span></td></tr>
<tr><td><b>All-In</b></td><td>Anthropic Goes Public…</td><td class="num">11-20</td><td class="num">3 日</td><td class="num">2.1 日</td><td><span class="pill due">已到期 · 隨時</span></td></tr>
<tr><td><b>My First Million</b></td><td>Charisma 指南</td><td class="num">11-20</td><td class="num">3 日</td><td class="num">2.9 日</td><td><span class="pill due">已到期 · 隨時</span></td></tr>
<tr><td><b>Founders</b></td><td>#440 鄭周永</td><td class="num">11-17</td><td class="num">6 日</td><td class="num">8.2 日</td><td><span class="pill ok">11/24–11/27</span></td></tr>
<tr><td><b>Knowledge Project</b></td><td>Bing Gordon</td><td class="num">11-19</td><td class="num">4 日</td><td class="num">8.8 日</td><td><span class="pill ok">11/26 前後</span></td></tr>
<tr><td><b>Acquired</b></td><td>Seinfeld</td><td class="num">10-19</td><td class="num">35 日</td><td class="num">31.4 日</td><td><span class="pill due">已超出 · 研究中</span></td></tr>
</tbody>
</table>
<p>六台合共 <b>2,986</b> 條歷史條目，GUID 全部已在 <code>state.json</code> 建檔。今日比對結果：<b>1 條未掃描</b>（Diary of a CEO 的 Eisman 集），其餘 2,985 條全部命中既有紀錄，無 feed 換 GUID、無重複計數。</p>

<div class="closing">
  <h4 class="sub" style="border:0;margin-top:0">今日三個可行動結論</h4>
  <p><b>1. 如果你持有 AI 相關股票，建立一個集中度儀表板。</b>三個數字每月看一次：Nvidia 前五大客戶佔比（現 70%）、三朵雲 AI 收入中 A／O 佔比（現 70%）、Anthropic 收入環比（現由 +150% 掉到 +45%）。任何一個明顯惡化，就是鏈條鬆動的第一聲，比任何「泡沫幾時爆」的預測可靠。</p>
  <p><b>2. 如果你想買 AI，但唔想赌邊個模型贏，走「鏟和鎬」。</b>Eisman 點名的類別：網絡（Arista、Cisco）、伺服器（Dell、Supermicro）、電力（GE Vernova、Quanta）、電氣化（Eaton）、冷卻（Vertiv）。判斷標準只有一條——<b>無論邊個模型贏，這些設備都要買</b>。</p>
  <p><b>3. 檢查你自己的「興奮句式」。</b>Eisman 最有用的一句不是關於 AI，而是關於語言：所有關於 AI 的樂觀句子，同 1999 年關於互聯網的句子逐字一樣。下次你聽到一句令你熱血沸騰的投資理由，問一句：<b>這句話在 1999 年是不是也有人講過？</b>如果係，就要問「今次邊一部分真係唔同」——而答案必須是具體數字，唔可以係「今次係真嘅」。</p>
</div>

<footer>
  報告生成時間 2026-11-23 09:54 UTC（香港時間 17:54）· 掃描器 <code>scanner/scan_fast.py</code> · 狀態檔 <code>scanner/state.json</code><br>
  資料來源：Diary of a CEO 官方 RSS（flightcast）＋ 官方 VTT 逐字稿 1,522 段全文核對；其餘五台為 RSS 最新條目比對<br>
  本報告只做內容整理與標註，不構成投資建議。所有引文均為節目原話；逐字稿為自動轉寫，人名拼寫已按公開資料校正。<br>
  Repo: github.com/JMOKSZ/mindset-podcasts
</footer>
</div>
"""

html = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>思維播客日報 · 2026-11-23</title>
<style>{CSS}</style>
</head>
<body>
{BODY}
</body>
</html>
"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with io.open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("wrote", OUT, len(html), "chars")
