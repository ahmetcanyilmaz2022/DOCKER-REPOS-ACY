# Kullanım Örneği
# Önce bir container çalıştır:

docker run -d -it ubuntu bash
>containera girmez ise;

docker exec -it a92 bash

# Container içinde değişiklik yap:
apt update
apt install -y curl
echo "Hello Docker" > /hello.txt

# Container’ı kapatmadan veya çıkış yaptıktan sonra imaj haline getir:
docker commit <container_id> mycustomubuntu:1.0
<container_id> → docker ps ile bulabilirsin
docker image ls         >>>>>>> yeni oluşan imajı görebilirsiniz
<container_id> → docker ps ile bulabilirsin
mycustomubuntu:1.0 → yeni imajın adı ve tag’

# Artık bu yeni imajdan container başlatabilirsin:
docker run -it mycustomubuntu:1.0 bash
Önceki değişikliklerin hepsi (curl yüklemesi, hello.txt dosyası) artık imajın içinde.

# temizlik 
docker ps -a
docker rm <id> <id> -f
docker image rm <imagename> <imagename>


# ÖNEMLİ NOT ####
Temizlik için opsiyonel (tüm dangling imaj ve kullanılmayan container’lar)
> docker system prune -a