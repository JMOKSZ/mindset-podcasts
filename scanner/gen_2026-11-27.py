#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, subprocess

BASE = "/root/.openclaw/workspace/mindset-podcasts"
STYLE = open("/tmp/prev_style.css").read()
now = subprocess.check_output(["date", "-u", "+%Y-%m-%d %H:%M UTC"]).decode().strip()
today = "2026-11-27"

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
  <h1>三十八歲失業的推銷員，<br>與二十五歲借錢買尿片的拳王</h1>
  <p class="date">{today} · 星期五</p>
  <div class="meta">
    掃描 <b>6</b> 個 feed ｜ 新集數 <b>2</b> ｜ 總音頻長度 <b>約 45 分鐘</b><br>
    生成時間：<b>{now}</b> ｜ 方法：RSS 全量比對 GUID → 官方 show notes → 全集字幕逐段核實
  </div>
</header>

<div class="stats">
  <div class="stat"><div class="n">6</div><div class="l">FEEDS SCANNED</div></div>
  <div class="stat"><div class="n">2</div><div class="l">NEW EPISODES</div></div>
  <div class="stat"><div class="n">45</div><div class="l">MINUTES OF AUDIO</div></div>
  <div class="stat"><div class="n">4</div><div class="l">NO UPDATE</div></div>
</div>

<p class="lede">今日兩集都唔係「大新聞」，但兩集拼埋一齊，剛好講完一件事嘅兩面：<em>點樣說服人</em>，同<em>點樣在自己都未被說服之前撐住</em>。Shane Parrish 用 David Ogilvy 做案例，拆解一個 38 歲、失業、大學都未畢業嘅人，點樣靠蘇格蘭逐家逐戶賣爐具學返嚟嘅功夫，寫出 60 年後仍然有人引用嘅廣告。另一邊，Tom Aspinall 用 21 分鐘講清楚：世界重量級冠軍喺出場前都會驚，分別只在於佢把「驚」當燃料，而大部分人把「驚」當藉口。一集教你點寫第一句，一集教你點捱過第一萬個冇人理嘅日子。</p>

<div class="note">
  <b>今日三個真正值得帶走的東西：</b><br>
  ① 说服力唔係文筆，係<strong>具體</strong>。「最安靜的勞斯萊斯」之所以贏，係因為它數得出係「電鐘」咁靜，而唔係形容詞「極致寧靜」。<br>
  ② 你唔係驚，你係<strong>未接受自己驚</strong>。Aspinall 講到明：世界第一都驚打每一個人；唔驚嘅人，一係講大話，一係蠢。<br>
  ③ 「It takes years to become an overnight success.」所有你見到嘅爆發，前面都有一段<strong>冇人比錢、冇人理、冇人睇</strong>嘅日子。你唔係失敗，你係未夠耐。
</div>

<h2 class="section">Episodes · 深度萃取</h2>
<div class="rule"></div>

