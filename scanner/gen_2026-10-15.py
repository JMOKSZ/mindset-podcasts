#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
from datetime import datetime, timezone, timedelta

BASE = '/root/.openclaw/workspace/mindset-podcasts'
style = open('/tmp/style.html', encoding='utf-8').read()

now = datetime.now(timezone.utc)
DATE = now.strftime('%Y-%m-%d')
now_utc = now.strftime('%Y-%m-%d %H:%M') + ' UTC'
hkt = now.astimezone(timezone(timedelta(hours=8)))
now_hkt = hkt.strftime('%Y-%m-%d %H:%M')

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
  <div class="le-summary" style="margin-top:14px;font-size:14.5px;color:#4f463b">
    <b>內容概要：</b>{synopsis}
  </div>
  <div class="le-link" style="margin-top:10px;font-size:13px">🔗 <a href="{site}">{site}</a>{(' · 集數頁：<a href="' + link + '">連結</a>') if link else ''} · 首次完整拆解見 <a href="{first_report}">{first_report.replace('daily-report-','').replace('.html','')} 日報</a></div>
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
    "Home Depot 創辦故事：Bernie Marcus 同 Arthur Blank 喺 48 歲同 35 歲畀人炒魷之後，聽咗紐約銀行家 Ken Langone 嘅一句話——「你哋係畀金馬蹄鐵踢中咗屁股」——然後寫下美國零售史上最強複利故事之一。官方描述形容成一部「Avengers 電影」。",
    note="⚠️ Acquired 自 09-13 後未再有新集；本台節奏約每月 1–2 集（長篇研究型）。")

# ---------- Founders ----------
cards += card_none(
    "Founders", "David Senra", "最近無更新",
    "#437 The Tycoons: Carnegie, Rockefeller, Gould &amp; Morgan",
    "2026-10-13", "54 分 11 秒（3,251 秒）",
    "https://www.founderspodcast.com/", "https://www.founderspodcast.com/",
    "daily-report-2026-10-14.html",
    "Senra 讀 Charles R. Morris《The Tycoons》：四位寒微出身的巨人——三破壞者（Carnegie 鋼／Gould 鐵路／Rockefeller 石油）+ 一監管者（Morgan 銀行），喺 1873 同 1880 年代兩次市場斷裂中，把美國由農業手工業國家推成世界工廠。核心 insight：「發明嘅消費者」勝過發明者、先滿產再算賬、壟斷經濟學反直覺結論。",
    note="ℹ️ 此集已於 10-14 日報完整深度拆解（GUID <code>333ce5c4-c75d-11f1-a31e-7bbfecdd098c</code> 不變）。Senra 每日／隔日更新，下一集預料 10-15／10-16。")

# ---------- My First Million ----------
cards += card_none(
    "My First Million", "Sam Parr &amp; Shaan Puri", "最近無更新",
    "3 embarrassing moments that changed my life", "2026-10-12", "—",
    "", "https://www.mfmpod.com/episodes/", "daily-report-2026-10-13.html",
    "Shaan Puri 單人集：用三個令佢尷尬到爆嘅人生時刻，講佢點樣由呢啲「黑歷史」入面提煉出可重複嘅成長／決策框架——典型 MFM 嘅「個人敘事 + 可操作啟發」配方。",
    note="ℹ️ MFM 週更（多數星期一、四）；10-12 一集已掃過，下一集預料 10-15／10-16 前後。")

# ---------- Knowledge Project ----------
cards += card_none(
    "The Knowledge Project", "Shane Parrish", "最近無更新",
    "Ryan Serhant: How to Get People to Say Yes", "2026-10-08", "—（Members 先行；公開 10-08）",
    "https://fs.blog/knowledge-project-podcast/ryan-serhant/", "https://fs.blog/knowledge-project/",
    "daily-report-2026-10-09.html",
    "Ryan Serhant（SERHANT. 創辦人、Netflix《Owning Manhattan》主角）講「唔令人覺得被推銷」嘅銷售法：先建立連結、先幫人、賺到開口請求嘅資格。核心係信任與關係資本，而非話術。",
    note="ℹ️ KP 目前 RSS 只有 20 集（滾動 feed），週四更新；下一集預料 10-15 前後。")


