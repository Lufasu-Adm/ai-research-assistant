import sys
import time

# Kita import fungsi-fungsi yang sudah kita buat di folder src
from src.scraper import get_tech_news
from src.ai_engine import generate_summary
from src.delivery import send_telegram_report

def main():
    print("\n" + "="*50)
    print(" 🚀  AI AUTO RESEARCH ASSISTANT START  ")
    print("="*50 + "\n")

    # --- STEP 1: SCRAPING (MATA) ---
    # Kamu bisa ganti topik di sini.
    # Contoh: "Berita Crypto hari ini", "Update Framework Laravel", dll.
    keyword = "Teknologi AI terbaru dan Cyber Security 2025"
    
    print(f"📡 Memulai pencarian berita: '{keyword}'...")
    news_data = get_tech_news(keyword)

    if not news_data:
        print("⚠️ Tidak ada berita yang ditemukan. Program istirahat.")
        return

    # --- STEP 2: AI PROCESSING (OTAK) ---
    print("\n🧠 Mengirim data ke AI untuk analisis...")
    report_content = generate_summary(news_data)

    if not report_content:
        print("⚠️ Gagal membuat rangkuman AI.")
        return

    # --- STEP 3: DELIVERY (MULUT) ---
    print("\n📨 Menyiapkan pengiriman ke Telegram...")
    send_telegram_report(report_content)

    print("\n" + "="*50)
    print(" ✅  MISSION COMPLETE: Laporan Selesai & Terkirim!  ")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()