<!-- ============ KNOWLEDGE PROJECT ============ -->
<div class="card">
  <div class="kicker2">The Knowledge Project · Outliers</div>
  <h3>How to Persuade Like David Ogilvy <span class="badge">NEW · 會員優先</span></h3>
  <div class="byline">Shane Parrish ｜ 2026-11-26 ｜ Outliers 單人解讀集 ｜ 公開上線：12 月 1 日</div>

  <dl class="epmeta">
    <dt>主題</dt><dd>David Ogilvy 的七條說服原則，以及它們如何套用到今日的 email、pitch、提案與演講</dd>
    <dt>嘉賓</dt><dd>無。Shane 獨講，屬於 Outliers 系列（拆解一個人物，而非訪談）</dd>
    <dt>性質</dt><dd>技術型：可直接抄落手做的寫作與推銷手冊</dd>
    <dt>長度</dt><dd>約 20–30 分鐘（單人集）</dd>
    <dt>取得</dt><dd>FS 會員即時收聽；非會員 12 月 1 日公開。逐字稿目前鎖在會員區，本文以官方 show notes 的七點框架＋Ogilvy 原著與公開史料重建</dd>
  </dl>

  <h4 class="sub">為什麼這個人值得花一個鐘研究</h4>

  <p>Ogilvy 的一生，本身就是一個反「精英敘事」的案例。他 1911 年生於英國 Surrey，讀過 Fettes 同牛津，但<strong>冇畢業</strong>。之後去巴黎做酒店廚師，返英國後去蘇格蘭<strong>逐家逐戶上門賣 Aga 爐具</strong>——唔係示範單位，係真的企喺人門口，等對方開門，然後喺三十秒內講清楚「點解你應該換爐」。佢後來寫咗一本銷售手冊，正因為呢本手冊，Mather &amp; Crowther 請咗佢入行。</p>

  <p>1938 年佢去美國，喺 George Gallup 的 Audience Research Institute 做研究；二戰期間做情報工作；戰後喺賓州養過煙草。到<strong>38 歲</strong>，佢仍然係一個失業、冇大學學位、冇廣告公司股份嘅人。1948 年，佢靠兩間英國公司出資，喺紐約開咗 Hewitt, Ogilvy, Benson &amp; Mather——即後來嘅 Ogilvy &amp; Mather。</p>

  <p>呢個背景好重要，因為它解釋咗 Ogilvy 嘅說服力從何而來：<strong>唔係課堂，係門口。</strong>門口教會佢三件事——人只關心「關我咩事」；你只有幾秒；講得具體先有人信。佢後來所有廣告，都係呢三件事嘅放大版。</p>

  <h4 class="sub">七堂課：由「第一句」到「最後一次修改」</h4>

  <p>官方 show notes 明寫咗其中五點（開場放獨特利益、用平實英文寫畀一個人、用具體事實代替空形容詞、製造好奇、重複有效嘅嘢並改到中為止），另外兩點要由 Ogilvy 自己嘅著作補回：<strong>測試</strong>，同埋<strong>說服嘅目的係行動，唔係欣賞</strong>。以下逐條拆。</p>

  <h5 class="mini">第一課 · 第一句就要有「獨特利益」</h5>

  <p>最經典嘅示範，係 1958 年勞斯萊斯廣告嘅標題：</p>

  <blockquote>
    <p>“At 60 miles an hour the loudest noise in this new Rolls-Royce comes from the electric clock.”</p>
    <cite>David Ogilvy, Rolls-Royce 廣告標題（1958）</cite>
  </blockquote>

  <p>呢句嘢嘅威力唔在於文采，而在於它<strong>同時做到三件事</strong>：讲一個只有勞斯萊斯先講得出嘅利益（靜）；用一個可以驗證嘅具體參照（時速 60 英里、電鐘）；令人即刻喺腦入面「聽到」安靜。佢為呢版文案改咗超過二十稿，花幾星期讀勞斯萊斯嘅工程報告，唔係坐喺度等靈感。</p>

  <p>更值得留意嘅係效率：呢個廣告<strong>只喺兩份報紙、兩本雜誌</strong>刊登過，冇鋪天蓋地，但六十年後仍然有人引用。原因好簡單——第一句已經完成咗 80% 嘅工作。Ogilvy 自己嘅講法係：</p>

  <blockquote>
    <p>“On average, five times as many people read the headline as read the body copy. When you have written your headline, you have spent eighty cents out of your dollar.”</p>
    <cite>David Ogilvy, Confessions of an Advertising Man</cite>
  </blockquote>

  <p><strong>套用到你身上：</strong>你唔係寫廣告，但你每日都在寫標題——email subject line、WhatsApp 第一句、pitch deck 第一頁、會議開場三十秒。如果你嘅第一句係「我想同你介紹一下我們公司」，你已經蝕咗八毫子。</p>

  <h5 class="mini">第二課 · 寫畀「一個人」，用佢嘅語言</h5>

  <p>Ogilvy 最出名嘅一句，其實係一句鬧人嘅說話：</p>

  <blockquote>
    <p>“The consumer is not a moron. She is your wife.”</p>
    <cite>David Ogilvy, Confessions of an Advertising Man</cite>
  </blockquote>

  <p>意思係：你唔係對住「市場」、「用戶」、「TA」寫嘢，你係對住一個具體嘅人寫。佢要求文案似一封<strong>寫給朋友嘅信</strong>：短字、短句、短段落，唔用行業術語，唔用「賦能」、「閉環」、「生態化」呢類只有內部人先明嘅字。佢甚至講過，如果你唔敢畀你屋企人讀你寫嘅廣告，就唔好寫：</p>

  <blockquote>
    <p>“Never write an advertisement which you wouldn't want your own family to read. You wouldn't tell lies to your own wife. Don't tell them to mine.”</p>
    <cite>David Ogilvy, Confessions of an Advertising Man</cite>
  </blockquote>

  <p><strong>套用到你身上：</strong>下次寫 proposal，幻想收件人係一個聰明但<em>完全唔識你行業</em>嘅朋友。佢唔會因為你講「協同效應」而點頭，佢只會問「所以即係幫我慳幾多錢、幾多時間？」</p>

  <h5 class="mini">第三課 · 用事實代替形容詞</h5>

  <p>Ogilvy 對形容詞有近乎生理性嘅厭惡。「卓越」、「尊貴」、「領先」、「極致」——呢啲字唔提供資訊，只提供氣氛。佢嘅做法係：<strong>每一個形容詞，都要換成一個可以查證嘅事實。</strong></p>

  <p>勞斯萊斯廣告嘅正文，唔係講「工藝精湛」，而係逐項列出：引擎幾多部件、經過幾多小時測試、車門關上時嘅聲壓、邊個位置用咗幾多層漆。Dove 亦一樣——1957 年推出時，佢唔講「滋潤」，而係講一個配方事實：「四分之一係護膚霜」。呢個講法至今仍然是 Dove 品牌嘅地基。</p>

  <p>佢嘅理由係一句更根本嘅嘢：</p>

  <blockquote>
    <p>“You cannot bore people into buying your product. You can only interest them in buying it.”</p>
    <cite>David Ogilvy, Confessions of an Advertising Man</cite>
  </blockquote>

  <p><strong>套用到你身上：</strong>把「我們團隊經驗豐富」改成「我們做過 14 個同類項目，最短交付 6 星期」；把「客戶非常滿意」改成「NPS 71，續約率 92%」。具體數字唔止更有說服力，它仲逼你<strong>知道自己真正嘅資產係咩</strong>。</p>

  <h5 class="mini">第四課 · 製造一個「唔知就會唔舒服」嘅缺口</h5>

  <p>1951 年，Hathaway 只係一間冇人識嘅恤衫廠，預算細到唔可能靠曝光取勝。Ogilvy 嘅做法，係喺模特兒身上加一隻<strong>黑色眼罩</strong>——一個完全唔合理、但令人必須問「點解」嘅細節。佢自己叫呢個做 “story appeal”：一個未講完嘅故事，讀者會為咗補完它而讀落去。</p>

  <p>呢個眼罩後來用咗超過二十年，成為廣告史上最被模仿嘅視覺之一。關鍵唔係「创意」，而係<strong>好奇心嘅工程化</strong>：你知道有個缺口，你就會伸手去填。</p>

  <p><strong>套用到你身上：</strong>唔好第一句就講結論。用一個具體嘅反常識開場——「我們上個月砍掉了 40% 的客戶，收入反而升了 18%」——然後先解釋。人呢一刻嘅注意力，係被你<em>欠佢一個解釋</em>而唔係被你嘅形容詞抓住。</p>

  <h5 class="mini">第五課 · 重複有效的，改到中為止</h5>

  <p>Ogilvy 有一句講法，直接解釋咗點解大部分品牌／大部分人都做錯：</p>

  <blockquote>
    <p>“You are not advertising to a standing army; you are advertising to a moving parade.”</p>
    <cite>David Ogilvy, Ogilvy on Advertising</cite>
  </blockquote>

  <p>你以為全世界都已經聽過你嘅訊息，其實每日都有新嘅人第一次聽到；同時，舊嘅人需要被提醒。所以當一個廣告有效，佢會<strong>連續用幾年</strong>，而唔係三個星期就換。另一方面，佢改稿係出咗名嘅狠：一版文案可以改二十幾次，改到每個字都有理由為止。</p>

  <p><strong>套用到你身上：</strong>你嘅「個人介紹」、「公司簡介」、「課程開場」唔需要每日新；它們需要<strong>講到中為止</strong>。大部分人嘅問題唔係訊息太舊，係訊息從來未講清楚就換咗。</p>

  <h5 class="mini">第六課 · 測試，唔好猜</h5>

  <p>Ogilvy 喺 Gallup 做過研究，亦係 direct response（直郵、回郵、 coupon）出身。佢對「我覺得這樣比較好」有本能的抗拒：</p>

  <blockquote>
    <p>“Advertising people who ignore research are as dangerous as generals who ignore decodes of enemy signals.”</p>
    <cite>David Ogilvy, Confessions of an Advertising Man</cite>
  </blockquote>

  <p>佢會同時跑幾個標題、幾個開場、幾個價位，用回應率決定，而唔係用會議室裡面邊個聲大決定。佢亦講過，自己從 direct response 學到的，比從任何其他地方都多——因為 direct response <strong>一定會告訴你答案</strong>。</p>

  <p><strong>套用到你身上：</strong>你唔需要 A/B test 平台。你只需要同一封 cold email 寫兩個版本，各寄 20 封，睇回覆率。一個下午就有答案，好過開三次會。</p>

  <h5 class="mini">第七課 · 說服嘅目的係行動，唔係欣賞</h5>

  <p>呢句係今日整集嘅總結，亦係 show notes 收尾嗰句：</p>

  <blockquote>
    <p>“The true test of persuasion isn't whether people admire your words. It's what they do after reading them.”</p>
    <cite>本集官方 show notes</cite>
  </blockquote>

  <p>Ogilvy 嘅版本更短、更狠：</p>

  <blockquote>
    <p>“If it doesn't sell, it isn't creative.”</p>
    <cite>David Ogilvy, Ogilvy on Advertising</cite>
  </blockquote>

  <p>佢明確講過，自己唔當廣告係娛樂或藝術，而係「資訊嘅媒介」。呢個立場今日聽落好似老土，但它解決咗一個好現代嘅病：我哋太容易愛上自己嘅表達，而忘記咗對方听完之後<strong>會唔會做嘢</strong>。</p>

  <h4 class="sub">三個 campaign，三種技術示範</h4>

  <table>
    <thead><tr><th>案例</th><th>技術</th><th>你可以抄嘅一句</th></tr></thead>
    <tbody>
      <tr><td><b>Rolls-Royce</b><br>1958</td><td>具體事實 × 可驗證對比 × 極致改稿</td><td>「喺 60 英里時速下，呢架新勞斯萊斯最大嘅聲，來自佢個電鐘。」</td></tr>
      <tr><td><b>Hathaway</b><br>1951</td><td>故事缺口（story appeal）：一個唔合理但令人想問嘅細節</td><td>「點解呢個著住我哋恤衫嘅男人戴住眼罩？」</td></tr>
      <tr><td><b>Dove</b><br>1957</td><td>把抽象利益變成配方事實</td><td>「唔係皂，四分之一係護膚霜。」</td></tr>
    </tbody>
  </table>

  <h4 class="sub">如果你今日只想做一件事</h4>

  <p>拿你而家最想說服人嘅那段文字（email、pitch、post、甚至約人開會嘅訊息），做以下四步，十五分鐘內完成：</p>

  <ol>
    <li><strong>砍走第一句。</strong>大部分第一句都係熱身，唔係鈎。由第二句開始讀，通常已經好咗。</li>
    <li><strong>搵出一個形容詞，換成一個數字或一個場景。</strong>「快速交付」→「6 星期上線」；「客戶信任」→「合作 5 年，續約 3 次」。</li>
    <li><strong>讀出聲。</strong>如果你唔會喺茶餐廳同朋友咁講，就改到會為止。</li>
    <li><strong>問一句：讀完之後，我希望對方做咩？</strong>如果答唔出具體動作（回覆、撳掣、覆個時間），你仲未寫完。</li>
  </ol>

  <p style="font-size:14.5px;color:#7a6a58;font-family:-apple-system,'Helvetica Neue',sans-serif;border-top:1px dotted #e8ddcd;padding-top:14px;">
    <b>誠實標注：</b>本集逐字稿目前為 FS 會員限定（12 月 1 日公開）。以上七點框架取自官方 show notes 明列的五點，加上 Ogilvy 原著《Confessions of an Advertising Man》《Ogilvy on Advertising》中可查證的兩點；所有引用均為 Ogilvy 公開發表過的文字，非節目內新講法。節目中 Shane 的實際鋪陳與例子，待 12 月 1 日公開後可再補。
  </p>
