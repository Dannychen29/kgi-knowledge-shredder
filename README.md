好！三件事一起給你。

一、專案計畫書（最終完整版）

壹、背景與痛點分析
1.1 產業現況
金融控股公司的員工每日面對龐大的知識更新壓力：

法規面：金管會定期更新法規，合規部門必須確保全員理解最新要求
產品面：壽險、投資型保單、財富管理等產品持續推陳出新
客戶面：CRM 框架、跨售策略需要持續內化
系統面：內部數位工具不斷迭代，員工需要跟上

這些知識不是彼此獨立的孤島。一份「高資產客戶遺產規劃」文件，同時涉及壽險、財富管理、稅務法規、客戶關係四個領域。傳統的分科訓練方式，無法反映這種跨域交織的現實。
1.2 傳統培訓的三大失效模式
失效模式傳統做法根本問題認知超載兩小時研討會人腦的工作記憶容量有限，一次塞太多反而什麼都留不住知識孤立50 頁合規 PDF閱讀是被動吸收，沒有主動提取就不會形成長期記憶時機錯誤季度性 e-learning學習與實際工作情境脫節，無法在需要時即時調用知識
1.3 核心科學依據：遺忘曲線
心理學家艾賓浩斯（Hermann Ebbinghaus）的研究指出，人學習新知識後若沒有主動複習：
學習當天  → 記得 100%
第 1 天後 → 記得 58%
第 3 天後 → 記得 40%
第 5 天後 → 記得 20%
第 30 天後 → 記得 10%
公司每年投入數百萬在培訓，但知識留存率不到兩成，這是一個可以被系統性解決的問題。
1.4 業務影響

業務員走進客戶會議時，對產品細節模糊不清，影響成交率
合規知識不紮實，增加法規違規風險和罰款可能
新進人員上手時間長，增加 onboarding 成本
跨部門知識無法有效流通，形成組織記憶斷層


貳、解決方案設計
2.1 核心理念：流動式學習（Flow-State Learning）
不要跟員工的忙碌行程對抗，而是為忙碌行程設計學習。
目標： 把學習從「季度性義務」轉變為「日常數位習慣」
方法： 捕捉零碎時間

通勤的 15 分鐘（MRT、公車）
等待客戶的 10 分鐘（咖啡廳）
兩個會議之間的 5 分鐘空檔

2.2 完整學習閉環設計
本系統不是單純的內容切割工具，而是一個具備完整學習閉環的知識系統：
【內容輸入層】
訓練師上傳文件（PDF/DOCX/TXT）
          ↓
【知識分類層】
選擇 Domain Tags（多對多標籤）
          ↓
【AI 處理層】
Gemini 自動生成 2 分鐘模組
+ Key Takeaways + Quiz
          ↓
【品質控制層】← 這是金融業的關鍵！
訓練師審核（Human-in-the-Loop）
Draft → Approved
          ↓
【學習互動層】
員工閱讀模組 → 複習重點 → 作答測驗
          ↓
【回饋統計層】
即時對錯回饋 + 正確率追蹤
          ↓
【跨域瀏覽層】
Browse by Domain（跨文件知識探索）
2.3 Human-in-the-Loop 機制
為什麼金融業特別需要這個？
AI 大型語言模型存在「幻覺（Hallucination）」問題，可能生成看起來合理但實際上錯誤的內容。在一般娛樂或創意場景，幻覺的代價是「不夠準確」。但在金融業：

錯誤的法規描述 → 合規違規 → 監管罰款
錯誤的產品說明 → 不當銷售 → 客訴和法律責任
錯誤的稅務資訊 → 客戶損失 → 公司信譽受損

因此本系統設計了明確的審核流程：
AI 生成 → 狀態：Draft（草稿）
             ↓
      訓練師審核內容
      訓練師試答測驗
             ↓
      確認無誤後 Approve
             ↓
      狀態：Approved（已核准）
             ↓
      （未來）推送給員工

