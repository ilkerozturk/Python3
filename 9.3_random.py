import random

result = random.random()  # 0.0 ile 1.0 arasında rastgele bir sayı üretir
print(f"{result:.2f}") # Virgülden sonra 2 basamak göster  

print("CODE BELOW!".center(50, "*") )

names = ['Ali', 'Veli', 'Ayşe', 'Fatma', 'Ahmet']   

random_name = random.choice(names)  # Listeden rastgele bir isim seçer
print(random_name)

random_names2 = names[random.randint(0, len(names)-1)]  # Listeden rastgele bir isim seçer
print(random_names2)


print("CODE BELOW!".center(50, "*") )