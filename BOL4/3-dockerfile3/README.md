multistage-app/
├── Dockerfile
├── package.json
├── package-lock.json
├── src/
│   ├── index.js
│   └── public/
│       └── index.html
├── .env
└── README.md
-------------------------------------------------------------------------------------------
# ------------------------
# 1. BUILD Stage
# ------------------------
WORKDIR /app                       # Build stage içinde çalışma dizinini /app yap
COPY package*.json ./              # package.json ve package-lock.json dosyalarını kopyala
RUN npm install                    # Bağımlılıkları yükle
COPY . .                           # Tüm uygulama dosyalarını container içine kopyala

# ------------------------
# 2. Production Stage
# ------------------------
FROM node:18-slim                   # Daha küçük ve hafif base imaj ile production stage başlat
WORKDIR /app                        # Çalışma dizinini /app olarak ayarla
COPY --from=builder /app ./         # Builder stage’den hazırlanan dosyaları al

ENV PORT=4000                       # Uygulamanın çalışacağı portu ortam değişkeni olarak ayarla
EXPOSE 4000                         # Container’ın hangi portu dinleyeceğini bildir (dokümantasyon amaçlı)
CMD ["node", "src/index.js"]        # Container çalıştığında uygulamayı başlat

# Bu Node.js web uygulamasında builder stage npm ile bağımlılıkları yükler ve tüm dosyaları hazırlar, production stage ise sadece çalışması için gerekli dosyaları alır. Sonuç: imaj daha küçük, gereksiz dosya yok ve güvenli.
-------------------------------------------------------------------------------------------



# BUILD EDELİM İMAJ OLUŞSUN 
docker build -t multistage-app .
# ÇALIŞTIR
# env dosyası kullanarak (önerilen)
docker run -d -p 4000:4000 --env-file .env multistage-app
>	•	-d → arka planda çalıştır
>	•	-p 4000:4000 → host port 4000 → container port 4000
>	•	.env içindeki PORT ve WELCOME_MESSAGE okunur


# TARAYICIDA AÇ
http://localhost:4000


# İMAJI REPOYA PUSH EDELİM 
# Login olalım 
docker login 
# Docker Hub’a push etmek için imajı kullanıcı adınla tag’le:
docker tag myapp1 ahmetcan2022/multistage-app:latest
> 	•	myapp1 → local imaj adı
>	•	ahmetcan/multistage-app:latest → Docker Hub’daki hedef repo

# PUSH 
docker push ahmetcan2022/multistage-app:latest
>	•	Bu komut Docker Hub’a imajını yükler
>	•	Artık başka bir bilgisayardan da

docker pull ahmetcan/multistage-app:latest
docker run -d -p 4000:4000 --env-file .env ahmetcan/multistage-app:latest

şeklinde çalıştırabilirsin.

# Özet
	-d → arka planda çalıştır
	•	-p 4000:4000 → host port 4000 → container port 4000
	•	.env → varsa ortam değişkenlerini container’a verir

# ENV yi filedan almadan kendimiz command içinde unique şekilde belirtebiliriz.
	•	Eğer .env yoksa direkt ENV ile de verebilir: 
docker run -d -p 3000:4000 -e PORT=4000 -e WELCOME_MESSAGE="Merhaba Docker!" ahmetcan/multistage-app:latest



# LOCAL DE İMAJ TAG i değiştir VERSİYONLA
docker tag multistage-app ahmetcan/multistage-app:1.1

>	•	multistage-app → local’de build ettiğin imajın adı
>	•	ahmetcan/multistage-app:1.1 → Docker Hub’daki yeni hedef tag

PUSH:
docker push ahmetcan/multistage-app:1.1

>Eğer imajı her build ettiğinde otomatik yeni bir tag vermek istiyorsan build aşamasında direkt tagli şekilde de yapabilirsin:

docker build -t ahmetcan/multistage-app:1.1 .


# TEMİZLİK
docker stop <container_id_or_name>
docker rm <container_id_or_name>

docker rmi multistage-app
docker rmi ahmetcan/multistage-app:latest

docker system prune -a