參、技術工具與選型理由
3.1 技術堆疊總覽
層級工具版本選擇理由程式語言Python3.12AI/ML 生態最完整，套件豐富Web 框架Flask3.1.1輕量直觀，適合功能明確的小型服務資料庫SQLite內建零環境設定，檔案型，Demo 最方便AI 引擎Gemini 2.5 Flash最新低延遲、低成本、中英文理解佳文件解析 PDFPyPDF23.0.1穩定的 PDF 文字提取文件解析 Wordpython-docx1.2.0完整的 DOCX 格式支援安全管理python-dotenv1.2.2環境變數管理，API Key 不暴露前端HTML+CSS+JS原生零框架依賴，部署門檻最低
3.2 為什麼選 Gemini 2.5 Flash？
不是因為「免費」，而是有明確的技術考量：
速度（Latency）： Flash 系列針對低延遲優化，使用者上傳文件後等待時間短，體驗流暢。
成本（Cost per Token）： 相比 GPT-4，Gemini Flash 的 token 成本更低，規模化後仍具經濟效益。
多語言能力（Multilingual）： 金融文件常見中英文混合，Gemini 對繁體中文的理解效果優於部分競品。
架構彈性（Model-Agnostic Design）： 我們將 AI 邏輯完全封裝在 gemini_service.py，未來只需修改這一個檔案，即可無縫替換成 OpenAI、Anthropic Claude 或任何其他模型，主應用程式邏輯完全不受影響。
3.3 為什麼選 SQLite？
現階段： 零安裝，整個資料庫是電腦裡的一個 .db 檔案，開發和 Demo 最方便。
未來升級： 只需修改 database.py 裡的連線字串，即可切換至 PostgreSQL 或 MySQL，四張表的結構和所有查詢語句完全不需要改變。這是良好的架構設計，不是技術債。

肆、程式碼架構詳解
4.1 設計原則：關注點分離（Separation of Concerns）
每個檔案只解決一個問題，就像一個專業的工作團隊：
database.py      → 解決「資料怎麼存」的問題
gemini_service.py → 解決「AI 怎麼呼叫」的問題
app.py           → 解決「請求怎麼處理」的問題
index.html       → 解決「畫面怎麼呈現」的問題
這樣的好處是：當你需要換 AI 模型，只改 gemini_service.py。當你需要換資料庫，只改 database.py。各個模組的修改不會互相影響。

4.2 database.py — 解決「資料怎麼存」
核心問題：如何表達「一份文件屬於多個領域」？
這是這個專案最重要的資料庫設計考點。
問題的本質：Many-to-Many（多對多）關係
文件 A ←→ Life Insurance
文件 A ←→ CRM
文件 A ←→ Compliance
文件 B ←→ CRM
文件 B ←→ Wealth Management
一份文件對應多個領域，一個領域也對應多份文件。如果只用兩張表，你沒有辦法在資料庫裡表達這件事。
解決方案：四張表 + 中間對應表（Junction Table）
KnowledgeDomains（領域字典）
├── domain_id（主鍵）
├── domain_name（Life Insurance / CRM / Compliance...）
└── description

SourceDocuments（原始文件）
├── doc_id（主鍵）
├── file_name
├── raw_text（原始內容）
└── upload_timestamp

Document_Domain_Map（中間對應表）← 解決 Many-to-Many 的關鍵
├── map_id（主鍵）
├── doc_id（外鍵 → SourceDocuments）
└── domain_id（外鍵 → KnowledgeDomains）

MicroModules（AI 生成的模組）
├── module_id（主鍵）
├── doc_id（外鍵 → SourceDocuments）
├── module_title
├── module_content
├── reading_time_minutes
└── status（draft / approved）← Human-in-the-Loop 的資料基礎
status 欄位的設計意義：
這個欄位是整個審核流程的資料基礎。沒有這個欄位，就沒有辦法在資料庫層面區分「AI 草稿」和「訓練師已核准」的內容。這一個欄位，支撐了整個 Human-in-the-Loop 機制的邏輯。

4.3 gemini_service.py — 解決「AI 怎麼呼叫」
核心問題：如何讓 AI 產生結構化、可用的內容？
這個檔案解決三個問題：
問題 1：API Key 安全性
pythonload_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
Key 從 .env 讀取，不寫死在程式碼裡。.env 加入 .gitignore，確保不上傳 GitHub。這是業界標準的安全做法，防止 Key 洩漏被盜用。
問題 2：如何讓 AI 產生有用的內容？（Prompt Engineering）
核心思路：把文件內容和選擇的知識領域一起注入 Prompt，並明確指定輸出格式。
你是金融公司的培訓內容產生器。
知識領域：[CRM, Life Insurance]

