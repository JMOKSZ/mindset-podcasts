#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, subprocess, html

BASE = "/root/.openclaw/workspace/mindset-podcasts"
STYLE = open("/tmp/prev_style.css").read()

now = subprocess.check_output(["date", "-u", "+%Y-%m-%d %H:%M UTC"]).decode().strip()
today = "2026-11-26"

DOC = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>思維播客日報 · {today}</title>
{STYLE}
</head>
<body>
<div class="wrap">

<header>
  <div class="kicker">Mindset Podcast Daily · Deep Scan</div>
  <h1>國王回來了，<br>而你的數碼身分正在被拍賣</h1>
  <p class="date">{today} · 星期四</p>
  <div class="meta">
    掃描 <b>6</b> 個 feed ｜ 新集數 <b>2</b> ｜ 總音頻長度 <b>約 2 小時 37 分</b><br>
    生成時間：<b>{now}</b> ｜ 方法：RSS 全量比對 GUID → 逐集抓取官方 show notes → 以節目原聲字幕交叉核實
  </div>
</header>

<div class="stats">
  <div class="stat"><div class="n">6</div><div class="l">FEEDS SCANNED</div></div>
  <div class="stat"><div class="n">2</div><div class="l">NEW EPISODES</div></div>
  <div class="stat"><div class="n">157</div><div class="l">MINUTES OF AUDIO</div></div>
  <div class="stat"><div class="n">4</div><div class="l">NO UPDATE</div></div>
</div>

<p class="lede">今日兩集，剛剛好是兩個極端。一邊是 <em>My First Million</em> 兩條友在感恩節家族聚會之間，用一個虛構式嘅「Jensen 回歸」講透三件事：CEO 幾時變成公眾人物、你嘅組合應該點樣承受「自己睇錯」、同埋點解大部分人唔係能力唔夠，而係<em>連盤數都未計過</em>。另一邊，<em>Diary of a CEO</em> 請來道德黑客 Ryan Montgomery，用 20 分鐘即場起底 Steven Bartlett 做開場——然後用一個鐘帶你入去一個比恐怖片更難受嘅真實世界：764 教派如何喺 Roblox、Discord 上系統性獵殺細路。兩集都唔係「聽完就算」，而係會改變你下星期某個決定嘅那種。</p>

<div class="note">
  <b>今日三個真正值得帶走的東西：</b><br>
  ① 「與其迫自己由 4 分變 7 分，不如把你的錢和時間押在 6、7 分的人身上」——Shaan 對 Pete Carroll 競爭力尺度的實用結論。<br>
  ② 「你唔係冇錢，你係未計過條數」——9 個月 runway 係一條小學算式，唔係一個階級問題。<br>
  ③ 飛航模式<strong>唔會</strong>關藍牙；你屋企嘅智能燈膽，可能係攻擊者進入你內網的後門。
</div>

<h2 class="section">Episodes · 深度萃取</h2>
<div class="rule"></div>

