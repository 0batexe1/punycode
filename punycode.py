import idna # Punycode işlemleri için
import os   # Dosya işlemleri için
import re   # Regex işlemleri için
from itertools import product # Kombinasyonlar için

def create_punycode_variations(input_string, char_substitutions):
    """
    Verilen metindeki hedef karakterleri Punycode'a uygun hale getirerek tüm olası varyasyonları oluşturur.
    Her varyasyon hem Punycode hem de Unicode hali olarak döner.
    """
    variations = set()
    
    # URL'den sadece domaini çekmeye çalış (http(s)://domain.com/path?query)
    domain_match = re.match(r'^(?:https?://)?([^/]+)', input_string)
    domain_part = domain_match.group(1) if domain_match else input_string.split('/')[0].split('?')[0] # En basit domain çıkarma
    
    path_part = ''
    if domain_match and len(input_string) > len(domain_match.group(0)):
        path_part = input_string[len(domain_match.group(0)):] # Path ve sonrası
    
    # Domain kısmını kelimelere ayır
    domain_labels = domain_part.split('.')

    # Her bir domain label'ı (örn. "example", "com") üzerinde çalış
    for label_index, label in enumerate(domain_labels):
        
        # Değişiklik yapılacak olası pozisyonlar ve onların alternatif karakterleri
        possible_changes_for_label = []
        for char_index, char_in_label in enumerate(label):
            if char_in_label in char_substitutions:
                possible_changes_for_label.append([(char_index, sub_char) for sub_char in char_substitutions[char_in_label]])
            else:
                possible_changes_for_label.append([(char_index, char_in_label)])

        # itertools.product kullanarak tüm olası kombinasyonları oluştur
        for combination in product(*possible_changes_for_label):
            new_label_chars = [''] * len(label)
            for char_pos, new_char in combination:
                new_label_chars[char_pos] = new_char
            
            modified_label = "".join(new_label_chars)

            if modified_label == label: # Değişiklik yoksa atla
                continue

            # Yeni domaini oluştur
            temp_labels = list(domain_labels)
            temp_labels[label_index] = modified_label
            modified_domain = ".".join(temp_labels)

            try:
                # 1. Punycode (IDN) dönüştürülmüş domain
                punycode_domain = idna.encode(modified_domain).decode('ascii')
                variations.add(punycode_domain + path_part)

                # 2. Unicode (direkt) domain
                variations.add(modified_domain + path_part)
                
            except idna.core.IDNAError:
                pass
            except UnicodeEncodeError:
                pass
                
    return sorted(list(variations))

