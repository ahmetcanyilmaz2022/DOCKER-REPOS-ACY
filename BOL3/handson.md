# NETWORK
docker network ls       sistemde docker networklere ait servisleri listeler

docker network inspect <networkname>          ilgili networke ait ayrıntılı bilgiler

docker container inspect <container name >     container hangi networkte inceleyebiliriz

# bridge network ağıda bir containerdan dışarıya ping 
docker container run -d -p 80:80 --name webserver ahmetcan2022/dockeregitimi
docker container exec  webserver
ping için gereksinimler: )
apt install net-tools
ifconfig
&&
apt install -y iputils-ping
ping 8.8.8.8
“google”
-----

# aynı bridge network ağız üzerinden first ve second isimli 2 farklı container arası trafik iletişim konstrolu 
docker run -d -p 80:80 --name first nginx
docker run -d -p 81:80 --name second nginx

FIRST CONTAINER:
docker container exec -it first bash 
root//
    apt update && apt upgrade -y 
    apt install net-tools -y
    ifconfig        <ip adresini not alalım >
sECOND CONTAINER;
docker container exec -it second bash         
root//
   apt update && apt upgrade -y 
   apt install net-tools -y
   apt install iputils-ping -y 
   ping <first container ip>
--------

# container oluşturma aşamasında var olan networku tanımlama 
# bridge
docker container run -d --name test1 --net bridge ahmetcan2022/dockeregitimi 
docker exec -it test1 bash 
root//
    apt update && apt upgrade -y 
    apt install net-tools -y
    ifconfig        <ip adresini not alalım >
# host
docker container run -d -it --name test1 --net host ahmetcan2022/dockeregitimi  bash
root//
    apt update && apt upgrade -y 
    apt install net-tools -y
    ifconfig        <ip adresini not alalım >
host network tanımladığımız için bulunduğumuz makinaya ait ip bilgileri alırız
-----

# Yeni bir NETWORK oluştur ve yeni bir containerı o networke bağla 
# Yeni bir network oluştur
docker network create my-network
>network türü belirtilmediği için default olarak bridge network oluşturulur)

>İstersen subnet ve gateway de belirleyebilirsin:
docker network create \
  --subnet=172.25.0.0/16 \
  --gateway=172.25.0.1 \
  my-network-with-subnet

>Containerı networke bağlayarak oluştur
docker run -d --name my-container --network my-network ahmetcan2022/app1sh


# NETWORK türü seçilerek network create etme :
docker network create -d bridge my-bridge
docker network create -d overlay my-overlay
docker network create -d overlay my-overlay
              -d = --driver ın kısaltması) 

# >Mevcut container’ı sonradan bir network’e eklemek
docker network create -d bridge my-network3
docker run -d --name my-container nginx
docker network connect my-network3 my-container
-----

# PORT PUBLISH
 docker run -d -p <host_port>:<container_port> my-image

>-p veya --publish → Port publish komutu
><host_port> → Host makinede açılacak port
><container_port> → Container içinde servis portu
# ÖRN:
docker run -d -p 8080:80 nginx
>Host port 8080 → Container port 80’e yönlendirilir
>Tarayıcıdan http://localhost:8080 ile nginx’e erişebilirsin


>>>>>UDP ÜZERİNDEN PORT AÇMAK İSTERSEK ?
docker run -d -p <host_port>:<container_port>/udp my-image
# ÖRN:
docker run -d -p 5000:5000/udp my-udp-app
Host port 5000 → Container port 5000 UDP’ye yönlendirilir
Container içindeki UDP servisine host üzerinden erişebilirsin
----


# DOCKER LOGS
Container Logları
Her Docker container, çalıştığı sürece STDOUT ve STDERR akışına yazı yazar.
Bu çıktılar Docker tarafından log driver aracılığıyla kaydedilir.
# Container içinde çalışan uygulama:
>STDOUT → normal loglar.    “standart output”
>STDERR → hata logları         “standart error”
Docker ikisini de toplar ve docker logs komutunda birlikte gösterir.