<!-- ============ MFM ============ -->
<div class="card">
  <div class="kicker2">My First Million</div>
  <h3>#885 we need to talk about Jensen <span class="badge">NEW · 51:42</span></h3>
  <div class="byline">Sam Parr &amp; Shaan Puri ｜ 2026-11-25 ｜ 感恩節特輯 · 閒聊密度極高的一集</div>

  <dl class="epmeta">
    <dt>主題</dt><dd>Jensen Huang 回歸 Nvidia 的治理風暴；Shaan 的組合拆解；Pete Carroll 的 1–7 競爭力尺度；100 歲人生與 sabbatical；Profit First 的個人版</dd>
    <dt>嘉賓</dt><dd>無嘉賓。兩位主持互相拆解，反而係今年最坦白的一集</dd>
    <dt>性質</dt><dd>投資哲學 + 人生設計 + 一點點公司治理八卦</dd>
  </dl>

  <h4 class="sub">一、Jensen 回歸：一場「Jenga」式的公司治理實驗</h4>
  <p>節目開場的設定很魔幻：Jensen Huang 重返 Nvidia 出任 CEO，市場即刻狂歡，NVDA 單日大漲 <strong>32%</strong>，相當於帳面市值進帳約 <strong>一萬億美元</strong>。Shaan 自爆上星期五同幾個朋友食飯，眾人一致認為「他一定會回來、股價被低估」，結果他買了一大批——今朝起身見到 Vince McMahon 表情符號（他的「大升」暗號）先知道發生咩事，笑稱擔心被當成內幕交易。</p>
  <p>Sam 接著講出本集最靚的一個比喻——<strong>Jenga theory</strong>：他以前返工時發現，辦公室裡大部分人都是可以抽走的積木，抽走整座塔都唔會冧；但總有一兩塊是承重位，一抽就全倒。「Jensen 就是那塊。」Nvidia 股價在事發前 30 日已跌 <strong>30–40%</strong>，其中一大跌就是消息公布當日。</p>
  <p>兩人把「應不應該走」拆成控方與辯方：</p>
  <ul>
    <li><strong>控方（不應下台）：</strong>與直屬下屬的婚外情屬違反行為準則，但雙方自願，歷史上權力男性的私德問題極少真正令其下台；更重要的是決策速度——「咁快就走，根本無可能做完調查」，董事會更像是自保。</li>
    <li><strong>辯方（應該下台）：</strong>若他明知而繞過對華出口管制，或事件會令董事會承受法律風險（節目提到董事會缺乏 D&amp;O 保險的曝險），那辭職是切割風險的唯一方法。</li>
    <li><strong>最尖銳的一點：</strong>Nvidia 的產品「重要到某些國家係法律禁止賣」——Sam 一句：「這是最好的營銷。」</li>
  </ul>
  <p>Shaan 引述《華爾街日報》報道，指涉事助理 Alice Wong 的丈夫在群組中吹噓妻子的角色，並有連串疑似「仙人跳」式的計劃；報道又指其丈夫在中國國資背景支持下建立數據中心生意。兩人都強調這些是<strong>報道與傳聞，不是定罪</strong>——但這正好帶出本集真正的問題。</p>

  <blockquote>
    <p>「如果你係一間美國 top 20 公司嘅 CEO，你基本上同一個政治人物一樣有權力。你影響美國安全、政治、經濟，有時仲多過政治人物。但有趣嘅係——你唔係選出嚟嘅。」</p>
    <cite>Sam Parr，談 CEO 為何突然變成「公眾人物」</cite>
  </blockquote>

  <p>兩人的歷史對照很精彩：JFK 的年代，記者知道一切但不寫；直到 Gary Hart（1987 年「Monkey Business」遊艇照）之後，傳媒才確立「私德與公職有關」的新規則。Sam 的結論不是道德判斷，而是結構性的：科技 CEO 現在享有明星級關注度，同時也承受明星級的私生活審查——而他們當初簽約時，無人告知這條款。</p>

  <h4 class="sub">二、Shaan 的組合：這不是選股，是「收藏」</h4>
  <p>Shaan 公開了自己的資產配置（只計流動資產）：</p>
  <table>
    <thead><tr><th>類別</th><th class="num">比例</th><th>說明</th></tr></thead>
    <tbody>
      <tr><td>S&amp;P 500</td><td class="num">約 12–13%</td><td>純指數</td></tr>
      <tr><td>Berkshire Hathaway</td><td class="num">約 12–13%</td><td>「半個指數」——一籃子防守型公司</td></tr>
      <tr><td>個股</td><td class="num">約 60%</td><td>Amazon、SpaceX、Tesla 為主，較細倉位有 Meta、Eli Lilly</td></tr>
      <tr><td>非個股（T-bills 等）</td><td class="num">約 40% 區間</td><td>與上列部分重疊計算，重點是「唔係單一股票」</td></tr>
    </tbody>
  </table>
  <p>方法論只有兩個字：<strong>conviction（信念）</strong>。倉位大小要大到「如果睇錯，唔會實質改變我的人生」，但又要大到「如果睇啱，值得」。他用 SpaceX 做例子：買入價是上市後插水後的「low hundreds」，他認為十年後 SpaceX 值 <strong>10–15 萬億美元</strong>，因為「最大護城河、最強順風、由史上最強創業者經營」。短期升跌完全不影響這個判斷。</p>
  <p>Sam 則完全相反：<strong>85% 指數、15% 債券、1–2% 個股</strong>，而且只買過兩隻——Oscar（見完 Mario 覺得他勁）和 Coinbase（看完 Brian Armstrong 訪問）。他連上週 S&amp;P 跌了都是今朝才知道。</p>
  <p>兩人都引用 Buffett 的「20 孔打孔卡」：一生只准做 20 次買賣決定，你會謹慎得多。Shaan 把它升級成一句更漂亮的框架：</p>
  <blockquote>
    <p>「我是一個 exceptional equity 的收藏家。就像藝術收藏家想要一幅畢卡索、一幅莫內——作為投資者，問題是：哪些公司是世界級、真正例外的？然後你怎樣持有它 10 年、20 年？」</p>
    <cite>Shaan Puri</cite>
  </blockquote>
  <p>還有個很實用的小工具：他做了一個 Mac 小 app，只顯示一個表情符號——哭臉 Jordan = 差日、Obama = 正常、Vince McMahon = 大升——刻意不讓自己看到數字。他試過整整一年不看組合。</p>

  <h4 class="sub">三、Pete Carroll 的 1–7 分：你在第幾分？</h4>
  <p>本集最有殺傷力的一段。Sam 引述 Pete Carroll（Seahawks 教練）的競爭力評分，Seahawks 的球探部門用 1 到 7 分，歷史上只有<strong>兩三個球員</strong>拿過 7 分：</p>
  <table>
    <thead><tr><th class="num">分數</th><th>定義</th></tr></thead>
    <tbody>
      <tr><td class="num">1–2</td><td>勉強生存，無乜好講</td></tr>
      <tr><td class="num">3–4</td><td>有競爭力，但動力來自<strong>外部</strong>：錢、地位、名聲、結果</td></tr>
      <tr><td class="num">5</td><td>內部驅動，自己個世界打理得井井有條</td></tr>
      <tr><td class="num">6</td><td>真正嘅料：唔理人點睇，做自己要做嘅事，教練只需讓開</td></tr>
      <tr><td class="num">7</td><td>唔止自己最大化，仲<strong>一定要帶人一齊去</strong>應許之地</td></tr>
    </tbody>
  </table>
  <p>Sam 的反應極度誠實：「我聽完即刻問自己喺邊——然後我很嬲，因為我知道我是 4。」他補一句更狠的：「你想爬山是為了看世界，還是為了讓世界看見你？」</p>
  <p>Shaan 沒有安慰他，反而給出一個更現實的解法：<strong>你不需要變成 7。</strong></p>
  <blockquote>
    <p>「你作為一個 4，應該做的是：讓自己身邊圍繞 5、6、7 分的人，投資他們、聘請他們，然後搭他們的順風車去應許之地。你可以享受你美好的 4 分人生。」</p>
    <cite>Shaan Puri</cite>
  </blockquote>
  <p>但他同時補上代價：「你不可能由 4 分變成 7 分而沒有成本。能量守恆——那能量是從別的地方轉換過來的。」他現階段選擇在 Lake Tahoe 陪小朋友滑雪整雪人，而不是去狩獵下一個投資。「如果這意味著我是 4 分或 4.5 分，那就這樣吧。我要的是人生 10 分。」</p>

  <h4 class="sub">四、100 歲的人生，與「計數」的尊嚴</h4>
  <p>Sam 介紹《The 100-Year Life》：活到 100 歲對這一代人不再離奇，真正的問題是<strong>退休年齡可能推到 80 歲</strong>，而我們的「人生軟件」仍然是「21 歲成年、30 歲結婚、60 歲退休、80 歲死」。他認為會出現一個巨大的市場與文化問題：如何在一段拉長了的人生裡，仍然覺得自己活得「好」。</p>
  <p>Shaan 由 Tim Ferriss《4-Hour Workweek》講到 Sam Altman 的兩年 sabbatical（OpenAI 之前）：讀生物學、核工程教科書、幫朋友的公司、順手投資了 Stripe 和 Airbnb。Altman 的原話（Shaan 轉述）是：最難受的是<strong>「要忍受一段你沒有一個令人印象深刻答案的時期」</strong>。Shaan 預言有人會把「sabbatical」重新包裝——叫「實驗期」、「探索期」、「充電期」——因為人們需要的只是<strong>air cover（名義上的許可）</strong>。</p>
  <p>然後是全集最實用的一段：Sam 直接反駁「這是特權」的說法。</p>
  <blockquote>
    <p>「創業者的標記不是聰明，是 resourcefulness——是取得資源的能力。你唔識寫 code，就去找技術共同創辦人；你冇錢，就去募資。大部分人從來沒有真正計過條數。」</p>
    <cite>Shaan Puri</cite>
  </blockquote>
  <p>他即場示範這條「小學算式」：假設你要 9 個月 runway，租金 3,000 美元一個月，加上其他開支——乘出來就是一個具體數字。你可能銀行裡已經有；或者你可以借、可以儲、可以搬回家住半年。他講了 Michael Birch 的故事：一位年薪 20 多萬美元的 iOS 工程師想創業但不停找藉口，Birch 一層層剝走藉口——「去募資」「想個 idea」「用你兩星期假期去想，不是去旅行」「你父母住哪？搬回去六個月」。最後工程師發現，他想要的其實是富人直接開張支票，而不是那個更值錢的東西：創業者的心態。</p>

  <h4 class="sub">五、兩個可以今晚就用的理財動作</h4>
  <p><strong>「Live like you have a car note.」</strong> Sam 在 YouTube 看到一個開漫畫店的黑人小生意人，儲了 10 萬美元創業。記者問他點儲，他說：「我只是當自己仍然有車貸。」他的車其實早已供完，但他每個月仍然把原本 1,500 美元的車貸轉去另一個戶口，連續兩三年。Sam 的評語：「每個月我都在供車，但那架車是我的夢想。」</p>
  <p><strong>Profit First（Mike Michalowicz）。</strong> 大部分人是「收入 − 支出 = 利潤」，結果利潤永遠是剩下那一點。正確做法是倒過來：收入一到，先撥 20% 去利潤戶口、再撥稅款戶口，剩下的才是支出預算。開五個銀行戶口，強迫自己在有限預算內想辦法。個人版就是：出糧第一件事，把錢轉去「未來的我 LLC」，然後靠剩下的生活。</p>

  <blockquote>
    <p>「不要讓儲蓄成為你付完所有垃圾之後剩下的東西。先決定你要多少，先撥走它，然後讓你的開支住在剩下來的那個空間裡。」</p>
    <cite>Shaan Puri</cite>
  </blockquote>

  <h5 class="mini">對 James 的啟示</h5>
  <ul>
    <li><strong>組合層面：</strong>如果你有 60% 以上集中在少數個股，用 Shaan 的測試問一次——「如果這間公司明天消失，我會唔會要賣樓？」如果會，倉位太大，同信念無關。</li>
    <li><strong>時間層面：</strong>「計數」這個動作，比「搵理由」便宜得多。今晚用 10 分鐘寫下：9 個月唔做正職，實際要幾錢？寫完通常會發現，恐懼大過數字。</li>
    <li><strong>人層面：</strong>如果你自認 4 分，唔需要自責。把 20% 的時間和金錢，刻意放在 6、7 分的人身上——這是唯一可持續的「借力」。</li>
  </ul>
