#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = '/root/.openclaw/workspace/mindset-podcasts'
style = open('/tmp/style.html', encoding='utf-8').read()

DATE = '2026-10-13'
now_utc = '2026-10-13 09:53 UTC'
now_hkt = '2026-10-13 17:53'

state = json.load(open(os.path.join(BASE, 'scanner', 'state.json')))
scanned_total = sum(len(v) for v in state.get('scannedEpisodes', {}).values())
scan = json.load(open(os.path.join(BASE, 'scanner', 'scan_result.json')))
feed_counts = ' / '.join(str(scan[k]['count']) for k in
                         ['acquired', 'founders', 'all-in', 'my-first-million', 'knowledge-project', 'diary-of-a-ceo'])


def card_none(name, host, tag, last_title, last_date, dur, link, site, first_report, synopsis, note=''):
    return f'''
<!-- ==================== {name} ==================== -->
<section class="pod">
  <div class="pod-head">
    <h2>{name}</h2>
    <span class="host">{host}</span>
    <span class="tag none">{tag}</span>
  </div>
  <div class="callout">
    📭 本台今日（{DATE}）比對 <code>state.json</code> 後<b>無新集數</b>。所有已發佈集數 GUID 均已掃過。<br>
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

# ---------- Acquired ----------
cards += card_none(
    "Acquired", "Ben Gilbert &amp; David Rosenthal", "最近無更新",
    "The Home Depot", "2026-09-13", "3 小時 35 分（12,902 秒）",
    "https://www.acquired.fm/episodes/home-depot", "https://www.acquired.fm/episodes",
    "daily-report-2026-09-14.html",
    "Home Depot 創辦故事：Bernie Marcus 同 Arthur Blank 喺 48 歲同 35 歲畀人炒魷之後，聽咗紐約銀行家 Ken Langone（就係令佢哋被炒嗰個人）嘅一句話——「你哋係畀金馬蹄鐵踢中咗屁股」——然後寫下美國零售史上最強複利故事之一。官方描述形容成一部「Avengers 電影」：只要 Avengers 被炒、破產、再疊起十呎高嘅空油漆罐扮有貨。Sol Price 等傳奇人物陸續客串出場。",
    note="⚠️ Acquired 自 09-13 後未再有新集；本台更新節奏約每月 1–2 集（長篇研究型），下一集通常緊接大主題。")

# ---------- Founders ----------
cards += card_none(
    "Founders", "David Senra", "最近無更新",
    "#436 Ari Emanuel's Autobiography", "2026-10-05", "1 小時 9 分（4,185 秒）",
    "", "https://www.founderspodcast.com/",
    "daily-report-2026-10-06.html",
    "David Senra 讀 Ari Emanuel（Endeavor／WME 掌門人）自傳《Roll The Calls》（題目源自 Emanuel 家族格言「唔好等，主動打過去」）嘅讀書筆記。Senra 一貫做法：抽書中行動者嘅決策、野心同偏執，講一個經紀人點樣由收發室做到建立橫跨演藝、體育、時尚嘅娛樂帝國。本集由 Ramp、Applovin、Vanta 贊助。",
    note="ℹ️ Founders 為週更（多數星期一），#436 對應 10-05；至 10-13 仍未見 #437，或延至下週。")

# ---------- Knowledge Project ----------
cards += card_none(
    "The Knowledge Project", "Shane Parrish", "最近無更新",
    "Ryan Serhant: How to Get People to Say Yes", "2026-10-08", "—（Members 先行；公開 10-08）",
    "https://fs.blog/knowledge-project-podcast/ryan-serhant/", "https://fs.blog/knowledge-project/",
    "daily-report-2026-10-09.html",
    "Ryan Serhant（SERHANT. 創辦人、《Million Dollar Listing New York》／Netflix《Owning Manhattan》主角）講「唔令人覺得被推銷」嘅銷售法：先建立連結、先幫人、賺到開口請求嘅資格。核心係信任與關係資本，而非話術。",
    note="ℹ️ KP 目前 RSS 只有 20 集（滾動 feed），週四更新；下一集預料 10-15 前後。")

# ---------- Diary of a CEO ----------
cards += card_none(
    "The Diary of a CEO", "Steven Bartlett", "最近無更新",
    "AI Extinction Risk Expert: If Your Job Is Repetitive, AI Will Do It Better Than You! | Eric Weinstein",
    "2026-10-12", "1 小時 52 分 48 秒（6,768 秒）",
    "https://podcasts.apple.com/us/podcast/eric-weinstein-the-secret-alien-programs-nobody-is/id1291423644?i=1000795890178",
    "https://thediaryofaceo.com/", "daily-report-2026-10-12.html",
    "Eric Weinstein（哈佛數學物理博士、前 Thiel Capital 董事總經理、《The Portal》主持）嘅文明風險總體檢：五大框架「大睡眠／人工生命／學術守門／被管理嘅現實／線粒體模型」。佢主張真正威脅唔係 AI 本身，而係會自我複製、利用人性弱點抽取資源嘅「人工生命」；人類生存策略係互相依賴而非控制。",
    note="ℹ️ 此集已於 10-12 日報完整拆解（GUID 不變，標題被發行方由《The Secret Alien Programs…》改成《AI Extinction Risk Expert…》，故本輪不視為新集）。")


# ==================== All-In — NEW EPISODE DEEP DIVE ====================
allin = f'''
<!-- ==================== All-In with Chamath, Jason, Sacks & Friedberg ==================== -->
<section class="pod">
  <div class="pod-head">
    <h2>All-In with Chamath, Jason, Sacks &amp; Friedberg</h2>
    <span class="host">Chamath · Jason · Sacks · Friedberg</span>
    <span class="tag new">🆕 新集數</span>
  </div>

  <div class="ep-title">Martin Shkreli: Big Pharma's Blind Spot, Betting Against Quantum &amp; What Prison Taught Him</div>
  <div class="ep-meta">
    🗓 2026-10-12（15:49 UTC 發佈）· ⏱ 25 分 17 秒 · 🎙 嘉賓：<b>Martin Shkreli</b>（前對沖基金交易員／藥廠 CEO，圖靈製藥創辦人；2015 年因抬高藥價爭議被封「Pharma Bro」，後因證券詐騙入獄，2022 年出獄）<br>
    🎧 集頁：<a href="https://allinchamathjason.libsyn.com/martin-shkreli-big-pharmas-blind-spot-betting-against-quantum-what-prison-taught-him">Libsyn</a> ·
    <a href="https://podcasts.apple.com/us/podcast/martin-shkreli-big-pharmas-blind-spot-betting-against/id1502871393?i=1000795982205">Apple Podcasts</a>
  </div>

  <h3>🕒 官方章節（25 分鐘，四段）</h3>
  <div class="chapters">
    <span class="tc">(0:00)</span> Martin Shkreli 加入 Besties<br>
    <span class="tc">(0:55)</span> 為何量子電腦係「一招走天涯」生意、點解佢要做空呢個板塊<br>
    <span class="tc">(7:42)</span> 大型藥廠賣得太便宜嘅藥，同佢由對沖基金交易員到藥廠嘅路<br>
    <span class="tc">(11:37)</span> AI、藥物研發，邊個先係真正贏家<br>
    <span class="tc">(21:32)</span> 天才與破規矩、資優兒童陷阱，同監獄教識佢嘅事
  </div>

  <div class="callout" style="margin-top:16px">
    <b>一句話總結：</b>Shkreli 用 25 分鐘講咗兩個「反共識」大賭注 —— <b>① 量子電腦係商業騙局</b>（技術或許成立，生意唔成立），<b>② 真正威脅 Nvidia 嘅唔係另一粒晶片，而係「光」</b>（photonic matmul，光子矩陣乘法）。佢同時畀咗兩個「可證偽」預言：<code>20 年內今日嘅 AI 加速卡（H100/B100/B200）全部入廢鐵場</code>、<code>未來 10 年唔會出現任何一款由 AI 有效研發嘅藥</code>。
  </div>

  <!-- 主題一 -->
  <h3>🎯 主題一：量子電腦 =「一招走天涯」生意（佢做空緊）</h3>
  <div class="le-summary">
    <p><b>核心論點（唔係物理唔得，而係生意唔存在）：</b>Shkreli 指量子運算嘅思想源頭係 Peter Shor 嘅思想實驗（證明某些算法喺唔同計算介質跑得更快）。呢個係電腦科學嘅革命性想法，但<b>從來唔係一間公司嘅藍圖</b>。</p>
    <ul>
      <li><b>速度同範圍硬傷：</b>「現代量子電腦運行時鐘只有幾百至幾千赫茲，唔係 GHz；佢哋係單核、單線程。」對絕大多數日常工作（如 merge sort），量子機唔止慢——係更差。</li>
      <li><b>唯一真優勢：</b>把「整數分解」同「橢圓曲線離散對數問題」由指數時間降到多項式時間。對密碼學家係世界級大事；對生意人——除非你盤生意就係「分解數字」，否則<b>一文不值</b>。佢叫呢個做「書呆子史上最酷嘅魔法」。</li>
      <li><b>冇量子 RAM：</b>冇儲存 ⇒ 只能處理輸入極細嘅問題。</li>
      <li><b>錢嘅流向：</b>Google、IBM、Microsoft、NASA 各自每年擲數以億計美元，賭「將來或者有啲嘢出到嚟」。Shkreli 判詞：<i>「那唔係好生意。」</i></li>
      <li><b>佢自己嘅倉位：</b>做空量子股，<b>已經輸咗數以百萬計美元</b>。佢話同老婆講：「我們輸咗幾百萬，但我哋賺咗幾十億嘅 insight。」——經典「結構性做空」問題：睇啱方向，但時間點錯會被夾爆。</li>
    </ul>
    <blockquote>
      「Chelsea 同我試過全世界每一部量子電腦。我們無法喺任何一部上面計 300 × 200。」（Chelsea 為其妻，MIT 出身、曾與 Scott Aaronson 教授量子運算；其父為 Nvidia 早期員工）
      <cite>— Martin Shkreli, All-In (2026-10-12)，經 BigGo Finance 逐字轉引</cite>
    </blockquote>
  </div>

  <!-- 主題二 -->
  <h3>🎯 主題二：Nvidia 真正嘅敵人係「光」，唔係另一粒晶片</h3>
  <div class="le-summary">
    <p>Shkreli 用一個字重新框定成個 AI 熱潮：<b>matmul（矩陣乘法）</b>。GPU 一生 99.9% 時間都係做矩陣乘法，而且係 n³ 成本——喺 Nvidia 機器上乘兩個 1000×1000 矩陣要十億次運算。</p>
    <p><b>但喺「光」入面，matmul 近乎免費。</b>佢引用 Microsoft 喺《Nature》發表嘅模擬光學運算論文，同點名幾間做 photonic matmul 核心嘅初創：<code>Neurophos</code>、<code>Opticore</code>、<code>Lumai</code>。佢認為呢啲系統「可以將 Nvidia 而家做嘅嘢玩到團團轉」。Sam Altman 都公開講過光子運算可能係未來。Shkreli 話佢同老婆正研究緊係咪自己開一間。</p>
    <blockquote>
      「我真係覺得 20 年後，呢啲 H100 會喺廢鐵場。B100 喺廢鐵場。B200 喺廢鐵場。我們會搵到更好嘅方法。」
      <cite>— Martin Shkreli, All-In (2026-10-12)</cite>
    </blockquote>
    <p><b>但佢好小心，唔叫 Nvidia 做空：</b>因為 <b>Jevons 悖論</b>（效率提升往往令總需求上升而非下降）短期會贏——佢引 Alex Wang 講「Jevons 會帶來百萬倍運算改善」。然而佢放唔低一個威脅：<i>「如果出現一個效率高一千倍嘅 transformer，對 NVIDIA 就係壞事，毫無疑問。我們唔會有百萬倍需求。」</i></p>
    <p><b>矛盾正正係當前時刻嘅寫照：</b>推 Nvidia 股價上歷史高位嘅同一股力量，最終可能毀掉佢嘅生意——<b>效率，而唔係競爭，才係真正敵人。</b></p>

    <h4>📊 Shkreli 對各玩家嘅判讀（原始表，逐格翻譯）</h4>
    <table class="kv">
      <tr><th>玩家</th><th>Shkreli 嘅讀法</th></tr>
      <tr><td>Nvidia</td><td>短期做多；Jevons 悖論成立，但「效率高 1000 倍嘅 transformer」係真實威脅</td></tr>
      <tr><td>光子初創（Neurophos / Opticore / Lumai）</td><td>最有可能長期取代 GPU 嘅 matmul 方案</td></tr>
      <tr><td>Meta</td><td>現有玩家入面位置最好——分發 + 產品執行力</td></tr>
      <tr><td>OpenAI</td><td>硬件對沖做得好；永遠會有最好嘅模型</td></tr>
      <tr><td>量子運算股票</td><td>做空；一條算法、冇儲存、冇商業模式</td></tr>
    </table>
  </div>

  <!-- 主題三 -->
  <h3>🎯 主題三：4000 億美元砸入 AI，贏家未必係你想像嗰啲</h3>
  <div class="le-summary">
    <ul>
      <li><b>佢做多 AI，但質疑邊個真正攞到價值。</b>佢用互聯網做類比：唯一保證嘅贏家係消費者同企業（免費資訊入咗口袋），基建公司只分到成個價值創造嘅一小撮。</li>
      <li><b>約 4,000 億美元風投已轉向 AI。</b>主持人 David Friedberg 問：係咪即係 VC 將 LP 嘅錢變相用嚟「買 compute tokens」？Shkreli 毫不猶豫同意——估值陷阱風險遠超任何單一公司。</li>
      <li><b>TAM 唔止白領：</b>佢舉例——McDonald's 可以花 100 億美元叫 OpenAI 出 1,000 萬張 GPU 去決定下一個三文治，照樣 NPV 為正。總可尋址市場 = 地球上每一門生意。</li>
      <li><b>AI 會「開公司」而唔止「服務公司」：</b>想像未來 <code>OpenAI Pharma</code>、<code>OpenAI Motors</code>、<code>OpenAI Aviation</code>——<i>「OpenAI 或 Anthropic 內部會有成個標普 500。」</i> 呢句可以係願景，也可以係壟斷噩夢。</li>
      <li><b>市場仍喺「day one」：</b>今日嘅聊天機械人，回頭睇會笑死人。</li>
    </ul>
  </div>

  <!-- 主題四 -->
  <h3>🎯 主題四：點名批評「恐懼販子」——Dario Amodei</h3>
  <div class="le-summary">
    <p>Shkreli 對 AI 安全倡議者嘅批評係<b>指名道姓、個人化</b>嘅。佢話自己協助普及——甚至會宣稱係佢發起——<b>effective accelerationism（e/acc）</b>運動，作為 effective altruism（EA）嘅對立面。佢嘅靶心：Anthropic CEO <b>Dario Amodei</b>，佢叫佢做「恐懼販子（fear-monger）」，並承認自己「有啲憎佢」，但尊重佢建咗一間兆美元公司。</p>
    <ul>
      <li><b>對出身嘅不滿：</b>佢將 Amodei 離開 OpenAI 框架成「將潘朵拉盒子拎去街口，再開一個競爭版潘朵拉盒子」——換轉係佢，大概會以「盜取商業秘密」起訴。</li>
      <li><b>更鋒利嘅係「往績」：</b>大約兩年前，Amodei 預測 1–5 年內將出現「全面失業」——按 Shkreli 計，呢個鐘剩返約三年。Amodei 亦講過 AI 會治好所有疾病。</li>
      <li><b>Shkreli 嘅對賭，直白可證偽：</b><code>「未來 10 年唔會有一款與 AI 相關嘅藥。AI 對藥物研發冇實質幫助。」</code></li>
      <li><b>佢有特殊根據：</b>佢砌過一部 Cray 叢集去分析藥物；佢話 GPU 好勁，但喺製藥領域 AI 實際做到嘅唔多——困擾藥物研發嘅「本體不可知」數據問題，唔會因為模型變大就解決。佢 2015 年曾開過一間小型 NLP 公司去讀 4,000 萬篇醫學論文，<b>結果唔work</b>——呢個或者係佢對「AI 助藥物研發」悲觀最誠實嘅數據點。</li>
      <li><b>安全觀：</b>「我覺得恐懼販賣有啲荒謬，會有需要恐慌嘅時候，但唔係而家。你可以熄咗部電腦。」佢歸功 Meta、總統同 Jensen Huang 有脊骨公開咁講；並暗示 OpenAI 其實都唔太信，只係唔想同 Anthropic 睇落太唔同。</li>
    </ul>
  </div>

  <!-- 主題五 -->
  <h3>🎯 主題五：令佢發達嘅「製藥套利」</h3>
  <div class="le-summary">
    <ul>
      <li><b>起點唔係交易台，而係「分子嘅無效率市場」。</b>佢 16 歲就喺 Jim Cramer 嘅對沖基金工作（當時人在曼哈頓、把口大、愛炒股）——親眼見 Cramer 靠每日買賣一切、扣除費用後年複合 23%。</li>
      <li><b>但佢結論係：自己係更好嘅企業家，唔係交易員。</b>佢嘅 edge：藥廠唔care細資產。佢用 <b>200 萬美元</b>向 Bristol-Myers 買咗一隻藥，圍繞佢建嘅公司今日上市、值 <b>60 億美元</b>。佢斷言：Pfizer 會因為「唔 fit 策略組合」而以 100 萬美元賤賣一隻價值 10 億嘅藥。</li>
      <li><b>瓶頸係人力頻寬：</b>讀論文、專利、走訪大學同藥廠去 vet 資產。2015 年佢開 NLP 公司想自動讀 4,000 萬篇論文——就係上文提到「唔work」嗰間。</li>
      <li><b>對「抬高藥價」事件嘅重新框定：</b>佢叫做「重新定位」。佢買入 Sparsentan，將佢由高血壓（「死寂、沉睡嘅市場」）搬去 <b>FSGS</b>（一種從未有任何獲批藥物嘅病）。該藥現已獲 FDA 批准並成為 blockbuster，服務約 <b>3 萬名</b>病人。佢話：「我都可以做返個好人。」</li>
    </ul>
  </div>

  <!-- 主題六 -->
  <h3>🎯 主題六：監獄真正教識佢嘅事（全集最赤裸嘅一段）</h3>
  <div class="le-summary">
    <blockquote>
      「我好難承認自己唔係世界上最好嘅對沖基金經理，但我係一個出色嘅企業家。就係咁簡單一個唔肯承認，送我入獄。」
      <cite>— Martin Shkreli, All-In (2026-10-12)</cite>
    </blockquote>
    <ul>
      <li><b>「資優人士的信天翁」：</b>佢話呢種想活成一個可能同現實唔符嘅自我形象，係聰明人嘅共同重擔。佢點名 Elizabeth Holmes、Raj Rajaratnam 作平行個案。</li>
      <li><b>佢而家覺得當時好蠢：</b>執著於「被睇成偉大交易員」，明明有咁多替代選項——長期投資者、價值投資者、企業家、科學家、爸爸。</li>
      <li><b>監獄反而「 refreshing 咁平凡」：</b>唔論背景或罪名，人人都在為「朋友冇聯絡」而失落、為掛住某人而失落。<i>「無論人達到幾高嘅高度，歸根究柢，人人都想做到最好嘅爸爸。」</i></li>
      <li><b>Chamath 拉出 SBF 平行線：</b>最聰明嘅人往往反傳統；而產生 alpha 嘅異端特質，可能同時令「守法」更難。Shkreli 同意——佢見過 Bankman-Fried、勸過佢「頂住」，並承認 SBF 2021–2022 嘅投資組合（早期 Anthropic、Robinhood）當時睇落係天才。共同線索係「資優者自我形象嘅心理壓力」。</li>
    </ul>
  </div>

  <h3>💡 行業 Insight（點解呢集對做生意／投資有意義）</h3>
  <div class="le-summary">
    <ul>
      <li><b>「睇啱方向」唔等於「賺到錢」。</b>Shkreli 做空量子已輸幾百萬，但論點可能仍然啱。佢自認 2000 年大概會估 Yahoo 同 Cisco 長倉。呢個係所有逆勢投資者嘅結構性兩難——市場唔會為 insight 找數，只為時間點找數。</li>
      <li><b>用 Jevons 悖論做 AI 硬件投資嘅壓力測試。</b>效率提升可能擴大總需求（利好 Nvidia 短期），但一旦「效率躍升」夠大，同樣會摧毀現有矽經濟。呢條張力線可以同時解釋點解要持有、又要對沖。</li>
      <li><b>「光子矩陣乘法」係一個可追蹤嘅技術主題。</b>Microsoft《Nature》論文 + Neurophos／Opticore／Lumai 三家初創，係一條可驗證嘅 watchlist。</li>
      <li><b>AI 製藥：估值同現實嘅落差。</b>若「10 年內冇 AI 有效研發嘅藥」成立，成個 AI-drug-discovery 板塊嘅敘事要重估。注意：呢句係<u>Shkreli 個人預測</u>，未經第三方核實。</li>
      <li><b>「藥物資產套利」係一門被低估嘅生意。</b>大藥廠策略組合盲點 ⇒ 細資產賤價 ⇒ 專注 vet 資產嘅營運者可以食呢個 inefficiency（200 萬 → 60 億嘅實例）。</li>
    </ul>
  </div>

  <h3>💬 原文摘錄（blockquote，逐字）</h3>
  <blockquote>「Chelsea and I have tried every single quantum computer in the world. We cannot multiply 300 by 200 on any of these.」</blockquote>
  <blockquote>「I do think in 20 years, these H100s are in the scrap heap. B100s are in the scrap heap. B200s are in the scrap heap. We're going to find ways to do this better.」</blockquote>
  <blockquote>「There will not be a single AI-relevant drug in the next 10 years. AI does not meaningfully help drug discovery.」</blockquote>
  <blockquote>「I had a hard time admitting I was not the best hedge fund manager in the world, but I was a wonderful entrepreneur. That simple refusal to admit that put me in prison.」</blockquote>
  <blockquote>「I've been short them. Unfortunately, we lost millions of dollars shorting quantum computing companies, but I told my wife that we gained billions in insight.」</blockquote>

  <div class="callout" style="margin-top:18px">
    ⚠️ <b>標註</b>：章節、逐字引用與玩家判讀表，取自官方 show notes／Apple Podcasts 集頁同 BigGo Finance 對該集嘅逐字轉引（一手為節目本身，BigGo 為二手整理）。Shkreli 嘅預測、對 Amodei 嘅指控、以及「e/acc 由我發起」等屬<b>其個人主張</b>，未經獨立核實。Jev 前置過濾（<code>news</code> profile）給此條 <code>worth 0.14</code>（低分主因：送檢文本為 show notes＋大量贊助商文案，屬二手／營銷口徑），按 profile 指引「只作相對排序、不作硬砍」，且為本輪真實新集，予以保留並完整拆解。
  </div>

  <div class="le-link" style="margin-top:14px">🔗 <a href="https://allin.com/">allin.com</a> · 集頁：<a href="https://allinchamathjason.libsyn.com/martin-shkreli-big-pharmas-blind-spot-betting-against-quantum-what-prison-taught-him">Libsyn</a> · <a href="https://podcasts.apple.com/us/podcast/martin-shkreli-big-pharmas-blind-spot-betting-against/id1502871393?i=1000795982205">Apple Podcasts</a> · 逐字整理：<a href="https://finance.biggo.com/news/372021a34d1fa625">BigGo Finance</a></div>