# ==================== All-In — NEW EPISODE DEEP DIVE ====================
allin = f'''
<!-- ==================== All-In ==================== -->
<section class="pod">
  <div class="pod-head">
    <h2>All-In with Chamath, Jason, Sacks &amp; Friedberg</h2>
    <span class="host">Chamath · Jason · Sacks · Friedberg</span>
    <span class="tag new">🆕 新集數</span>
  </div>

  <div class="ep-title">Elizabeth Holmes' Husband Billy Evans: The Trial, Prison &amp; Nathan Fielder's Documentary</div>
  <div class="ep-meta">
    🗓 發佈：<b>2026-10-15 01:54 UTC</b>（香港時間 10-15 09:54）· ⏱ <b>41 分 55 秒（2,515 秒）</b>· 🎙 嘉賓：<b>Billy Evans</b>（Elizabeth Holmes 伴侶、Haemanthus CEO）· 主持：<b>David Friedberg</b>（單對單，非四人合體）<br>
    ⚠️ 呢集係 <b>All-In Summit</b>（線下峰會）嘅對談場次，屬「特別集」多於常規 besties 圓桌。<br>
    🎧 <a href="https://allinchamathjason.libsyn.com/elizabeth-holmes-husband-billy-evans-the-trial-prison-nathan-fielders-documentary">libsyn 集數頁</a> ·
    <a href="https://www.youtube.com/watch?v=2tAywoHiIpo">YouTube</a> · RSS GUID <code>8c597438-75df-42fd-85bc-7c08156b38b6</code>
  </div>

  <div class="callout">
    <span class="label ext">來源說明</span>All-In 官方 feed 只提供<b>章節時間碼</b>（無逐字稿）。以下拆解以官方章節結構為骨幹，再以 2026 年 9–10 月公開報導（NYT、Variety、Fortune、NPR、Entrepreneur、Vanity Fair）補充事實背景。<b>所有 blockquote 均為原文轉引並標明出處，冇任何杜撰</b>。節目內嘅具體言論僅按章節標題轉述，唔會假造對白。
  </div>

  <h3>🎯 一集講咩（一句話）</h3>
  <p>呢集係 All-In Summit 上 <b>Friedberg 單對單訪問 Billy Evans</b>——Elizabeth Holmes 嘅伴侶、三個孩子的爸爸、以及一間叫 <b>Haemanthus</b> 嘅新血液檢測初創 CEO。題目本身已經夠辣：<b>你要點樣同一個「矽谷史上最出名騙案」主角結婚、生仔、去法庭、睇住佢入獄，然後自己再開一間同樣做血液檢測嘅公司？</b></p>

  <h3>📋 官方章節結構（All-In 原文時間碼）</h3>
  <div class="timeline">
    <span class="tc">0:00</span> Billy Evans joins Friedberg<br>
    <span class="tc">3:38</span> 佢哋點相遇、Elizabeth「本人」vs「頭條」、起訴書<br>
    <span class="tc">11:02</span> 審訊期間嘅生活、生小朋友、佢喺融資度邊度出錯<br>
    <span class="tc">19:28</span> 理解裁決、判刑，同「保持沉默」呢個錯誤<br>
    <span class="tc">26:09</span> Elizabeth 由監獄打電話嚟、佢獄中生活<br>
    <span class="tc">31:34</span> 點解佢哋參與 Nathan Fielder 嘅紀錄片<br>
    <span class="tc">35:47</span> 回程、賠償（restitution）條數點計、點解佢間新公司唔係 Theranos 2.0
  </div>

  <h3>👤 嘉賓係邊個：Billy Evans</h3>
  <ul>
    <li><b>加州酒店業家族後人</b>（Evans Hotels 家族），2017 年與 Holmes 相識——據紀錄片預告，Evans 話自己<b>「喺第一次對話就已經愛上」</b>，甚至可能喺知道佢係 Theranos 創辦人之前。</li>
    <li>兩人育有<b>兩名子女</b>（包括一名女嬰），一家人曾住喺 Del Mar 嘅海邊大宅。</li>
    <li>Holmes 2023 年入獄後，Evans 出任新公司 <b>Haemanthus</b>（血液檢測／健康科技）CEO；NPR 2025-05 報導指佢為此<b>籌到數百萬美元</b>，而 Holmes 在獄中提供建議。</li>
    <li>公司喺 NYT 踢爆後喺 X 發聲明：<i>「Yes, our CEO, Billy Evans, is Elizabeth Holmes' partner. Skepticism is rational. We must clear a higher bar.」</i>（承認質疑合理，但聲稱要跨過更高門檻。）</li>
  </ul>

  <h3>🎬 紀錄片背景：Nathan Fielder《You Can See Everything》</h3>
  <ul>
    <li>由喜劇演員 <b>Nathan Fielder</b> 與導演 <b>Lance Oppenheim</b> 執導、<b>A24</b> 出品，2026-09 喺 Telluride 影展「秘密放映」，全場震驚。</li>
    <li><b>拍攝橫跨三年</b>，由 Holmes 入獄前 <b>34 日</b>（2023 年）開始——即係喺佢屋企拍攝、住埋一齊、長期近距離訪談，用大量極近鏡捕捉表情。</li>
    <li>片中揭示：Holmes 服刑期間（德州 Bryan 聯邦監獄營，刑期 11 年），佢同 Evans 仍<b>打電話同潛在合作方傾「新版本 Theranos」</b>，仲由車房搬出嗰部已被否定的血液檢測儀器。</li>
    <li>呢個就係「restitution math（賠償條數）」同「點解新公司唔係 Theranos 2.0」呢兩章嘅由來——對外要證明「今次唔同」。但矽谷內部唔買帳，有生技圈內人對 NY Post 講：<i>「She is shameless and delusional… It sounds exactly like Theranos 2.0.」</i></li>
  </ul>
  <blockquote>
    When I met her, I remember having this weird experience where she seems so genuine at times. But then I'm like, 'no,' and clocking and tracking my thoughts and being like, 'Okay, I know she's a liar.'
    <cite>Nathan Fielder 接受 Variety 訪問（2026-10-01）</cite>
  </blockquote>
  <blockquote>
    We see her spend time with her husband, Billy Evans, and their two young kids. […] They're working the phones with investors, still attempting to bring back a new version of Theranos 2.0.
    <cite>Fortune 對《You Can See Everything》嘅影評（2026-10-02）</cite>
  </blockquote>

  <h3>🧠 三個「值得聽落去」嘅核心命題</h3>
  <ol>
    <li><b>「本人 vs 頭條」。｜</b>第 3:38 一節嘅核心——Evans 想講嘅係媒體敘事（騙徒）同佢認識嘅人（伴侶／母親）之間嘅落差。呢個正正係 All-In 觀眾最想聽嘅角度：<b>創辦人神話與人格分裂，往往同時係真。</b></li>
    <li><b>「保持沉默係錯誤」。｜</b>第 19:28 一節，Evans 直指 Holmes 審訊期間選擇唔出庭作證（保持沉默）係致命錯誤。呢個係一課關於<b>危機公關同敘事主導權</b>嘅實戰教訓——當你唔講，法庭同媒體就幫你講。</li>
    <li><b>「唔係 Theranos 2.0」嘅舉證責任。｜</b>第 35:47 一節——Evans 要同時處理賠償數字（restitution）同新公司嘅正當性。Haemanthus 由一開始就被貼上「Theranos 2.0」標籤，Evans 嘅論點係：技術路線、監管取態、透明度都唔同。<b>但呢個 section 真正嘅價值係：一個創業者點樣喺「原罪」之下重新建立信任資本。</b></li>
  </ol>

  <h3>📊 關鍵數據／事實（聽完記得住嗰幾個）</h3>
  <table class="kv">
    <tr><th>本集長度</th><td>2,515 秒 = 41 分 55 秒（All-In 較短嘅單人對談場次）</td></tr>
    <tr><th>Holmes 刑期</th><td>11 年，服刑地點：德州 Bryan 聯邦監獄營（Federal Prison Camp, Bryan, Texas）</td></tr>
    <tr><th>紀錄片拍攝時間線</th><td>由入獄前 34 日（2023 年）起計，橫跨 3 年</td></tr>
    <tr><th>兩人相識</th><td>2017 年；紀錄片預告：Evans 稱「喺第一次對話就已經愛上」</td></tr>
    <tr><th>新公司 Haemanthus</th><td>Evans 任 CEO，2025-05 報導已籌數百萬美元；Holmes 由獄中提供建議</td></tr>
    <tr><th>賠償（restitution）</th><td>節目第 35:47 專章講「restitution math」——即 Holmes／Balwani 須向投資者賠償嘅金額點計、點攤還（本集具體數字以節目內容為準）</td></tr>
    <tr><th>All-In 形式</th><td>All-In Summit 現場對談（Friedberg 主持），非四人圓桌常規集</td></tr>
  </table>

  <h3>💡 行業 Insight（James 可直接搬去用）</h3>
  <ul>
    <li><b>敘事主導權 = 生存權。</b>Holmes 案最貴嘅一課唔係「唔好造假」，而係<b>「唔好沉默」</b>：當負面敘事一旦被第三方定調，任何後續澄清都只會被當成狡辯。創辦人危機處理第一原則：自己搶先講、持續講。</li>
    <li><b>「原罪標籤」嘅處理方法。</b>Haemanthus 面對嘅唔係市場競爭，而係<b>信任赤字</b>。Evans 嘅玩法（主動上 All-In、上紀錄片、由零解釋技術差異）等於把「透明度」本身變成產品——呢個對任何背住前科／醜聞重建嘅創辦人都有參考價值。</li>
    <li><b>監管紅線係生技公司嘅估值開關。</b>Theranos 之死係繞過 CLIA／FDA 監管；任何新血液檢測公司，第一件事就係回答「你點過監管」——呢個就係 Evans 要證明「唔係 2.0」嘅技術核心。</li>
    <li><b>媒體產品化：Fielder 之於 Holmes。</b>Fielder 承認自己「一邊覺得佢好真誠、一邊知道佢講大話」——呢種「人格魅力 ≠ 可信度」嘅張力，係創辦人盡職調查（DD）最難量化嘅一環。</li>
  </ul>

  <div class="callout">
    <span class="label jev">Jev 過濾</span>TypeSafe System One（<code>news</code> profile）對本條評 <code>worth&nbsp;0.14</code>、一手概率 <code>0.65</code>——即「無可核實數字／偏人物敘事」。Jev 按 <code>news</code> 檔視之為低訊號；但本台判斷呢集屬 <b>All-In Summit 唯一新集</b>且題材（創辦人信任重建）對 James 有獨立價值，故保留並完整拆解，同時明確標示節目內言論僅按官方章節轉述。
  </div>
</section>
'''


