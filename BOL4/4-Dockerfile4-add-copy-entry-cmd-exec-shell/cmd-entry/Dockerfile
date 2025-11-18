# Base image
FROM node:18             # Node.js 18 imajını temel al
# Çalışma dizini oluştur
WORKDIR /app             # Container içindeki çalışma dizini /app
# Dosyaları kopyala
COPY package*.json ./    # package.json ve package-lock.json kopyalanır
RUN npm install          # Node.js bağımlılıklarını yükle
COPY . .                 # Projedeki tüm dosyaları container içine kopyala
EXPOSE 3000              # Container 3000 portunu açar
# CMD → varsayılan çalışacak komut
CMD ["node", "src/index.js"]   # Container çalıştığında node src/index.js çalışır
                                 # docker run ile override edilebilir
-----------------------------------------------------------------------------------

# Base image
FROM python:3.9-slim        # Minimal Python 3.9 imajını kullan
WORKDIR /app                 # Container içindeki çalışma dizini /app
COPY app/requirements.txt .  # requirements.txt kopyala
RUN pip install --no-cache-dir -r requirements.txt  # Python bağımlılıklarını yükle
COPY app/ .                  # Uygulama dosyalarını kopyala
EXPOSE 5000                  # Container portu aç
# ENTRYPOINT → her zaman çalışacak ana komut
ENTRYPOINT ["python", "app.py"]  # Container çalıştığında hep python app.py çalışır
                                   # docker run ile değiştirilemez