import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}


    def loadUsers(self):
        if os.path.exists("/Users/ilkerozturk/Documents/Dev-Folder/Python3/Dersler/15.5_Json-Demo/library/users.json"):
            try:
                with open("/Users/ilkerozturk/Documents/Dev-Folder/Python3/Dersler/15.5_Json-Demo/library/users.json", "r", encoding="utf-8") as file:
                    users = json.load(file)
                    for user in users:
                        self.users.append(User(user["username"], user["password"], user["email"]))
                        print(f"Kullanıcı Adı: {user['username']}, Parola: {user['password']}, Email: {user['email']}")
            except FileNotFoundError:
                pass
        else:
            pass 
        
    def register(self, user: User):
        self.users.append(user)
        print("Kullanıcı oluşturuldu")
        self.savetoFile()

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Giriş başarılı")
                break
            else:
                print("Kullanıcı adı veya parola hatalı")
        pass
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Çıkış yapıldı")

    def identity(self):
        if self.isLoggedIn:
            print(f"Giriş Yapıldı - Kullanıcı Adı: {self.currentUser.username}, Email: {self.currentUser.email}")
        else:
            print("Giriş yapılmadı, lütfen giriş yapınız")

    def savetoFile(self):
        with open("/Users/ilkerozturk/Documents/Dev-Folder/Python3/Dersler/15.5_Json-Demo/library/users.json", "w", encoding="utf-8") as file:
            json.dump([user.__dict__ for user in self.users], file, ensure_ascii=False, indent=4)
            



userRepository = UserRepository()

while True:
    print("Menü".center(50,"*"))
    secim = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Identity\n6- Exit\nSeçiminiz: ")
    if secim == "6":
        break
    elif secim == "1":
        username = input("Kullanıcı Adı: ")
        password = input("Parola: ")
        email = input("Email: ")
        user = User(username, password, email)
        userRepository.register(user)
    elif secim == "2":
        username = input("Kullanıcı Adı: ")
        password = input("Parola: ")
        userRepository.login(username, password)
    elif secim == "3":
        userRepository.logout()
    elif secim == "4":
        userRepository.loadUsers()
    elif secim == "5":
        userRepository.identity()
    else:
        print("Geçersiz seçim")