# ÖRNEKTE
* Bir web servisi (nginx)
* Bir backend servisi (alpine tabanlı basit bir API)
> Hepsi tek bir YAML dosyasında tanımlanıyor ve tek komutla Swarm’a deploy ediliyor.

# Stack’i Swarm’a Deploy Etme
* docker stack deploy -c docker-stack.yml myapp
> Bu komut ile:
- -c docker-stack.yml → “Bu stack’i şu dosyadaki tanımlara göre kur.”
- docker-stack.yml dosyasında tanımladığın servisler oluşturulur,
- Overlay network otomatik kurulur,
- Servisler node’lara dağıtılır,
- Swarm tüm yük dağıtımı ve yönetimi üstlenir.

# STACK i Görüntüle
* docker stack ls
* docker stack services myapp
* docker stack ps myapp