#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, datetime

BASE = "/root/.openclaw/workspace/mindset-podcasts"
CSS = open("/tmp/report_css.html", encoding="utf-8").read()

now = datetime.datetime.utcnow()
hkt = now + datetime.timedelta(hours=8)
STAMP = now.strftime("%Y-%m-%d %H:%M UTC") + " / " + hkt.strftime("%H:%M HKT")

HTML = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>思維播客日報 · 2026-11-10</title>
{css}
</head>
<body>
<div class="wrap">

<header>
  <div class="kicker">Mindset Podcasts · Daily Deep Scan</div>
  <h1>把 AI 從螢幕裡拖出來</h1>
  <p class="date">2026 年 11 月 10 日 · 星期二</p>
  <div class="meta">
    <b>掃描時間</b> {stamp}<br>
    <b>覆蓋</b> 6 個播客 · 6 條 RSS 全部 HTTP 200 · 共 2,837 集索引<br>
    <b>本期</b> 新集數 1 集（My First Million #880）· 其餘 5 個播客最近無更新<br>
    <b>萃取方式</b> RSS 全文 + 官方 shownotes + 完整英文逐字稿（38 分 21 秒，1,157 段）逐段讀完，非摘要轉述
  </div>
</header>

<div class="stats">
  <div class="stat"><div class="n">6</div><div class="l">播客來源</div></div>
  <div class="stat"><div class="n">1</div><div class="l">新集數</div></div>
  <div class="stat"><div class="n">8</div><div class="l">拆解賽道</div></div>
  <div class="stat"><div class="n">38<span style="font-size:15px">min</span></div><div class="l">逐字稿長度</div></div>
</div>

<p class="lede">今日只有一集，但這一集值得你整段聽——或者整段讀完這份報告。Shaan Puri 做了一份他稱為「如果我而家想靠 AI 致富，我會去邊」的簡報，逐頁講給 Sam Parr 聽。結論同全網 99% 的 AI 內容相反：<em>AI 嘅錢唔在 bits，在 atoms。</em>內容、SaaS、工具都係「race to the bottom」；真正未定價的，是藥、食物、戰爭、房屋、材料、自駕、海洋、人體硬件這八個「AI 落到實體世界」的賽道。</p>

<div class="note">
  <b>點聽：</b>想聽原聲，YouTube 版 38 分鐘（比 RSS 的 40:44 短，片尾廣告位剪掉），搜「AI will 10x these 8 industries in the next decade」。<br>
  <b>點讀：</b>下面按八個賽道逐個拆，每個賽道都有「他講咗乜 / 背後嘅數字 / 你可以點切入」。最後兩節是他離題但最有價值的一段：美國點解會贏，同一個「free agent 該點揀下一站」的練習。<br>
  <b>誠實提示：</b>Shaan 自己講明「我冇深入研究過任何一個」。呢個係一張<strong>方向圖</strong>，唔係投資建議。文中所有數字我都標明出處係「他說的」；有幾個我認為要打問號的地方，集中在〈批判性評估〉一節。
</div>

<h2 class="section">本期新集數 · 1 集</h2>
<div class="rule"></div>

