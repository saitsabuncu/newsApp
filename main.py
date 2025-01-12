from dotenv import load_dotenv
import os
import requests

# .env dosyasını yükle
load_dotenv(dotenv_path="C:/Users/casper/exampleProject/newsAPI/news_api.env")

# API anahtarını al
api_key = os.getenv("NEWS_API_KEY")

if not api_key:
    raise ValueError("API anahtarı bulunamadı! Lütfen .env dosyasını kontrol edin.")

# Haber API'sini çağırmak için URL
url_everything = "https://newsapi.org/v2/everything"

# Kullanıcıdan sorgu parametrelerini alın
query = input("Aramak istediğiniz haber konusu: ")
language = input("Hangi dilde arama yapmak istiyorsunuz? (örneğin: tr, en): ")
sort_by = input("Haberleri nasıl sıralamak istersiniz? (örneğin: relevance, popularity, publishedAt): ")

# API'ye GET isteği gönder
response = requests.get(url_everything, params={
    "apiKey": api_key,
    "q": query,
    "language": language,
    "sortBy": sort_by
})

# Haberleri işleyin ve ekrana yazdırın
if response.status_code == 200:
    haberler = response.json()["articles"]
    for i, haber in enumerate(haberler[:10], start=1):  # İlk 10 haberi göster
        print(f"{i}. Haber")
        print(f"Kaynak: {haber['source']['name']}")
        print(f"Başlık: {haber['title']}")
        print(f"URL: {haber['url']}\n")
else:
    print(f"Bir hata oluştu. Hata kodu: {response.status_code}")
