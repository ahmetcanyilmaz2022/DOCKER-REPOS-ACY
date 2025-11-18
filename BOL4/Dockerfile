FROM         Base image belirler, hangi imajdan başlayacağını söyler                    FROM: node:18
WORKDIR      Container içindeki çalışma dizinini ayarlar                                WORKDIR /app
COPY         Dosya/dizinleri host’tan container’a kopyalar                              COPY . .
ADD          COPY gibi ama URL’den de dosya indirebilir, archive dosyalarını açabilir   ADD app.tar.gz /app
RUN          Container build edilirken çalıştırılacak komut                             RUN npm install
CMD          Container çalıştığında varsayılan komutu belirler                          CMD ["node", "app.js"]
ENTRYPOINT   Container çalıştırılırken temel komut olarak ayarlanır                     ENTRYPOINT ["python3"]
ENV          Ortam değişkeni tanımlar                                                   ENV PORT=3000
EXPOSE       Container’ın dinleyeceği portu bildirir (sadece dokümantasyon)             EXPOSE 3000
ARG          Build-time değişken tanımlar                                               ARG NODE_ENV=production
VOLUME       Kalıcı veri dizini tanımlar                                                VOLUME /data/db
USER         Container içinde hangi kullanıcı ile çalışacağını ayarlar                  USER node
LABEL        Metadata ekler (yazar, sürüm vb.)                                          LABEL version="1.0"
ONBUILD      Türev image’ler build edildiğinde tetiklenir                               ONBUILD COPY . /app
STOPSIGNAL   Container durdurulurken gönderilecek sinyali ayarlar                       STOPSIGNAL SIGTERM
HEALTHCHECK  Container’ın sağlık durumunu kontrol eden komut                            HEALTHCHECK  CMD curl -f http://localhost/
 