</div>

<!-- ============ DOAC ============ -->
<div class="card">
  <div class="kicker2">The Diary of a CEO</div>
  <h3>The Hacker Who Hunts Predators: Do These 3 Things Before You Get Hacked! <span class="badge">NEW · 1:45:29</span></h3>
  <div class="byline">Steven Bartlett × Ryan Montgomery（aka 0day）｜ 2026-11-26 ｜ 前半是實用保安，後半是必須被看見的黑暗</div>

  <dl class="epmeta">
    <dt>主題</dt><dd>你的數碼足跡有多赤裸；20 分鐘 OSINT 起底示範；智能家居／Wi-Fi／汽車／充電線的實體攻擊；764 教派如何系統性獵殺兒童；家長與普通人可以做的十件事</dd>
    <dt>嘉賓</dt><dd>Ryan Montgomery — 道德黑客、Pentester 創辦人、Sentinel Foundation 反人口販運合作者；9 歲自學入侵、11 歲接觸毒品、15 歲海洛英成癮、多次入獄，21 歲離開賓州後創辦三間戒治機構並出售</dd>
    <dt>份量</dt><dd>資訊密度極高，但後三分之一含極度令人不安的兒童剝削描述。節目組已在開頭與章節中加上求助熱線</dd>
  </dl>

  <h4 class="sub">一、開場即處刑：20 分鐘找到了什麼</h4>
  <p>Ryan 用一個只供執法機構使用的工具「OSI Pilot」，即場對 Steven 做開源情報調查。起點只是一個舊 email——來自某次資料外洩。然後是一條完美的攻擊鏈：</p>
  <ol>
    <li>從外洩資料拿到一個<strong>獨特密碼</strong>；</li>
    <li>用「反向密碼搜尋」找出所有用過同一密碼的帳號 → 解鎖更多 email；</li>
    <li>由 email 關聯到出生日期、電話號碼；</li>
    <li>用反向人臉辨識，把他不同時期的照片歸戶；</li>
    <li>結果：12 年前去過的健身房、童年住過的屋、一張早已下架的鐵路卡聯署、多個舊帳號、部分舊密碼。</li>
  </ol>
  <p>整件事 <strong>20 分鐘</strong>，全部是公開或外洩資料。Ryan 的母親——一個一生未用過電腦的人——同樣有數碼足跡：藥房登記的電話、年輕時去過的賭場（MGM 外洩）、資料被數據中間商轉賣。<strong>「你唔用電腦，唔等於你冇足跡。」</strong></p>
  <p>他點名 2024 年的 National Public Data（NPD）外洩：<strong>28 億筆記錄</strong>曝光，而美國只有約 3 億人。他的判斷是：如果你超過 30 歲，你住過的每一個地址、電話、完整社會安全號碼，幾乎肯定已在外面。免費查詢方法是 npd.pentester.com；查到中招，第一步是<strong>凍結信用</strong>（freeze credit）——它不會影響你現有信用，只是阻止別人用你的名開卡、借貸、買車。</p>

  <blockquote>
    <p>「我不能誠實地告訴你，你的手機是安全的。但另一方面，大部分人完全不知道有陌生人在看著他們。」</p>
    <cite>Ryan Montgomery</cite>
  </blockquote>

  <h4 class="sub">二、枱面上的 gadget：每一個都便宜、易買、有效</h4>
  <table>
    <thead><tr><th>裝置</th><th>做什麼</th><th>你應該點應對</th></tr></thead>
    <tbody>
      <tr><td>Biscuit（3D 打印小盒）</td><td>Wi-Fi／藍牙攻擊：deauth 踢你落線、捕捉四步握手包、離線爆破（約 20,000 次／秒）、藍牙通知洪水令手機「廢掉」</td><td>路由器開 WPA3；但大部分路由器处于 transient mode 會降回 WPA2，實際上「冇乜可以做」</td></tr>
      <tr><td>假熱點（captive portal）</td><td>30 秒內建立一個叫「flight story free」的開放網絡，弹出假 Google 登入頁，即場拿到 Steven 的 email 與密碼</td><td>公共 Wi-Fi 永遠用 VPN；任何「登入後才可使用」的頁面都要當成可疑</td></tr>
      <tr><td>智能燈膽／智能插頭</td><td>出廠即連中國雲端伺服器；被改裝後可掃內網、嗅探未加密流量、直接看你的 IP camera，甚至不需要你的 Wi-Fi 密碼</td><td>把 IoT 裝置放在獨立 VLAN；不要與手機、電腦同網段</td></tr>
      <tr><td>「不是薄荷糖」的裝置</td><td>放在袋裡即可令 Ring、門鈴、IP camera 離線</td><td>實體安全：重要場所定期掃描；不要讓陌生人單獨留在辦公室</td></tr>
      <tr><td>OMG 充電線</td><td>內建迷你電腦，300 字元／秒注入鍵盤輸入；可 geofence 自動執行、用 Shortcuts 偷走全部相片／聯絡人再自我刪除</td><td>只用自己買的線；公共 USB 口一律不用</td></tr>
      <tr><td>Chameleon Ultra</td><td>讀寫 RFID／NFC：複製酒店房卡、門禁扣、甚至隔著銀包讀信用卡</td><td>用真正的 RFID 屏蔽銀包（他用的一個樣辦失敗了，提醒你要測試）</td></tr>
      <tr><td>KARR 汽車警報漏洞</td><td>舊 app 內藏明文「萬能鑰匙」，影響約 <strong>220 萬</strong>架美國汽車；可解鎖、鎖車、熄匙、響號</td><td>查自己車是否有 KARR，更新至最新 firmware</td></tr>
      <tr><td>Flock 車牌攝影機偵測器</td><td>定位街上的 ALPR 攝影機；無人機 Remote ID 亦令操控者位置、姓名可被查出</td><td>理解「私有監控 + 政府購買數據」的灰色地帶</td></tr>
    </tbody>
  </table>

  <p>幾個特別值得記住的細節：</p>
  <ul>
    <li><strong>飛航模式不會關藍牙。</strong> 你以為斷網就安全，但藍牙仍然開著，附近的人仍然可以連上來。要真正關掉，必須入 Settings → Bluetooth 手動關。</li>
    <li><strong>法國三間血庫被入侵</strong>，血漿冷藏櫃的溫度被改成 230°F（約 122°C）；歐洲超市的聯網雪櫃亦曾被攻擊，造成數百萬計的損壞與食物報廢。「物聯網」不是方便，是攻擊面。</li>
    <li><strong>會話 cookie 比密碼更危險。</strong> 攻擊者偷到你的 session cookie，就可以直接「變成你」登入，<em>繞過密碼、2FA、甚至 YubiKey</em>。這就是為什麼資料外洩不只洩密碼。</li>
    <li><strong>Mobile Advertising ID</strong> 被賣給數據中間商，再賣給執法機構或任何人；軟件可以把你的生活模式畫成熱點圖——「你每個星期幾點去邊間店」。</li>
  </ul>

  <blockquote>
    <p>「我唔係什麼陰謀論者。但我研究過這些裝置點樣同互聯網溝通——幾乎全部都是同中國的雲端伺服器溝通。你叫燈膽變紅，訊號不是由手機直接去燈膽，而是手機 → 中國 → 你路由器 → 燈膽。」</p>
    <cite>Ryan Montgomery</cite>
  </blockquote>

  <h4 class="sub">三、AI 與保安：不是補 patch 的時代了</h4>
  <p>Steven 引述 Sam Altman 近期的說法：AI 意味著我們要徹底重新思考「網絡安全」是什麼。Ryan 同意，但加了一個很重要的區分：</p>
  <blockquote>
    <p>「我不完全同意它叫『人工智慧』。它很擅長把已有的模式拼在一起。你問它怎樣開這個盒，它會從訓練資料裡找最接近的答案——但它不能<em>真正創造</em>一種前所未見的開法。當它不知道，它就會 hallucinate。」</p>
    <cite>Ryan Montgomery</cite>
  </blockquote>
  <p>但同一個能力，用在找漏洞上，就是另一回事：模型可以在極短時間內找出人類幾年都找不到的 bug。「我們不再可能把所有 bug 補完。我們要做的，是用同一種技術建立一種全新的防禦盾。」他認為真正的分水嶺是 AGI——「一個沒有良知的智能，究竟算不算智能？」</p>

  <h4 class="sub">四、764：這一集真正的主菜</h4>
  <p>節目後半段，Ryan 打開電腦，展示他兩年來協助 FBI 調查的資料。他事先聲明：不會講出任何加害者或受害者的名字，因為<strong>「他們就是想要知名度」</strong>。</p>
  <p><strong>764 是什麼：</strong>一個由德州一名少年創立的虛無主義撒旦教派（nihilistic satanic cult），與多個分支合稱「the com」。FBI 已將它列為國內恐怖組織；<strong>58 個</strong>分局動員，<strong>500 多個</strong>目標正在調查中。集團有<strong>數百頁的教學手冊</strong>，教成員如何在 Roblox、Minecraft、Discord、X、Reddit、Instagram 上尋找及操控受害者。</p>
  <p><strong>獵殺流程（手冊原文，Ryan 逐段讀出）：</strong></p>
  <blockquote>
    <p>「Grooming 是一種非常常用且容易取得控制權的方法。通常，當你成功 grooming 你的受害者，她會完全照你說的做，無論是什麼。你必須讓你的受害者以為你是她的神，你擁有她，而且永遠都會。」</p>
    <p>「你可以在 Roblox 等遊戲，或 X、Reddit、Instagram 等社交平台尋找受害者……叫她公主、親愛的、甜心。女性喜歡被叫暱稱。傾談一段時間後，叫她做你女朋友，她很可能會答應。」</p>
    <p>「要成功 extort 一個女性，你必須擁有以下個人資料：地址、姓名、電話號碼、裸照。有了這些，你可以威脅把裸照傳給她的父母、swatting、公開個人資料。如果她不服從，就叫她做血簽、割自己、殺她的貓、或者自殺。」</p>
    <cite>764 外洩手冊，Ryan Montgomery 在節目中讀出</cite>
  </blockquote>
  <p>他們的口號是「content is content」——不接受淺層的「cat scratches」，要求<strong>深度疤痕、割上受害者自己的用戶名和集團名</strong>。受害者年齡可以是 8、9、10、11 歲。要加入私人頻道，新成員要提交「proof of crime」：縱火、傷人、殺動物的影片。</p>
  <p>節目播出了幾段已公開的影片：一名女孩被倒數 30 秒，威脅不剪掉馬尾就把裸照發出；一名父親在視像通話中撞破 27 歲男子，對方若無其事地要求「叫你個女掀衫」；以及最令人無法直視的一段——<strong>一名 13 歲男孩在直播中上吊身亡，聊天室裡的人在笑</strong>。Ryan 說，他在 Shawn Ryan 節目播出後，一名女孩在停車場用電纜自縊，直播聊天室的人說「如果她裸體吊死會更性感」。</p>

  <blockquote>
    <p>「我最大的成就不是拘捕了幾多個加害者。拘捕一千個，都不會令他們不存在。如果你令一個細路一開始就不成為受害者，我覺得你做了一件更好的事。」</p>
    <cite>Ryan Montgomery</cite>
  </blockquote>

  <h4 class="sub">五、家長與普通人真正可以做的十件事</h4>
  <p>這一節是全集的實用核心，我按可執行程度排序：</p>
  <ol>
    <li><strong>凍結信用</strong>（美國）：查 npd.pentester.com，中招就 freeze。這是最低成本、最高回報的一步。</li>
    <li><strong>關閉所有 app 的廣告追蹤</strong>（iOS：Settings → Privacy → Tracking）。</li>
    <li><strong>手機開 Advanced Data Protection + Lockdown Mode</strong>；重要帳號加 <strong>YubiKey</strong> 硬體金鑰。</li>
    <li><strong>藍牙要手動關</strong>，不要以為飛航模式萬能。</li>
    <li><strong>IoT 裝置獨立 VLAN</strong>；沒有 IT 知識就找人或用支援 VLAN 的路由器。</li>
    <li><strong>公共 Wi-Fi 一律 VPN</strong>；不要用公共 USB 充電口，自帶充電寶與線。</li>
    <li><strong>不要買來歷不明的便宜智能裝置</strong>——「便宜」不是唯一風險，但它是一個訊號。</li>
    <li><strong>家長：安裝監控軟件</strong>（他點名 Bark，無贊助），但更關鍵的是<strong>關係</strong>——如果小朋友怕你沒收電話，他出事時不會告訴你。</li>
    <li><strong>教小朋友說出實情</strong>：告訴他們這些集團存在、專挑脆弱的孩子、由遊戲與社交平台入手。無需恐嚇，但要具體。</li>
    <li><strong>對所有訊息保持懷疑</strong>：用 AI 檢查截圖、查域名有無串錯、視像／語音訊息都可能是 deepfake。他的公司曾因一封釣魚 email 損失 <strong>20 萬美元</strong>；DOAC 一名新員工第一週被冒充 Steven 的 email 騙去買 <strong>1,000 英鎊</strong>禮品卡。</li>
  </ol>

  <blockquote>
    <p>「你可以拘捕一千個掠食者，但只要你令一個細路不成為受害者，你就做了一件更好的事。預防，才是最大的成就。」</p>
    <cite>Ryan Montgomery</cite>
  </blockquote>

  <h5 class="mini">對 James 的啟示</h5>
  <ul>
    <li><strong>今晚做三件事：</strong>查一次 NPD／外洩（或本地 equivalent）；關掉手機 app 的廣告追蹤；把屋企的智能裝置搬去 guest network。三十分鐘內可完成。</li>
    <li><strong>如果你有小朋友或侄甥：</strong>與其沒收電話，不如建立「唔會被鬧」的匯報通道。764 的受害者幾乎全部是<em>不敢講</em>的孩子。</li>
    <li><strong>AI 保安的投資含義：</strong>Ryan 的判斷「防守要換模型，不是補 patch」意味著身份驗證（passkeys、硬體金鑰）、網絡分段、端點偵測會是長期需求——不是一次性熱潮。</li>
  </ul>
