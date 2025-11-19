	Docker Compose Full-Stack Demo 🚀

Bu proje, Docker Compose kullanarak tam bir full-stack uygulama kurmayı gösteren örnek bir demo uygulamasıdır. Amacı, birden fazla servisi tek bir ortamda çalıştırmayı öğrenmek ve mikroservis mantığını kavramaktır.

Projede Neler Yapıldı?
	1.	Web (Frontend)
	•	Nginx ile statik HTML sayfası sunuldu.
	•	Modern bir index.html ve buton aracılığıyla API’ye veri isteği gönderiliyor.
	•	Volume ile host bilgisayardaki ./app klasörü container içine mount edildi.
	2.	API (Backend)
	•	Node.js ve Express kullanılarak REST API oluşturuldu.
	•	MySQL veritabanına bağlanıyor ve /users endpoint’i üzerinden veri sağlıyor.
	•	Environment variable ile DB bağlantı bilgileri güvenli bir şekilde tanımlandı.
	3.	Database (MySQL)
	•	MySQL 8 container olarak çalıştırıldı.
	•	Volume kullanılarak veriler kalıcı hale getirildi (dbdata).
	•	Healthcheck ile API’nin DB hazır olana kadar beklemesi sağlandı.
	4.	phpMyAdmin
	•	MySQL veritabanını görselleştirmek ve yönetmek için eklendi.
	•	ARM64 uyumluluğu için platform ayarı yapıldı.
	5.	Docker Compose Özellikleri
	•	Multi-container yapı, servisler arası network ve bağımlılık yönetimi (depends_on).
	•	Restart policy ile servis çöktüğünde yeniden başlatma.
	•	Frontend ve API arasındaki iletişimi test etmek için networkler kullanıldı.

Projenin Faydası
	•	Docker ve Compose ile multi-container uygulama yönetimi pratiği kazandırır.
	•	Full-stack yapıdaki veri akışını (Frontend → API → DB) gösterir.
	•	CI/CD ve production ortamlarına hazırlık için temel deneyim sağlar.
	•	Node.js, MySQL ve Nginx’i birlikte çalıştırmayı öğretir.
	
	
	
	
	1.	Web (Nginx) → Statik içerik sunar, frontend portu 8080.
	2.	API (Node.js) → DB ile iletişim kurar, port 3000 üzerinden istek alır.
	3.	DB (MySQL) → Verileri saklar, kalıcı volume kullanır.
	4.	phpMyAdmin → DB yönetimi, sadece backend network’e bağlı.
	5.	Networks → Servisler arası iletişim ve güvenlik. Frontend ve backend ayrı ama gerekli servisler çapraz bağlı.
	6.	depends_on → Başlangıç sırasını kontrol eder (DB önce, API sonra, Web en son).
	7.	Volumes → DB verilerini korur, container silinse bile veri kaybolmaz.
