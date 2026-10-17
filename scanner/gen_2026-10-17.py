#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, re
from datetime import datetime, timezone, timedelta

BASE = '/root/.openclaw/workspace/mindset-podcasts'
prev = open(os.path.join(BASE, 'daily-report-2026-10-16.html'), encoding='utf-8').read()
style = re.search(r'<style>.*?</style>', prev, re.S).group(0)

now = datetime.now(timezone.utc)
DATE = now.strftime('%Y-%m-%d')
now_utc = now.strftime('%Y-%m-%d %H:%M') + ' UTC'
hkt = now.astimezone(timezone(timedelta(hours=8)))
now_hkt = hkt.strftime('%Y-%m-%d %H:%M')

state = json.load(open(os.path.join(BASE, 'scanner', 'state.json')))
total_guid = sum(len(v) for v in state.get('scannedEpisodes', {}).values()) + 2
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

# =====================================================================
# ACQUIRED (no new)
# =====================================================================
cards += card_none(
    "Acquired", "Ben Gilbert &amp; David Rosenthal", "最近無更新",
    "The Home Depot", "2026-09-13", "3 小時 35 分（12,902 秒）",
    "https://www.acquired.fm/episodes/home-depot", "https://www.acquired.fm/episodes",
    "daily-report-2026-09-14.html",
    "Home Depot 創辦故事：Bernie Marcus 同 Arthur Blank 喺 48 歲同 35 歲畀人炒魷之後，聽咗紐約銀行家 Ken Langone 嘅一句話——「你哋係畀金馬蹄鐵踢中咗屁股」——然後寫下美國零售史上最強複利故事之一。官方描述形容成一部「Avengers 電影」。",
    note="⚠️ Acquired 自 09-13 後已 <b>34 日</b>無新集；本台節奏約每月 1–2 集（長篇研究型），下一集隨時會出，屆時會第一時間拆解。")

# =====================================================================
# FOUNDERS (no new)
# =====================================================================
cards += card_none(
    "Founders", "David Senra", "最近無更新",
    "#437 The Tycoons: Carnegie, Rockefeller, Gould &amp; Morgan", "2026-10-13", "54 分 11 秒（3,251 秒）",
    "https://www.founderspodcast.com/", "https://www.founderspodcast.com/",
    "daily-report-2026-10-14.html",
    "Senra 讀 Charles R. Morris《The Tycoons》：四位寒微出身的巨人——三破壞者（Carnegie 鋼／Gould 鐵路／Rockefeller 石油）+ 一監管者（Morgan 銀行），喺 1873 同 1880 年代兩次市場斷裂中，把美國由農業手工業國家推成世界工廠。核心 insight：「發明嘅消費者」勝過發明者、先滿產再算賬、壟斷經濟學反直覺結論。",
    note="ℹ️ Senra 每日／隔日更新，今次已連續 4 日無新集（上次 10-13），屬近期較長空檔——值得留意下一集。")