請把以下文字切成 2 分鐘學習模組。
每個模組必須包含：
- title（標題）
- content（2 分鐘學習內容）
- key_takeaways（3 個重點）
- quiz（一道選擇題，含正確答案）
- reading_time_minutes（閱讀時間）

回傳格式：純 JSON 陣列，不要任何多餘文字
這樣的 Prompt 設計確保三件事：

相關性：Domain 注入讓 AI 知道要強調哪些知識領域
結構性：強制指定 JSON 格式，確保輸出可以被程式處理
完整性：同時要求內容、重點、測驗，一次生成完整的學習單元

問題 3：AI 回傳格式不穩定怎麼辦？（Graceful Degradation）
pythontry:
    return json.loads(raw_response)
except json.JSONDecodeError:
    return [{"title": "Module 1", "content": raw_response, ...}]
AI 偶爾會在 JSON 前後多說廢話，導致解析失敗。這個 try/except 確保即使解析失敗，系統仍然回傳一個備用模組，不會讓使用者看到錯誤頁面。這叫做「優雅降級」。

4.4 app.py — 解決「請求怎麼處理」
核心問題：如何協調前端、AI、資料庫三者之間的溝通？
Flask 用 Route（路由）把不同網址對應到不同功能：
路由方法解決什麼問題/GET回傳主頁 HTML/api/domainsGET前端需要知道有哪些 Domain 可以選/api/uploadPOST核心流程：上傳→解析→AI→存檔→回傳/api/historyGET顯示所有上傳記錄/api/modules/<doc_id>GET從歷史記錄查看某份文件的模組/api/doc_domains/<doc_id>GET查詢某份文件當時選的 Domain/api/modules_by_domain/<domain_id>GET跨文件查詢同一 Domain 的所有模組/api/modules/<doc_id>/approve_index/<index>POST訓練師審核通過，更新 status
/api/upload 的完整流程（最重要）：
1. 驗證：有沒有上傳檔案？
2. 驗證：有沒有選 Domain？（至少一個）
3. 解析：根據副檔名選擇 PyPDF2 或 python-docx 讀取文字
4. 存檔：INSERT INTO SourceDocuments
5. 存檔：INSERT INTO Document_Domain_Map（每個 Domain 一筆）
6. AI：呼叫 generate_micro_modules()
7. 存檔：INSERT INTO MicroModules（每個模組 status='draft'）
8. 回傳：JSON 包含 doc_id、file_name、domains、raw_text、modules
每一步都有意義，缺一不可。步驟 5 建立的 Domain 對應關係，是之後「跨文件瀏覽」功能的資料基礎。步驟 7 存的 status='draft'，是 Human-in-the-Loop 機制的起點。

4.5 index.html — 解決「畫面怎麼呈現」
核心問題：如何讓訓練師直觀地完成整個工作流程？
前端由三層組成：
HTML（骨架）— 解決「有什麼」
定義了頁面的完整結構：

上傳區 + Domain 選擇區（步驟 1、2）
SHRED 按鈕 + 狀態提示（步驟 3）
學習統計顯示（即時回饋）
Split-Screen 預覽（原文 + AI 模組）
Browse by Domain（跨文件瀏覽）
Upload History（歷史記錄）

