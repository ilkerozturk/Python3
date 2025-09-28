sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

"""i = 0

while i < len(sayilar):
    print(sayilar[i])
    i += 1
"""

"""sayi1 = int(input("Lütfen bir sayı girin: "))
sayi2 = int(input("Lütfen bir sayı daha girin: "))

i = sayi1
while i <= sayi2:
    print(i)
    i += 1"""

"""i=100

while i >= 1:
    print(i)
    i -= 1"""

"""sayi1, sayi2, sayi3 = int(input("Lütfen bir sayı girin: ")), int(input("Lütfen bir sayı daha girin: ")), int(input("Lütfen bir sayı daha girin: "))

liste = [sayi1, sayi2, sayi3]
liste.sort()
i = 0

while i < len(liste):
    print(liste[i])
    i += 1"""

"""urunSayisi = int(input("Lütfen kaç ürün gireceğinizi yazın: "))

urunler = {}

i = 0
while i < urunSayisi:
    urunAdi = input("Lütfen ürün adını girin: ")
    urunFiyati = int(input("Lütfen ürün fiyatını girin: "))
    urunler[urunAdi] = urunFiyati
    i += 1

i = 0
while i  < urunSayisi:  

    urun = list(urunler.keys())[i]
    urunFiyati = urunler[urun]
    print(f"{urun}: {urunFiyati} TL'dir")
    i += 1"""

liste = {"elma": 3, "armut": 4, "muz": 5, "çilek": 7}

print(f"Ürünlerimiz:  {', '.join(liste.keys())} ")