# ---- Base Image ----
FROM node:18
# Çalışma dizini
WORKDIR /app
# Bağımlılık dosyalarını kopyala
COPY package*.json ./
# Bağımlılıkları yükle
RUN npm install
# Tüm kaynak kodu kopyala
COPY . .
EXPOSE 3000
CMD ["node", "src/index.js"]
----------------------------------------

    # ---- Base Image ----
FROM node:18
WORKDIR /app
# Bağımlılık dosyalarını kopyala (ADD ile)
ADD package*.json ./
RUN npm install
# Proje kodunu ADD ile kopyala
ADD . .
# Örnek 1: Tar dosyasını otomatik extract et
# project.tar.gz → otomatik olarak /app/project içine açılır
ADD project.tar.gz /app/project/
# Örnek 2: URL'den dosya indir
ADD https://example.com/config.json /app/config.json
EXPOSE 3000
CMD ["node", "src/index.js"]