CSS（外觀）— 解決「看起來怎樣」
深色科技風格，用 CSS 變數統一管理配色：
css--accent: #00e5ff    /* 主色：青色，代表「可操作」*/
--accent2: #ff4d6d   /* 警示色：紅色，代表「需注意」*/
--accent3: #b8ff57   /* 成功色：綠色，代表「已完成」*/
Draft 狀態用紅色，Approved 狀態用綠色，直觀反映審核進度。
JavaScript（邏輯）— 解決「怎麼動起來」
每個函數解決一個具體問題：
loadDomains() — 解決「頁面載入時怎麼取得 Domain 清單」
呼叫 /api/domains，動態產生可點擊的 chip 按鈕，同時建立 Browse by Domain 的標籤列。
checkReady() — 解決「按鈕什麼時候可以按」
每次使用者選 Domain 或上傳檔案，就重新判斷兩個條件是否都滿足，並顯示對應的提示文字，讓使用者清楚知道還缺什麼。
renderPreview() — 解決「AI 回傳的 JSON 怎麼變成畫面」
把模組資料動態渲染成卡片，包含內容、Key Takeaways、可互動測驗，以及 Draft/Approve 控制項。
selectOption() — 解決「測驗作答和即時回饋」
使用者點選選項後，比對 AI 給的正確答案，即時用顏色區分對錯，更新正確率統計。
approveModule() — 解決「訓練師怎麼核准模組」
呼叫後端 API 更新資料庫 status，同時更新前端 UI 顯示 Approved 狀態，按鈕變為禁用防止重複點擊。
browseByDomain() — 解決「怎麼跨文件瀏覽同一領域的模組」
呼叫 /api/modules_by_domain/，展示來自不同文件但標記了相同 Domain 的所有模組，實現跨文件知識交叉學習。

伍、預期效益與成果
5.1 功能完成度
功能狀態說明PDF / DOCX / TXT 上傳✅三種格式全部支援多選 Domain 標籤系統✅至少一個，無上限AI 自動生成 2 分鐘模組✅Gemini 2.5 Flash每模組附 Key Takeaways✅3 個重點摘要互動式 Quiz 測驗✅可點選，即時對錯回饋學習正確率統計✅即時更新AI 風險警示✅提醒訓練師審核Human-in-the-Loop 審核✅Draft / Approved 狀態Split-Screen 預覽✅原文左側，模組右側跨文件 Domain 瀏覽✅Browse by Domain上傳歷史記錄✅含 Domain 標籤顯示Many-to-Many 資料庫✅Junction Table 設計API Key 安全管理✅.env 環境變數GitHub 版本控制✅含 Tag 標記
5.2 商業效益
對訓練師：

從手動製作 PPT 數小時 → 上傳文件幾分鐘自動生成
Domain 標籤讓知識庫自動分類，跨文件索引自動建立
Human-in-the-Loop 確保內容品質，降低合規風險

對員工：

2 分鐘模組配合零碎時間，降低認知負擔
Key Takeaways 快速複習重點，不需閱讀全文
測驗題即時鞏固記憶，主動提取對抗遺忘曲線
正確率統計讓學習進度可視化

對公司：

培訓成本降低，知識留存率顯著提升
合規風險降低（Human-in-the-Loop 防止錯誤內容流出）
跨域知識流通，消除組織記憶孤島
可規模化：新增文件即可擴充知識庫，不需額外開發

5.3 技術亮點
學習閉環（Learning Loop）：
內容生成 → 重點摘要 → 互動測驗 → 即時回饋 → 正確率統計，形成完整的學習反饋迴路，這是從「內容工具」升級為「學習系統」的關鍵差異。
Human-in-the-Loop：
AI 輔助生成，人工審核把關，平衡了效率和準確性，符合金融業對內容品質的高標準要求。
Model-Agnostic 架構：
AI 邏輯獨立封裝，未來替換模型只需修改一個檔案，具備高度的技術彈性。
Many-to-Many 知識圖譜雛形：
Domain 分類 + 跨文件瀏覽，實際上已經是一個小型的企業知識圖譜，為未來的個人化學習路徑打下基礎。

陸、未來展望
功能商業價值技術方向間隔重複推送對抗遺忘曲線，提升留存率根據測驗結果計算推送時機個人化學習路徑針對弱點強化，提升效率根據答錯模組推薦相關內容模組層級細粒度標籤更精準的知識分類AI 為每個模組分配獨立標籤學習進度儀表板管理層可視化員工知識狀況UserProgress 資料表 + 圖表雲端部署全公司可用，不限本地Docker + Cloud Run 或 Render

二、新版 README
打開 README.md 全選貼上：
markdown# KGI Knowledge Shredder

An AI-powered micro-learning platform that transforms training documents into interactive 2-minute learning sprints — built for KGI Financial Holdings.

---

## The Problem

