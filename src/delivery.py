import os
import requests
from dotenv import load_dotenv

# Load config dari .env
load_dotenv()

# PERBAIKAN DI SINI: Panggil NAMA variabelnya, bukan isinya
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_report(report_text):
    print("\n--- DEBUG INFO ---")
    # Kita cek apakah Python berhasil membaca .env
    print(f"Token Status: {'✅ Oke' if BOT_TOKEN else '❌ KOSONG (Cek .env)'}")
    print(f"Chat ID Status: {'✅ Oke' if CHAT_ID else '❌ KOSONG (Cek .env)'}")

    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Error: Gagal baca .env. Pastikan nama variabelnya TELEGRAM_BOT_TOKEN dan TELEGRAM_CHAT_ID")
        return

    # URL API Telegram (Pakai f-string biar otomatis baca token dari variabel)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": report_text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }

    try:
        print("📨 Mengirim laporan ke Telegram...")
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            print("✅ Laporan SUKSES terkirim ke Telegram!")
        else:
            print(f"❌ Gagal kirim Telegram: {response.text}")
            
    except Exception as e:
        print(f"❌ Error Connection: {e}")