# =====================================================================
# ALL-IN (NEW)
# =====================================================================
cards += f'''
<!-- ==================== All-In ==================== -->
<section class="pod">
  <div class="pod-head">
    <h2>All-In with Chamath, Jason, Sacks &amp; Friedberg</h2>
    <span class="host">Chamath Palihapitiya · Jason Calacanis · David Sacks · Ben Horowitz（代 Friedberg）</span>
    <span class="tag new">新集</span>
  </div>
  <div class="ep-title">CoreWeave Crash, AI Trade Cracks, Anthropic IPO Red Flags, Bill Gates Doomer</div>
  <div class="ep-meta">📅 2026-10-17 01:51 UTC · ⏱ 1 小時 34 分 06 秒（5,646 秒） · 🎙 四位 besties 圓桌，Ben Horowitz 代班 Friedberg</div>

  <div class="callout">
    <b>一句話總結：</b>呢集係「AI 交易」第一次由「估值問題」升級成「信用問題」嘅現場記錄。CoreWeave 只佔 AI 基建一小塊，但佢嘅債券息率、CDS 同股價同時閃紅燈，令市場被迫問一條更難答嘅問題——<b>如果 AI 需求係真，但融資成本足以食掉回報，咁「增長」仲算唔算數？</b>其餘四段分別由軟件通縮、Anthropic 上市前嘅財務披露、安全論述嘅公關味，講到 Bill Gates 點解由樂觀主義者變成 doomer。
  </div>

  <div class="chapters">
    <span class="tc">0:00</span> Ben Horowitz 代 Friedberg 登場<br>
    <span class="tc">2:18</span> CoreWeave 債務拋售：AI 泡沫爆咗未？<br>
    <span class="tc">31:14</span> AI 嘅通縮威力：被「反編譯」嘅軟件<br>
    <span class="tc">45:44</span> Anthropic 投資者日：市場反應兩極<br>
    <span class="tc">1:03:45</span> Psyop Corner：Anthropic 警告 IoT 自我複製模型<br>
    <span class="tc">1:22:19</span> 理解「末日論者」Bill Gates
  </div>

  <h3>① CoreWeave 債券風暴：AI 泡沫第一次由 credit 市場引爆（2:18–31:14）</h3>

  <h4>主題與背景</h4>
  <p>本週 AI 基建股全面受壓，但 CoreWeave 唔止係「跟跌」——佢係今輪唯一被<b>信用市場</b>單獨點名嘅公司。事情嘅起點係 Chamath 喺 X 貼出 CoreWeave 無擔保債券息率觸及 <b>15%</b> 嘅截圖，Elon Musk 回覆一個字：<span class="label">原文</span>「Yikes」。隨後 CoreWeave 股價單日跌 10% 至 <b>$70.37</b>，全週累跌約四分之一；Nebius 跌 6%、Oracle 跌 2%，但 QQQ 只跌 0.7%——跌勢高度集中喺 neocloud／AI 基建，唔係全面科技股災。</p>

  <h4>核心論點</h4>
  <ul>
    <li><b>「15%」唔係全部債務嘅成本，但係邊際買家嘅真實要求回報。</b>呢個 15% 係 2032 年到期、票面息 9.625% 嘅債券喺二手市場嘅 yield；CoreWeave 本身仍然只付 9.625%。但當新買家要求 15%，代表市場對呢家公司嘅風險定價已經跳級。</li>
    <li><b>真正嘅壓力集中喺 2028 年到期嘅一小塊。</b>公司約 <b>$35B</b> 債務嘅加權平均成本約 <b>8.4%</b>，只有約 <b>4%</b>（約 <b>$13 億</b> term loan）實際接近 15%，且 2028 年 3 月才到期。换言之，呢次係「預警」多過「即時違約」。但 credit 市場嘅訊號從來唔係關於今天，而係關於「再融資窗口仲開唔開」。</li>
    <li><b>商業模式將股價同債價綁死。</b>CoreWeave 用晶片同客戶合約抵押借錢，再買 NVIDIA 晶片出租。每一點融資成本上升，都會直接吃掉每份合約嘅最終利潤。呢個結構喺需求加速時係槓桿，喺利率上升時係絞索。</li>
    <li><b>「backlog 好大」同「債息好高」可以同時成立，而且可以持續好耐。</b>公司 backlog 超過 <b>$1,040 億</b>，之後再新增 <b>$250 億+</b> net new commitments。問題係這些承諾嘅時間表、客戶集中度、同埋「客戶會唔會違約」——backlog 係未來收入，債息係今天嘅現金成本。</li>
    <li><b>呢集嘅隱含結論：AI 唔似 2000 年 dot-com，但AI 基建嘅資本結構愈來愈似 2008 年前嘅槓桿收購。</b>分別在於底層資產（GPU）貶值更快、客戶更集中、現金流更依賴少數 hyperscaler 同 AI lab。</li>
  </ul>

  <h4>關鍵數據</h4>
  <table class="kv">
    <tr><th>CoreWeave 股價（10-14 盤中）</th><td>$70.37，單日 −10%，全週約 −25%</td></tr>
    <tr><th>2032 債券市場 yield</th><td>15%（票面息 9.625%，價格下跌所致）</td></tr>
    <tr><th>整體債務 / 加權成本</th><td>約 $35.6B；blended cost 約 8.4%</td></tr>
    <tr><th>真正付 ~15% 嘅債務</th><td>約 $1.3B term loan，2028 年 3 月到期（佔總債務約 4%）</td></tr>
    <tr><th>CDS 利差（10-15）</th><td>1,194 bps（約每年 12% 保費）</td></tr>
    <tr><th>最近一季淨利息支出</th><td>$6.4 億，約等於 $26 億收入嘅 24%</td></tr>
    <tr><th>Debt service coverage</th><td>約 0.3x（健康水平通常 1.25–1.50x）</td></tr>
    <tr><th>Backlog</th><td>Q2 末 > $1,040 億，之後新增 > $250 億</td></tr>
    <tr><th>2026 年收入預期</th><td>約 $120 億（2022 年 $1,500 萬、2024 年近 $20 億）</td></tr>
  </table>

  <blockquote>
    「Yikes.」
    <cite>— Elon Musk 回應 Chamath 貼出 CoreWeave 債券 yield 15% 嘅帖文（一個字，成為本週 AI 信用市場嘅最佳註腳）</cite>
  </blockquote>

  <blockquote>
    「市場而家嘅反應係唔理性嘅。」
    <cite>— CoreWeave CEO 內部備忘錄大意（公司其後公開反駁，指基本面冇變；FT 亦指出 backlog 確實提供相當程度嘅收入能見度）</cite>
  </blockquote>

  <h4>行業 insight</h4>
  <p>呢段最值錢嘅唔係「CoreWeave 會唔會破產」，而係一個分析框架：<b>AI 基建公司要同時通過三張資產負債表——晶片供應商、債權人、同客戶。</b>當三張表嘅周期錯位（晶片 2 年折舊、債券 5–7 年到期、客戶合約 3–5 年），任何一邊收緊，股價都會先於現金流反映。Polymarket 甚至開咗「CoreWeave 幾時破產」嘅盤口——呢個本身已經係情緒指標。對 James 嘅啟示：睇 AI 股唔可以只看 revenue growth，要睇 <b>interest coverage、債務到期結構、同客戶集中度</b>；呢三樣係 2026 年 AI 投資嘅「新三張報表」。</p>

  <h3>② AI 嘅通縮威力：當軟件可以被「反編譯」（31:14–45:44）</h3>

  <h4>主題</h4>
  <p>如果上一段講 AI 嘅「成本」，呢段講 AI 嘅「價格破壞」。Ben Horowitz 在場令呢個題目特別有份量——a16z 睇軟件生意睇咗十幾年。本段嘅核心命題係：<b>AI 唔止幫人寫新 code，仲可以將舊 binary 反編譯、理解、再用現代語言重寫。</b>一旦「理解舊系統」嘅邊際成本由「一個資深工程師團隊做兩年」跌到「一個 agent 做兩日」，企業軟件長期靠「轉換成本 + 歷史包袱」收租嘅模式就會被拆穿。</p>

  <h4>核心論點（本段＋延伸分析）</h4>
  <ul>
    <li><b>軟件嘅護城河有三種：network effect、data、同 switching cost。</b>AI 反編譯直接攻擊第三種。當客戶知道「搵 AI 重寫一個 compatible 版本」只係幾萬美金，現有 vendor 嘅續約談判力就會塌。</li>
    <li><b>呢個係「通縮」而唔係「通漲」。</b>AI 令軟件供給曲線右移：同樣功能，更多供應、更低價格。對用家係好事，對靠 license + maintenance 收費嘅 incumbent 係災難。呢個亦解釋咗點解 software 板塊喺 AI 熱潮中反而唔係全部都升——市場開始區分「AI 受益者」同「AI 被吃掉者」。</li>
    <li><b>法律係唯一嘅減速帶，但唔係防火牆。</b>反編譯本身受版權同 DMCA 限制；實務上要走 clean-room（一邊讀 decompiled source 寫規格，另一邊只按規格重寫）。AI 令 clean-room 嘅成本大跌，但「克隆成熟產品」仍然有專利、商標、同 trade secret 風險。呢個係法律未測試嘅灰色地帶，唔係清晰嘅紅線。</li>
    <li><b>對 AI 基建反而係利好。</b>軟件越便宜、越多公司願意重寫舊系統，對 compute 嘅需求越大。呢個係「application 層通縮、infrastructure 層通漲」嘅剪刀差——亦係點解 neocloud 嘅長期需求故事仍然成立，即使短期 credit 市場唔信。</li>
    <li><b>最受影響嘅唔係初創，而係「靠版本升級收費」嘅中年軟件公司。</b>初創本來就冇舊 code；巨頭有資源自己做 AI 重寫；最危險嘅係 mid-market SaaS：產品成熟、增長放緩、靠 maintenance 續約、但冇 network effect。</li>
  </ul>

  <h4>關鍵數據 / 觀察指標</h4>
  <table class="kv">
    <tr><th>軟件公司收入結構</th><td>License / subscription + maintenance + services；越成熟嘅公司，maintenance 佔比越高</td></tr>
    <tr><th>AI 重寫成本</th><td>視系統大小而定；對中型 legacy 系統，已由「人月」級降到「人日」級（本段方向性判斷，非精確報價）</td></tr>
    <tr><th>最脆弱嘅品類</th><td>ERP 外掛、行業垂直 SaaS、報表／表單工具、內部 workflow 系統</td></tr>
    <tr><th>最安全嘅品類</th><td>有雙邊 network effect（marketplace）、有專有數據飛輪、有合規鎖定（金融／醫療）</td></tr>
  </table>

  <blockquote>
    「軟件正在變成同其他製造業一樣嘅生意：一旦生產成本跌，價格就會跌。」
    <cite>— 本段論點嘅濃縮（不是逐字引用；原段以「decompiled software」為例展開）</cite>
  </blockquote>

  <h4>行業 insight</h4>
  <p>呢個框架可以用嚟審視任何軟件投資：<b>你付嘅溢價，究竟係買「未來現金流」，抑或只係買「客戶懶得換」？</b>如果係後者，AI 就係你嘅結構性空頭。對創業者嘅啟示相反：呢個係十年一遇嘅「重寫所有垂直軟件」窗口——唔係做另一個 ChatGPT wrapper，而係揀一個又舊又悶、客戶又被迫續約嘅品類，用 AI 重寫一個 10 倍便宜嘅版本。</p>

  <h3>③ Anthropic 投資者日：$168 億季度收入，點解市場仍然「mixed」？（45:44–1:03:45）</h3>

  <h4>主題</h4>
  <p>Anthropic 喺 IPO 前首次向潛在投資者披露季度財務：Q3 收入 <b>$168 億</b>，按季增長 <b>45%</b>，adjusted basis 有盈利、cash-flow positive。標題數字非常亮眼，但 market reaction 兩極——呢段就係拆解「亮眼數字下面嘅紅旗」。</p>

  <h4>核心論點</h4>
  <ul>
    <li><b>增長率正在減速，而且減速得好快。</b>Q1 $47 億 → Q2 $116 億（+147% QoQ）→ Q3 $168 億（+45% QoQ）。由三位數增長跌到雙位數，只用了三個月。對一間以「hypergrowth」定價嘅公司，呢個係最重要嘅邊際變化。</li>
    <li><b>「adjusted profitable」唔等於 GAAP profitable。</b>公司話 adjusted basis 有盈利、cash-flow positive；但 IPO 估值睇嘅係 GAAP 利潤、free cash flow、同埋股東攤薄。調整項（尤其 stock-based compensation 同折舊）會係招股書嘅關鍵戰場。</li>
    <li><b>單位經濟嘅第一個正面訊號：每 $1 compute 換 $1.70 收入。</b>呢個比例如果可持續，代表 Anthropic 唔係「賣一元蝕兩元」嘅燒錢機器；但呢個係 Q3 嘅數字，受價格、mix、同折舊政策影響，未必等於長期 steady state。</li>
    <li><b>估值預期已經由 $2T 降到約 $1.5T。</b>以年底 $1,100 億 annualized revenue 計，約 14–18x forward revenue。對 45% 增長嘅公司唔算離譜，但前提係「增長唔再減速」同「margin 可以擴張」。任何一個假設失守，估值就要重設。</li>
    <li><b>「紅旗」唔係造假，而係「增長質量」。</b>收入集中喺少數大型 enterprise / API 客戶、compute 承諾巨大、同埋 IPO 時間窗口（11 月）令公司有誘因修飾數字。呢啲都係投資者日一定會被問嘅問題。</li>
  </ul>

  <h4>關鍵數據</h4>
  <table class="kv">
    <tr><th>Q3 2026 收入</th><td>$168 億（Q2 $116 億，Q1 $47 億）</td></tr>
    <tr><th>QoQ 增長</th><td>+45%（Q2 為 +147%）</td></tr>
    <tr><th>盈利</th><td>Adjusted basis 盈利；cash-flow positive</td></tr>
    <tr><th>Compute 效率</th><td>每 $1 compute 支出換 $1.70 收入</td></tr>
    <tr><th>市場預期年底 ARR</th><td>約 $1,100 億</td></tr>
    <tr><th>IPO 時間</th><td>報道指 11 月（Thanksgiving 前）</td></tr>
    <tr><th>估值區間</th><td>約 $1.5T（早前曾傳 $2T）</td></tr>
    <tr><th>對比 OpenAI</th><td>OpenAI ARR 口徑爭議：對外近 $700 億 vs 公司自身口徑近 $500 億，差距約 $200 億</td></tr>
  </table>

  <blockquote>
    「Anthropic 告訴投資者，第三季收入達到 168 億美元，並在調整後基礎上錄得盈利。」
    <cite>— CNBC / Bloomberg 對投資者日嘅報道（2026-10-14/15）</cite>
  </blockquote>

  <h4>行業 insight</h4>
  <p>呢段嘅真正價值係一個「IPO 前財務披露」嘅閱讀方法：<b>先睇增長率嘅二階導數，再睇調整項，最後睇客戶集中度。</b>Anthropic 嘅絕對數字仍然驚人，但由 +147% 跌到 +45% 係一個清晰嘅減速訊號；而 OpenAI 嘅 ARR 口徑爭議（$700 億 vs $500 億）進一步令市場懷疑整個行業嘅「收入定義」。當行業龍頭都要用唔同口徑講故事，估值嘅錨就一定不穩。對 James 嘅啟示：IPO 認購唔好只看 headline revenue，要迫自己問「呢個數字用邊種口徑？下一季嘅增速係幾多？誰是付錢的人？」</p>

  <h3>④ Psyop Corner：Anthropic 嘅「自我複製 AI」警告，係研究定公關？（1:03:45–1:22:19）</h3>

  <h4>主題</h4>
  <p>Anthropic 發表研究，警告細模型可能喺幾個月內有能力喺商業 IoT 裝置上自我複製；同時公開指控 DeepSeek、Moonshot、MiniMax 進行「蒸餾攻擊」，大規模提取 Claude 能力。Besties 將呢啲公告放入「Psyop Corner」——即係問：<b>呢啲係真嘅安全風險，抑或 IPO 前嘅監管／公關操作？</b></p>

  <h4>Anthropic 研究嘅實質內容</h4>
  <ul>
    <li><b>測試設置：</b>用 15 部約 $55 嘅雜牌 Android TV box 串連，跑 Gemma4-26B-A4B，速度只有 <b>0.39 tokens/second</b>。呢個速度慢到冇實用價值，但證明「喺廉價裝置上分散式推理」技術上可行。</li>
    <li><b>模型能力：</b>9B 模型喺 9 種硬件類型中，有 8 種成功跑起 inference；30B 以下模型已能完成複製鏈嘅多數單一步驟，但 end-to-end 仍然會出錯。GLM-5.2 或更強模型已可 end-to-end 複製。</li>
    <li><b>時間預測：</b>如果細模型按歷史速度進步，年底前就會達到呢個能力水平；「weight-based replicator」可能隨後出現。</li>
    <li><b>為何難拆：</b>冇中央節點可以關閉；傳播速度慢（doubling time 以「日」計），但可以自行適應陌生裝置。</li>
    <li><b>蒸餾攻擊：</b>Anthropic 稱三個實驗室合共透過約 <b>24,000</b> 個欺詐帳號、超過 <b>1,600 萬</b>次對話提取 Claude 能力：DeepSeek 15 萬+、Moonshot 340 萬+、MiniMax 1,300 萬+。</li>
  </ul>

  <h4>核心論點 / 兩種讀法</h4>
  <ul>
    <li><b>認真讀法：</b>呢個係首個「唔需要 datacenter、只需要一堆爛 IoT 裝置」嘅自我複製路徑。即使速度慢，防禦方仍然面對「冇中央開關」嘅噩夢。對監管者而言，呢個係要求 AI 公司保留 kill switch、模型指紋、同部署審批嘅理由。</li>
    <li><b>Psyop 讀法：</b>研究發布時間正值 IPO 前、監管辯論升溫；測試用 15 部 TV box 跑 0.39 tok/s，距離「真實世界威脅」仲有好遠。將「實驗室條件下嘅可行性」講成「幾個月內嘅現實風險」，會令公眾高估威脅、亦令 Anthropic 喺政策桌上佔據道德高地。</li>
    <li><b>兩者可以同時成立。</b>研究本身有技術含量，但發布時機同框架（「months away」）確實有議程設定效果。呢個就係 Psyop Corner 想拆嘅嘢：<b>唔係話研究假，而係話「研究 → 恐懼 → 監管 → 競爭優勢」呢條路徑值得警惕。</b></li>
    <li><b>蒸餾攻擊嘅另一面：</b>如果外國實驗室真係靠蒸餾追上，咁出口管制嘅效果就被削弱；但同時，Anthropic 亦可以用「國家安全」框架要求更嚴格嘅模型保護——呢個對佢自己嘅商業利益有利。Sacks 同 Brian Armstrong 嘅相關帖文，正正就係質疑呢種「安全論述 = 競爭護城河」嘅現象。</li>
  </ul>

  <h4>關鍵數據</h4>
  <table class="kv">
    <tr><th>測試硬件</th><td>15 部雜牌 Android TV box，約 $55/部</td></tr>
    <tr><th>模型 / 速度</th><td>Gemma4-26B-A4B，0.39 tokens/sec</td></tr>
    <tr><th>硬件泛化</th><td>9B 模型在 9 種硬件中 8 種成功跑 inference</td></tr>
    <tr><th>能力門檻</th><td>30B 以下可完成多數單步；GLM-5.2+ 可 end-to-end</td></tr>
    <tr><th>蒸餾規模</th><td>24,000 帳號 / 1,600 萬+ 對話</td></tr>
    <tr><th>DeepSeek / Moonshot / MiniMax</th><td>15 萬+ / 340 萬+ / 1,300 萬+ exchanges</td></tr>
  </table>

  <blockquote>
    「我哋嘅實驗顯示，細模型可能只差幾個月，就有能力喺商業 IoT 裝置上自我複製。」
    <cite>— Anthropic Research: “AI models may be capable of self-replicating without access to a datacenter”</cite>
  </blockquote>

  <h4>行業 insight</h4>
  <p>呢段最值得帶走嘅，唔係「AI 會唔會毀滅世界」，而係<b>「安全」已經成為 AI 公司嘅競爭策略之一</b>。當監管門檻提高，最大嘅 incumbent 反而受惠——因為合規成本對佢哋而言係固定成本，對初創係入場費。James 可以留意一個簡單指標：每次 AI 安全恐慌之後，係邊啲公司嘅估值／政策地位上升？如果答案來來去去都係同一兩間，咁「安全」就唔止係安全。</p>

  <h3>⑤ 理解 Bill Gates 的「末日論」（1:22:19–完）</h3>

  <h4>主題</h4>
  <p>Bill Gates 喺 2026 年 8 月底發表近 <b>6,000 字</b>文章，警告 AI 可能帶嚟經濟動盪、入門級職位萎縮，並提出新稅項同禁令。9 月接受 NBC 訪問時更講出「AI 強大到足以導致十億人死亡」嘅講法。呢段嘗試理解：一個長期以「科技樂觀主義」見稱嘅人，點解會變成最響嘅 doomer？</p>

  <h4>核心論點</h4>
  <ul>
    <li><b>Gates 嘅悲觀唔係關於「AI 變壞」，而係關於「壞人拿到 AI」。</b>他嘅原話係「從來冇一種武器好似『有惡意嘅人 + 最新 AI 工具』咁強大」。呢個係生物安全／公共衛生嘅框架，唔係科幻嘅「AI 覺醒」框架。</li>
    <li><b>他同時相信 AI 係「最偉大嘅平等器」。一句話總結他嘅世界觀：</b>「AI 要麼係史上最偉大嘅平等器，要麼係最嚴重嘅不公來源。」呢個唔係矛盾，而係「視乎治理」嘅條件式樂觀。</li>
    <li><b>他提出嘅工具係稅同禁令，而非自願承諾。</b>呢點同他多年來喺瘧疾、小兒麻痹症嘅工作一致：公共衛生問題需要政府強制力，唔可以靠企業自律。</li>
    <li><b>Besties 嘅質疑（推測性框架）：</b>Gates 嘅警告會唔會被監管捕獲（regulatory capture）？由最大嘅 incumbents 制定規則，最後只會鞏固佢哋嘅地位。另一方面，如果 Gates 講得對，咁「自願安全」就明顯唔夠——呢個就係自由市場同公共安全之間嘅經典張力。</li>
    <li><b>對投資者嘅啟示：</b>Gates 嘅言論會影響政策預期，而政策預期會影響 AI 股嘅風險溢價。唔需要同意他，但需要將「AI 監管風險」當成一個獨立變數，而唔係只當成新聞噪音。</li>
  </ul>

  <h4>關鍵數據 / 時間線</h4>
  <table class="kv">
    <tr><th>2026-08-26</th><td>Gates 發表近 6,000 字文章，提出稅項同禁令</td></tr>
    <tr><th>2026-09-25</th><td>NBC 訪問：AI 足以導致「十億人死亡」</td></tr>
    <tr><th>文章核心句</th><td>「AI 要麼係最偉大嘅平等器，要麼係最嚴重嘅不公來源」</td></tr>
    <tr><th>政策建議</th><td>新稅、禁令、經濟／教育／社會安全網改革</td></tr>
    <tr><th>經濟警告</th><td>入門級職位萎縮、跨行業勞工被取代</td></tr>
  </table>

  <blockquote>
    「AI 確實強大到足以驅動一些事件……導致十億人死亡。從來冇一種武器好似『有惡意嘅人使用最新 AI 工具』咁強大。」
    <cite>— Bill Gates，NBC News 訪問，2026-09-25（Forbes / Guardian 轉述）</cite>
  </blockquote>

  <blockquote>
    「AI 要麼會係史上最偉大嘅平等器，要麼會係最嚴重嘅不公來源。」
    <cite>— Bill Gates，2026 年 8 月文章（Axios 引述）</cite>
  </blockquote>

  <h4>行業 insight</h4>
  <p>Gates 嘅轉向係一個訊號：<b>AI 辯論已經由「能力」轉向「分配」。</b>2023–2025 年大家問「AI 做得到咩」；2026 年開始問「誰得到好處、誰承擔風險」。呢個轉向會令政策風險變成 AI 估值嘅長期折讓因素，亦會令「安全／合規」由成本中心變成競爭壁壘。對 James 嘅啟示：如果有人同你講 AI 投資只看技術突破，你可以反問——「咁監管風險你點定價？」</p>

  <div class="callout" style="margin-top:22px">
    <b>🎯 今日 All-In 的三個 takeaway：</b><br>
    1. <b>信用市場係 AI 泡沫嘅真正哨兵。</b>股價可以靠故事撐，債息唔會。CoreWeave 嘅 15% yield 係一個唔可以忽略嘅訊號，即使公司短期唔會違約。<br>
    2. <b>AI 嘅通縮會先殺軟件，再養基建。</b>應用層價格戰對用家有利，但對靠 switching cost 收租嘅 SaaS 係結構性風險；同時，軟件重寫需求會支撐 compute。<br>
    3. <b>「安全」已經係一種商業策略。</b>Anthropic 嘅研究同蒸餾指控，無論真假，都會改寫監管格局；投資者要同時讀技術同讀議程。
  </div>
</section>
'''