Financial employees face an impossible volume of information: regulatory updates, product knowledge, compliance rules. Traditional training (2-hour seminars, 50-page PDFs) ignores the **Forgetting Curve** — people forget up to 80% of new information within 5 days without reinforcement.

## The Solution

A complete learning loop:
**Upload → Tag → AI Generate → Trainer Review → Learn → Quiz → Track**

Documents are broken into 2-minute micro-modules with key takeaways and quizzes, designed for the "in-between" moments of the day.

---

## Features

| Feature | Description |
|---------|-------------|
| Document Upload | PDF, DOCX, TXT support with drag-and-drop |
| Domain Tagging | Multi-select knowledge domain tags (Many-to-Many) |
| AI Generation | Gemini 2.5 Flash generates 2-min learning sprints |
| Key Takeaways | 3 highlighted key points per module |
| Interactive Quiz | AI-generated MCQ with instant correct/incorrect feedback |
| Learning Stats | Real-time accuracy tracking across all answered quizzes |
| AI Warning | Prompts trainer to review before approving |
| Human-in-the-Loop | Draft → Approved workflow for content quality control |
| Split-Screen Preview | Raw text left, generated modules right |
| Browse by Domain | Cross-document knowledge exploration by tag |
| Upload History | Access all previously processed documents |
| SQLite Database | Full Many-to-Many relational schema |

---

## Why Human-in-the-Loop?

AI can hallucinate — generating content that looks correct but isn't. In financial services, this means compliance risk. Every AI-generated module starts as **Draft** and must be explicitly **Approved** by a trainer before use. This ensures accuracy without sacrificing efficiency.

---

## Database Schema
KnowledgeDomains     SourceDocuments
(domain dictionary)  (uploaded files)
\               /
Document_Domain_Map
(junction table)
|
MicroModules
(AI-generated, status: draft/approved)

---

## Tech Stack

| Layer | Technology | Reason |
|-------|-----------|--------|
| Backend | Python 3.12 + Flask | Lightweight, AI ecosystem |
| Database | SQLite | Zero-config, upgradeable to PostgreSQL |
| AI | Google Gemini 2.5 Flash | Low latency, cost-effective, multilingual |
| Frontend | HTML + CSS + JavaScript | Zero framework dependency |
| File Parsing | PyPDF2, python-docx | PDF and Word support |
| Security | python-dotenv | API key isolation from codebase |

---

## How to Run

### 1. Clone
```bash
git clone https://github.com/Dannychen29/kgi-knowledge-shredder.git
cd kgi-knowledge-shredder
```

### 2. Install
```bash
pip install flask google-genai python-docx PyPDF2 python-dotenv
```

### 3. Configure API Key
```bash
cp .env.example .env
# Edit .env and add your Gemini API key
```
Get a free key: https://aistudio.google.com/apikey

### 4. Run
```bash
python app.py
```

### 5. Open
http://127.0.0.1:5000

---

## Workflow

1. **Upload** a PDF, DOCX, or TXT training document
2. **Select** one or more knowledge domain tags
3. **SHRED** — AI generates 2-minute modules with takeaways and quizzes
4. **Review** each module (AI warning displayed, status shows Draft)
5. **Approve** modules that pass trainer review (status → Approved)
6. **Learn** — read content, review key takeaways
7. **Quiz** — answer the multiple choice question, get instant feedback
8. **Track** — monitor accuracy across all quizzes in the session
9. **Browse** — explore modules across all documents by domain tag

---

## Future Roadmap

- **Spaced Repetition** — push review reminders before forgetting occurs
- **Personalized Learning** — recommend modules based on quiz weaknesses
- **Progress Dashboard** — visualize learning metrics per employee
- **Fine-grained Module Tags** — AI assigns per-module domain labels
- **Cloud Deployment** — production-ready for company-wide use

---

## Project Structure
kgi-knowledge-shredder/
├── app.py                 # Flask backend, all API routes
├── database.py            # SQLite schema and connection
├── gemini_service.py      # Gemini AI integration (model-agnostic)
├── templates/
│   └── index.html         # Full frontend UI
├── .env.example           # API key template
├── requirements.txt       # Python dependencies
└── README.md