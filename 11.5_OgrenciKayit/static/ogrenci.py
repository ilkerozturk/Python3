class Ogrenci:
    
    @staticmethod # Statik metot self ya da cls parametresi almaz
    def getinfo(ogrenciNo):
        with open("/Users/ilkerozturk/Documents/Dev-Folder/Python3/Dersler/11.5_OgrenciKayit/library/ogrenciler.txt", 'r', encoding='utf-8') as dosya:
            satirlar = dosya.readlines()
            for satir in satirlar:
                if ogrenciNo in satir:
                    print(satir)
                    break
            else:
                print("Öğrenci bulunamadı.")
        
     

    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.notlar = []

    def not_ekle(self, not_degeri):
        self.notlar.append(float(not_degeri))

    def ortalama_hesapla(self):
        if len(self.notlar) == 0:
            return 0
        return sum(self.notlar) / len(self.notlar)

    def dosyaya_yaz(self, dosya_yolu):
        with open(dosya_yolu, 'a', encoding='utf-8') as dosya:
            dosya.write(f"{self.ad},{self.soyad},{self.numara},{self.notlar},{self.ortalama_hesapla()}\n")
    
            
