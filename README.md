# NewsAPI Haber Uygulaması

Bu proje, **NewsAPI** kullanarak belirli konular hakkında haberleri sorgulamak, listelemek ve kullanıcıya sunmak için geliştirilmiştir. Ayrıca, **.env** dosyası ve **GitHub Secrets** kullanılarak API anahtarlarının güvenliğini sağlamaktadır.

---

## 🚀 Özellikler

- **Haber Arama**: Kullanıcıdan alınan sorgu parametrelerine göre haber arama.
- **Dil Seçeneği**: Haberleri belirli bir dilde sorgulama (örneğin: Türkçe, İngilizce).
- **Sıralama Seçeneği**: Haberleri `publishedAt`, `popularity` veya `relevance` gibi ölçütlere göre sıralama.
- **Güvenli API Anahtarı Kullanımı**:
  - API anahtarlarını `.env` dosyasında veya **GitHub Secrets** ile saklama.

---

## 📂 Proje Yapısı

```plaintext
project/
├── main.py               # Ana Python dosyası
├── news_api.env          # API anahtarını içeren .env dosyası
├── README.md             # Proje açıklamaları
```

---

## 🔧 Kurulum

### 1. Gerekli Kütüphaneleri Yükleyin
Proje için aşağıdaki kütüphanelerin kurulu olması gerekir:
```bash
pip install python-dotenv requests
```

### 2. `.env` Dosyasını Ayarlayın
Proje dizininde bir `.env` dosyası oluşturun ve API anahtarınızı buraya ekleyin:
```
NEWS_API_KEY=your_api_key_here
```

> **Not:** Eğer GitHub Secrets kullanıyorsanız `.env` dosyasına gerek kalmaz. Ancak `load_dotenv` ile çevresel değişkenleri yüklediğinizden emin olun.

### 3. Projeyi Çalıştırın
Proje dizininde aşağıdaki komutla uygulamayı başlatabilirsiniz:
```bash
python main.py
```

---

## 🔑 GitHub Secrets Kullanımı

GitHub Actions ile API anahtarını güvenli bir şekilde saklamak için şu adımları izleyin:

1. **Secrets Ekleme**:
   - GitHub reposunda `Settings > Secrets and variables > Actions > New repository secret` seçeneğine gidin.
   - Yeni bir secret ekleyin:
     - Name: `NEWS_API_KEY`
     - Value: `your_api_key_here`

2. **GitHub Actions Dosyası Örneği**:
   ```yaml
   name: NewsAPI Workflow
   on:
     push:
       branches:
         - main

   jobs:
     run-newsapi:
       runs-on: ubuntu-latest
       steps:
         - name: Check out the code
           uses: actions/checkout@v3
         - name: Run Python Script
           env:
             NEWS_API_KEY: ${{ secrets.NEWS_API_KEY }}
           run: python main.py
   ```

---

## 📝 Kullanım

### Programı Çalıştırma
1. Program başladığında sizden şu bilgileri isteyecektir:
   - **Haber Konusu**: Örneğin, "futbol", "teknoloji".
   - **Dil**: Haberlerin dili. Örneğin, "tr" (Türkçe) veya "en" (İngilizce).
   - **Sıralama Kriteri**: `relevance`, `popularity`, veya `publishedAt`.

2. **Örnek Girdi**:
   ```
   Aramak istediğiniz haber konusu: teknoloji
   Hangi dilde arama yapmak istiyorsunuz? (örneğin: tr, en): tr
   Haberleri nasıl sıralamak istersiniz? (örneğin: relevance, popularity, publishedAt): publishedAt
   ```

3. **Örnek Çıktı**:
   ```
   1. Haber
   Kaynak: TechCrunch
   Başlık: Yeni yapay zeka modelleri piyasaya sürüldü
   URL: https://techcrunch.com/ai-news
   ```

---

## 🌟 Geliştirme Önerileri

- **Haberleri JSON veya CSV Dosyasına Kaydetme**: Çekilen haberleri bir dosyaya saklayarak daha sonra kullanılabilir hale getirin.
- **Hata Yönetimi**: Kullanıcıya API yanıtına bağlı olarak daha anlamlı hata mesajları sunun.
- **Görselleştirme**: Haberleri masaüstü veya web arayüzü ile sunun (örneğin, Tkinter veya Flask kullanarak).

---

## 📌 Notlar

- API anahtarınızı GitHub'a yüklememeye dikkat edin.
- `.env` dosyanızı `.gitignore` ile koruyun:
  ```
  .env
  ```

---

## 🛠️ Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

---

## ✨ İletişim

Herhangi bir soru veya öneriniz için lütfen [email@example.com](mailto:email@example.com) adresinden iletişime geçin.
```