<div class="card">
  <h3>What I'd build if I wanted to get rich with AI<span class="badge new">NEW</span></h3>
  <div class="byline">My First Million · Episode 880 · Shaan Puri &amp; Sam Parr</div>

  <dl class="epmeta">
    <dt>發布</dt><dd>2026-11-09 11:00 UTC（美東 11/9 早上）</dd>
    <dt>長度</dt><dd>40:44（YouTube 版 38:21）</dd>
    <dt>形式</dt><dd>Shaan 主講一份自製簡報，Sam 做聽眾兼吐槽</dd>
    <dt>主題</dt><dd>AI 在「實體世界」的八個賽道，以及一個職涯決策框架</dd>
    <dt>RSS</dt><dd>feed 第 919 集索引，本集 GUID 617e3102-dbaa-11f1-b3ad-ffb0a2346a74</dd>
    <dt>來源</dt><dd>官方 shownotes（章節＋公司連結）＋ YouTube 自動字幕全文</dd>
  </dl>

  <div class="verdict">
    <b>一句話：</b>當所有人都喺度用 AI 生成內容同寫 SaaS，真正的超額回報正在轉移到「要起工廠、要過 FDA、要造硬件」的行業——因為那些行業的瓶頸不是智力，是<strong>物理世界嘅摩擦</strong>，而 AI 剛好第一次開始能壓低那個摩擦。
  </div>

  <h4 class="sub">1. 開場：兩種互相矛盾的情緒</h4>
  <p>集數由 Sam 一句話定調，那句話幾乎是所有創業者今年的心裡話：</p>
  <blockquote>
    <p>“You were talking about moats, and as a person who likes the game of business — I don't like to get made obsolete.”</p>
    <cite>Sam Parr，開場第 10 秒</cite>
  </blockquote>
  <p>Shaan 把它拆成兩種同時存在的情緒：一種是「AI 乜都做得到，咁我仲可以做乜」；另一種是「AI 乜都做得到，身邊個個都喺度做勁嘢，我應該做得更多」。兩種情緒都指向同一個癱瘓狀態——<em>你坐在電腦前面，知道可以造任何東西，但唔知造乜</em>。</p>
  <p>然後他用 Anthropic 做對照，把焦慮具體化：</p>
  <ul class="tight">
    <li>他口中的 Anthropic 是「資本主義史上最快的生意」——約 5 年創造 <strong>~2 兆美元</strong>價值。</li>
    <li>七個共同創辦人、約 2,500 日，集體創造的淨值等於<strong>每日 9,600 萬美元</strong>。</li>
    <li>但創辦人團隊今天合計只持有公司約 <strong>2%</strong>（他與 Sam 在節目中互相確認的粗略數字）。</li>
  </ul>
  <p>最後那個數字是整集的隱藏伏筆：連親手造出史上最快增長公司的人，都被稀釋到 2%。所以「去唔去得切」這個問題本身問錯了——正確的問題是「去邊個球場」，而不是「點樣喺呢個球場贏」。這條線在最後 10 分鐘會開花結果。</p>

  <h4 class="sub">2. 核心論點：bits 係紅海，atoms 係藍海</h4>
  <p>他先引用（並故意誤植為）Michael Scott 的名言「Skate to where the puck is going」，然後給出全集最鋒利的一段判斷：</p>
  <blockquote>
    <p>“I think that using AI in the world of bits, which is basically like digital stuff, has very low returns. Anybody who's like ‘I'm using AI to make content’ — it's a race to the bottom there. I think using AI to make software, SaaS, make tools, is kind of a race to the bottom. Do it if it's just where your heart is, but to me, that's not where the opportunity is.”</p>
    <cite>Shaan Puri，約 3:05</cite>
  </blockquote>
  <p>他的推理鏈是這樣：任何「輸入是文字、輸出是文字／像素」的生意，邊際成本已經趨零，而邊際成本趨零的行業，利潤必然流向<strong>擁有需求端</strong>的那一方（平台、渠道、品牌），而不是生產方。相反，如果你做的東西需要<strong>工廠、監管批准、實體供應鏈、現場施工</strong>，AI 只幫你加速當中的「設計與搜索」環節，卻不會把整個行業商品化——因為瓶頸在物理世界，不在智力。</p>
  <p>所以他說「五年前該做的事是去 OpenAI、Anthropic 打工，或者去做 Runway、Midjourney、ChatGPT 那類東西。當時唔明顯，但少數人看到咗」。而他認為未來五年的「action」在以下八處。</p>

  <h4 class="sub">3. 八個賽道，逐個拆</h4>

  <h5 class="mini">① Drugs &amp; Miracles · 藥與奇蹟</h5>
  <p><strong>他講咗乜：</strong>起點是一條推特——「現正自行治好自己癌症的人」名單。第一個人是 GitLab 出身的一位工程師：用 AI 對自己的腫瘤做定序、跑候選藥物、合成化合物、然後自己服食，腫瘤縮小。Shaan 說這個人後來把流程做成一個可以登記的服務，Sam 補充「我一個患癌的朋友登記了，情況很好」。名單上還有另外七個人做類似的事。</p>
  <p><strong>背後嘅數字（他給的）：</strong>一款新藥傳統上要 <strong>10 年、20 億美元</strong>，失敗率 <strong>80–90%</strong>。正因為這三個數字，這個遊戲歷來只有某個規模以上的藥廠玩得起。</p>
  <p><strong>行業正在發生嘅事：</strong></p>
  <ul class="tight">
    <li><strong>Eli Lilly</strong> 被他形容為「lean in 得最狠」的藥廠——買算力買到像一間科技公司。他給的類比很精準：Citadel、Jane Street 自建數據中心去把 AI 用在金融，Lilly 就是把同一件事用在藥物。</li>
    <li><strong>Isomorphic Labs</strong>（Google 旗下）：Demis Hassabis 由 DeepMind 轉為全力投入，命题直接是「如何治好癌症」。</li>
    <li>Sam 提到前製作人 Ben 的個案：確診時預後極差，發推之後被一堆 AI 圈的人接上線，現在用上了相關療法，狀況明顯好轉。</li>
  </ul>
  <p><strong>你可以點切入：</strong>他給的建議很直接——「如果你係聰明人，加入其中一間，或者自己起一間。從來冇一個時刻比現在更適合做高影響力的事，因為技術窗口打開了，以前不可能得到的結果現在可能」。</p>
  <p><strong>我嘅判讀：</strong>這是八個賽道裡最不像「創業機會」、但最像「人才套利」的一個。真正的門檻不是算法，是<em>願意花 3–5 年與濕實驗室、臨床、監管打交道</em>。對香港／亚洲的讀者，切入點更可能是 CRO、生物資訊、臨床數據基建，而不是直接做藥。</p>

  <h5 class="mini">② Food Is Technology · 食物即技術</h5>
  <p><strong>他講咗乜：</strong>一家剛出 stealth 的 YC 公司 <strong>Nitroduck</strong>，用 CRISPR 改水果——更高產量、更好食、更有營養。他用一個很好的錨定講清楚這個行業有多「慢而巨大」：Honeycrisp 蘋果由育種到上市花了 <strong>20 年</strong>，而我們今天一年 365 日都買得到。</p>
  <blockquote>
    <p>“Where does the food come from, dude? … It's not just there. It comes from somewhere. Each one of these things is a genetic organism. And just like we're going to be applying biotech and AI to our bodies, we're going to be applying it to plant bodies.”</p>
    <cite>約 7:40</cite>
  </blockquote>
  <ul class="tight">
    <li><strong>David Friedberg</strong>（All-In 那位）被點名為最知名的實踐者：做新品種薯仔與粟米，賣的是更好的種子與作物，讓農民得到更好產量、風味與抗性。</li>
    <li>賽道不止種子：還包括用電腦視覺操作的新式農機——「new kinds of tractors」。</li>
  </ul>
  <p><strong>我嘅判讀：</strong>這一段 Shaan 講得最淺，但商業含金量可能最高。種子是有專利、有 recurring revenue、有極高轉換成本的生意（農民一旦轉品種，配套農藝一齊轉）。問題是監管週期以年計，不適合想要 12 個月見現金流的人。</p>

  <h5 class="mini">③ Warfare · 戰爭</h5>
  <p><strong>他講咗乜：</strong>他先自嘲自己對軍事的想像（坦克、士兵、船、戰機）是「fantasy」，用太太小時候幻想婚禮 vs 30 歲真實婚禮的比喻，說明現實與想像的落差。他認為真實的戰爭已經是<strong>無人機打無人機</strong>：便宜、可大量生產、一小塊金屬加自主飛行就可以造成巨大破壞，而對手可能派出極昂貴的裝備。</p>
  <ul class="tight">
    <li><strong>Anduril</strong>：他點名最明顯的受惠者。</li>
    <li><strong>Joe Lonsdale</strong> 投資的水下公司：他形容為「Anduril 的海軍版」。</li>
  </ul>
  <p>然後是全集最離奇的一段：兩人討論一次抓捕行動——行動在市中心進行、幾乎無人死亡，現場守衛事後聲稱「企喺度但郁唔到」，有人流鼻血、嘔吐、倒地。他們引述報導說是<strong>聲波或定向能武器</strong>，並提到 Trump 用 “discombobulator” 形容它。Sam 補一個親身經歷：三藩市一間由車房改成的硬件 coworking，晚上 11 點只剩一個人，那人正在造「可以從極遠距離把無人機打下來的雷射」，見到他第一句話是「你最好后退」。Sam 說：「我本來要去錄 podcast，突然想，而家錄好嗎？」</p>
  <p><strong>⚠️ 我嘅判斷：</strong>這一段是<strong>二手轉述＋未經證實</strong>（Jev 對本集的 primary_source 評分為 0.4，主要就是這類內容拉低）。當故事聽可以，千萬不要當技術現狀引用。真正可驗證的部分只有一個：廉價自主無人機正在改寫戰場成本結構，這一點在烏克蘭已經被反覆證實。</p>

  <h5 class="mini">④ Building Homes With Robots · 用機器人起屋</h5>
  <p>這是全集最長、最具體、也最令他興奮的一段。他的框架是「生活成本」：大部分人的壓力來自生活成本，而生活成本最大的一項是住屋。</p>
  <table>
    <thead><tr><th>他給的數字</th><th>數值</th><th>意義</th></tr></thead>
    <tbody>
      <tr><td>按揭利率</td><td class="num">7.25%</td><td>高利率鎖死了換樓與供應</td></tr>
      <tr><td>建造成本（他所在地區，好一點的房子）</td><td class="num">$600–800 / 平方呎</td><td>這是「賣價」的主要組成</td></tr>
      <tr><td>高端預製屋的可達成本</td><td class="num">便宜 20 倍</td><td>他的原話是 “20 times cheaper”</td></tr>
      <tr><td>他認為出現「天壤之別」的時間</td><td class="num">10 年內</td><td>“within 10 years away”</td></tr>
    </tbody>
  </table>
  <p><strong>案例：ZURU Tech（Nick Mowbray 兄弟）</strong></p>
  <ul class="tight">
    <li>在中國有一座工廠，<strong>一日印一間屋</strong>。Shaan 特別強調「唔係嗰種廉價 3D 打印」——而是更高效的<strong>灌混凝土</strong>工藝，用 iPhone 工廠級的自動化去造屋。</li>
    <li>洛杉磯山火後，他們買入約 <strong>6,000 萬–8,000 萬美元</strong>的災後地皮，準備建 <strong>2,000 萬–4,000 萬美元</strong>的豪宅，全部在中國工廠生產、模組化、到現場像 Lego 一樣組裝。</li>
    <li>為了測試抗震，他們在工廠裡自建<strong>地震模擬器</strong>：把整間 5,000 平方呎的屋放上去，逐個按鈕重演過去 50 年地球上五大地震（智利、摩洛哥……），確保結構通過。</li>
    <li>工廠外面有一排<strong>約 100 間</strong>原型屋，工人直接住進去，一邊住一邊每日迭代設計。</li>
    <li>這家公司<strong>沒有拿外部資金</strong>，兩兄弟投入約 <strong>10 億美元</strong>自有資本；他們做了 20 年高度自動化工廠，本業是玩具。</li>
  </ul>
  <p><strong>為什麼玩具業是護城河：</strong>Shaan 講了一段我認為是全集最漂亮的技術洞察。他引 Elon 的觀點：若問 Musk 最佩服誰的製造能力，答案是 <strong>Lego</strong>——因為要在規模化下做到每塊積木都精準互扣，公差必須近乎零。然後是 Tesla 的 Hot Wheels 故事：開會時 Musk 拿着一架 Hot Wheels 說，為什麼車底要 200 件零件？「注成一個模具就好」；工程師說「但 Elon，這架車只有兩吋大」，他答「那就把它做大」。結果 Tesla 自建了唯一能做到那個尺寸的機器，<strong>領先其他車廠約 7 年</strong>，因為機器是他們自己造的。</p>
  <p><strong>你可以點切入：</strong>他沒明說，但邏輯很清楚——不是去造屋，而是去做<em>令造屋變便宜的中間層</em>：模組接口標準、現場吊裝編排軟件、建材物流、審批合規自動化。香港／大灣區讀者對這個賽道有天然的地理優勢，問題是本地市場規模與審批制度。</p>

  <h5 class="mini">⑤ New Materials · 新材料</h5>
  <p>他講得最誠實的一段，前後不到 40 秒：「我唔完全明白呢樣嘢，我需要去同啲瘋狂嘅人一齊坐低。」他提到三藩市有人在做字面意義上的煉金術——声称可以用其他材料造出黃金——以及有人在發明全新材料。結論：「我覺得有趣，但遠超我嘅能力範圍。」</p>
  <p><strong>我嘅判讀：</strong>把它留在名單上是對的（材料科學是所有硬件的上游），但這一段沒有可行的切入點。真正的訊號是：如果你識材料科學的人，現在是他們被低估的時刻。</p>

  <h5 class="mini">⑥ Full Self-Driving Everything · 全自駕萬物</h5>
  <p>他的第一手證言：每天開 Tesla，按一個掣，它負責 <strong>90–95% 的里程</strong>；唯一接手的情況是停車場裡他想自己挑車位。</p>
  <p>然後是賽道的擴張：倉庫叉車、摩天大廈外牆清潔機、船底清除藤壺、橋樑檢測維修。「人們正在造那些會自動去維護我們這個世界嘅機器——而今天這些工作全部要靠大量人力。」</p>
  <p><strong>我嘅判讀：</strong>這是八個賽道裡<em>最容易被低估</em>的一個，因為它不性感。但「維護既有世界」是存量市場，付費方是政府、物業、船東、基建營運商——預算穩定、合約長、不靠消費情緒。</p>

  <h5 class="mini">⑦ Weather and Oceans · 天氣與海洋</h5>
  <p>嘉賓 <strong>Will O'Brien</strong> 曾上節目談海洋科技。Shaan 的類比是：太空科技因為 SpaceX 變得極熱，海洋科技正站在同一個轉折點前。「right around the corner」。</p>

  <h5 class="mini">⑧ Human Body Hardware · 人體硬件</h5>
  <p>Neuralink 是代表。但更打動他的是朋友 <strong>Tyler</strong> 做了多年的一個項目：<strong>Adam limbs</strong>——用想的就可以令機械臂拿起東西。</p>
  <blockquote>
    <p>“Somebody goes to war, they fight for our country, they lose their arm or their leg — they're given this really shitty prosthetic, like a stiff piece of plastic. The technology is actually out there now where you can put a robotic arm onto your arm and use your mind to say ‘pick that up’ and it'll pick it up. It's kind of a shame that we just haven't done the engineering to bring the cost down.”</p>
    <cite>約 25:50</cite>
  </blockquote>
  <p>他的結論不是「技術未到」，而是「<strong>工程與成本未做</strong>」——這正是他整集的方法論：機會不在發明，在<em>把已存在的東西做到可負擔</em>。</p>

  <h4 class="sub">4. 離題但最重要：美國為什麼會贏（以及可能點輸）</h4>
  <p>講完八個賽道，Sam 接管了大約 10 分鐘，講他近來讀歷史的發現。這段值得單獨看，因為它是整集的<strong>宏觀底座</strong>。</p>
  <p><strong>Sam 的版本——美國是「七、八個順風同時吹」的產物：</strong></p>
  <ul class="tight">
    <li>1880–1970 年間的美國增長爆炸，不只是價值觀（個人自由、平等、私有產權、資本主義）——那是<em>第一個以這組原則立國的國家</em>。</li>
    <li>但還有運氣：1880–1890 年代 Rockefeller 的石油、Carnegie 用鐵礦石煉鋼；真正被低估的是 <strong>Duluth, Minnesota 的鐵礦</strong>與巨型銅礦。</li>
    <li>地理套利：礦石上船，經<strong>五大湖</strong>（「大小等同一個海洋」）極快運到紐約與各地。到 1950 年代，經五大湖運送的鐵礦足以<strong>每年造 5,000 萬架車</strong>。</li>
    <li>農業能力 + <strong>50 個免關稅州</strong>＝統一大市場。</li>
    <li>1940 年代二戰把歐洲、北非、亞洲大片地區打爛，美國因為「夠遠」而完好。</li>
    <li>今天他看到同一個 pattern 的開端：<strong>美國的數據中心建設遠遠拋離其他國家</strong>，加上創業精神與人口，他認為這是又一次工業革命級別的擴張。</li>
  </ul>
  <p><strong>Shaan 的版本——三種悲觀，其實係不確定與恐懼：</strong></p>
  <ol class="tight">
    <li><strong>制度漂移：</strong>美國最受歡迎的地區（紐約、加州）正走向社會主義——仇視富豪、仇視企業、仇視 AI，也就是仇視剛才那組「進步的驅動力」。資本主義的輸出本來是：你可以建成公司、變有錢、再投資下一個世代，形成自我循環。這個循環是否正在斷？</li>
    <li><strong>製造業空心化：</strong>幾十年外包給中國之後，再工業化「講就好聽、舉手好易、做就極難」。他用的比喻是「一間很久沒有創新的大公司」——即使你意識到要創新，你郁得動這艘船嗎？</li>
    <li><strong>AI 懷疑論：</strong>要麼 AI 太強導致大規模失業，要麼 AI 不夠強、是一個巨大泡沫、大家過度投資會拖垮市場。「總之點都係輸。」</li>
  </ol>
  <p>然後 Sam 給出全集的<strong>政治金句</strong>，也是我認為最可直接挪用的一段策略思考：</p>
  <blockquote>
    <p>“Somebody should make the Common Sense political party. Common sense is such an amazing phrase that lets you take the moral high ground. If you say you're the Common Sense Party, it implies that everybody else is being a dumbass. And then also — who can argue with common sense?”</p>
    <cite>Sam Parr，約 33:20</cite>
  </blockquote>
  <p>他接着說，關鍵不是做「中間派」——「moderate 聽起來就像所有東西的稀釋版、被動、唔會做任何事」；也不是做第三黨——「third place 聽起來就係第三名」。正確做法是<strong>滲透其中一個大黨，把平台圍繞「common sense」重新命名，然後不斷重複這個詞</strong>。他舉 Trump 的 “America First” 為例：誰能站出來反對「美國優先」？他先佔了道德高地，再把議程塞進去。</p>
  <p>Shaan 補上 Munger 的 <strong>lollapalooza effect</strong>：任何極端離群值，通常都是七、八個順風同時出現的結果；再加上網絡效應——最好的經濟吸引最好的人，最好的人令經濟更好，形成自我加速。最後一句是我最喜歡的比喻：</p>
  <blockquote>
    <p>“We're like a 7-foot-tall eighth grader who gets drafted number one. Just don't blow it.”</p>
    <cite>約 35:45</cite>
  </blockquote>

  <h4 class="sub">5. 收尾：一個 free agent 的練習</h4>
  <p>整集的真正目的在最後 8 分鐘才揭曉。Shaan 有個表親，跟他同年、自認「更聰明更好看的版本」，剛賣掉公司成為 free agent，正準備做所有人都會做的事：</p>
  <blockquote>
    <p>“We look inside the peephole and we say, ‘All right, what do I see? What's the best thing I see here?’ When actually the job is to expand your field of vision.”</p>
    <cite>約 33:05 之後</cite>
  </blockquote>
  <p>他列出那個「peephole」裡的五個錯誤問題：我認識邊啲人？我住的地方有咩工？我以前做過乜？我擅長乜？——全部都會把你鎖在原本的行業裡，即使那個行業根本沒有順風。</p>
  <p><strong>他給的替代練習（我建議你今晚就做）：</strong></p>
  <ol class="tight">
    <li>假設有人給你 <strong>1,000 萬美元</strong>，利潤全歸你，但你必須全數投入五間公司。</li>
    <li>寫下你會選的五間。</li>
    <li>然後問：我為什麼會選它們？我對它們了解多少？我能不能去那裡工作、投資、或者造一個 adjacent 的東西？</li>
  </ol>
  <p>這個練習的作用不是選股，是<strong>強迫你由「勞工思維」切換到「投資人思維」</strong>。他的觀察是：投資人有一個特權——他們可以移動到錢正在被賺的地方；而創業者和打工仔傾向留在自己的行業、自己的 lane。</p>
  <p>然後是 Mark Pincus 那句（Shaan 引用，我認為是全集最該抄下來的一句）：</p>
  <blockquote>
    <p>“Go find the right body of water — it's far more important than trying to be the best sailor in a shitty body of water.”</p>
    <cite>Shaan 引 Mark Pincus，約 34:15</cite>
  </blockquote>
  <p>最後他承認了這份簡報的性質：</p>
  <blockquote>
    <p>“It's not like I went deeply researched any of these. But I know enough to know that there's a lot of opportunity in each one of these, and you just have to then go start digging and figure out what's the exact angle.”</p>
    <cite>約 36:05</cite>
  </blockquote>
  <p>Sam 的反應也很真實：「我看到這些，我很想它發生。我不會去做，但我想有人去做。」Shaan 回：「我們處於不同的季節。」</p>

  <h4 class="sub">6. 關鍵數據一覽</h4>
  <table>
    <thead><tr><th>數字</th><th>內容</th><th>出處</th></tr></thead>
    <tbody>
      <tr><td class="num">~$2T</td><td>Anthropic 五年創造的價值（他口中的估算）</td><td>Shaan</td></tr>
      <tr><td class="num">$96M / 日</td><td>七位共同創辦人集體每日創造的淨值</td><td>Shaan</td></tr>
      <tr><td class="num">~2%</td><td>創辦團隊今日合計持股（粗略）</td><td>兩人對話</td></tr>
      <tr><td class="num">10 年 / $2B / 80–90%</td><td>傳統新藥：時間 / 成本 / 失敗率</td><td>Shaan</td></tr>
      <tr><td class="num">20 年</td><td>Honeycrisp 蘋果由育種到上市</td><td>Shaan</td></tr>
      <tr><td class="num">7.25%</td><td>當時按揭利率</td><td>Shaan</td></tr>
      <tr><td class="num">$600–800</td><td>每平方呎建造成本（他所在地區）</td><td>Shaan</td></tr>
      <tr><td class="num">20x</td><td>高端預製屋相對傳統建造的便宜幅度</td><td>Shaan</td></tr>
      <tr><td class="num">1 間 / 日</td><td>ZURU 中國工廠的產能</td><td>Shaan</td></tr>
      <tr><td class="num">$1B</td><td>Mowbray 兄弟投入的自有資本</td><td>Shaan</td></tr>
      <tr><td class="num">90–95%</td><td>Tesla FSD 代駕里程比例（他的個人體驗）</td><td>Shaan</td></tr>
      <tr><td class="num">5,000 萬架 / 年</td><td>1950 年代五大湖鐵礦可支撐的汽車產量</td><td>Sam</td></tr>
    </tbody>
  </table>

  <h4 class="sub">7. 批判性評估：邊啲可以信，邊啲要打問號</h4>
  <p>我不打算把這集當聖旨，以下是我的判斷：</p>
  <table>
    <thead><tr><th>論點</th><th>我的評分</th><th>理由</th></tr></thead>
    <tbody>
      <tr><td>「AI 內容與工具是 race to the bottom」</td><td>大致成立，但過度簡化</td><td>供給側確實商品化；但擁有分發與工作流（不是模型）的公司仍有厚利潤。他把「做工具」與「擁有渠道」混為一談。</td></tr>
      <tr><td>「機會在 atoms」</td><td>強烈同意</td><td>這是本集最耐用的一句。AI 降低的是搜索與設計成本，不是監管、施工、臨床的成本——後者才是護城河。</td></tr>
      <tr><td>ZURU「一日一屋、便宜 20 倍」</td><td>可信但需驗證</td><td>工廠自動化與模組化是真的；「20 倍」是概數，且未計土地、審批、地基、現場作業。地皮本身才是加州房價的主因。</td></tr>
      <tr><td>定向能武器令守衛「郁唔到」</td><td>高度存疑</td><td>二手轉述、無具體來源，兩人自己在節目中也只是覆述報導。當故事聽。</td></tr>
      <tr><td>「一個人用 AI 治好自己的癌症」</td><td>個案真實性待查，但趨勢真</td><td>AI 輔助的腫瘤定序與藥物重定位確有真實案例；但「自行合成並服食」涉及極高風險，不構成可複製路徑。</td></tr>
      <tr><td>「美國數據中心建設遠超所有國家 → 新工業革命」</td><td>方向合理，因果太粗</td><td>資本開支確實驚人，但是否轉化為生產力，取決於電網、許可、與應用層落地，這些他沒碰。</td></tr>
    </tbody>
  </table>

  <h4 class="sub">8. 如果只帶走三件事</h4>
  <ol class="tight">
    <li><strong>換球場，不要換泳姿。</strong>「right body of water」比「best sailor」重要。你現在的行業有順風嗎？如果沒有，努力只會讓你更快到達錯的地方。</li>
    <li><strong>找「物理摩擦」當護城河。</strong>凡是需要工廠、審批、施工、臨床、現場服務的生意，AI 是加速器而不是替代品。這一類生意的估值邏輯在未來 5 年會被重寫。</li>
    <li><strong>做那個「把成本降低 10 倍」的人，而不是「發明新技術」的人。</strong>Adam limbs 的例子最清楚：技術早就在，缺的是工程與成本。大多數人的機會在後者。</li>
  </ol>

  <p class="src">節目連結：<a href="https://www.mfmpod.com/what-id-build-if-i-wanted-to-get-rich-with-ai/">mfmpod.com</a> · YouTube 版標題「AI will 10x these 8 industries in the next decade」· 本集為 RSS 第 880 集（feed 內第 919 個條目）。</p>