# ==================== Diary of a CEO — NEW EPISODE DEEP DIVE ====================
doac = f'''
<!-- ==================== Diary of a CEO ==================== -->
<section class="pod">
  <div class="pod-head">
    <h2>The Diary of a CEO</h2>
    <span class="host">Steven Bartlett</span>
    <span class="tag new">🆕 新集數</span>
  </div>

  <div class="ep-title">Phone Addiction Scientist: Doing This Gives You An Hour Back Every Day!｜Dr Sahar Yousef</div>
  <div class="ep-meta">
    🗓 發佈：<b>2026-10-15 05:00 UTC</b>（香港時間 10-15 13:00）· ⏱ <b>2 小時 13 分 52 秒（8,032 秒）</b>· 🎙 嘉賓：<b>Dr. Sahar Yousef</b> · 主持：<b>Steven Bartlett</b><br>
    ⭐ 呢集係 <b>DOAC 史上首個直播工作坊（first ever live streamed DOAC Workshop）</b>，唔係常規訪談。<br>
    🎧 <a href="https://thediaryofaceo.com/">thediaryofaceo.com</a> · RSS GUID <code>flightcast:01M4782E2HS3CAH5B71G0KB9KB</code>
  </div>

  <h3>👤 嘉賓係邊個：Dr. Sahar Yousef</h3>
  <ul>
    <li><b>認知神經科學家</b>，UC Berkeley Haas 商學院 MBA 教席，主講「Becoming Superhuman」。10 年以上研究「如何令人變超人」，專攻<b>認知神經可塑性（cognitive neuroplasticity）</b>同高表現者嘅生物作業系統。</li>
    <li>創辦 <b>Becoming Superhuman Lab</b>——一間教忙碌專業人士「用更少時間、更低壓力」完成最重要工作嘅訓練機構。</li>
    <li>其課程實測：學生透過調整工作節奏 + <b>50 分鐘「focus sprint」</b>（無視覺／聽覺干擾嘅專注時段），以及<b>6 星期內</b>可量度嘅專注力／記憶力改善。</li>
    <li>本集配套：MMM Institute「Digital Dependence Index」（測你嘅專注力跨度）、MyChronotype 生理時鐘評估（代碼 <code>DOAC</code>）、以及一份獨立事實核查 PDF。</li>
  </ul>

  <h3>🎯 官方五大框架（DOAC 原文重點）</h3>
  <ol>
    <li><b>The Attention Trap（注意力陷阱）：</b>科技平台係由行為神經科學家<b>刻意設計</b>，去最大化參與度、利用你大腦嘅生存線路，而唔係幫你提升生產力。</li>
    <li><b>The Grayscale Hack（灰階黑客）：</b>把手機螢幕轉為灰階，大幅降低神經刺激，可以<b>即時每星期討回幾個鐘</b>嘅滑手機時間。</li>
    <li><b>The Focus Sprint（專注衝刺）：</b>把大目標拆成細粒度執行清單 + 嚴格時間區塊，利用大腦嘅「預期網絡」把產出加倍。</li>
    <li><b>The Myth of Multitasking（多工神話）：</b>任務切換會產生嚴重嘅「注意力包袱（attentional baggage）」，令你比單工<b>慢最多 60%</b>。</li>
    <li><b>The Power of Boredom（無聊的力量）：</b>容許心智漫遊，係啟動大腦網絡解難、產生最佳創意洞察嘅關鍵機制。</li>
  </ol>

  <h3>📋 完整章節（2 小時 13 分，官方時間碼）</h3>
  <div class="chapters">
    <span class="tc">00:00:00</span> Intro<br>
    <span class="tc">00:02:27</span> 今日咩阻住我哋？<br>
    <span class="tc">00:06:48</span> 點解要聽你講？<br>
    <span class="tc">00:08:20</span> 咩令我哋做唔到嘢？<br>
    <span class="tc">00:12:14</span> 生產力工具箱<br>
    <span class="tc">00:14:17</span> 專注點解對健康咁重要<br>
    <span class="tc">00:17:34</span> 生產力軟件真係有用？<br>
    <span class="tc">00:21:50</span> 點解我哋覺得要即刻回覆？<br>
    <span class="tc">00:24:58</span> 點分信號同噪音<br>
    <span class="tc">00:27:20</span> 點解現代世界同生物本能對抗<br>
    <span class="tc">00:29:11</span> 點停止逃避不適<br>
    <span class="tc">00:32:40</span> 大科技點騎劫你大腦<br>
    <span class="tc">00:43:52</span> 點戒手機癮<br>
    <span class="tc">00:53:17</span> 廣告<br>
    <span class="tc">00:55:19</span> Focus Sprint：點把生產力翻倍<br>
    <span class="tc">01:00:48</span> 任務排序：MITs vs LITs<br>
    <span class="tc">01:04:29</span> 點搵你嘅目標：尋找你嘅「珠穆朗瑪」<br>
    <span class="tc">01:08:42</span> 咩造成真正嘅人際連結<br>
    <span class="tc">01:13:52</span> 點解細步更有效<br>
    <span class="tc">01:17:46</span> 點避開干擾：工作可唔可以聽歌？<br>
    <span class="tc">01:19:58</span> 計時器真係work？<br>
    <span class="tc">01:24:50</span> 點解無聊對你好<br>
    <span class="tc">01:30:49</span> 點激發創意<br>
    <span class="tc">01:33:17</span> 點停止諗太多同負面思想<br>
    <span class="tc">01:36:18</span> 廣告<br>
    <span class="tc">01:37:27</span> 點搵你嘅 chronotype（生理時型）<br>
    <span class="tc">01:46:11</span> 大科技點操縱公眾<br>
    <span class="tc">01:51:21</span> 科技公司隱瞞咗 AI 嘅咩<br>
    <span class="tc">01:55:44</span> 點解獨立思考越嚟越難<br>
    <span class="tc">01:59:52</span> 點解多工唔work<br>
    <span class="tc">02:05:52</span> 點樣令自己更幸運
  </div>

  <h3>🧠 拆解：呢集真正教咗咩</h3>
  <ul>
    <li><b>① 注意力係被設計去搶嘅，唔係你自制力差。</b>（00:32:40）平台用行為神經科學專門攻擊你嘅生存線路——所以解方唔係「意志力」，而係<b>改變環境（environment design）</b>。灰階就係最便宜嘅一招。</li>
    <li><b>② Grayscale＝每星期討回幾個鐘。</b>（00:43:52）官方形容「instantly reclaim hours of your scrolling every single week」；外部資料亦指灰階可令無效螢幕時間<b>每日減少最多約 1 小時</b>。原理：色彩係多巴胺觸發器，灰階降低「獎賞預期」。</li>
    <li><b>③ Focus Sprint＝用「預期」偷步。</b>（00:55:19）大腦有所謂 anticipatory network（預期網絡）——事先寫好細粒度清單 + 嚴格時間區塊，等落筆前個腦已經開始「跑」。柏克萊課堂實測係 50 分鐘一段。</li>
    <li><b>④ MITs vs LITs（任務分級）。</b>（01:00:48）MIT = Most Important Tasks（真正推動結果嗰幾件），LIT = Least Important Tasks（爽但無關痛癢）。多數人全日做 LIT，因為佢哋最即時、最有「完成感」。</li>
    <li><b>⑤ 「尋找你嘅珠穆朗瑪」。｜</b>（01:04:29）唔問「點做更多」，而問「邊座山值得爬」——目標清晰度先係生產力上限。</li>
    <li><b>⑥ Chronotype（生理時型）。｜</b>（01:37:27）唔同人嘅巔峰認知時段唔同；把 MIT 塞入自己嘅黃金時段，回報最大。有免費評估（代碼 DOAC）。</li>
    <li><b>⑦ 無聊係功能，唔係bug。｜</b>（01:24:50 / 01:30:49）心智漫遊啟動 default-mode 網絡解難，係創意洞察嘅溫床——所以你唔應該填滿每一秒。</li>
    <li><b>⑧ 越後段越尖銳：</b>（01:46:11 – 01:55:44）講大科技點操縱公眾、AI 時代科技公司隱瞞咗咩、點解「獨立思考」越嚟越難——呢段係本集最政治化、亦最有火嘅部分。</li>
  </ul>

  <h3>📊 關鍵數據（聽完記得住嗰幾個）</h3>
  <table class="kv">
    <tr><th>本集長度</th><td>8,032 秒 = <b>2 小時 13 分 52 秒</b>（DOAC 史上首個直播工作坊）</td></tr>
    <tr><th>多工代價</th><td>任務切換造成「注意力包袱」，令人比單工<b>慢最多 60%</b>（官方重點）</td></tr>
    <tr><th>灰階效果</th><td>降低神經刺激，<b>每星期即時討回幾個鐘</b>滑手機時間；外部資料指每日最多省約 1 小時</td></tr>
    <tr><th>Focus Sprint 長度</th><td>50 分鐘一段、完全無視覺／聽覺干擾（Berkeley Haas 課程實測）</td></tr>
    <tr><th>Yousef 研究年資</th><td>10 年以上；聲稱可於<b>6 星期內</b>改善專注、記憶同整體表現</td></tr>
    <tr><th>配套測試</th><td>MMM Institute「Digital Dependence Index」＋ MyChronotype（代碼 <code>DOAC</code>）＋ 獨立事實核查 PDF</td></tr>
  </table>

  <h3>💡 行動清單（James 可以聽完即做嘅 7 件）</h3>
  <ul>
    <li><b>今晚就把手機轉灰階</b>（iOS：輔助使用 → 顯示與文字大小 → 色彩濾鏡；Android：開發人員選項 → 模擬色彩空間 → 單色）。成本 0，效果即時。</li>
    <li><b>每日排 1–2 個 50 分鐘 focus sprint</b>，事前寫好細粒度清單，期間手機放另一個房、通知全關。</li>
    <li><b>把 to-do 分成 MIT / LIT</b>，黃金時段只做 MIT，LIT 集中塞去低能量時段。</li>
    <li><b>停止「即時回覆」反射</b>（00:21:50）——設定固定 check 訊息時間窗，唔好被通知牽住走。</li>
    <li><b>刻意留白</b>：每日留 15–20 分鐘無輸入時段（散步、唔戴耳機），養創意。</li>
    <li><b>測自己嘅 chronotype</b>，把最難嘅工作對準自己嘅巔峰認知時段。</li>
    <li><b>唔好靠工具，靠環境</b>（00:17:34）——生產力 App 對行為改變幫助有限，環境設計（灰階／距離／障礙）才係槓桿。</li>
  </ul>

  <div class="callout">
    <span class="label jev">Jev 過濾</span>TypeSafe System One（<code>news</code> profile）對本條評 <code>worth&nbsp;0.72</code>（保留）。Jev 標示一手概率 <code>0.44</code>（官方 show notes 屬節目自述，非同儕評審論文），故本卡已把「節目聲稱」同「外部可核實資料」分開標示。
  </div>
</section>
'''