# UYGULAMA 
# log takibi için bir container oluşturalım 
docker run -d --name logsapp nginx

# logsapp isimli container loglarını alalım :
docker logs logsapp

# Canlı izleme (tail -f gibi):
docker logs -f logsapp

# Son N satırı görmek:
docker logs --tail 6 logsapp

# Timestamps ile logları görmek:
>Timestamp log, her bir log satırının hangi tarihte ve saatte üretildiğini gösteren zaman bilgisidir.
docker logs -t logsapp

# logları localde bir file yapısına göndermek:
docker logs logsapp > log.txt

# Log Ayarları
>Max boyut ve döndürme (rotation):
docker run -d \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  nginx
Burada anlatılmak istenen şey kısaca şöyle:
>	•	--log-opt max-size=10m → Her container log dosyası en fazla 10 MB olana kadar büyür.
>	•	--log-opt max-file=3 → Eğer log 10 MB’a ulaşıp döndürüldüyse, en fazla 3 eski log dosyası saklanır.
----------


# Bir container’da: hangi komutlar çalışıyor, PID’ler ne, hangi user ile çalışıyor, CPU kullanıyor mu, giriş scripti hangisi
docker top <container name or id>

# çalışmakta olan konteynerlerin anlık kaynak kullanımını gösteren bir komuttur.
docker stats
----

# LIMIT MEMORY CPU RAM
## MEMORY
>Docker container’da memory (RAM) kullanımı, container’ın çalışırken tüketebileceği bellek miktarını ifade eder.
>Limit koymazsan container host’un kullanılabilir RAM’ini istediği kadar kullanabilir.
>>Limit koyarsan:

docker container run -d --memory=100m --name memorycontainer ahmetcan2022/dockeregitimi

<<<<<<<<<<<<<<<<<<<<<<<<<<<<< --memory-swap=200m >>>>>>>>>>>>>>>>>>>> komuta eklendiğinde ekstra swap alanı eklemiş oluruz 

docker container run -d -m 100m --name memorycontainer ahmetcan2022/dockeregitimi

* → Bu container en fazla 100MB RAM kullanabilir.
* Memory limit aşılırsa container OOM (Out Of Memory) killer tarafından durdurulabilir.
* Kısaca: Memory → container’ın çalışırken kullanabileceği RAM miktarıdır

# * KONTROL * = docker stats


## CPU 
>Docker container’da CPU kullanımı, container’ın host CPU’sundan ne kadar pay alabileceğini kontrol etmeyi sağlar.
>Limit koymazsan container host’un CPU’sunu ihtiyacı kadar kullanabilir.
>Limit koymak için örnek:

docker container run -d --cpus="1.5" --name cpuscontainer ahmetcan2022/dockeregitimi

* veya       <<<<<<<<cpus = core sayısı ARALIĞI spesifik cpu seçimi>>>>>>>>>>>>>. aşağdıa ise şu cpu ları kullan diyerek core numarası belirtebiliriz.

docker container run -d --name --cpus="1.5" --cpuset-cpu=”1,3" cpuscontainer ahmetcan2022/dockeregitimi

* → Container en fazla 1.5 CPU çekirdeği kullanabilir.
* Ayrıca CPU shares ile öncelik atayabilirsin, örneğin yoğun sistemde hangi container daha çok CPU alır.
* Kısaca: CPU → container’ın host CPU kaynak kullanım sınırı ve önceliği
----------


# ENVIRONMENT
>Docker’da container oluştururken environment variable (env) kullanmak, uygulamanın dışardan yapılandırılmasını sağlar. 
# Environment Variable Nedir?
* Container içinde çalışan uygulamalara dinamik değerler iletmek için kullanılır.
* Örnekler: database URL, port, API key, debug modu, kullanıcı adı vb.
* Uygulamayı her seferinde yeniden build etmeden farklı değerlerle çalıştırabilirsin.

docker container run -d --env MYVAR=myvalue --env MYVAR-E=myvalue2 --name myenvcont ahmetcan2022/dockeregitimi
docker exec -it myenvcont bash 
printenv    veya       env