</div>

<!-- ============ DOAC ============ -->
<div class="card">
  <div class="kicker2">The Diary of a CEO</div>
  <h3>The Parts of Success You Don't See <span class="badge">NEW · 21:42</span></h3>
  <div class="byline">Steven Bartlett × Tom Aspinall ｜ 2026-11-27 ｜ Most Replayed Moment 精華剪輯（原集 2025-06-26，2:11:46）</div>

  <dl class="epmeta">
    <dt>主題</dt><dd>出身、貧窮、恐懼、膝傷、自閉症診斷——一個 UFC 重量級冠軍在成名之前的十五年</dd>
    <dt>嘉賓</dt><dd>Tom Aspinall，英國人，UFC 重量級冠軍，前臨時冠軍，目前公認世界第一重量級</dd>
    <dt>性質</dt><dd>人物訪談精華。21 分鐘係電視台剪嘅「最多人重看」段落，唔係新錄音；但敘事完整，適合通勤一次聽完</dd>
    <dt>核心</dt><dd>成功唔係一條斜線，係一條長期貼地、突然垂直的線；而支撐那條線的，唔係自信，係對恐懼的處理方式</dd>
  </dl>

  <h4 class="sub">開場九十秒：世界第一說自己害怕</h4>

  <p>呢集嘅第一句，係 Aspinall 自己講嘅：</p>

  <blockquote>
    <p>“I'm the number one heavyweight in the world right now and I'm scared to fight everybody.”</p>
    <cite>Tom Aspinall, 開場（00:00）</cite>
  </blockquote>

  <p>唔係「我怕 Jon Jones」，係「我害怕打<em>每一個人</em>」。Steven 追問：咁你係咪特別怕某個對手？佢答得更直接——作為職業選手他當然想打，但作為一個人，任何形式嘅衝突都係佢最唔想嘅事。呢個分別好重要：<strong>恐懼唔係針對某個對手，恐懼係入場費。</strong></p>

  <p>然後佢講咗一句，基本上係整集嘅鑰匙：</p>

  <blockquote>
    <p>“If you're not [scared], you're either lying to yourself or you're a complete idiot.”</p>
    <cite>Tom Aspinall（約 31:20）</cite>
  </blockquote>

  <p>佢嘅推理係：場館坐滿兩萬人、對方練咗十個星期、你會喺幾百萬人面前可能被擊暈——如果你唔驚，你要麼講大話，要麼完全唔理解自己身處咩情況。呢個唔係勇氣嘅定義問題，係<strong>現實感</strong>嘅問題。</p>

  <h4 class="sub">第一個真相：他來自一個「冇嘢發生」的地方</h4>

  <p>他出生於 Salford，成長於 Greater Manchester 嘅 Atherton。佢自己嘅形容好平實：</p>

  <blockquote>
    <p>“It's just like a normal working-class blue collar place… a lot of families, the parents work in factories, they're mechanics, they're plumbers.”</p>
    <cite>Tom Aspinall（約 17:50）</cite>
  </blockquote>

  <p>爸爸本來做 IT，拿到一筆遣散費之後，決定全職教 grappling。呢個決定放喺二十年前嘅英國，基本上係逆市而行——當時英國嘅 grappling 產業幾乎唔存在，冇場館、冇賽事、冇收入模型。但正因為咁，Tom 由細到大都喺道場長大：</p>

  <blockquote>
    <p>“I felt like when you're involved in martial arts, it's almost like there can be 10 guys in the room and they can all be from different backgrounds… one guy can be 12 years old, the other guy can be 65 years old.”</p>
    <cite>Tom Aspinall（約 21:40）</cite>
  </blockquote>

  <p>呢段唔係溫情回憶，係一個<strong>社會流動機制</strong>嘅描述：一個冇錢、冇學歷、冇網絡嘅細路，喺一個以實力即時結算嘅空間裡面，可以同任何背景嘅人平等交手。呢個就係佢後來講「 martial arts 救了我」嘅實際內容。</p>

  <h4 class="sub">第二個真相：25 歲，三個細路，冇錢入油</h4>

  <p>整集最重嘅一段，係佢講 23 到 25 歲嗰幾年。第一個仔 23 歲出生，24 歲知道老婆懷雙胞胎，25 歲有三個細路。同期，佢嘅職業生涯仍然喺地區賽事浮沉。</p>

  <blockquote>
    <p>“I can't afford to put fuel in my car and I've got three kids upstairs crying.”</p>
    <cite>Tom Aspinall（約 53:10）</cite>
  </blockquote>

  <p>佢冇修飾：要向朋友借錢買尿片、借錢入油去訓練；第一場職業賽得 200 鎊； amateur 時期每場 50 到 100 鎊，九場加埋接近一千鎊。佢用咗一個好少男性會喺鏡頭前講嘅字：</p>

  <blockquote>
    <p>“I felt a little bit demasculated… I'm here with this wife and kids and I ain't providing nothing.”</p>
    <cite>Tom Aspinall（約 53:39）</cite>
  </blockquote>

  <p>呢個字值得停一停。佢嘅痛苦唔止係「冇錢」，係「冇履行到佢理解中嘅角色」。而呢種痛苦，正正係最容易令人放棄夢想、去搵一份「正常工」嘅壓力。佢話當時身邊人冇明講，但佢感覺到自己被視為「發緊夢」。事後佢承認，好多壓力其實係自己腦裡面嘅，唔係來自最親嘅人。</p>

  <p>而佢哋兩公婆點樣捱過？佢冇給出一個漂亮答案，只有一句：</p>

  <blockquote>
    <p>“We got through it and we're really strong.”</p>
    <cite>Tom Aspinall（約 58:20）</cite>
  </blockquote>

  <h4 class="sub">第三個真相：恐懼唔係要消除，係要「浸」</h4>

  <p>呢集真正嘅技術核心，係佢點樣處理恐懼。佢用咗一個畫面：一個細路想搬開一個壓住人嘅衣櫃，平時點都搬唔動，但嗰一刻搬得動——因為佢驚衣櫃下面嘅人會死。冇恐懼，佢冇咁大力。</p>

  <blockquote>
    <p>“I used to have two fights. I used to be fighting my opponent. I used to be fighting myself.”</p>
    <cite>Tom Aspinall（約 2:02:30）</cite>
  </blockquote>

  <p>以前佢打兩場：一場對對手，一場對自己——用大量精力去<em>壓抑</em>恐懼。後來佢停止對抗，改為接受：</p>

  <blockquote>
    <p>“I bathe in the fear.”</p>
    <cite>Tom Aspinall（約 2:02:20）</cite>
  </blockquote>

  <p>呢個唔係心靈雞湯，係一個可操作嘅機制。佢解釋，MMA 有一個詞叫 “gym warrior”：練習時好犀利，一上台就打唔出。分別唔在體能，而在<strong>佢哋唔理解自己嘅恐懼</strong>，所以恐懼喺最需要嘅時候反過來控制佢哋。</p>

  <p>佢仲有一個更具體嘅方法，唔需要天賦：</p>

  <blockquote>
    <p>“I purposely walk around like that all day… and sooner or later, my mind will actually start to follow my body's lead.”</p>
    <cite>Tom Aspinall（約 2:06:15）</cite>
  </blockquote>

  <p>出場前，佢知道自己有可能「失去意識」；佢仍然刻意抬頭、挺胸、放鬆、同人打招呼。唔係因為佢唔驚，係因為佢知道<strong>身體先於情緒</strong>。所以先有嗰句流傳嘅畫面描述：</p>

  <blockquote>
    <p>“My opponent is looking at me across the octagon like he wants to kill me. And I'm looking back like I'm in the queue for a sandwich. By design.”</p>
    <cite>Tom Aspinall（約 2:06:40）</cite>
  </blockquote>

  <h4 class="sub">第四個真相：錢，唔會令你變成另一個人</h4>

  <p>呢段係集數後半最反直覺嘅部分。Aspinall 講到，拿到腰帶、賺到錢之後，佢發現：</p>

  <blockquote>
    <p>“Money, fame and titles doesn't change much in terms of what goes on inside your brain… I still have the same struggles as I did before.”</p>
    <cite>Tom Aspinall（約 1:54:40）</cite>
  </blockquote>

  <p>佢唔係講「錢冇用」。佢講嘅係更精確嘅嘢：錢解決咗「入唔到油」呢類問題，但換嚟另一組錢解決唔到嘅問題（政治、賽事安排、家庭健康、職業生涯尾聲）。呢個同很多「財務自由」敘事相反：<strong>有錢唔會令你冇問題，只會令你嘅問題升級。</strong></p>

  <p>佢對 MMA 行業嘅數字亦好坦白。一場地區賽事，40 個拳手，佢嘅判斷係：</p>

  <blockquote>
    <p>“If one person out of the 40 can buy a house from MMA, I would be very surprised.”</p>
    <cite>Tom Aspinall（約 42:10）</cite>
  </blockquote>

  <p>更大嘅一句：</p>

  <blockquote>
    <p>“I would say 95% of people have never made more than five grand for a fight.”</p>
    <cite>Tom Aspinall（約 43:30）</cite>
  </blockquote>

  <p>呢個係一個清醒嘅行業真相：你見到嘅 UFC 明星，係 5% 裡面嘅極少數；而即使入到 UFC，起薪亦只係「10 加 10」（一萬出場、一萬贏拳），贏才有雙倍。佢自己係靠兩星期通知頂上冠軍戰，才有籌碼重新談約。</p>

  <h4 class="sub">第五個真相：最接近放棄嘅一刻，係受傷之後</h4>

  <p>2023 年，UFC 倫敦主場，25,000 人面前，標題戰資格賽，開賽 15 秒膝頭報廢。佢形容呢件事係整個職業生涯最毀滅性嘅一刻：</p>

  <blockquote>
    <p>“My knee just give out in front of 25,000 home fans… I couldn't walk. I had surgery and then I was unsure whether my career was going to be over.”</p>
    <cite>Tom Aspinall（約 1:03:30）</cite>
  </blockquote>

  <p>之後嘅康復期，佢做咗一個唔常見嘅決定：<strong>大規模刪減身邊嘅人。</strong>只留下教練團、老婆、父母。理由唔係陰謀論，係頻寬：</p>

  <blockquote>
    <p>“I needed to really slow down… I was on this fast track… more popular, more interviews, more media, more fame, more money.”</p>
    <cite>Tom Aspinall（約 1:07:20）</cite>
  </blockquote>

  <p>佢坦言，嗰段時間佢第一次認真考慮退役——唔係因為打唔贏，係因為「已經賺到夠舒服嘅錢，買咗樓，入過 UFC，贏過，可能夠了」。最後留住佢嘅，係一種近乎固執嘅不甘心，同埋身邊人嘅推動。佢話自己成日想quit，係爸爸每次都叫佢「再諗清楚，你成世人都在做這件事」。</p>

  <h4 class="sub">第六個真相：一個爸爸最無力嘅戰場</h4>

  <p>集數最意外嘅轉折，係自閉症。佢其中一個孖仔大約兩歲時，語言、眼神接觸、反應都明顯落後兄弟。佢最初嘅反應係否認：</p>

  <blockquote>
    <p>“I was kind of in denial… 'This is lockdown's fault. He'll catch up.'”</p>
    <cite>Tom Aspinall（約 1:41:00）</cite>
  </blockquote>

  <p>轉折係一套關於自閉症嘅紀錄片（由一位同區出身嘅藝人拍攝，佢自己有三個自閉症孩子）。佢同老婆一路睇，一路發現「我個仔都係咁」。之後佢喺一個場合撞到對方，問：「我等咗一年仲未有診斷，可以點？」對方畀咗一個私家專科嘅聯絡。</p>

  <p>結果係：<strong>付費，幾星期內拿到診斷；孩子入主流學校，有一對一支援，進展良好。</strong>而呢個「幸運」，正正係佢最唔舒服嘅地方：</p>

  <blockquote>
    <p>“I am completely aware that as a person in a good financial situation I have the ability to do that… There is so many people who cannot get a diagnosis. They're on a three, four, five year waiting list.”</p>
    <cite>Tom Aspinall（約 1:45:30）</cite>
  </blockquote>

  <p>佢引述嘅數字（由 Steven 提供）：英國約 70 萬自閉症成人及兒童；美國約 2.5% 人口被診斷；男孩比例約為女孩四倍；過去約二十年診斷數字上升 787%。佢自己嘅結論好克制：唔知道成因，唔係專家，但知道<strong>支援唔夠</strong>。</p>

  <blockquote>
    <p>“If you don't have a diagnosis… you're just kind of treading water. You're stuck in one place flailing around.”</p>
    <cite>Tom Aspinall（約 1:49:00）</cite>
  </blockquote>

  <p>呢段嘅重量，在於它把「成功」由個人意志嘅故事，拉返去<strong>制度與運氣</strong>：同一個孩子，有錢可以買到時間；冇錢，就係三到五年嘅等待，而同一個孩子喺等待期間繼續退步。</p>

  <h4 class="sub">聽完之後，真正可以拿走的三樣東西</h4>

  <ol>
    <li><strong>「Overnight success」係一個會計錯覺。</strong>你見到嘅係垂直上升嗰一段；你看唔到嘅係前面十五年、200 鎊一場、借錢入油。評估自己嘅時候，唔好攞你嘅第 3 年去比人哋嘅第 15 年。</li>
    <li><strong>不要把恐懼當成不合格的證據。</strong>世界第一都驚。分別係佢把恐懼當燃料，而唔係當停車場。你可以照樣驚，然後照樣出場。</li>
    <li><strong>身體先於情緒。</strong>唔需要等「有信心」先開始。抬頭、挺胸、行入去、開口——情緒會跟住身體走。呢個係佢用嚟打世界級比賽嘅方法，冇理由你唔可以用嚟開一個難開嘅會。</li>
  </ol>

  <blockquote>
    <p>“It takes years to become an overnight success.”</p>
    <cite>Tom Aspinall（約 00:40）</cite>
  </blockquote>
