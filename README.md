# NewsApp

NewsAPI kullanılarak geliştirilmiş bir Python uygulamasıdır. Kullanıcıların belirli konular hakkında güncel haberleri aramasına, filtrelemesine ve listelemesine olanak sağlar.

## Project Overview

Bu proje, Python öğrenme sürecimde REST API kullanımı, JSON verilerinin işlenmesi ve çevresel değişkenlerle güvenli yapılandırma konularını uygulamalı olarak öğrenmek amacıyla geliştirilmiştir.

Kullanıcı tarafından girilen konu, dil ve sıralama kriterlerine göre NewsAPI üzerinden haberler çekilir ve terminal ekranında listelenir.

## Features

* Haber arama
* Dil seçimi (Türkçe, İngilizce vb.)
* Sıralama seçenekleri

  * relevance
  * popularity
  * publishedAt
* JSON veri işleme
* Çevresel değişken (.env) desteği
* API tabanlı veri çekme

## Technologies Used

* Python 3
* Requests
* Python Dotenv
* NewsAPI

## Installation

Install dependencies:

```bash
pip install requests python-dotenv
```

Create a `.env` file:

```env
NEWS_API_KEY=your_api_key_here
```

Run the application:

```bash
python main.py
```

## Example Usage

```text
Search topic: technology
Language: en
Sort by: publishedAt
```

Example output:

```text
Source: TechCrunch
Title: New AI models released
URL: https://example.com/news
```

## What I Learned

Through this project I practiced:

* Working with REST APIs
* Processing JSON responses
* Using environment variables
* Error handling
* User input validation
* Data filtering and presentation

## Future Improvements

* Graphical user interface (Tkinter)
* Export results to JSON or CSV
* Save search history
* Category filtering
* News dashboard

## Developer

Mustafa Sait Sabuncu

## License

MIT License
