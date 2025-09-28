"""ad = input("Adınız nedir? ")
yas = int(input("Yaşınız kaç? "))
egitim = input("Eğitim durumunuz nedir? (ilkokul,lise, üniversite, yüksek lisans): ").lower()

if yas < 18:
    print(f"Merhaba {ad}, henüz reşit değilsiniz. Bu nedenle ehliyet alamazsınız.")
elif 18 <= yas < 65:
    if egitim == "ilkokul":
        print(f"Merhaba {ad}, ilkokul mezunu olduğunuz için ehliyet alamazsınız.")
    elif egitim == "lise":
        print(f"Merhaba {ad}, lise mezunu olduğunuz için ehliyet alabilirsiniz.")
    elif egitim == "üniversite":
        print(f"Merhaba {ad}, üniversite mezunu olduğunuz için ehliyet alabilirsiniz.")
    elif egitim == "yüksek lisans":
        print(f"Merhaba {ad}, yüksek lisans mezunu olduğunuz için ehliyet alabilirsiniz.")
    else:
        print(f"Merhaba {ad}, eğitim durumunuzu belirtmediniz.")"""

"""sozlu1=float(input("Sözlü 1 notunuzu giriniz: "))
sozlu2=float(input("Sözlü 2 notunuzu giriniz: "))
yazili1=float(input("Yazılı 1 notunuzu giriniz: "))

result = float(((sozlu1+sozlu2)*0.4) + (yazili1*0.6))

if 0 <= result < 25:
    print(f"Notunuz: {result:.2f} - Notunuz: FF - Kaldınız.")
elif 25 <= result < 45:
    print(f"Notunuz: {result:.2f} - Notunuz: DD - Kaldınız.")
elif 45 <= result < 55:
    print(f"Notunuz: {result:.2f} - Notunuz: DC - Geçtiniz.")
elif 55 <= result < 70:     
    print(f"Notunuz: {result:.2f} - Notunuz: CC - Geçtiniz.")
elif 70 <= result < 85:
    print(f"Notunuz: {result:.2f} - Notunuz: BB - Geçtiniz.")
elif 85 <= result <= 100:
    print(f"Notunuz: {result:.2f} - Notunuz: AA - Geçtiniz.")
elif result > 100:
    print(f"Notunuz: 100 - Notunuz: AA - Geçtiniz.")
else:
    print("Geçersiz not girdiniz.")"""

import datetime

today = datetime.date.today()
vTarih = input("Lütfen trafiğe çıkış tarihinizi GG/AA/YYYY formatında giriniz: ")
gTarih = datetime.datetime.strptime(today.strftime("%d/%m/%Y"), "%d/%m/%Y")
vTarih = datetime.datetime.strptime(vTarih, "%d/%m/%Y")

hesapla = gTarih-vTarih

gun = hesapla.days/365


if gun <= 1:
    print(f"Aracınız 1. servis aralığında.")
elif 1 < gun <= 2:
    print(f"Aracınız 2. servis aralığında.")
elif 2 < gun <= 3:
    print(f"Aracınız 3. servis aralığında.")
elif 3 < gun <= 4:
    print(f"Aracınız 4. servis aralığında.")    
else:
    print(f"Aracınızı sanayiye götürünüz.")

