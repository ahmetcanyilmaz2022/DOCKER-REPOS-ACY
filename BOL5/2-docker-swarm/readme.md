# Docker Swarm'ı modunu aktif edin. Docker Swarm modu aktif etmek için aşağıdaki komutu çalıştırabilirsiniz:

* docker swarm init

>Bu komut, Docker Swarm'ı kuracak ve Swarm leader manager olarak komutu çalıştırdığınız host'u seçecektir.
>Eğer host cihazda birden fazla NIC varsa, swarm ile kullanacağınız NIC'in ip adresini özellikle belirtmelisiniz.;

* docker swarm init --advertise-addr <IP_ADDRESS>

>Bu komut ile, <IP_ADDRESS> parametresi ile belirtilen IP adresi leader swarm manager olarak seçilecektir.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Docker Swarm Cluster'a Manager ve Worker Node Nasıl Eklenir ve Çıkarılır?
> Manager eklemede kullanılacak token kodunu öğrenmek için:
* docker swarm join-token manager

>Worker eklemede kullanılacak token kodunu öğrenmek için:
docker swarm join-token worker
çıktı:)
* docker swarm join --token <TOKEN> <IP_ADDRESS>:<PORT>
> bu cıktıyı kopyaladıktan sonra terminat üzerinden input verdiğiniz herbir docker host sunucu worker olacaktır .
>Bir node'u swarm cluster'dan çıkarmak için ilgili hostta şu komutu çalıştırabilirsiniz:
* docker swarm leave

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Node Listele 
* docker node ls
* ile işaretlenen node leader manager'dır.

>node 5 ise manager token ı girmiş olduğumuz reachable modunda bekleyen yedek bir yönetici olarak düşünebiliriz.

>Bir worker node'u manager node yapmak için promote komutunu kullanabilirsiniz.
* docker node promote [NODE_ID]

> Bir manager node'u worker node yapmak için demote komutunu kullanabilirsiniz.
* docker node demote [NODE_ID]

>Bir node'u cluster'dan kaldırmak için rm komutunu kullanabilirsiniz.
* docker node rm [NODE_ID]

> Bir node'un detaylarını görmek için inspect komutunu kullanabilirsiniz.
* docker node inspect [NODE_ID]

>Bir node'un üzerinde çalışan servisleri ve durumlarını görmek için ps komutunu kullanabilirsiniz.
* docker node ps [NODE_ID]

------------------------------------------------------------------------------------------------------
## SERVICE
>Bir servisi oluşturmak için kullanabileceğin temel komut şöyledir
* docker servicecreate --name <SERVICE_NAME> <IMAGE>
Burada:
><SERVICE_NAME> → Servise vereceğin isim,
><IMAGE> → Çalıştırılacak container’ın Docker imajıdır.

>Bu komutu çalıştırdığında, tanımladığın servis Swarm cluster’a eklenir ve yönetimi otomatik olarak manager node tarafından gerçekleştirilir. Servisin hangi node’da çalışacağından kaç kopya oluşturulacağına kadar tüm süreçleri Swarm kendisi üstlenir.
---------

> Örneğin, Swarm üzerinde basit bir nginx servisi oluşturmak istediğimizde kullanacağımız en temel komut şöyle olur:
* docker service create --name web nginx
>Bu komut, web isimli bir servis oluşturur ve nginx imajını kullanarak ilgili container’ı cluster’a dahil eder.

> Servisi oluştururken container’a ait yapılandırmaları da doğrudan bu aşamada verebilirsiniz. Örneğin servisin dış dünyaya 8080 portundan erişilebilir olmasını istiyorsak:
* docker service create --name web --publish 8080:80 nginx

>Eğer uygulamanın yük altında daha performanslı çalışmasını istiyor ve bunun için birden fazla container ayağa kaldırmak istiyorsak, sadece --replicas parametresini eklememiz yeterli:
* docker service create --name web --replicas 3 nginx

> Bu komutla web servisi altında toplam 3 adet nginx container oluşturulur ve Swarm bu container’ları otomatik olarak uygun node’lara dağıtır. Gelen trafik ise Swarm’ın dahili load balancer’ı tarafından bu üç replica arasında paylaştırı


# Docker üzerinde 2 tip servis modu vardır. Bunlar: global ve replicated modudur.
# * Global mod, cluster'da yer alan tüm node'lara, oluşturulan servisin birer container'ını koyar. Manager node'larda bu container'lara sahiptir.

# * Replicated mod, varsayılan servis modudur ve --replicas parametresi ile belirtildiği kadar container'ı node'lara paylaştırır. Eğer sayı belirtmezseniz varsayılan olarak 1 adet container oluşturulur.
> Servis oluştururken --mode ile kullanacağınız modu belirtebilirsiniz.
* docker service create --name web --mode global nginx

# Eğer container'ların belirli bir node üzerinde  çalışmasını istersek şu şekilde kısıtlama ekleyebiliriz:
* docker service create --name web --replicas 3 --constraint "node.hostname==node_name" nginx