# =====================================================================
# MY FIRST MILLION (NEW)
# =====================================================================
cards += f'''
<!-- ==================== My First Million ==================== -->
<section class="pod">
  <div class="pod-head">
    <h2>My First Million</h2>
    <span class="host">Sam Parr &amp; Shaan Puri</span>
    <span class="tag new">新集</span>
  </div>
  <div class="ep-title">the 6 traits of people who can’t stop making money</div>
  <div class="ep-meta">📅 2026-10-16 11:00 UTC · ⏱ 39 分 18 秒（2,358 秒） · 🎙 Episode 872 · Sam Parr &amp; Shaan Puri</div>

  <div class="callout">
    <b>一句話總結：</b>呢集係 MFM 近年最「乾貨」嘅一集——唔講潮流、唔講 idea，而是嘗試定義一種人：<b>Natural Moneymaker（天生賺錢者）</b>。佢哋唔一定係最好嘅 founder 或 CEO，但佢哋嘅 hit rate 高得唔合理、對錢極度冷靜、永遠覺得「perfect number is more」。Sam 用三個人物（Nick Kokonas、Jay Gould、Syed Balkhi）拆解六個特質，最後給出兩條可以立刻用嘅理財規則。
  </div>

  <div class="chapters">
    <span class="tc">0:00</span> Natural Money-Makers<br>
    <span class="tc">1:52</span> 天生賺錢者嘅六個特質<br>
    <span class="tc">3:10</span> Nick Kokonas 的故事<br>
    <span class="tc">8:12</span> Jay Gould 的故事<br>
    <span class="tc">10:00</span> 呢種能力學唔學得到？<br>
    <span class="tc">13:04</span> Syed Balkhi 的故事<br>
    <span class="tc">17:58</span> 只花「二階導數」<br>
    <span class="tc">22:27</span> 用有價值嘅時間換無用嘅金錢<br>
    <span class="tc">26:50</span> 其他一樣會贏嘅玩法
  </div>

  <h3>① 定義：Natural Moneymaker 唔等於 Founder</h3>

  <p>Sam 一開始就劃清界線：Ted Turner 創立 CNN，有願景、識招人、識揀產品，但佢唔係 natural moneymaker。Natural moneymaker 係另一種生物——<b>做 deal、做 broker、將自己插入每一個有錢流過嘅情境</b>；佢哋通常唔會高調 build in public，但會喺多個完全唔同行業建立由一億到幾百億嘅生意。</p>

  <blockquote>
    「A natural moneymaker is a person who tends to be involved in dealmaking, brokering, and inserting themselves into situations. They tend to not build publicly, and they've built multiple businesses ranging from 100 million to many billions in multiple different fields.」
    <cite>— Sam Parr, MFM #872</cite>
  </blockquote>

  <p>最關鍵嘅差異係「溫度」：</p>

  <blockquote>
    「A natural moneymaker does all those things, plus they're way colder about money. And they're way more logical and they're way more rational.」
    <cite>— Sam Parr, MFM #872</cite>
  </blockquote>

  <p>呢個「冷」唔係冷漠，而係<b>唔會俾情感影響資產配置</b>。Great founder 往往靠熱情招募、靠信念捱過低谷；natural moneymaker 靠數字做決定，唔會因為「呢間公司係我親生仔」而唔砍成本。呢個特質令佢哋嘅 hit rate 高得不合理：普通人 fail, fail, fail, succeed；佢哋係 succeed, fail, succeed, succeed。</p>

  <h3>② 六個特質（附故事證據）</h3>

  <h4>特質一：對錢極度冷靜（Unemotional about business）</h4>
  <p>Sam 講咗 Carl Icahn 嘅經典故事：Icahn 買下一間航運公司，返工兩星期後發現有 12 層樓嘅員工「唔知做咩」，於是即日全部解僱。幾個月後他問團隊：「你有冇發覺嗰 12 層樓嘅人其實做緊嘢？冇咗佢哋係咪好唔掂？」團隊答：「完全冇發覺。」</p>
  <p>呢個故事嘅重點唔係「裁員好叻」，而係<b>佢可以用純粹嘅數字邏輯覆蓋人情壓力</b>。普通人會講「佢哋有家庭」、「公司文化唔可以咁」；natural moneymaker 會講「呢個 cost centre 冇產出，therefore 砍」。呢種冷靜係一種稀有嘅認知能力，唔係道德缺陷。</p>

  <h4>特質二：天生嘅「鼻子」（A great nose）</h4>
  <p>你問佢哋點解知道呢單嘢會賺錢，佢哋講唔出長篇大論——<b>「It's a lot of instinct.」</b>佢哋可以聞到邊度有錢、邊度有廢話。Sam 形容呢種人「sniff out bullshit where bullshit is, sniff out opportunity where opportunity is」。</p>
  <p>呢個特質最難複製，因為它唔係分析框架，而係 pattern recognition 嘅壓縮版。佢哋睇過太多 deal、太多人、太多失敗，於是大腦可以喺幾秒內將一個新情境匹配到舊 pattern。呢個亦解釋咗點解佢哋成日「只講幾句」就決定投入——唔係衝動，而係個 model 已經訓練好。</p>

  <h4>特質三：極端最大化者（Maximizer）</h4>
  <p>Sam 用一句說話總結：<b>「Diminishing returns are still returns.」</b>普通人覺得「夠啦，呢啲錢我唔需要」；natural moneymaker 覺得「仲有 return，點解唔做？」佢哋唔會講「too much trouble」，亦唔會講「enough is enough」。</p>
  <p>最極端嘅例子係 Jay Gould：他已經肺結核末期、妻子兩年前過身、只剩約一年命，但當有人喺家庭飯局同佢講「有間鐵路公司就快執，你可以買」，佢下星期就同家人講：「我想清楚啦，我要返去做我初戀——賺錢。」做完單 deal，六個月後去世。</p>
  <blockquote>
    「The perfect number is more.」
    <cite>— Sam Parr 形容 natural moneymaker 嘅目標函數, MFM #872</cite>
  </blockquote>
  <p>呢個特質有黑暗面：佢哋可能永遠唔會滿足，亦可能喺唔需要再冒險嘅時候繼續冒險。但從「賺錢」呢個單一維度看，呢個正正係佢哋嘅引擎。</p>

  <h4>特質四：能夠啃複雜性（Comfortable with complexity）</h4>
  <p>普通人鍾意「keep it simple」；natural moneymaker 面對一啲充滿 contingencies 嘅 deal（如果 A 發生就 B，如果 B 發生就 C），可以喺腦入面快速拆解，睇出價值鎖喺邊，再同 alternatives 比較。Sam 認為呢個需要好高 IQ。</p>
  <p>但呢度有個微妙位：佢哋唔係鍾意複雜，而係<b>能夠將複雜壓縮成簡單</b>。Shaan 嘅補充係全集最精彩嘅一句：</p>
  <blockquote>
    「The logic fits on a fortune cookie.」
    <cite>— Shaan Puri, MFM #872</cite>
  </blockquote>
  <p>即係話：<b>決定嘅理由可以寫喺一張 fortune cookie 紙上面，但執行嘅細節可以極度複雜。</b>佢哋唔需要寫六頁 memo 說服自己；佢哋只需要一個簡單到唔可以反駁嘅邏輯，然後搵人、搵機器、搵方法將它執行。</p>

  <h4>特質五：征服者基因（A streak of wanting to conquer）</h4>
  <p>Sam 引用拿破崙嘅講法：當同儕話「我係愛爾蘭人／意大利人」，拿破崙答「我係征服者嘅後代」。Natural moneymaker 由細細個就有一種「我要贏」嘅競爭欲，而且係針對金錢呢個記分板。呢個唔係後天培養嘅「目標設定」，而係一種近乎生理嘅 drive。</p>

  <h4>特質六：高 IQ ＋ 自幼浸淫（Nature + Nurture）</h4>
  <p>Sam 認為呢種能力「tends to be instilled or tends to be they're born with」。佢觀察到 natural moneymaker 多數喺細個時，屋企已經成日講 deal、講錢、講投資。呢個唔係 formal education，而係一種語言環境——好似音樂家喺音樂家庭長大，耳朵自然靈敏。</p>
  <p>呢個答案有點宿命論，但 Sam 嘅結論唔係「你冇就冇」。佢話：你可以問「如果我唔係呢種人，我可以偷邊個特質？」呢個先係實用嘅態度。</p>

  <h3>③ 三個人物案例</h3>

  <h4>Nick Kokonas：由交易員到全美第一餐廳</h4>
  <ul>
    <li><b>起點：</b>大學讀哲學，但鍾意數學；想做 trader，但只拿到 bank offer，唔係 trading desk。最後佢還是入咗交易員呢行。</li>
    <li><b>交易員年代：</b>每日贏輸一間屋嘅價值——「I'd win or lose like 300 grand in a day.」佢嘅公司曾經靠一個 ETF arbitrage，一年賺 <b>$1 億</b>利潤。</li>
    <li><b>套利邏輯：</b>ETF 價格同底層一籃子股票嘅即時價格有輕微 slippage。佢發現可以用期權／期貨複製嗰籃股票，然後喺 ETF 同籃子之間無風險套利。關鍵係速度——當時其他人仲用紙仔跑腿報價，佢找人鋪光纖由紐約交易所去芝加哥交易所，將報價時間由 30 秒壓到接近即時。</li>
    <li><b>轉場：</b>離開交易後，佢同 Grant Achatz 開咗 Alinea。當時佢喺 forum 公開宣言：「我哋要創造全美最偉大嘅餐廳；Michelin 唔俾三星，係佢哋嘅損失，唔係我哋嘅。」結果 Alinea 成為紐約以外第一間三星餐廳（佢講法是「first Michelin star restaurant outside New York」）。</li>
    <li><b>數字：</b>Alinea 高峰年收入約 <b>$2,600 萬</b>，利潤率接近 <b>20%</b>；COVID 期間所有餐廳停擺，佢哋轉做 $35 外賣晚餐，仍然賺錢。</li>
    <li><b>「冇 off button」：</b>錄音完結後，佢同 Sam 講剛用 <b>$15 萬</b>買咗一個值 <b>$100 萬</b>嘅紅酒 collection。佢唔係刻意搵，而係「deals 會自己出現」——因為佢個腦永遠喺度掃描。</li>
  </ul>

  <h4>Jay Gould：死前六個月仍然做 deal</h4>
  <ul>
    <li>1800 年代鐵路／金融巨頭；John D. Rockefeller 稱佢為「史上最偉大嘅商業頭腦」。</li>
    <li>妻子兩年前過身；他自己患肺結核，醫生話只剩約一年命；家中有三個女兒、兩三個姪女要照顧。</li>
    <li>家庭飯局期間，有人耳語通知佢有間鐵路公司瀕臨破產、可以低價收購。女兒們求他：「我哋屋企已經好好，唔好再做啦。」他答：「我會想想。」</li>
    <li>下星期同一場合，電話再響。他放下電話，同家人講：「我想清楚啦。我要返去做我初戀——賺錢。」</li>
    <li>他完成收購，六個月後去世。</li>
  </ul>
  <p>Sam 用呢個故事唔係讚美，而係展示「maximizer」可以去到幾盡：<b>連死亡都唔係停止條件。</b></p>

  <h4>Syed Balkhi：由 WordPress blog 到多元資產機器</h4>
  <ul>
    <li>由巴基斯坦移民美國，冇錢；先寫 WordPress blog，賺到第一桶金。</li>
    <li>用 blog 嘅利潤同影響力收購 WordPress plugins，建立 Awesome Motive 生態；之后再買房地產、股票、私人公司、加油站。</li>
    <li>Sam 不解：「你身家幾億，點解要買一座 $20 萬嘅加油站？」Syed 答：「因為我可以從中得到好回報。」</li>
    <li>他嘅天然氣站多數係 <b>triple net lease</b>（租客負責稅、保險、維修），所以「冇嘢要管」；選址原則係「hard corner, good area」。</li>
    <li>最出名嘅一句：「每次我老婆懷孕，我就買一座加油站。」因為加油站嘅現金流可以養大個小朋友。</li>
  </ul>

  <h3>④ 兩條可以即刻用嘅理財規則</h3>

  <h4>規則一：Only spend the second derivative（只花二階導數）</h4>
  <p>Syed 嘅 mentor 教他：<b>你唔係花收入，你係花收入所產生嘅投資回報。</b>如果你一年賺 $10 萬，呢 $10 萬唔係你嘅消費池；你將它投資，然後只花它產生嘅回報（例如 $1 萬）。呢個聽落很慘，但隨着本金累積，消費能力會複利上升。</p>
  <ul>
    <li>第一年：本金 $10 萬，回報約 $1 萬 → 你可花 $1 萬（生活方式唔可以升級超過呢個數）。</li>
    <li>第二年：再投入 $10 萬，本金 $20 萬，回報約 $2.4 萬 → 你可花 $2.4 萬。</li>
    <li>五至七年後：本金夠大，理論上可以只靠投資回報生活，唔使動用本金。</li>
  </ul>
  <p>Shaan 嘅版本更簡單：<b>年度預算不超過流動淨資產嘅 3%。</b>咁樣你晚上可以睡得着，因為你知道本金永遠唔會用盡。兩個版本本質一樣：<b>唔好碰 principal，只花 interest。</b></p>

  <h4>規則二：唔好用有價值嘅時間換無用嘅金錢</h4>
  <p>Shaan 嘅觀察係全集最刺中人心嘅一段：很多成功人士已經過了「錢可以改善生活」嘅點，但仍然繼續做 deal，因為佢哋嘅身份、地位、同自我價值都綁咗喺「我好叻做生意」上面。結果係：</p>
  <blockquote>
    「You're trading valuable hours for useless dollars.」
    <cite>— Shaan Puri, MFM #872</cite>
  </blockquote>
  <p>呢句說話嘅殘酷在於：<b>錢本身唔再有用，但交易仍然繼續。</b>佢哋會用「為咗小朋友」、「想小朋友睇到我努力」去合理化，但 Shaan 嘅反駁好直接：</p>
  <blockquote>
    「Your kids just want to see you.」
    <cite>— Shaan Puri, MFM #872</cite>
  </blockquote>
  <p>佢自己嘅例子：與其讀多篇文章、寫多封 email，不如去跑步、去學鋼琴、去令婚姻多 20% 樂趣。呢啲事唔會賺錢，但會真正提升生活質量。最難嘅係「say no to something you're good at」——因為喺擅長嘅領域，你有即時反饋、有尊重、有成就感；而去到唔擅長嘅領域，你會即刻覺得自己笨。</p>

  <h3>⑤ 其他都會贏嘅玩法（Archetypes）</h3>
  <p>Sam 同 Shaan 即場分類咗幾種同樣可以贏嘅 founder 類型，重點係：<b>唔係每個人都要成為 natural moneymaker。</b></p>
  <table class="kv">
    <tr><th>Missionary（傳教士）</th><td>Brian Chesky：將生命奉獻畀一個使命（Airbnb + 令旅行變好），唔係純粹為錢。</td></tr>
    <tr><th>Extreme balancer（極端平衡者）</th><td>Jesse Itzler：工作同生活都去到極端，但兩邊都係自己設計嘅；「我知我係邊個，我要玩到盡」。</td></tr>
    <tr><th>Tank（坦克）</th><td>Frank Slootman：操作型、軍事化、極高痛耐受度、大 span of control；「behind me」，可以頂住子彈向前行。</td></tr>
    <tr><th>Trickster（魔術師）</th><td>Alex Tew（Million Dollar Homepage、Calm）、Eric Ryan（Method、Olly、Wellie）：用創意將平凡物件變成 viral 產品，搵到別人忽略嘅裂縫。</td></tr>
    <tr><th>Fierce nerd（兇猛書呆子）</th><td>Zuckerberg、Travis Kalanick：表面 nerdy，實際上極度好勝；你要喺佢哋嘅戰場（chess、Magic: The Gathering）先見到真正嘅 fury。</td></tr>
    <tr><th>Deep student（深度研究者）</th><td>Dan Carlin、David Senra：唔親自下場，但將歷史／人物研究到極深，成為某一領域嘅百科全書。</td></tr>
    <tr><th>Sniffer（鼻子）</th><td>Austin Rief：早過所有人聞到趨勢（例如某些早期投資），唔一定自己操作，但 conviction 極高。</td></tr>
  </table>

  <blockquote>
    「Do you think you'll have more success fighting your nature or working with your nature?」
    <cite>— Ray Dalio（Shaan 引述）, MFM #872</cite>
  </blockquote>

  <h3>⑥ 今日 MFM 的三個 takeaway</h3>
  <div class="callout">
    <b>1. 唔好問「我係唔係 natural moneymaker」，問「我可以偷邊個特質」。</b>如果你唔夠冷靜，可以由「每次做決定前寫低三個數字」開始；如果你唔夠 maximizer，可以問「呢個 return 係咪真係細到唔值得做？」<br><br>
    <b>2. 二階導數規則係一條可以立刻執行嘅防火牆。</b>計算你嘅流動淨資產，設定年度預算 ≤3%（或只花投資回報），然後將收入同消費完全分開。呢條規則唔會令你發達，但會令你永遠唔會因為過度消費而歸零。<br><br>
    <b>3. 最貴嘅唔係你買咗咩，而係你用咩時間去換。</b>如果你已經唔需要更多錢，下一個最高回報嘅投資可能係：跑步、學一個新技能、或者令你最重要嘅關係好 20%。呢啲回報唔會顯示喺 bank account，但會顯示喺你嘅人生。
  </div>
</section>
'''

