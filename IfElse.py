# Projemiz içerisinde belli bir koşula göre yapılacak işlemler var ise veya bu işlemlerde bir değişim olacak ise
# IF - Elif - Else yapısını kullanabiliriz.

# If bloğunda bir koşul belirtiriz. Eğer koşul sağlanıyor ise If bloğu, sağlanmıyor yani False dönüyor ise Else bloğu çalışır.
# Birden fazla koşul var ise Elif blokları ile koşullarımızı arttırabiliriz.

# Else ve Elif blokları opsiyoneldir.

# Temel Syntax

# if ifade1:
#     sağlanıyorsa yapılacak iş(ler)
# elif ifade2:
#     sağlanıyorsa yapılacak iş(ler)
# elif ifade3:
#     sağlanıyorsa yapılacak iş(ler)
# else
#     Üstteki koşullar sağlanmazsa yapılacak iş(ler)



# Karşılaştırma Operatörleri

# '==' (Eşit mi?) eşitliğin solundaki değer, sağ taraftaki değere eşit mi kontrolü yapar ve true/false (bool tipinde) değer döner
# '!=' (Eşit Değil mi?) eşitliğin solundaki değer, sağ taraftaki değere eşit değil mi kontrolü yapar ve true/false (bool tipinde) değer döner
# '>' (Büyük mü?) eşitliğin solundaki değer, sağ taraftaki değerden büyük mü kontrolü yapar ve true/false (bool tipinde) değer döner
# '<' (Küçük mü?)eşitliğin solundaki değer, sağ taraftaki değerden küçük mü kontrolü yapar ve true/false (bool tipinde) değer döner
# '>=' (Büyük veya Eşit mi?)eşitliğin solundaki değer, sağ taraftaki değerden büyük ya da eşit mi kontrolü yapar ve true/false (bool tipinde) değer döner
# '<=' (Küçük veya eşit mi?)eşitliğin solundaki değer, sağ taraftaki değerden küçük veya eşit mi kontrolü yapar ve true/false (bool tipinde) değer döner


# Örnek 1 => Kullanıcı tarafından girilen kelime "admin" ise hoşgeldin mesajı, geri kalan durumlarda ise giriş bilgisi hatalı! yazısını ekrana bastırınız.

kulAdi = input("Lütfen Kullanıcı Adınızı Giriniz: ")

if kulAdi == "admin":
    print("Hoşgeldiniz!")
else:
    print("Giriş bilgisi hatalı!")


# Örnek 2 => Kullanıcının gireceği not eğer 0-100 aralığı dışında ise hatalı giriş yazısını ekrana getiriniz.

ogrenciNotu = int(input("Lütfen bir not giriniz: "))
if ogrenciNotu > 100 or ogrenciNotu < 0:
    print("Hatalı Not Girişi!")
else:
    print("Not girişi başarılı!")


# Örnek 3 => Kullanıcı tarafından girilen değerin uzunluğu 8 karaktere eşit veya daha fazla ise kayıt başarılı!
# değilse otomatik bir şifre kullanıcıya gösterilsin.

deger = input("Lütfen şifrenizi giriniz : ")
if len(deger) < 8:
    print("Şifreniz çok kısa. Otomatik atanan şifreniz : 12345678 olarak belirlenmiştir.")
else:
    print("Girilen şifre {} başarı ile kaydedilmiştir! ".format(deger))
#Üstteki yazım şekli string format yöntemidir. {}'ler içerisine,  .format() bölümünde parantez içerisinde değerler atanabilir. Birden çok değer virgüller ile ayrılabilir.



# Mantıksal Operatörler

# 'Ve' anlamını taşıyan AND kelimesi ile birden çok koşulun aynı anda sağlanması durumunu kontrol edebiliriz.
# 'Veya' anlamını taşıyan OR kelimesi ile birden çok koşuldan sadece birinin sağlanması durumunu kontrol edebiliriz.

# Örnek 4 => Kullanıcıdan gelecek kullanıcı adı admin ve şifre 123 ise giriş başarılı, değilse giriş hatası şeklinde uyarınız

kullaniciAdi = input("lütfen kullanıcı adınızı giriniz : ")
sifre = input("Lütfen şifrenizi giriniz : ")

if kullaniciAdi=="admin" and sifre=="123":
    print("Giriş Başarılı!")
else:
    print("Giriş Hatası!")

# Örnek 5 => //Girilen not 0 - 30 araligi ise "FF" 30 - 50 araligi "DD" 50 - 70 "BB" 70-90 "BB" 90 - 100 "AA" aldınız seklinde kullaniciyi uyariniz..

varNot = int(input("Lütfen Notunuzu Giriniz: "))
if 0 < varNot or varNot > 100:
    print("Hatalı Not Girişi!")
elif 0 < varNot <= 30:  # Şu şekilde kısaltılabilir.
    print("Notunuz : FF")
elif 30 < varNot <= 50:
    print("Notunuz : DD")
elif varNot> 50 and varNot<=70: # Uzun yazılışları 'and' ile gösterilebilir.
    print("Notunuz : CC")
elif varNot>70 and varNot<=90:
    print("Notunuz : BB")
else:
    print("Notunuz : AA")

#  Disaridan siparis alinacak olan kitap miktari girilsin. Sipari sayisi 20'den azsa toplam ucretten %5, 20 - 50 araliginda ise %10, 50-100 araligi ise %15, 100'den fazla ise %25 indirim yapilsin. Kitabın birim fiyatı => 5 TLdir... Amac => Odenecek tutari kullaniciya gostermek...
#
birimFiyat = 5
alinanSiparisMiktari = int(input("Lütfen kitap miktarını giriniz: "))
toplamOdenecekTutar = 0

if 0 < alinanSiparisMiktari <= 20:
    toplamOdenecekTutar = (birimFiyat*alinanSiparisMiktari)*0.95
elif 20 < alinanSiparisMiktari <= 50:
    toplamOdenecekTutar =(birimFiyat*alinanSiparisMiktari)*0.90
elif 50 < alinanSiparisMiktari <= 100:
    toplamOdenecekTutar = (birimFiyat * alinanSiparisMiktari) * 0.85
elif alinanSiparisMiktari > 100:
    toplamOdenecekTutar = (birimFiyat * alinanSiparisMiktari) * 0.75


print("Toplam Ödenecek Tutar : {}".format(toplamOdenecekTutar))


# Disaridan urun adi girilecek, kasiyer bize urunun hangi reyonda oldugunu soyleyecek...
# Domates, Biber, Patlican => Sebze Reyonu
# Diş Macunu, Parfüm, Şampuan => Kozmetik Reyonu
# Cep Telefonu, Bilgisayar, Ses Sistemi => Teknoloji Reyonu
# Başka bir ürün girilirse "Bu ürün bizde yok!" uyarisi verilsin!

urun = input("Lütfen Bir Ürün Adı Giriniz : ")

if urun == "Domates" or urun == "Patlican" or urun== "Biber":
    print("Sebze Reyonuna Gidiniz!")
elif urun == "Diş Macunu" or urun == "Parfüm" or urun == "Şampuan":
    print("Kozmetik Reyonuna Gidiniz!")
elif urun == "Cep Telefonu" or urun == "Bilgisayar" or urun == "Ses Sistemi":
    print("Teknoloji Reyonuna Gidiniz!")
else:
    print("Bu Ürün Bizde Yoktur!")