</section>
'''
cards += allin


# ==================== My First Million — NEW EPISODE DEEP DIVE ====================
mfm = f'''
<!-- ==================== My First Million ==================== -->
<section class="pod">
  <div class="pod-head">
    <h2>My First Million</h2>
    <span class="host">Sam Parr &amp; Shaan Puri</span>
    <span class="tag new">🆕 新集數</span>
  </div>

  <div class="ep-title">3 embarrassing moments that changed my life</div>
  <div class="ep-meta">
    🗓 2026-10-12（11:52 UTC 發佈）· ⏱ 24 分 01 秒（1,441 秒）· 🎙 主持：<b>Shaan Puri</b>（單人集，Sam 缺席）· 🎬 Episode 870 · 📄 提及之推廣：《$1M Solopreneur MVP guide》<br>
    🎧 集頁：<a href="https://www.mfmpod.com/3-embarrassing-moments-that-changed-my-life/">mfmpod.com</a>
  </div>

  <div class="callout" style="margin-top:16px">
    <b>一句話總結：</b>呢集唔係訪問、係一篇「口述自傳式」單人獨白。Shaan 用三個令自己尷尬嘅故事——<b>一個私人生活、一個生意、一個最近發生</b>——每個 story 收尾都接一條 heuristics（行動準則）。三條 lessons 分別係：<code>You Can Make Hell Out of Heaven</code>／<code>Worship at the Church of Action</code>／<code>The Decision Is Upstream of All Action</code>。
  </div>

  <h3>🕒 官方章節（24 分鐘）</h3>
  <div class="chapters">
    <span class="tc">(0:00)</span> intro<br>
    <span class="tc">(1:15)</span> 最近的尷尬事<br>
    <span class="tc">(5:20)</span> Lesson：「You Can Make Hell Out of Heaven」<br>
    <span class="tc">(8:15)</span> 生意上嘅尷尬事<br>
    <span class="tc">(12:58)</span> Lesson：「Worship at the Church of Action」<br>
    <span class="tc">(15:35)</span> 私人生活嘅尷尬事<br>
    <span class="tc">(19:55)</span> Lesson：「The Decision Is Upstream of All Action」
  </div>

  <h3>🧩 結構拆解（三段故事 × 三條 lessons）</h3>
  <div class="le-summary">
    <ol>
      <li><b>①（1:15 → 5:20）最近嘅尷尬 →「You Can Make Hell Out of Heaven」</b><br>
      先講「最近發生」嘅一件尷尬事，收尾嘅 lesson 係一句極簡嘅心智轉換：<b>你可以把地獄砌成天堂</b>。即係話：同一件客觀壞事，你點 frame 佢（困境 vs 素材），決定你行去邊。Shkreli 全集講「大藥廠睇唔上嘅資產」，同呢條 lesson 異曲同工——同一舊嘢，換個框就係金。</li>

      <li><b>②（8:15 → 12:58）生意上嘅尷尬 →「Worship at the Church of Action」</b><br>
      生意場上出醜，收尾 lesson 係叫你「去行動教會崇拜」——即係<b>少諗多做，用行動而非空想嚟買單</b>。呢條係 Shaan 一貫嘅 business 信仰：決策做得快、落地先算數。</li>

      <li><b>③（15:35 → 19:55）私人生活嘅尷尬 →「The Decision Is Upstream of All Action」</b><br>
      最個人嘅一段，lesson 係把鏡頭再往上推一格：<b>「決定」在所有「行動」嘅上游</b>。即係話，你在下游拼命執行，可能救唔到一個一開始就揀錯嘅上游決定——所以真正嘅槓桿點係「揀」，唔係「做」。</li>
    </ol>
    <p class="le-summary" style="margin-top:6px"><b>三條 lessons 連成一條線：</b>先換框（Hell→Heaven）→ 再落手行動（Church of Action）→ 但記住最高槓桿係上游嘅「決定」（Decision upstream）。呢個係一個「心智 → 執行 → 決策」嘅閉環，比單純嘅「努力／正面思考」深一層。</p>
  </div>

  <h3>💡 為何值得聽（對做生意／個人決策嘅 takeaway）</h3>
  <div class="le-summary">
    <ul>
      <li><b>尷尬 = 免費嘅資訊。</b>Shaan 用「公開出醜」做教材：把羞恥事件轉成可複用嘅原則，係一種低成本嘅自我教練技術。</li>
      <li><b>「Decision upstream of action」係槓桿思考法。</b>大部分人優化「做」嘅效率，高手優化「揀」嘅質素——因為一個上游決定，會乘以所有下游行動。</li>
      <li><b>單人集 = 高信噪比。</b>冇嘉賓、冇 round table，24 分鐘即係 3 個故事 + 3 條 heuristics，適合通勤一次聽完。</li>
    </ul>
  </div>

  <h3>💬 原文摘錄（官方 show notes，逐字）</h3>
  <blockquote>
    「Episode 870: Shaan Puri tells 3 embarrassing stories. One from his personal life, one from business, and a most recent one.」
  </blockquote>
  <blockquote>
    「(5:20) Lesson: “You Can Make Hell Out of Heaven”」
  </blockquote>
  <blockquote>
    「(12:58) Lesson: “Worship at the Church of Action”」
  </blockquote>
  <blockquote>
    「(19:55) Lesson: “The Decision Is Upstream of All Action”」
  </blockquote>

  <div class="callout" style="margin-top:18px">
    ⚠️ <b>標註</b>：以上章節、三條 lesson 標題與「三個故事」框架，全部取自官方 show notes（一手）。三個故事嘅<u>具體情節</u> Shaan 只喺音檔內口述，官方文字沒有載明——因此本文只還原「結構＋lesson」，不對故事細節作猜測或杜撰。Jev 前置過濾給此條 <code>worth 0.69</code>（有數字但屬營銷／二手口徑），予以保留。
  </div>

  <div class="le-link" style="margin-top:14px">🔗 <a href="https://www.mfmpod.com/episodes/">mfmpod.com/episodes</a> · 集頁：<a href="https://www.mfmpod.com/3-embarrassing-moments-that-changed-my-life/">連結</a></div>
