"""input = input("Lütfen 0-100 arasında bir sayı girin:" )"""

"""if 0 <= int(input) <= 100:
    print("Geçerli bir sayı girdiniz.")
else:
    print("Geçersiz bir sayı girdiniz. Lütfen 0-100 arasında bir sayı girin.")"""

"""if int(input) %2 == 0 and 0 <= int(input) <= 100:
    print("Girilen sayı pozitif ve çift bir sayıdır.")
elif int(input) %2 != 0 and 0 <= int(input) <= 100:
    print("Girilen sayı pozitif ve tek bir sayıdır.")
else:
    print("Geçersiz bir sayı girdiniz. Lütfen 0-100 arasında bir sayı girin.")"""

"""eposta = "ilker.ozturk@btinteraktif.com"
parola = "123456"

girilen_eposta = input("Lütfen eposta adresinizi girin: ")
girilen_parola = input("Lütfen parolanızı girin: ") 

if girilen_eposta == eposta and girilen_parola == parola:
    print("Giriş başarılı.")
elif girilen_eposta != eposta and girilen_parola == parola:
    print("Eposta adresiniz yanlış.")
elif girilen_eposta == eposta and girilen_parola != parola:
    print("Parolanız yanlış.")
else:
    print("Eposta adresiniz ve parolanız yanlış.")  """

"""input1 = input("Lütfen 0-100 arasında bir sayı girin:" )
input2 = input("Lütfen 0-100 arasında bir sayı daha girin:" )
input3 = input("Lütfen 0-100 arasında bir sayı daha girin:" ) 

result = [int(input1), int(input2), int(input3)]
result.sort()
print("Girilen sayıların küçükten büyüğe sıralanmış hali:", result)"""

"""vize = int(input("Lütfen vize notunuzu girin: "))
final = int(input("Lütfen final notunuzu girin: ")) 
ortalama = vize * 0.6 + final * 0.4

if ortalama >= 50 and final >= 50:
    print("Tebrikler, dersi geçtiniz.")
elif ortalama >= 50 and final < 50:
    print("Final notunuz 50'den düşük olduğu için dersten kaldınız.")
elif final >= 70:
    print("Final notunuz 70 veya üzeri olduğu için dersten geçtiniz.")
else:
    print("Maalesef dersten kaldınız.")"""

"""Adınız = input("Lütfen adınızı girin: ")
kilonuz = float(input("Lütfen kilonuzu kg cinsinden girin: "))  
boyunuz = float(input("Lütfen boyunuzu metre cinsinden girin: "))  

result = kilonuz / (boyunuz ** 2)

if result <= 18.4:
    print(f"{Adınız}, vücut kitle indeksiniz {result:.2f} ve zayıfsınız.")
elif 18.5 <= result <= 24.9:
    print(f"{Adınız}, vücut kitle indeksiniz {result:.2f} ve kilonuz normal.")
elif 25 <= result <= 29.9:
    print(f"{Adınız}, vücut kitle indeksiniz {result:.2f} ve kilonuz fazla.")
elif 30 <= result <= 34.9:
    print(f"{Adınız}, vücut kitle indeksiniz {result:.2f} ve 1. derece obezsiniz.")
elif 35 <= result <= 44.9:
    print(f"{Adınız}, vücut kitle indeksiniz {result:.2f} ve 2. derece obezsiniz.")
else:
    print(f"{Adınız}, vücut kitle indeksiniz {result:.2f} ve 3. derece obezsiniz.") 
    """

