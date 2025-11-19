# NELER YAPACAĞIZ ?
Projede Neler Yapıyoruz?

Web servisi (nginx)
demo-web container’ı ile basit bir HTML sayfasını sunuyoruz.
Tarayıcıdan http://localhost:8080 adresine giderek çalışan sayfayı görebiliyoruz.
Web servisi, frontend network’ü üzerinden diğer servislerle iletişim kurabiliyor.

Database servisi (MySQL 8)
demo-db container’ı ile MySQL veritabanı çalıştırıyoruz.
MYSQL_ROOT_PASSWORD ve MYSQL_DATABASE ortam değişkenleri ile başlangıç ayarlarını yapıyoruz.
Veritabanı verileri, dbdata volume’ü sayesinde container silinse bile korunuyor.
Database, hem backend hem de frontend network’üne dahil edilerek, gerektiğinde web servisiyle iletişim kurabiliyor
.
Network kullanımı
frontend ve backend olmak üzere iki özel network oluşturduk.
Servisleri bu network’lere dahil ederek, servisler arası iletişim ve izolasyonu simüle ettik.
Böylece gerçek dünya projelerinde servislerin güvenli ve kontrollü iletişimini anlamış olduk.

Volume kullanımı
dbdata volume’ü ile MySQL verilerini kalıcı hale getirdik.
Böylece container’ı silsek bile veriler kaybolmuyor.

# UYGULAMAYI BAŞLAT
docker compose up -d 
>	•	-d parametresi container’ları arka planda çalıştırır.
>	•	İlk çalıştırmada Docker imajları repolardan çekilecektir, bu yüzden biraz zaman alabilir.

# KONTROL ET
docker compose ps
>	•	Çıktıda iki container’ı görmelisin: demo-web ve demo-db
>	•	Web sayfasını görmek için tarayıcıdan: http://localhost:8080/index.html
docker volume ls 
docker network ls



# LOGLARI TAKİP ET
docker compose logs -f web     VEYA  db 

>	•	Bu komut web container’ının loglarını canlı olarak gösterir.

# DEĞİŞİKLİK VE RESTART 
örnek olarak web volume pat adresinde değişiklik yapmak istedik
app/index.html    değilde      app2/index2.html path ini containera mounth etmek istedik  
 compose.yaml üzerinde services altında  web kısmında volume path değişikliği yapıp save ettikten sonra :

docker compose restart web      //// yeterli olmayacaktı imaj değişiklikleri gibi işlerde kullanırız 

>Alternatif olarak sadece web servisini yeniden oluşturmak gerekecektir.

      docker compose up -d --no-deps --build web  ]önemli

>	•	--no-deps → db yeniden başlamaz
>	•	--build → image rebuild gerekirse rebuild eder


>	•	Sadece web container yeniden başlar, db etkilenmez.
>	•	Web sayfasını yenilediğinde yeni içerik görünecektir.


# DURDUR 
docker compose down

removed:
[+] Running 4/4
 ✔ Container demo-web         Removed                                                                                                                                                                                          0.2s 
 ✔ Container demo-db          Removed                                                                                                                                                                                          1.2s 
 ✔ Network uygulama_backend   Removed                                                                                                                                                                                          0.4s 
 ✔ Network uygulama_frontend  Removed  

 # docker volume ls ???
 ➜  uygulama git:(main) ✗ docker volume ls
DRIVER    VOLUME NAME
local     minikube
local     uygulama_dbdata

volume yapıları kalıcıdır 



--------------------------------------
# compose içinde 2 farklı container network bağımlılık testleri
Web container’a gir
docker exec -it demo-web /bin/bash
apt update & apt upgrade -y
apt install -y iputils-ping
ping demo-db




 MySQL bağlantısını test etmek

Web container’a mysql-client yükleyip deneyebilirsin
apt update
apt install -y mariadb-client-compat
mysql -h demo-db -u root -p1234 demo
	•	Eğer bağlanabiliyorsan network ve DB bağlantısı çalışıyor demektir.
	•	Bu komut DB’ye bağlanmayı ve multi-container network’ün aktif olduğunu doğrular.