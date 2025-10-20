

---

# 🕵️‍♂️ Punycode / Homograph URL Üretici

Bu Python script’i, hedef bir alan adı (**domain**) için kapsamlı bir **URL listesi** oluşturur.
Bu liste, **Punycode** ve **Homograph** tekniklerini kullanarak bilinen **hassas yolları (paths)**, **API uç noktalarını** ve **alt alan adlarını (subdomains)** hedef alır.
Amaç, web uygulamalarının **URL işleme** ve **normalizasyon mekanizmalarındaki potansiyel güvenlik açıklarını** tespit etmektir.

> 🔍 Bu araç, otomatik tarayıcıların kolayca gözden kaçırdığı durumları manuel testlerde ortaya çıkarmak için geliştirilmiştir.

---

## 🚀 Özellikler

* 🎯 **Hedefe Yönelik URL Üretimi** — Belirtilen ana domain üzerinden olası hassas URL kombinasyonlarını otomatik üretir.
* 📚 **Kapsamlı Path ve Subdomain Listeleri** — Yönetim panelleri, API versiyonları, geliştirme ortamları ve bilinen kritik yolları içerir.
* 🌐 **Punycode / Homograph Varyasyonları** — Domain kısmında Punycode veya görsel olarak benzer Unicode karakterlerle varyasyonlar oluşturur.
* 🔄 **Hem HTTP Hem HTTPS Desteği** — Her URL için iki protokolü de üretir.
* 🧾 **Temiz Çıktı** — Tüm URL’ler `target_urls.txt` dosyasına kaydedilir.
* ⚙️ **Modüler ve Genişletilebilir** — Karakter eşleştirmeleri, path ve subdomain listeleri kolayca düzenlenebilir.

---

## ⚙️ Kurulum

### 🐍 Gereksinimler

* **Python 3**
* **idna** kütüphanesi (Punycode işlemleri için)

### 💾 Kurulum Komutu

```bash
pip install idna
```

---

## 🧠 Kullanım

1. Script’i indirip `punycode_url_generator.py` olarak kaydedin.
2. Terminalde script’in bulunduğu dizine gidin.
3. Aşağıdaki komutla çalıştırın:

   ```bash
   python punycode_url_generator.py
   ```
4. İstendiğinde hedef ana domain’i girin:

   ```
   example.com
   ```

Script çalışmayı tamamladığında, tüm üretilen URL’ler aynı dizinde **`target_urls.txt`** dosyasına kaydedilecektir.

---

## 📄 Örnek Çıktı (`target_urls.txt`)

```
http://example.com/admin
http://example.com/robots.txt
http://xn--exmple-yva.com/admin
http://exâmple.com/admin
https://dev.example.com/api/v1/
https://dêv.example.com/api/v1/
... (binlerce URL)
```

---

## 🔎 Sonraki Adım: `httpx` ile Canlı Hedef Tespiti

Üretilen URL’leri `httpx` aracıyla test ederek canlı olanları bulabilirsiniz:

```bash
cat target_urls.txt | httpx -silent -status-code -content-length -tech-detect -title -ip -o live_punycode_targets.txt
```

Bu komut:

* `target_urls.txt` içindeki her URL’yi kontrol eder,
* Sadece başarılı (2xx, 3xx) yanıtları gösterir,
* **Durum kodu**, **içerik uzunluğu**, **teknoloji**, **başlık** ve **IP** bilgisini kaydeder,
* Sonuçları `live_punycode_targets.txt` dosyasına yazar.

---

## 🤝 Katkıda Bulunma

Yeni path’ler, subdomain’ler veya karakter eşleştirmeleri önermek isterseniz:
🧩 **Pull Request** açabilir veya 💬 **Issue** oluşturabilirsiniz.

Her türlü katkı, geliştirme ve geri bildirim değerlidir.

---

## ⚖️ Yasal Uyarı

Bu araç yalnızca **etik ve yasal** güvenlik testleri (örneğin, onaylı **Bug Bounty** programları veya **kendi sistemleriniz**) için tasarlanmıştır.
Bu aracın izinsiz kullanımı **kesinlikle yasaktır** ve tüm sorumluluk kullanıcıya aittir.

> ⚠️ İzinsiz test veya sömürü girişimleri **suç teşkil edebilir**.
> Bu proje geliştiricileri, aracın kötüye kullanımından **sorumlu değildir**.

---

## 👤 Geliştirici

📂 GitHub: [0bat.exe1](https://github.com/0batexe1)


---