</div>

<h2 class="section">No Update · 最近無更新</h2>
<div class="rule"></div>

<div class="card slim">
  <div class="kicker2">Acquired</div>
  <h3 style="font-size:23px">最近無更新 <span class="badge grey">LAST: 2026-10-18</span></h3>
  <div class="lastknown"><b>最後一集：</b>Seinfeld ｜ 3 小時 50 分 ｜ 2026-10-18<br>
  上一集：The Home Depot（2026-09-13）｜ Disney: The Renaissance and the Empire（2026-08-09）<br>
  <span style="color:#7a6a58">註：Acquired 一向低頻、長篇，通常每 4–8 週一集。距今約 5.5 週，屬正常節奏。</span></div>
</div>

<div class="card slim">
  <div class="kicker2">Founders</div>
  <h3 style="font-size:23px">最近無更新 <span class="badge grey">LAST: 2026-11-17</span></h3>
  <div class="lastknown"><b>最後一集：</b>#440 The Most Inspiring Autobiography I've Ever Read: Born of This Land — Chung Ju-yung ｜ 49 分<br>
  上一集：#439 How Eiichiro Oda Works（2026-11-04）｜ #438 James Garfield's Extraordinary Rise（2026-10-26）<br>
  <span style="color:#7a6a58">註：David Senra 通常每週一集；上集距今 9 日，可能與美國感恩節週有關。</span></div>