</div>

<h2 class="section">其餘五個播客 · 最近無更新</h2>
<div class="rule"></div>

<div class="card">
  <div class="byline">Acquired · Ben Gilbert &amp; David Rosenthal</div>
  <div class="lastep">
    <div class="lastep-label">最後已知劇集</div>
    <div class="lastep-title">Seinfeld</div>
    <div class="lastep-meta">2026-10-18 21:00 PDT · RSS 218 集 · 本期無新集</div>
  </div>
  <p class="src">10 月 18 日的 Seinfeld 特輯之後未見新集，符合他們月更級的節奏。若未聽，那是他們少見地拆解「純內容生意如何靠重播權收租三十年」——與今日 MFM 講的「擁有渠道 vs 擁有生產」是同一個命題的兩個年代版本。</p>
</div>

<div class="card">
  <div class="byline">Founders · David Senra</div>
  <div class="lastep">
    <div class="lastep-label">最後已知劇集</div>
    <div class="lastep-title">#439 How Eiichiro Oda Works</div>
    <div class="lastep-meta">2026-11-04 19:18 UTC · RSS 464 集 · 本期無新集</div>
  </div>
  <p class="src">尾田榮一郎的工作方式。與今日 MFM 的「ZURU 兩兄弟做廿年工廠才造屋」其實是同一種耐力敘事：極長的鋪墊期，換取後期無人能追的產能。</p>
