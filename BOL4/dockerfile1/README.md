
FROM node:18              # Node.js 18 imajını temel al
WORKDIR /app              # Container içinde çalışma dizinini /app yap
COPY . .                  # Projedeki tüm dosyaları container içindeki /app dizinine kopyala
RUN npm install           # Projenin bağımlılıklarını yükle
CMD ["npm", "start"]      # Container çalıştığında "npm start" komutunu çalıştır


.
├── Dockerfile
├── node_modules
├── package-lock.json
├── package.json
├── README.md
└── src
    ├── app.js
    └── routes.js

✔️ Bu yapı ne anlama geliyor?
	•	Dockerfile → Container imajını oluşturacak dosya
	•	package.json / package-lock.json → Proje bağımlılık listesi
	•	node_modules → npm install sonrası oluşan bağımlılıklar
	•	src/ → Application kodların (app.js, routes.js vs.)

# BUILD EDELİM İMAJ OLUŞSUN 
docker build -t myapp1 .
# ÇALIŞTIR
docker run -d -p 3000:3000 myapp1
# TARAYICIDA AÇ
http://localhost:3000
http://localhost:3000/users

> “Bu uygulama basit bir Node.js Express uygulamasıdır. Ana sayfa (/) ve kullanıcı listesi (/users) gibi endpoint’leri var. Dockerfile sayesinde uygulama container içinde çalıştırılabiliyor ve her ortamda aynı şekilde çalışıyor.”

# İMAJI REPOYA PUSH EDELİM 
# Login olalım 
docker login 
# Docker Hub’a push etmek için imajı kullanıcı adınla tag’le:
docker tag myapp1 ahmetcan2022/myapp1:latest
> 	•	myapp1 → local imaj adı
>	•	ahmetcan/myapp1:latest → Docker Hub’daki hedef repo

# PUSH 
docker push ahmetcan2022/myapp1:latest
>	•	Bu komut Docker Hub’a imajını yükler
>	•	Artık başka bir bilgisayardan da

docker pull ahmetcan/myapp1:latest
docker run -d -p 3000:3000 ahmetcan/myapp1:latest

şeklinde çalıştırabilirsin.

# Özet
	1.	Login → docker login
	2.	Tag → docker tag myapp1 <username>/myapp1:latest
	3.	Push → docker push <username>/myapp1:latest

