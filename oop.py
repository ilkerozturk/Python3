#Object Oriented Programming (OOP)

# Sınıf Tanımlama => Person (name, surname, year)
import datetime


class Person:

    address = "No information"  # Sınıf Özelliği (Class Attribute)

    # Yapıcı Metot (Constructor)
    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.year = year
    #class içinde fonksiyon tanımlama

# Obje Oluşturma

    def intro(self):
        print("Hello There! I am " + self.name + " " + self.surname + " and I am " + str(self.calculateAge()) + " years old.")

    def calculateAge(self, currentYear= datetime.datetime.now().year):
        return currentYear - self.year


p1 = Person("Ali", "Tok", 1990)
p2 = Person("Ayşe", "Arıman", 1995)  

# Obje Özelliklerine Erişim

#print(f"{p1.name} {p1.surname} {p1.year}'yılında doğdu. Adres: {p1.address}")


# Yeni Class Örneği
class Circle:   
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        

    def circumference(self):
        return 2 * self.radius * Circle.pi
    
    def area(self):
        return self.pi * (self.radius ** 2)
    

daire = input("Dairenin yarıçapını giriniz:(cm) ")


c1 = Circle()

c1.radius = float(daire)

print(f"Yarıçapı {c1.radius} 'cm olan dairenin çevresi: {c1.circumference()} cm'dir.")
print(f"Yarıçapı {c1.radius} 'cm olan dairenin alanı: {c1.area()} cm²'dir.")