</section>
'''
cards += mfm


html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>思維播客日報 · {DATE}</title>
{style}
</head>
<body>
<div class="wrap">

<header class="top">
  <h1>思維播客日報 · {DATE}</h1>
  <div class="sub">6 個英文商業／思維播客 · 每日深度掃描 · 為 James 而設的「第二對耳仔」</div>
  <div class="meta">
    🕘 報告生成時間：<b>{now_utc}</b>（= 香港時間 {now_hkt}）<br>
    📡 掃描方式：6 條 RSS feed 直接抓取 XML，逐集比對 GUID 去重<br>
    🧮 Jev 前置過濾（TypeSafe System One, <code>news</code> profile）：本輪 2 條候選 → All-In 0.14 / MFM 0.69；兩條皆為真實新集，按「只作相對排序」指引保留並完整拆解<br>
    🧑‍💻 Repo：<a href="https://github.com/JMOKSZ/mindset-podcasts">JMOKSZ/mindset-podcasts</a>
  </div>
</header>

<div class="summary">
  <b>今日重點：6 台之中 2 台有新集 —— All-In（Martin Shkreli）同 My First Million（Shaan Puri 單人集）。</b>
  <ul>
    <li>🆕 <b>All-In</b>：10-12 新集《Martin Shkreli: Big Pharma's Blind Spot, Betting Against Quantum &amp; What Prison Taught Him》（25 分）——量子係「一招走天涯」生意、光子 matmul 才是 Nvidia 真威脅、$400B AI 資本、點名 Dario Amodei、藥物套利、監獄教訓。<b>下方完整拆解。</b></li>
    <li>🆕 <b>My First Million</b>：Ep 870《3 embarrassing moments that changed my life》（24 分）——Shaan 三個尷尬故事 + 三條 heuristics（Make Hell Out of Heaven／Church of Action／Decision Is Upstream）。<b>下方完整拆解。</b></li>
    <li>📭 <b>Acquired、Founders、Knowledge Project、Diary of a CEO</b>：本輪逐條比對後<b>均無未掃過嘅新 GUID</b>。（DOAC 的 Eric Weinstein 集 GUID 不變、僅標題被改，不視為新集。）</li>
    <li>📅 最近一次有更新（其他台）：<b>DOAC</b> 10-12（Eric Weinstein 文明風險）、<b>KP</b> 10-08（Ryan Serhant 銷售）、<b>Founders</b> 10-05（#436 Ari Emanuel）。Acquired 節奏最疏。</li>
  </ul>
</div>

<div class="stats">
  <div class="stat"><span class="n">6/6</span><span class="l">RSS 抓取成功</span></div>
  <div class="stat"><span class="n">2</span><span class="l">今日新集數</span></div>
  <div class="stat"><span class="n">{scanned_total:,}</span><span class="l">累計追蹤集數</span></div>
  <div class="stat"><span class="n">6</span><span class="l">播客台數</span></div>
</div>

{cards}

<footer class="bot">
  <div class="timeline">
    ⏱ <b>本輪掃描時序</b><br>
    <code>09:53Z</code> 讀 podcasts.json（6 台）/ state.json（{scanned_total:,} 個已掃 GUID）<br>
    <code>09:53Z</code> Fetch 6 條 RSS feed → 全部 HTTP 200（{feed_counts} 集）<br>
    <code>09:53Z</code> GUID 逐條比對 → <b>2 條新內容</b>（All-In · Martin Shkreli｜MFM · Ep 870）<br>
    <code>09:53Z</code> Jev triage 2 條 → 0.14 / 0.69（皆保留，作完整拆解）<br>
    <code>09:53Z</code> 抓 Apple Podcasts 集頁／官方 show notes／BigGo 逐字整理補完<br>
    <code>09:53Z</code> 生成日報 → 更新 state.json lastScan → git push
  </div>
  <p>📬 本報告由 Vee Mok 為 James 自動生成 · 每日深度掃描 6 個英文商業／思維播客 · 所有內容基於真實 RSS／官方集頁／逐字整理，未經核實之數字與預測已標 ⚠️。</p>
  <p>🔗 <a href="https://jmoksz.github.io/mindset-podcasts/">jmoksz.github.io/mindset-podcasts</a> · <a href="https://github.com/JMOKSZ/mindset-podcasts">GitHub Repo</a></p>
</footer>

</div>
</body>
</html>
'''

open(BASE + f'/daily-report-{DATE}.html', 'w', encoding='utf-8').write(html)
print("written", len(html), "bytes; scanned_total =", scanned_total)
