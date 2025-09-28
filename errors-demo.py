
# Hataları yakalamak için try-except blokları kullanılır.

"""liste = ["1", "2", "3", "4a", "a5", "6", "7", "8", "9b"]

liste2 = []

for i in liste:
    try:
        liste2.append(int(i))
    except ValueError:
        print(f"{i} sayıya dönüştürülemedi.")
    
print(f"İşlem tamamlandı: {liste2}")"""

# Kullanıcı "q" girerse döngüden çıkılır. Ancak girdi sayı değilse hata mesajı verilir.

while True:
    sayi = input("Bir sayı girin (çıkmak için 'q'): ")
    if sayi.lower() == 'q':
        print("Çıkılıyor...")
        break
    try:
        sayi = int(sayi)
        print(f"Girdiğiniz sayı: {sayi}")
    except ValueError:
        print("Geçersiz giriş, lütfen bir sayı girin.")