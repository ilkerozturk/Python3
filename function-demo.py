"""def write(arg):
    sayi = int(input("Kaç kere yazdırmak istersiniz: "))
    for i in range(sayi):
        print(arg)

write("Merhaba Dünya")"""

"""def liste(*argm):
    list = []
    for i in argm:
        list.append(i)
    print(list)

liste(1,2,3,4,5,6,7,8,9)"""

"""def asal(argm):
    for sayi in argm:
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i) == 0:
                    
                    break
            else:
                print(sayi, "asal sayıdır")
    

asal(range(1,100))"""

sayi = int(input("Bir sayı giriniz: "))

def tambolen(sayi):  
    for i in range(1, sayi + 1):
        if (sayi % i) == 0:
            print(i)
tambolen(sayi)