import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

# Load API Key dari .env
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def get_tech_news(query="technology news artificial intelligence"):
    """
    Fungsi untuk mencari berita terbaru via Google News (SerpAPI).
    Output: List berisi judul, link, dan snippet berita.
    """
    print(f"🔍 Sedang mencari berita tentang: '{query}'...")

    params = {
        "engine": "google",
        "q": query,           # Kata kunci pencarian
        "tbm": "nws",         # Google News
        "api_key": SERPAPI_KEY,
        "gl": "id",           # Lokasi Google (id = Indonesia, us = USA)
        "hl": "id",           # Bahasa (id = Indonesia, en = Inggris)
        "num": 5              # Ambil 5 berita teratas saja
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        
        # Cek apakah ada hasil berita
        if "news_results" not in results:
            print("⚠️ Tidak ada berita ditemukan.")
            return []

        news_list = results["news_results"]
        cleaned_data = []

        # Kita rapikan datanya (hanya ambil yang penting)
        for item in news_list:
            data = {
                "title": item.get("title"),
                "link": item.get("link"),
                "date": item.get("date"),
                "source": item.get("source"),
                "snippet": item.get("snippet", "Tidak ada ringkasan.")
            }
            cleaned_data.append(data)
        
        print(f"✅ Berhasil mendapatkan {len(cleaned_data)} berita.")
        return cleaned_data

    except Exception as e:
        print(f"❌ Error saat scraping: {e}")
        return []

# --- Blok ini hanya jalan kalau file ini dijalankan langsung (bukan di-import) ---
if __name__ == "__main__":
    # Test function
    berita = get_tech_news("Nvidia RTX 5090 terbaru")
    
    print("\n--- HASIL TEST SCRAPER ---")
    for i, b in enumerate(berita, 1):
        print(f"{i}. {b['title']}")
        print(f"   🗓️ {b['date']} | 📰 {b['source']}")
        print(f"   🔗 {b['link']}")
        print("-" * 30)