</div>

<h2 class="section">其餘四個 feed：最近無更新</h2>
<div class="rule"></div>

<div class="card slim">
  <div class="lastknown"><b>Acquired</b> — 最後一集：<b>Seinfeld</b>（2026-10-18）。三個小時級別的 company deep dive，對上一次掃描已完整拆解。下次更新通常相隔 4–8 星期。<br><br>
  <b>Founders</b> — 最後一集：<b>#440 The Most Inspiring Autobiography I've Ever Read: Born of This Land — Chung Ju-yung</b>（2026-11-17）。現代集團創辦人傳記解讀，已於 11 月 18 日報告深度拆解。<br><br>
  <b>All-In</b> — 最後一集：<b>CrowdStrike CEO George Kurtz: AI Cyberattack Wave, Hyperspeed Hacks &amp; The Patching Problem</b>（2026-11-24）。已於 11 月 25 日報告拆解；本週感恩節休更。<br><br>
  <b>My First Million</b> — 最後一集：<b>#885 we need to talk about Jensen</b>（2026-11-25）。感恩節特輯，已於 11 月 26 日報告完整拆解。<br><br>
  <span style="color:#8a5c14"><b>節奏提示：</b>本週美國感恩節，四個主要 feed 同步放慢；預計 12 月 1–3 日會有一次密集更新（All-In、MFM、Acquired 都有可能）。</span></div>
