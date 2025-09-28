plakalar = {
    "34": {
        "şehir": "İstanbul",
        "plaka_kodu": 34,
        "nüfus": 15029231,
        "alan_kodu": [212, 216],
    },
    "06": {
        "şehir": "Ankara",
        "plaka_kodu": 6,
        "nüfus": 5663325,
        "alan_kodu": [312, 416],
    },
    "35": {
        "şehir": "İzmir",
        "plaka_kodu": 35,
        "nüfus": 4320519,
        "alan_kodu": [232],
    },
    "51": {
        "şehir": "Niğde",
        "plaka_kodu": 51,
        "nüfus": 365419,
        "alan_kodu": [388],
    },
    "16": {
        "şehir": "Bursa",
        "plaka_kodu": 16,
        "nüfus": 3056120,
        "alan_kodu": [224],
    },
    "01": {
        "şehir": "Adana",
        "plaka_kodu": 1,
        "nüfus": 2237940,
        "alan_kodu": [322],
    },
    "55": {
        "şehir": "Samsun",
        "plaka_kodu": 55,
        "nüfus": 1364627,
        "alan_kodu": [362],
    },
    "10": {
        "şehir": "Balıkesir",
        "plaka_kodu": 10,
        "nüfus": 1220613,
        "alan_kodu": [266],
    },
    "26": {
        "şehir": "Eskişehir",
        "plaka_kodu": 26,
        "nüfus": 887475,
        "alan_kodu": [222],
    },
    "52": {
        "şehir": "Ordu",
        "plaka_kodu": 52,
        "nüfus": 763190,
        "alan_kodu": [452],
    },
}

"""
print(plakalar["34"])      # "İstanbul"
print(plakalar["06"])     # 25
print(plakalar.get("35"))  # "İzmir"
print(plakalar.get("10"))  # "Balıkesir"    
print(plakalar.keys())     # Tüm anahtarları verir  
print(plakalar.values())   # Tüm değerleri verir
print(plakalar.items())    # Tüm anahtar ve değerleri verir
"""

result = f"İstanbulun plaka kodu: {plakalar['34']["plaka_kodu"]} Nüfusu: {plakalar['34']["nüfus"]} Alan kodları: {plakalar['34']["alan_kodu"]} 'dır."
print(result)
