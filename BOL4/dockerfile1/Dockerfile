FROM node:18              # Node.js 18 imajını temel al
WORKDIR /app              # Container içinde çalışma dizinini /app yap
COPY . .                  # Projedeki tüm dosyaları container içindeki /app dizinine kopyala
RUN npm install           # Projenin bağımlılıklarını yükle
CMD ["npm", "start"]      # Container çalıştığında "npm start" komutunu çalıştır
