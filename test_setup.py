import os
from dotenv import load_dotenv
import requests

# 1. Load Environment
load_dotenv()
print("⚙️  Memeriksa konfigurasi...")

# 2. Cek API Keys
groq_key = os.getenv("GROQ_API_KEY")
serp_key = os.getenv("SERPAPI_KEY")
tele_token = os.getenv("TELEGRAM_BOT_TOKEN")
tele_id = os.getenv("TELEGRAM_CHAT_ID")

if groq_key and serp_key and tele_token:
    print("✅ Semua API Key terdeteksi di .env")
else:
    print("❌ Ada API Key yang kosong! Cek file .env kamu.")
    exit()

# 3. Test Kirim Pesan ke Telegram (Simpel)
print("\n📨 Mencoba kirim pesan tes ke Telegram...")
url = f"https://api.telegram.org/bot{tele_token}/sendMessage"
payload = {
    "chat_id": tele_id,
    "text": "Halo Ruphas! Setup Python berhasil. Bot siap bekerja! 🚀"
}

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Pesan terkirim! Cek Telegram kamu sekarang.")
    else:
        print(f"❌ Gagal kirim Telegram: {response.text}")
except Exception as e:
    print(f"❌ Error koneksi: {e}")

print("\n🎉 Setup Selesai! Siap lanjut coding core system.")