</div>

<div class="card slim">
  <div class="kicker2">All-In</div>
  <h3 style="font-size:23px">最近無更新 <span class="badge grey">LAST: 2026-11-24</span></h3>
  <div class="lastknown"><b>最後一集：</b>CrowdStrike CEO: AI Cyberattack Wave, Hyperspeed Hacks, &amp; The Patching Problem ｜ 53 分 ｜ 2026-11-24<br>
  上一集：Anthropic Goes Public, Nvidia in Crisis, Markets Tank, Open Source Crackdown?（2026-11-20）｜ Databricks CEO: AGI Is Already Here（2026-11-17）<br>
  <span style="color:#7a6a58">註：昨日已掃描並深入拆解 CrowdStrike CEO 一集。今次無新集。</span></div>
</div>

<div class="card slim">
  <div class="kicker2">The Knowledge Project</div>
  <h3 style="font-size:23px">最近無更新 <span class="badge grey">LAST: 2026-11-19</span></h3>
  <div class="lastknown"><b>最後一集：</b>Bing Gordon: Learning From Bezos, Jobs, and Spielberg ｜ 2026-11-19<br>
  上一集：Jon McNeill: How Elon Musk Makes Decisions（2026-11-05）｜ [Outliers] K.C. Irving: Competing with Giants（2026-10-29）<br>
  <span style="color:#7a6a58">註：Shane Parrish 約兩週一集，下一集可能下週出現。</span></div>