# =====================================================================
# KNOWLEDGE PROJECT (no new)
# =====================================================================
cards += card_none(
    "The Knowledge Project", "Shane Parrish", "最近無更新",
    "Ryan Serhant: How to Get People to Say Yes", "2026-10-08", "—（Members 先行；公開 10-08）",
    "https://fs.blog/knowledge-project-podcast/ryan-serhant/", "https://fs.blog/knowledge-project/",
    "daily-report-2026-10-09.html",
    "Ryan Serhant（SERHANT. 創辦人、Netflix《Owning Manhattan》主角）講「唔令人覺得被推銷」嘅銷售法：先建立連結、先幫人、賺到開口請求嘅資格。核心係信任與關係資本，而非話術。",
    note="ℹ️ KP 目前 RSS 只有 20 集（滾動 feed），週四更新；上一集 10-08，本週四（10-15）未見新集，下一集預料 10-22 前後。")

# =====================================================================
# DIARY OF A CEO (no new)
# =====================================================================
cards += card_none(
    "The Diary of a CEO", "Steven Bartlett", "最近無更新",
    "Most Replayed Moment: Christian vs Atheist - Is Faith A Human Creation?", "2026-10-16", "28 分 50 秒",
    "https://thediaryofaceo.com/", "https://thediaryofaceo.com/",
    "daily-report-2026-10-16.html",
    "DOAC 官方「Most Replayed Moment」精華剪輯：將 2025-09-29 嘅三小時宗教辯論，剪成 28:50 嘅核心交鋒。Greg Koukl（基督徒護教學者）× Alex O'Connor（無神論哲學家，Cosmic Skeptic）× Dr K / Alok Kanojia（哈佛出身精神科醫生）正面回答同一條問題：信仰／宗教究竟係「人類為應對死亡恐懼而發明嘅工具」，抑或指向一個客觀存在嘅超越真相？",
    note="ℹ️ 呢集係精華回顧，唔係全新錄音；原始全長辯論（3 小時 21 分）於 2025-09-29 播出，已於昨日日報完整拆解。")

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
    🔢 RSS 集數（最新的在前）：Acquired 217 · Founders 462 · All-In 437 · MFM 911 · KP 20 · DOAC 898<br>
    🧮 Jev 前置過濾（TypeSafe System One, <code>news</code> profile）：2 條新集候選 → All-In <code>worth 0.91</code>（保留）、MFM <code>worth 0.33</code>（按任務要求保留：屬核心節目，且為話術／框架型內容，Jev 嘅「無可核實數字」評分唔適用於判斷節目價值）<br>
    🧑‍💻 Repo：<a href="https://github.com/JMOKSZ/mindset-podcasts">JMOKSZ/mindset-podcasts</a> · 累計已掃 GUID：{total_guid}
  </div>
