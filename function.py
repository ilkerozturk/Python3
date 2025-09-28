"""def sayHello(name = "There!"):
    print("Hello" + ", " + name)  

sayHello()
# This function prints "Hello, World!" to the console."""
"""
def total(num1,num2):
    return num1 + num2  

print(total(int(input("Enter first number: ")), int(input("Enter second number: "))))

# This function takes two numbers as input and returns their sum."""


import datetime

def yasHesapla(dogumYili):
    return datetime.datetime.now().year - dogumYili

print(yasHesapla(int(input("Doğum yılınızı giriniz: "))))
# This function calculates the age based on the birth year provided by the user.    