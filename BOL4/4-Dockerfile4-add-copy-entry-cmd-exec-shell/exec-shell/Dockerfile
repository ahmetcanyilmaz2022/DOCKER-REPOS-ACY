FROM alpine:3.18
WORKDIR /app
COPY run.sh .
# EXEC FORM → Komut JSON dizi formatındadır.
# Shell kullanılmaz, komut doğrudan çalışır.
CMD ["sh", "run.sh"]

--------------------------------------------

FROM alpine:3.18
WORKDIR /app
COPY run.sh .
# SHELL FORM → Komut shell üzerinden çalıştırılır.
CMD sh run.sh