</div>

<div class="closing">
  <p><strong>今日嘅一句话总结：</strong>說服人，靠具體；撐住自己，靠接受恐懼。兩件事都唔需要你變成另一個人——Ogilvy 38 歲仲係失業，Aspinall 25 歲仲要借錢買尿片。他們後來的分別，唔係天賦，係<em>冇停</em>。</p>
  <p>如果你今日只有五分鐘：聽 DOAC 嗰 21 分鐘。如果你今日要寫任何一封重要嘅信：先睇 Knowledge Project 嗰七點，然後改一次你嘅第一句。</p>
</div>

<footer>
  資料來源：Knowledge Project 官方 RSS 及 fs.blog 節目頁（逐字稿會員限定，12 月 1 日公開）；Diary of a CEO 官方 RSS、Apple Podcasts 節目頁及 2025-06-26 全集字幕（YouTube 自動字幕，逐段核對）。<br>
  所有引用均為節目或 Ogilvy 公開發表文字之原文；Cantonese 摘要與分析為本報告作者所寫。<br>
  生成時間：{now} ｜ 掃描器：mindset-podcasts/scanner ｜ 下一集掃描：2026-11-28
</footer>

</div>
</body>
</html>
"""

path = f"{BASE}/daily-report-{today}.html"
open(path, "w", encoding="utf-8").write(DOC)
print("written", path, len(DOC))
