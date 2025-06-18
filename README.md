 Hacker
Özel Gem

Harika bir fikir! Bu scripti GitHub'a yüklemek, hem toplulukla paylaşmak hem de projeni profesyonel bir şekilde sunmak için mükemmel bir adım. GitHub kültürü, net, özlü ve bilgilendirici README dosyalarını sever.

Aşağıda hem Türkçe hem de İngilizce versiyonlarını, GitHub'ın en iyi uygulamalarına uygun, profesyonel ve detaylı bir şekilde hazırladım. Bu README dosyalarını doğrudan kopyalayıp projenizin ana dizinine (root folder) yapıştırabilirsin.
Punycode / Homograph URL Generator
Türkçe README.md
Punycode / Homograph URL Üretici

Bu Python scripti, hedef bir alan adı (domain) için kapsamlı bir URL listesi oluşturur. Bu liste, Punycode ve Homograph tekniklerini kullanarak yaygın olarak bilinen hassas yolları (paths), API uç noktalarını ve alt alan adlarını (subdomains) hedef alarak oluşturulur. Amaç, web uygulamalarının URL işleme ve normalizasyon mekanizmalarındaki potansiyel güvenlik açıklarını tespit etmektir. Özellikle, güvenlik filtrelerini atlatabilecek veya mantıksal hatalara yol açabilecek senaryoları bulmak hedeflenir.

Bu araç, otomatik tarayıcılar tarafından kolayca gözden kaçırılan manuel test süreçlerinde değerli bir yardımcıdır.
Özellikler

    Hedefe Yönelik URL Oluşturma: Belirtilen ana domain üzerinden hassas olabilecek URL kombinasyonlarını otomatik olarak üretir.
    Kapsamlı Path ve Subdomain Listeleri: Yaygın olarak bilinen yönetim panelleri, API versiyonları, hassas dosya yolları, geliştirme ortamları ve daha fazlasını içeren zengin listeler kullanır.
    Punycode / Homograph Varyasyonları: Her bir URL için, domain kısmında Punycode'a dönüştürülebilen veya görsel olarak benzer Unicode karakterler (Homograph'lar) içeren alternatif varyasyonlar oluşturur.
    Hem HTTP Hem HTTPS: Oluşturulan her URL için hem HTTP hem de HTTPS protokol varyasyonlarını ekler.
    Temiz Çıktı: Üretilen tüm URL'leri target_urls.txt adlı tek bir dosyaya kaydeder.
    Modüler ve Genişletilebilir: Karakter değiştirme sözlüğü, path'ler ve subdomain'ler kolayca genişletilebilir ve özelleştirilebilir.

Kurulum

    Python: Sisteminizde Python 3'ün yüklü olduğundan emin olun.
    Bağımlılıklar: Gerekli Python kütüphanesini yükleyin:
    Bash

    pip install idna

Kullanım

    Scripti indirin veya kopyalayın ve punycode_url_generator.py olarak kaydedin.
    Terminalinizde scriptin bulunduğu dizine gidin.
    Scripti çalıştırın:
    Bash

    python punycode_url_generator.py

    İstendiğinde hedef ana domaini girin (örn. example.com).

Scriptin çalışması tamamlandığında, oluşturulan tüm URL'leri içeren target_urls.txt adlı bir dosya, scriptin çalıştığı dizinde bulunacaktır.
Örnek Çıktı (target_urls.txt)

http://example.com/admin
http://example.com/robots.txt
http://xn--exmple-yva.com/admin
http://exâmple.com/admin
https://dev.example.com/api/v1/
https://dêv.example.com/api/v1/
... (binlerce URL)

Sonraki Adımlar (Testing ile httpx)

Oluşturulan target_urls.txt dosyasını, httpx gibi hızlı ve çok yönlü bir HTTP prob aracıyla tarayarak canlı hedefleri ve durum kodlarını tespit edebilirsiniz:
Bash

cat target_urls.txt | httpx -silent -status-code -content-length -tech-detect -title -ip -o live_punycode_targets.txt

