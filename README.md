# 🤖 AI Auto Research Assistant

**AI Auto Research Assistant** adalah bot pintar yang bekerja secara otonom untuk melakukan riset berita teknologi harian, menganalisis dampaknya menggunakan AI (LLaMA 3), dan mengirimkan laporan ringkas langsung ke Telegram.

Proyek ini dibuat untuk mengotomatisasi proses *tech monitoring* tanpa campur tangan manusia.

---

## ✨ Fitur Utama

* 🕵️ **Auto Scraping:** Mencari berita terbaru dari Google News (via SerpAPI).
* 🧠 **AI Analysis:** Membaca, merangkum, dan menganalisis dampak berita menggunakan Groq (LLaMA 3.3).
* 📩 **Smart Delivery:** Mengirim laporan dalam format HTML rapi ke Telegram.
* ⏰ **Scheduler:** Berjalan otomatis setiap pagi (07:00) menggunakan scheduler.

---

## 🛠️ Teknologi yang Digunakan

* **Python 3.10+**
* **Groq API** (LLM Engine)
* **SerpAPI** (Google Search Engine)
* **Telegram Bot API**
* **Git & GitHub** (Version Control)

---

## 🚀 Cara Menjalankan (Local)

1.  **Clone Repository**
    ```bash
    git clone [https://github.com/Lufasu-Adm/ai-research-assistant.git](https://github.com/Lufasu-Adm/ai-research-assistant.git)
    cd ai-research-assistant
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Environment Variables**
    Buat file `.env` dan isi dengan API Key Anda:
    ```env
    GROQ_API_KEY=gsk_...
    SERPAPI_KEY=...
    TELEGRAM_BOT_TOKEN=...
    TELEGRAM_CHAT_ID=...
    ```

4.  **Jalankan Program**
    * Manual: `python main.py`
    * Otomatis: `python scheduler.py`

---
## 🖼️ Screenshot 

| Home Screen |
|:---:|
| <img src="https://github.com/Lufasu-Adm/ai-research-assistant/blob/main/assets/WhatsApp%20Image%202025-12-11%20at%2011.51.12_784c2af3.jpg" width="200" alt="Home"> | 

---

## 👤 Author

**Jordan Wijayanto**