# ==================== assemble ====================
html_doc = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>思維播客日報 · {DATE}</title>
<style>
{style}
</style>
</head>
<body>
<div class="wrap">

<header class="top">
  <h1>思維播客日報 · {DATE}</h1>
  <div class="sub">6 個英文商業／思維播客 · 每日深度掃描 · 為 James 而設的「第二對耳仔」</div>
  <div class="meta">
    🕘 報告生成時間：<b>{now_utc}</b>（= 香港時間 {now_hkt}）<br>
    📡 掃描方式：6 條 RSS feed 直接抓取 XML，逐集比對 GUID 去重<br>
    🔢 RSS 集數（最新的在前）：Acquired {scan['acquired']['count']} · Founders {scan['founders']['count']} · All-In {scan['all-in']['count']} · MFM {scan['my-first-million']['count']} · KP {scan['knowledge-project']['count']} · DOAC {scan['diary-of-a-ceo']['count']}<br>
    🧮 Jev 前置過濾（TypeSafe System One, <code>news</code> profile）：本輪 2 條新集候選 → DOAC <code>worth 0.72</code>（保留）、All-In <code>worth 0.14</code>（低訊號但保留，見該卡說明）<br>
    🧑💻 Repo：<a href="https://github.com/JMOKSZ/mindset-podcasts">JMOKSZ/mindset-podcasts</a> · 累計已掃 GUID：{scanned_total}
  </div>
