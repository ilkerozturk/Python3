import random

sayi = random.randint(1, 100)
print("1 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misin?")

hak = int(input("Kaç hak kullanmak istersiniz? "))

for i in range(hak):
    tahmin = int(input("Tahmininizi girin: "))
    
    if tahmin < sayi:
        print("Daha yüksek bir sayı söyleyin.")
    elif tahmin > sayi:
        print("Daha düşük bir sayı söyleyin.")
    else:
        print(f"Tebrikler! {i+1}. denemede doğru tahmin ettiniz.")
        break
else:
    print(f"Üzgünüm, hakkınız bitti. Doğru sayı {sayi} idi.")  

# Bu kod, kullanıcıya belirli sayıda tahmin hakkı vererek rastgele seçilen bir sayıyı bulmasını sağlar.

