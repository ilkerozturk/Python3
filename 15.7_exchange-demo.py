import requests
import json

api_key = "9a0e6f73111785ac73acb3c5" 
api_address = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

bozParaBirimi = input("Lütfen bozdurmak istediğiniz para birimini giriniz (Örneğin: EUR, USD, TRY): ").upper()
anaParaBirimi = input("Lütfen çevirmek istediğiniz para birimini giriniz (Örneğin: EUR, USD, TRY): ").upper()
miktar = float(input(f"Lütfen bozdurmak istediğiniz miktarı {bozParaBirimi} cinsinden giriniz: "))

api_address = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{bozParaBirimi}"


requests.get(api_address)
response = requests.get(api_address)  
data = response.json()  


if data['result'] == 'success':
    oran = data['conversion_rates'][anaParaBirimi]
    print(f"{miktar} {bozParaBirimi} = {miktar * oran} {anaParaBirimi} olarak çevrildi.")
else:
    print("Hata: Geçersiz para birimi veya API hatası.")