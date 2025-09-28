#Range metodu

"""for i in range(1,100,2):
    print(i)
print("Bitti")  """

"""print(list(range(1,100,2)))"""

#enumerate metodu - index numarası ile birlikte listeleme yapar.

"""isim = "İlker Öztürk"

index = 0

for i in isim:
    print(f"{index} . indexteki harf : {i}")
    index += 1

"""

#zip metodu - iki listeyi birleştirir.

liste1 = [1,2,3,4,5] 
liste2 = ["a","b","c","d","e"]  

for i,j in zip(liste1,liste2):
    print(f"liste1 : {i} , liste2 : {j}")