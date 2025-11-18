# docker version 
>docker version, hem Docker Client (istemci) hem de Docker Server (Engine) tarafının sürüm ve yapı (build) bilgilerini gösteren bir komuttur.

# docker info
>Docker’ın sistem genel durumunu gösterir — yani senin Docker Engine’ının kaynaklarını, ayarlarını ve çalışma durumunu özetler.

# docker help
>Docker komut satırında kullanabileceğin tüm alt komutları ve komutların ne işe yaradığını özet halinde gösterir.
Yani Docker’ın “yardım menüsü”dür.

### Docker create&list&deatach container ###
# docker create

docker container run  -p 8080:80 ahmetcan2022/dockeregitimi

-p = Port yönlendirme
publish etme
Host 8080 → Container 80

docker container run  ahmetcan2022/app1sh:latest

# run containerları listele
docker container ls  
docker container ps
# run ve stop containerları listele
docker container ls -a
docker container ps -a

# Docker deatach & add name 
docker container run --name website -d -p 8080:80 ahmetcan2022/dockeregitimi
docker container run --name myapp -d ahmetcan2022/app1sh:latest

# Docker logs & stop & rm “delete”
docker container log <container-name or id>
docker container stop <container-name or id>
docker container rm <container-name or id>
docker container  rm -f <container_name_or_id>

# Docker image ls & rm “delete”
docker image rm
docker image prune

# Docker EXEC
docker exec -it website bash
exit

>attach → Mevcut sürece bağlanırsın, ana sürece bağlı, riskli.
>Exec → Yeni terminal/shell açarsın, ana süreç güvenli.

>içeriye Tek Komut Gönderme (Girmeden)
>Bazen sadece küçük bir şey çalıştırmak istersin
docker exec website ls /usr/share/nginx/html

>Nginx container içindeki index.html dosyasını görmek:
>Bazen sadece küçük bir şey çalıştırmak istersin
docker exec website cat /usr/share/nginx/html/index.html

# UYGULAMA
docker container run --name website -d -p 8080:80 ahmetcan2022/dockeregitimi
browser= localhost:8080

docker exec -it website bash
cd usr/share/nginx/html/
apt update & apt upgrade -y
apt install vim -y
vim index.html      değişiklik yapılmalı

browser= localhost:8080

-------------------------------------
# DOCKER VOLUME
volume oluştur:
<docker volume create mydata >
listele 
<docker volume ls>
volume hakkında bilgi al 
<docker volume inspect mydata>
volume sil 
<docker volume rm mydata>


Volume’u Container’a Bağlamak

<docker run -d \
  --name myapp \
  -v mydata:/data \
  ahmetcan2022/app1sh:latest>

>-v mydata:/data → mydata adlı volume’u container’ın /data dizinine bağlar.
>myapp → container ismi

>Çalıştığını Test Edelim:

docker exec -it myapp bash
ls /data
echo "MyData test dosyası" > /data/test.txt
exit


>>Container’ı Silelim ve Yeniden Oluşturalım
>>Container’ı kaldır; 
<docker rm -f myapp>

>tekrar oluştur 
<docker run -d \
  --name myapp \
  -v mydata:/data \
  ahmetcan2022/app1sh:latest>

>tekrar içine girelim ve kaldırdığımız container içinden eklediğimiz volume yani test.txt ve içeriği burada gözükecekmi??

<docker exec -it myapp bash>
cat /data/test.txt

<mydata volume senin uygulamanın “hard diski” gibi çalışıyor.
Container silinse bile veri duruyor, yeniden başlattığında aynı yerden devam ediyor.Veya farklı bir container yapısına bağlanabiliyor!!!!
Container içinde var olan ephermal yani geçici volume kullanmak yerine Persistent kalıcı volume  yapısını kullanmış olduk. Containerı kayıp edebiliriz fakat içindeki vol de yer alan bilgileri kurtarmıs veya yeni container üzerinden hayata geçirmiş oluruz>


------------------

# BIND MOUNT
docker container run --name mynginx -d -p 80:80 -v /Users/ahmetcan/Desktop/website:/usr/share/nginx/html nginx 


for windows users:)
docker run --name mynginx -d -p 80:80 -v /c/Users/AhmetCan/Desktop/website:/usr/share/nginx/html nginx