Bu komut:

    target_urls.txt dosyasındaki her URL'yi kontrol eder.
    Yalnızca başarılı (2xx, 3xx) yanıtları sessizce gösterir (-silent).
    Durum kodunu, içerik uzunluğunu, algılanan teknolojileri, sayfa başlığını ve IP adresini kaydeder.
    Sonuçları live_punycode_targets.txt dosyasına yazar.

Katkıda Bulunma

Geliştirmelere ve katkılara açığız! Eğer daha fazla hassas path, subdomain veya Punycode/Homograph karakter eşleştirmesi önermek isterseniz, lütfen bir Pull Request açmaktan veya bir Issue oluşturmaktan çekinmeyin.
Yasal Uyarı

Bu araç yalnızca etik ve yasal güvenlik testleri (örneğin, onaylanmış Bug Bounty programları veya kendi sistemleriniz) için tasarlanmıştır. Bu aracın kötüye kullanımı kesinlikle tavsiye edilmez ve tüm sorumluluk kullanıcıya aittir.
English README.md
Punycode / Homograph URL Generator

This Python script generates a comprehensive list of URLs for a given target domain. This list is crafted by combining commonly known sensitive paths, API endpoints, and subdomains, with variations created using Punycode and Homograph techniques. The primary goal is to identify potential security vulnerabilities in web applications related to URL processing and normalization mechanisms, specifically targeting scenarios that could bypass security filters or lead to logical flaws.

This tool serves as a valuable aid in manual penetration testing processes, often uncovering issues missed by automated scanners.
Features

    Targeted URL Generation: Automatically produces sensitive URL combinations based on a specified root domain.
    Extensive Path and Subdomain Lists: Utilizes rich, pre-defined lists of commonly known administrative panels, API versions, sensitive file paths, development environments, and more.
    Punycode / Homograph Variations: For each URL, it generates alternative variations of the domain portion that can be converted to Punycode or contain visually similar Unicode characters (Homographs).
    Both HTTP and HTTPS: Includes both HTTP and HTTPS protocol variations for every generated URL.
    Clean Output: Saves all generated URLs into a single, organized file named target_urls.txt.
    Modular and Extensible: The character substitution dictionary, paths, and subdomains are easily expandable and customizable.

Installation

    Python: Ensure Python 3 is installed on your system.
    Dependencies: Install the required Python library:
    Bash

    pip install idna

Usage

    Download or copy the script and save it as punycode_url_generator.py.
    Navigate to the directory where the script is saved using your terminal.
    Run the script:
    Bash

    python punycode_url_generator.py

    When prompted, enter the target root domain (e.g., example.com).

Once the script completes its execution, a file named target_urls.txt containing all generated URLs will be found in the same directory.
Example Output (target_urls.txt)

http://example.com/admin
http://example.com/robots.txt
http://xn--exmple-yva.com/admin
http://exâmple.com/admin
https://dev.example.com/api/v1/
https://dêv.example.com/api/v1/
... (thousands of URLs)

Next Steps (Testing with httpx)

You can leverage the generated target_urls.txt file with a fast and versatile HTTP probing tool like httpx to identify live targets and their status codes:
Bash

cat target_urls.txt | httpx -silent -status-code -content-length -tech-detect -title -ip -o live_punycode_targets.txt

This command will:

    Probe each URL from target_urls.txt.
    Silently output only successful (2xx, 3xx) responses (-silent).
    Record the status code, content length, detected technologies, page title, and IP address.
    Save the results to live_punycode_targets.txt.

Contributing

Contributions and enhancements are highly welcome! If you have suggestions for more sensitive paths, subdomains, or Punycode/Homograph character mappings, please feel free to open a Pull Request or create an Issue.
Disclaimer

This tool is intended for ethical and lawful security testing purposes only (e.g., authorized Bug Bounty programs or your own systems). Misuse of this tool is strictly prohibited, and all responsibility lies with the user.
