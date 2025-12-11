import schedule
import time
from main import main  

def tugas_harian():
    print("\n⏰ ALARM TRIGGERED: Waktunya mencari berita harian!")
    main()  

# --- KONFIGURASI JADWAL ---
# Ganti jam di bawah ini sesuai keinginanmu (Format 24 Jam)
schedule.every().day.at("07:00").do(tugas_harian)
# --- KONFIGURASI TESTING (Opsional) ---
# Kalau mau tes sekarang (jalankan setiap 1 menit), buka komen (#) di bawah ini:
# schedule.every(1).minutes.do(tugas_harian)

print("⏳ Scheduler Aktif! Menunggu jadwal eksekusi...")
print("   (Biarkan jendela ini terbuka agar program terus berjalan)")
print("   (Tekan Ctrl + C di keyboard untuk berhenti)\n")

# Loop agar program tidak mati (Standby Mode)
while True:
    schedule.run_pending()
    time.sleep(1)