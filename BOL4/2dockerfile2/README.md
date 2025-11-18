.
├── Dockerfile
└── app
    ├── app.py
    ├── requirements.txt
    ├── static
    │   └── style.css
    ├── templates
    │   └── index.html
    └── utils.py

FROM python:3.9-slim               # Python 3.9 slim base imajını kullan (hafif, minimal Linux tabanlı)
WORKDIR /app                        # Container içinde çalışma dizinini /app olarak ayarla

COPY app/requirements.txt .         # requirements.txt dosyasını container içine kopyala
RUN pip install --no-cache-dir -r requirements.txt   # Python bağımlılıklarını yükle, cache kullanma

COPY app/ .                         # app klasöründeki tüm uygulama dosyalarını container içine kopyala

ENV APP_USER=admin                   # Ortam değişkeni APP_USER tanımla (kullanıcı adı)
ENV APP_PASSWORD=supersecurepassword # Ortam değişkeni APP_PASSWORD tanımla (şifre)
ENV PORT=5000

EXPOSE 5000                          # Containerın dinleyeceği port

CMD ["python", "app.py"]            # Container çalıştırıldığında bu komut çalışsın (uygulamayı başlat)




# BUILD EDELİM İMAJ OLUŞSUN 
docker build -t mypythonapp .

# NOT # WARNING
SecretsUsedInArgOrEnv: Do not use ARG or ENV instructions for sensitive data (ENV "APP_PASSWORD")
>Dockerfile’da ENV ile şifre koymak güvenli değil; çünkü build sırasında imaj katmanlarında saklanır ve biri imajı inceleyebilir. Şifreleri .env dosyası veya Docker secrets ile vermek daha güvenlidir.

# ÇALIŞTIR
docker run -d -p 5001:5000 mypythonapp
# TARAYICIDA AÇ
>	•	-p 5001:5000 → host port 5001, container port 5000
>	•	Tarayıcıda: http://localhost:5001 → uygulamayı görebilirsin

> admin
> supersecurepassword

# İMAJI REPOYA PUSH EDELİM 
# Login olalım 
docker login 
# Docker Hub’a push etmek için imajı kullanıcı adınla tag’le:
docker tag mypythonapp ahmetcan2022/mypythonapp:latest
> 	•	mypythonapp → local imaj adı
>	•	ahmetcan/mypythonapp:latest → Docker Hub’daki hedef repo

# PUSH 
docker push ahmetcan2022/mypythonapp:latest
>	•	Bu komut Docker Hub’a imajını yükler
>	•	Artık başka bir bilgisayardan da

docker pull ahmetcan/mypythonapp:latest
docker run -d -p 5000:5000 ahmetcan/mypythonapp:latest

şeklinde çalıştırabilirsin.

# Özet
	1.	Login → docker login
	2.	Tag → docker tag myapp1 <username>/mypythonapp:latest
	3.	Push → docker push <username>/mypythonapp:latest


# TEMİZLİK
docker stop <container_id_or_name>
docker rm <container_id_or_name>

docker rmi mypythonapp
docker rmi ahmetcan/mypythonapp:latest

docker system prune -a