</div>

<div class="closing">
  <h2 class="section" style="margin-top:0">一句總結</h2>
  <div class="rule"></div>
  <p>今日兩集其實講同一件事的兩面：<strong>權力與曝露是同一枚硬幣。</strong> Jensen 因為權力太大，私生活變成公共風險；你因為生活太數碼，連 12 年前去過的健身房都變成攻擊者的線索。分別只是——Jensen 有董事會和公關團隊處理，你只有你自己。<br><br>
  所以今日最實際的功課不是「學 Jensen」，而是 Ryan 的那句：<strong>預防，勝過事後補救。</strong> 今晚花三十分鐘，把自己的數碼足跡收窄一點；然後用 Shaan 的那條算式，計一次「如果我要 9 個月自由，實際要幾錢」。一個保護你，一個釋放你。</p>
</div>

<footer>
  資料來源：各節目官方 RSS feed（GUID 全量比對）、官方 show notes、以及節目原聲字幕逐段核實。所有引述均取自節目內容；涉及第三方報道與未經法庭裁定的指控，已於文中標明為「報道／傳聞」。<br>
  掃描時間：{now} ｜ 下一集更新：明日 09:53 UTC ｜ 專案：<a href="https://jmoksz.github.io/mindset-podcasts/">jmoksz.github.io/mindset-podcasts</a>
</footer>

</div>
</body>
</html>
"""

out = f"{BASE}/daily-report-{today}.html"
open(out, "w").write(DOC)
print("written", out, len(DOC), "chars")