</div>

<div class="card">
  <div class="byline">All-In with Chamath, Jason, Sacks &amp; Friedberg</div>
  <div class="lastep">
    <div class="lastep-label">最後已知劇集</div>
    <div class="lastep-title">Midterm Blood Bath, $4T AI Sell Off, Data Center Freeze, What's Next for Trump</div>
    <div class="lastep-meta">2026-11-07 18:27 UTC · RSS 443 集 · 本期無新集</div>
  </div>
  <p class="src">11 月 7 日的選舉與 AI 拋售覆盤，前日已完整拆解。本週末無新集，符合「週五錄、週六出」的節奏。值得注意的是今日 MFM 講的「數據中心建設」與 All-In 講的「$4T AI sell-off」是同一枚硬幣的兩面：資本開支的確定性 vs 回報的不確定性。</p>
</div>

<div class="card">
  <div class="byline">My First Million · Sam Parr &amp; Shaan Puri</div>
  <div class="lastep">
    <div class="lastep-label">狀態</div>
    <div class="lastep-title">本集已於上方完整拆解</div>
    <div class="lastep-meta">2026-11-09 11:00 UTC · RSS 919 集 · 本期 1 集新</div>
  </div>
  <p class="src">上集「The 2 businesses AI can never make obsolete」與本集是連續的兩步：先講 AI 取代不了什麼，再講 AI 該被放到哪裡。建議按此順序補聽。</p>
