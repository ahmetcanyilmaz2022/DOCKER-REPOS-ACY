docker build --build-arg BUILD_USER=Ali -t argenv-example .
çıktı :
Build yapan: Ali
Runtime user during build: Can

--------------------------------------

docker run -it argenv-example sh
# container içinde gözlemle 
echo $BUILD_USER
# Çıktı: boş → ARG artık yok

echo $RUNTIME_USER
# Çıktı: Can → ENV runtime için var

Çok kısa akılda kalıcı:
	•	ARG = build sırasında kullanılan geçici değişken
	•	ENV = container çalışırken erişebileceğin değişken