def main():
    print("--- Hedefe Yönelik Punycode URL Test Listesi Oluşturucu ---")
    print("Bu script, verdiğiniz ana domain üzerinden kritik path'ler, subdomain'ler ve API endpoint'leri için")
    print("hem normal hem de Punycode/Homograph URL varyasyonları oluşturur.")
    print("---------------------------------------------------------\n")

    base_domain_input = input("Lütfen hedef ana domaini girin (örn: example.com): ").lower()
    
    # --- GENİŞLETİLMİŞ LİSTELER ---

    # Ortak ve hassas path'ler ve dosyalar
    common_paths = [
        "/",
        # Yönetim ve Kimlik Doğrulama
        "/admin", "/admin/", "/dashboard", "/dashboard/", "/login", "/login/", "/logout", "/logout/",
        "/account", "/account/", "/profile", "/profile/", "/user", "/user/", "/users/", "/settings", "/settings/",
        "/setup", "/install", "/wizard", "/config", "/configure", "/controlpanel", "/cpanel",
        "/admin.php", "/admin.aspx", "/admin.jsp", "/admin_login.php", "/login.php",
        "/_status", "/server-status", "/phpmyadmin/", "/phpPgAdmin/", # Sunucu bilgileri
        "/manager/html", "/host-manager/html", # Apache Tomcat
        "/jenkins/", "/jira/", "/confluence/", "/gitlab/", "/gitea/", # Geliştirici & CI/CD araçları
        "/bitbucket/", "/svn/", "/hg/", # Versiyon kontrol sistemleri
        "/wp-admin/", "/wp-login.php", "/xmlrpc.php", # WordPress
        "/drupal/", "/joomla/", "/magento/", # CMS
        
        # API Endpoints
        "/api", "/api/", "/api/v1/", "/api/v2/", "/api/v3/", "/api/auth/", "/api/user/", "/api/users/",
        "/rest", "/rest/", "/rest/v1/", "/graphql", "/graphql/", "/rpc", "/rpc/",
        "/oauth/token", "/oauth/authorize", "/auth/callback", "/auth/login", # OAuth/Auth
        
        # Bilgi Sızdıran Dosyalar ve Dizinler
        "/robots.txt", "/sitemap.xml", "/.git/config", "/.env", "/.env.local", "/.env.development",
        "/crossdomain.xml", "/clientaccesspolicy.xml", # Flash/Silverlight politikaları
        "/.well-known/security.txt", "/.well-known/assetlinks.json", "/.well-known/apple-app-site-association",
        "/config.json", "/config.yml", "/config.xml", "/web.config",
        "/backup.zip", "/backup.tar.gz", "/backup.sql", "/db.sql", "/dump.sql",
        "/phpinfo.php", "/test.php", "/info.php", "/debug.php", "/status.php",
        "/temp/", "/tmp/", "/uploads/", "/images/", "/files/", "/download/", # Dizin listelemeleri, dosya yüklemeleri
        "/vendor/", "/node_modules/", "/bower_components/", "/package.json", "/composer.json", # Bağımlılıklar
        "/logs/", "/error_log", "/access_log", # Log dosyaları
        
        # Varsayılan Sayfalar / Test Sayfaları
        "/index.php", "/index.aspx", "/default.asp", "/default.aspx", "/home.html", "/main.html",
        "/test/", "/dev/", "/dev_old/", "/old/", "/archive/", "/temp/", # Eski/Test dizinleri
        "/README.md", "/LICENSE.md", "/CHANGELOG.md", # Dokümantasyon
        "/health", "/healthz", "/metrics", # Sağlık kontrolü / Metrikler
        "/version", "/info", # Versiyon bilgisi
    ]

    # Yaygın subdomain'ler
    common_subdomains = [
        "www", "dev", "test", "staging", "qa", "uat", "beta", "demo", "sandbox", "poc",
        "api", "admin", "console", "dashboard", "portal", "panel", "management", "mgmt",
        "auth", "sso", "login", "secure", "app", "web", "shop", "store", "ecom",
        "blog", "docs", "wiki", "support", "help", "kb", "knowledge", "community",
        "mail", "smtp", "pop", "imap", "ftp", "cdn", "assets", "static", "images", "img",
        "internal", "int", "private", "vpn", "vps", "server", "proxy", "gw", "gateway", "ns",
        "db", "sql", "git", "repo", "code", "devops",
        "status", "monitor", "grafana", "kibana", "prometheus", "alert", # İzleme
        "jenkins", "jira", "confluence", "bitbucket", "gitlab", "redmine", # Geliştirici araçları
        "vault", "secret", "secrets", # Hassas bilgi depolama
        "autodiscover", "exchange", # Outlook Web Access/Exchange
        "mfa", "2fa", # Çok faktörlü kimlik doğrulama
        "download", "files", "share", # Dosya paylaşımı
        "proxy", "vpn", "remote", # Uzak erişim
    ]

    # Hedef karakterlerin farklı dillerdeki benzerleri (Homograph karakterler)
    char_substitutions = {
        'a': ['а', 'ä', 'á', 'å', 'à', 'â'],  # Kiril, Almanca, İspanyolca, İsveççe, Fransızca
        'o': ['о', 'ö', 'ó', 'ø', 'ò', 'ô'],  # Kiril, Almanca, İspanyolca, Danimarkaca, Fransızca
        'e': ['е', 'ë', 'é', 'è', 'ê'],  # Kiril, Almanca, Fransızca
        'i': ['і', 'í', 'ï', 'î'],      # Kiril, İspanyolca, Fransızca
        'c': ['с', 'ç'],          # Kiril, Fransızca/Türkçe
        'p': ['р'],          # Kiril
        's': ['ѕ', 'ş'],          # Kiril, Türkçe
        'u': ['ú', 'ü', 'û', 'ù'],      # İspanyolca, Almanca, Fransızca
        'n': ['ń', 'ñ'],          # Lehçe, İspanyolca
        'l': ['l', 'ı', 'ĺ'], # Küçük L, büyük I (Türkçe), Polonya L
        '0': ['0', 'O', 'О'], # Sıfır, büyük O (Latin), büyük O (Kiril)
        'r': ['г'],          # Kiril
        'x': ['х'],          # Kiril
        'v': ['ѵ'],          # Kiril
        'y': ['у'],          # Kiril
        # Harf ve rakam karışık benzerlikler (örn: 1 yerine l, 0 yerine O gibi) - WAF bypass'ında da kullanılır
        '1': ['1', 'l', 'i'],
        'z': ['ʐ'], # Kiril
        # ... isteğe göre daha fazla eklenebilir
    }

    all_urls = set()

    print("\nURL'ler oluşturuluyor...")

    # 1. Ana domain ve path kombinasyonları
    for path in common_paths:
        base_url = f"http://{base_domain_input}{path}"
        all_urls.add(base_url) # Normal URL
        
        # Punycode varyasyonları (domain kısmı için)
        punycode_vars = create_punycode_variations(base_domain_input, char_substitutions)
        for pv in punycode_vars:
            all_urls.add(f"http://{pv}{path}")

    # 2. Subdomain ve path kombinasyonları
    for sub in common_subdomains:
        full_subdomain = f"{sub}.{base_domain_input}"
        for path in common_paths:
            base_url = f"http://{full_subdomain}{path}"
            all_urls.add(base_url) # Normal URL

            # Punycode varyasyonları (subdomain + main domain için)
            punycode_vars = create_punycode_variations(full_subdomain, char_substitutions)
            for pv in punycode_vars:
                all_urls.add(f"http://{pv}{path}")
                
    # HTTP ve HTTPS varyasyonları ekle
    final_urls = set()
    for url in all_urls:
        final_urls.add(url.replace("http://", "https://"))
        final_urls.add(url) # HTTP'yi de koru

    output_filename = "target_urls.txt"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(f"--- Hedef Domain İçin URL Test Listesi ({base_domain_input}) ---\n")
        f.write(f"Oluşturulma Tarihi: {os.path.getctime(output_filename)}\n\n")
        
        if final_urls:
            sorted_urls = sorted(list(final_urls))
            for url in sorted_urls:
                f.write(url + "\n")
            print(f"\n{len(sorted_urls)} adet URL '{output_filename}' dosyasına kaydedildi.")
        else:
            f.write("Hiçbir URL oluşturulamadı. Lütfen geçerli bir domain girin veya karakter sözlüğünü genişletin.\n")
            print("\nHiçbir URL oluşturulamadı.")

if __name__ == "__main__":
    main()