</div>

<div class="card">
  <div class="byline">The Knowledge Project · Shane Parrish</div>
  <div class="lastep">
    <div class="lastep-label">最後已知劇集</div>
    <div class="lastep-title">Jon McNeill: How Elon Musk Makes Decisions</div>
    <div class="lastep-meta">2026-11-05 10:55 UTC · RSS 20 集 · 本期無新集</div>
  </div>
  <p class="src">11 月 5 日的 Musk 決策框架。RSS 只保留最近 20 集，所以「20 集」不代表節目總數。今日 MFM 提到 Tesla 用單一模具取代 200 件零件、並自建機器領先七年——那正是 McNeill 那集講的「決策→物理實作」的具體案例，兩集可以對讀。</p>
</div>

<div class="card">
  <div class="byline">The Diary of a CEO · Steven Bartlett</div>
  <div class="lastep">
    <div class="lastep-label">最後已知劇集</div>
    <div class="lastep-title">Katt Williams: I Lied My Way Into Comedy! List The 300 People Ahead Of You, Then Outwork Each One!</div>
    <div class="lastep-meta">2026-11-09 06:00 UTC · RSS 908 集 · 本期無新集</div>
  </div>
  <p class="src">昨日已深度拆解。Katt 的「列出前面 300 個人，逐個超越」與今日 Shaan 的「五間公司練習」是同一個機制：把模糊的野心，變成一份可數的名单。</p>
