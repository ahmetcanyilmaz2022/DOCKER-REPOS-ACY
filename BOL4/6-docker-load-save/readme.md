docker save ve docker load Docker dünyasında imajları dosya olarak taşımak veya yedeklemek için kullanılır. 

# docker SAVE Nedir?
Amaç: Docker imajını tar veya .tar.gz dosyası olarak kaydetmek
Böylece imajı başka bir bilgisayara veya sunucuya taşıyabilirin.
Commit edilmiş veya build edilmiş imajları dosya olarak dışarı aktarır.


# UYGULAMA SAVE
# önce bir docker image oluşturalım
docker build -t mypythonapp:1.0 .
# imajı save edelim
docker save -o myapp_image.tar mypythonapp:1.0
#açıklama
> -o myapp_image.tar → oluşturulacak dosya
> mypythonapp:1.0 → kaydedilecek Docker imajı
(Bu komut sonrası myapp_image.tar dosyası oluşur, bunu USB, e-posta veya SCP ile başka bir yere taşıyabilirsin.


# docker LOAD Nedir?
Amaç: docker save ile kaydedilmiş bir imajı Docker’a geri yüklemek
Dosyadan imajı Docker imaj listene ekler.
# UYGULAMA LOAD
# imajı save edelim
docker load -i myapp_image.tar
(-i myapp_image.tar → yüklemek istediğin dosya
İşlem sonrası imaj docker images listende görünür ve container başlatabilirsin.

# çalıştırmak istersek
docker run -d -it --name mypythonapp mypythonapp:1.0 bash

# temizlik 
docker image rm mypythonapp:1.0