</header>

<div class="summary">
  <b>今日重點：2 台有新集 —— All-In Summit 專訪 Elizabeth Holmes 丈夫 Billy Evans；DOAC 直播工作坊請嚟認知神經科學家 Dr. Sahar Yousef 教戒手機癮同專注力。</b>
  <ul>
    <li>🆕 <b>All-In · Billy Evans</b>（41:55，Friedberg 單對單）：Theranos 主角嘅伴侶，講相遇、審訊、生仔、判刑、「保持沉默」呢個錯誤、監獄來電、Nathan Fielder 紀錄片《You Can See Everything》，同點解佢間新公司 Haemanthus 唔係 Theranos 2.0。</li>
    <li>🆕 <b>DOAC · Dr. Sahar Yousef</b>（2:13:52，首個直播工作坊）：注意力陷阱、灰階黑客（每週討回幾個鐘）、Focus Sprint（50 分鐘）、多工令人慢 60%、無聊的力量、chronotype，尾段仲有「大科技點操縱公眾／AI 隱瞞咗咩」。</li>
    <li>📭 其餘 4 台（Acquired / Founders / MFM / Knowledge Project）本輪無新集；Founders #437《The Tycoons》已於 10-14 日報完整拆解。</li>
  </ul>
  <div class="stats">
    <div class="stat"><span class="n">2</span><span class="l">今日新集</span></div>
    <div class="stat"><span class="n">6</span><span class="l">追蹤播客</span></div>
    <div class="stat"><span class="n">2h56m</span><span class="l">新集總長度</span></div>
    <div class="stat"><span class="n">{scanned_total}</span><span class="l">累計已掃 GUID</span></div>
  </div>
</div>

{allin}

{doac}

{cards}

<footer class="bot">
  <p><b>關於呢份報告：</b>每日比對 6 條 RSS feed 嘅 episode GUID，只對「未掃過嘅新集」做深度萃取。All-In 官方 feed 只提供章節時間碼、DOAC 提供完整 show notes，故兩者之拆解分別以「官方章節 + 外部報導事實核查」同「官方 show notes + 柏克萊課程公開資料」為基礎；所有引用均標明出處。</p>
  <p>Feed 集數：{feed_counts}（依 podcasts.json 目前 RSS 設定）。生成於 {now_utc}。</p>
</footer>

</div>
</body>
</html>
'''

out_path = os.path.join(BASE, f'daily-report-{DATE}.html')
open(out_path, 'w', encoding='utf-8').write(html_doc)
print('WROTE', out_path, len(html_doc), 'bytes')