# Eğer container'ların belirli bir node üzerinde çalışmamasını istersek şu şekilde kısıtlama ekleyebiliriz:
* docker service create --name web --replicas 3 --constraint "node.hostname!=node_name" nginx

# Eğer container'ların manager node'lar üzerinde çalışmamasını istersek şu şekilde kısıtlama ekleyebiliriz:
* docker service create --name web --replicas 3 --constraint "node.role!=manager" nginx

>> Şimdi service'ler  ile kullanacabileceğimiz komutları inceleyelim:

> docker service ls: Bu komut ile Swarm cluster'ında bulunan tüm container'ları görebilirsiniz Yukarıdaki örneğimizin çıktısı şu şekilde gözükecektir:

ID             NAME      MODE         REPLICAS   IMAGE          PORTS
scvuh7ohf668   web       replicated   3/3        nginx:latest
-------------------

* docker service ps <SERVICE_NAME>

> Bu komut ile <SERVICE_NAME> parametresi ile belirtilen container'ın bilgilerini görebilirsiniz. Bu bilgiler arasında container'ın çalıştığı host, replicas sayısı ve durumu gibi bilgiler bulunur. Yine  aynı şekilde yukarıdaki örneğin çıktısı şu şekilde olacaktır:

ID             NAME      IMAGE          NODE       DESIRED STATE   CURRENT STATE                ERROR     PORTS
jgbut76c945p   web.1     nginx:latest   manager2   Running         Running about a minute ago             
i7iav35c37a2   web.2     nginx:latest   manager1   Running         Running about a minute ago             
knxihcpylgl3   web.3     nginx:latest   worker1    Running         Running about a minute ago
-----------------


docker service scale <SERVICE_NAME>=<REPLICAS>
>  Bu komut ile <SERVICE_NAME> parametresi ile belirtilen container'ın replicas sayısı <REPLICAS> parametresi ile belirtilen sayıya ayarlanır. Örneğin, docker service scale web=5 komutu ile web isimli container'ın replicas sayısı 5'e ayarlanır ve bu container 5 tane olarak çalıştırılır.
------------------------

## NETWORK
> Docker swarm, init komutunu kullandığınızda ingress  isimli bir overlay driver networku sizin için otomatik olarak oluşturur ve tüm servisleri bu network'e ekler.
# Yeni bir swarm overlay network oluşturmak için aşağıdaki komutu kullanabilirsiniz:
* docker network create --driver overlay network_name
# Artık servislerinizi oluştururken --network parametresi ile  overlay network'ümüzü belirtebiliriz.
* docker service create --network over_net --name web --publish 8080:80 nginx
-------------------



## Docker Swarm Servislerin Güncellenmesi
> Docker swarm cluster'ınızda yer alan servislerinizle ilgili bir güncelleme yapacağınız zaman update komutunu kullanabilirsiniz. Böylece manual olarak ve service ve container kaldırıp tekrar kurmadan swarm'ın otomatik olarak güncelleme işlerini yapmasını sağlayabilirsiniz.

# Service güncellemesi: Docker Swarm'da bir servisi güncellemek için aşağıdaki komut kullanılır. Örnek olarak, "web" isimli hizmeti güncellemek isteyelim.
* docker service update --image <new_image> web
>Örnek olarak kullandığınız image'in yeni versiyonunu update komutunu kullanarak servisinizi upgrade etmiş olursunuz. Diğer türlü servisi kaldırıp baştan kurmanız gerekecekti.

# Docker Swarm update komutu ile bir servisi güncellerken kullanabileceğiniz bazı parametreler ve açıklamaları şunlardır:

* --image: Servisi güncellemek için kullanılacak olan yeni görüntüyü belirler.
* --args: Servisi çalışması için gereken argümanları belirler.
* --env-add: Servis için yeni bir ortam değişkeni ekler.
* --env-rm: Servis içindeki bir ortam değişkenini siler.
* --replicas: Servisin çalışması için gereken örnek sayısını belirler.
* --limit-cpu: Servis için kullanılabilir olan maksimum CPU miktarını belirler.
* --limit-memory: Servis için kullanılabilir olan maksimum bellek miktarını belirler.
* --constraint-add: Servis için bir kısıtlama ekler.
* --constraint-rm: Servis içindeki bir kısıtlama siler.
* --update-parallelism: Servis güncellemesi sırasında aynı anda güncellenebilecek örnek sayısını belirler. Örneğin --update-parallelism 2 komutu ile güncelleme işlemi aynı anda 2 container üzerinde  gerçekleşir. Varsayılan değeri 1'dir.
* --update-delay: Servis güncellemesi sırasında güncelleme taskları arasındaki ne kadar bekleneceğini belirtir. S saniye, m dakika, h saat olarak tipini belirtebiliriz. Örneğin --update-delay 10s

>Eğer güncellemeyi geri almak isterseniz rollback komutunu kullanabilirsiniz. Bu komut son çalıştırılan update komutunu geri alır.
* docker service rollback