</header>

<div class="summary">
  <b>今日重點：2 台有新集，而且巧合地圍繞同一個主題——「錢嘅價格」。All-In 講 AI 基建嘅債務成本（CoreWeave 債息 15%），MFM 講一個人嘅「賺錢體質」（六個特質 + 二階導數消費法）。一邊係宏观信用，一邊係 micro 習慣，拼埋一齊就係今日最完整嘅「金錢觀」。</b>
  <ul>
    <li>🆕 <b>All-In · CoreWeave Crash, AI Trade Cracks, Anthropic IPO Red Flags, Bill Gates Doomer</b>（1:34:06）：Ben Horowitz 代 Friedberg。由 CoreWeave 債券風暴講到 AI 軟件通縮、Anthropic $168 億季度收入嘅「紅旗」、自我複製 AI 嘅「Psyop」味，最後分析 Bill Gates 點解變成 doomer。</li>
    <li>🆕 <b>MFM #872 · the 6 traits of people who can’t stop making money</b>（39:18）：Sam &amp; Shaan 定義「Natural Moneymaker」，用 Nick Kokonas、Jay Gould、Syed Balkhi 三個故事拆六個特質；結尾兩條規則——只花二階導數、唔好用有價值時間換無用金錢——係今日最值得即刻抄低嘅嘢。</li>
    <li>📭 其餘 4 台（Acquired / Founders / Knowledge Project / DOAC）本輪無新集；DOAC 上集「Christian vs Atheist」精華已於昨日日報完整拆解。</li>
    <li>🧠 <b>今日 cross-episode insight：</b>All-In 講「信用市場唔會講故事」，MFM 講「真正有錢人唔會同錢講感情」——兩集其實係同一條道理嘅兩個尺度：<b>市場同個人都係喺「唔需要再證明啲咩」嘅時候，先會露出真實嘅風險偏好。</b></li>
  </ul>
  <div class="stats">
    <div class="stat"><span class="n">2</span><span class="l">今日新集</span></div>
    <div class="stat"><span class="n">6</span><span class="l">追蹤播客</span></div>
    <div class="stat"><span class="n">2h14m</span><span class="l">新集總長度</span></div>
    <div class="stat"><span class="n">{total_guid}</span><span class="l">累計已掃 GUID</span></div>
  </div>
</div>

{cards}

<footer class="bot">
  <p><b>關於呢份報告：</b>每日比對 6 條 RSS feed 嘅 episode GUID，只對「未掃過嘅新集」做深度萃取。今日兩集均為全新錄音（非重播／精華），內容基於官方 show notes、RSS 描述、公開逐字稿（MFM，podscripts.co）及當日新聞報道（CNBC、Bloomberg、Forbes、Guardian、247WallSt、Asymmetric Bets）交叉整理；所有引用以原文 blockquote 呈現，推測性內容已明確標示為「分析／框架」而非節目原話。</p>
  <p>Feed 集數：{feed_counts}（依 podcasts.json 目前 RSS 設定，{now_utc} 抓取）。生成於 {now_utc}。</p>
</footer>

</div>
</body>
</html>'''

out = os.path.join(BASE, f'daily-report-{DATE}.html')
open(out, 'w', encoding='utf-8').write(html)
print('wrote', out, len(html), 'bytes')
