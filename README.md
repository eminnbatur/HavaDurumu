🌤 Türkiye Hava Durumu Uygulaması - Tkinter GUI
Bu proje, Python ve Tkinter kullanılarak geliştirilmiş basit ve kullanışlı bir masaüstü hava durumu uygulamasıdır. Türkiye’deki 81 ilin isimlerini içeren autocomplete (otomatik tamamlama) özelliği sayesinde kullanıcı, istediği ilin güncel hava durumunu kolayca sorgulayabilir.

Özellikler
Türkiye’deki 81 ilin tamamı için şehir seçimi ve autocomplete desteği

OpenWeatherMap API üzerinden güncel hava durumu bilgisi çekme

Sıcaklık, nem, hava açıklaması ve hava durumu ikonlarının görsel olarak gösterilmesi

Kullanıcı dostu arayüz (Tkinter GUI)

Hava durumu verilerinin lokal olarak kaydedilmesi (storage modülü ile)

Hatalı veya boş girişlerde kullanıcıyı uyaran mesaj kutuları

Kullanılan Teknolojiler
Python 3.x

Tkinter (GUI için)

Pillow (PIL) - ikon görselleri için

requests - API istekleri için

OpenWeatherMap API

Kurulum ve Çalıştırma
Depoyu klonlayın veya indirin:

bash
Kopyala
Düzenle
git clone <repo-link>
Gerekli Python paketlerini yükleyin:

bash
Kopyala
Düzenle
pip install -r requirements.txt
(requirements.txt dosyasına requests ve Pillow eklenmeli)

OpenWeatherMap API anahtarınızı weather.py dosyasına ekleyin.

Uygulamayı başlatın:

bash
Kopyala
Düzenle
python main.py
Dosya Yapısı
main.py — Tkinter arayüzü ve uygulamanın ana kodu

weather.py — Hava durumu API’sine bağlanan fonksiyonlar

storage.py — Hava durumu verilerini kaydetme fonksiyonları

requirements.txt — Projede kullanılan Python paketleri


