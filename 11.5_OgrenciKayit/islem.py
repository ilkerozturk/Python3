from static.ogrenci import Ogrenci


while True:    
    
    print("\nÖğrenci Kayıt Sistemi")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Sil")
    print("3. Öğrenci Bilgilerini Göster")
    print("4. Çıkış")   
    secim = input("Seçiminiz (1-4): ") 

    if secim == "1":
        ogrenci_adi = input("Öğrenci Adı: ")
        ogrenci_soyadi = input("Öğrenci Soyadı: ")
        ogrenci_numarasi = input("Öğrenci Numarası: ")
        ogrenci = Ogrenci(ogrenci_adi, ogrenci_soyadi, ogrenci_numarasi)
        not1 = input("Not1 girin: ")
        ogrenci.not_ekle(not1)
        not2 = input("Not2 girin: ")
        ogrenci.not_ekle(not2)
        not3 = input("Not3 girin: ")
        ogrenci.not_ekle(not3)
        print(ogrenci.notlar)
        print("Öğrenci başarıyla eklendi.")
        ogrenci.dosyaya_yaz("/Users/ilkerozturk/Documents/Dev-Folder/Python3/Dersler/11.5_OgrenciKayit/library/ogrenciler.txt")
    elif secim == "2":
        numara_sil = input("Silinecek öğrencinin numarasını girin: ")
        
        with open("/Users/ilkerozturk/Documents/Dev-Folder/Python3/Dersler/11.5_OgrenciKayit/library/ogrenciler.txt", 'r', encoding='utf-8') as dosya:
            # Dosyadaki tüm satırları oku
            satirlar = dosya.readlines()
            indexNo = list(enumerate(satirlar))
            for index, satir in indexNo:
                if numara_sil in satir:
                    print(f"{satir} siliniyor...")
                    del satirlar[index]
        with open("/Users/ilkerozturk/Documents/Dev-Folder/Python3/Dersler/11.5_OgrenciKayit/library/ogrenciler.txt", 'w', encoding='utf-8') as dosya:
            dosya.writelines(satirlar)
        print(f"{numara_sil} numaralı öğrenci silindi.")
    elif secim == "3":
        
       Ogrenci.getinfo(input("Öğrenci Numarasını Girin: "))

    elif secim == "4":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim. Lütfen 1-4 arasında bir değer girin.")

    

