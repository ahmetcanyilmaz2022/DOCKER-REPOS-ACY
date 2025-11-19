Docker Compose Nedir? 
Docker Compose, birden fazla container’dan oluşan uygulamaları tek bir dosya (docker-compose.yml) ile tanımlayıp kolayca yönetmeni sağlayan bir araçtır.
Bir uygulama genelde tek container’dan ibaret olmaz.
Örneğin:
Web uygulaması → app container
Database → db container
Cache → redis container
Reverse proxy → nginx container
Bu parçaların hepsinin birlikte ve uyumlu şekilde çalışması gerekir.
İşte Docker Compose tam olarak bunun için vardır.
--------------------
Neden Docker Compose kullanırız?
1) Çoklu container’ı tek komutla yönetmek
docker compose up -d
docker compose down
Bu iki komutla tüm servisleri yağa kaldırır veya durdurabiliriz

2) Tüm uygulama altyapısını tek bir dosyada tanımlamak
Database, web, cache… hepsi tek yml dosyasından yönetilir.

3) Kolay taşınabilirlik
Başka birine verirsin: docker compose up ile aynı şekilde ayağa kalkar

4) Network, volume, environment ayarları otomatik
Her servis için ayrı ayrı ayar yapmaya gerek yok.
-------------
# Compose Komutları
Terminalde Compose V kontrolü
docker compose version

Projeyi Başlat
docker compose up -d

Durdur
docker compose down

Log takibi
docker compose logs -f

Tek Bir Servisi Restart Et
docker compose restart db