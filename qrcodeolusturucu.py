import urllib.parse
import urllib.request
size="512x512"
veri=input("Qr kod içerisinde yer alacak veriyi giriniz:")
veriler={
	'size' : size,
	'data' : veri
	}
parametreler = urllib.parse.urlencode(veriler)
api_link ="https://api.qrserver.com/v1/create-qr-code/?" + parametreler
urllib.request.urlretrieve(api_link,"karekod.png")
print("Başarılı,bulunduğunuz dizine oluşturuldu.")