</div>

<h2 class="section">本期總結</h2>
<div class="rule"></div>

<div class="verdict">
  <b>一句話：</b>今日只有一集，但它把 2026 年最擁擠的共識反轉了一次——當所有人都在用 AI 生成內容，真正的定價權正在轉移到那些<strong>需要工廠、批文與施工現場</strong>的行業。而 Shaan 最誠實的地方，是他在最後承認自己沒有深入研究任何一個賽道：這份簡報的價值不在於那八個答案，而在於那個<strong>「換一片水域」的動作</strong>。
  <p style="margin:14px 0 0">如果只做一件事：今晚寫下「給你一千萬、利潤歸你、只能投五間公司」的那五個名字。你會發現自己對真正發生中的事情，了解得比想像中少——那正是這集想讓你看見的東西。</p>
</div>

<footer>
  <div class="foot-line">掃描器 v3 · RSS diff by GUID · 逐字稿來源：YouTube 自動字幕 · 6/6 feed 正常</div>
  <div class="foot-line">生成時間：{stamp} · 下一期：2026-11-11 09:5x UTC</div>
  <div class="foot-line"><a href="https://jmoksz.github.io/mindset-podcasts/">jmoksz.github.io/mindset-podcasts</a></div>
</footer>

</div>
</body>
</html>
""".replace("{css}", CSS).replace("{stamp}", STAMP)

out = os.path.join(BASE, "daily-report-2026-11-10.html")
open(out, "w", encoding="utf-8").write(HTML)
print("written", out, len(HTML))

# --- update state ---
sp = os.path.join(BASE, "scanner", "state.json")
st = json.load(open(sp))
res = json.load(open(os.path.join(BASE, "scanner", "scan_result.json")))
added = 0
for pid, e in res.items():
    lst = st["scannedEpisodes"].setdefault(pid, [])
    for n in e["new"]:
        if n["guid"] not in lst:
            lst.append(n["guid"]); added += 1
st["lastScan"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
json.dump(st, open(sp, "w"), ensure_ascii=False, indent=1)
print("state updated, added", added, "lastScan", st["lastScan"])
