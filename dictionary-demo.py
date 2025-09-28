"""user_info = {
    "ogrenci_numarasi": input("Öğrenci Numaranızı Giriniz: "),
    "ad": input("Adınızı Giriniz: "),
    "soyad": input("Soyadınızı Giriniz: "),
    "yas": int(input("Yaşınızı Giriniz: ")),
    "telefon": input("Telefon Numaranızı Giriniz: "),
}"""

user_info = {}

for i in range(3):  
            
    number = int(input("Öğrenci Numaranızı Giriniz: "))
    ad = input("Adınızı Giriniz: ")
    soyad = input("Soyadınızı Giriniz: ")
    sinif = input("Sınıfınızı Giriniz: ")
    bolum = input("Bölümünüzü Giriniz: ")




    user_info[number] ={
    "ad": ad,
    "soyad": soyad,
    "sinif": sinif,
    "bolum": bolum
    }


print(user_info)

