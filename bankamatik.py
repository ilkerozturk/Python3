hesapAdı = {
    "355355": {
        "ad": "Ahmet Yılmaz",
        "hesap_sifre": "123456",
        "bakiye": 4500.75,
        "ekhesap": 1000.00,
        "para_birimi": "TRY",
    },
    "458458": {
        "ad": "Ayşe Demir",
        "hesap_sifre": "123456",
        "bakiye": 5500.00,
        "ekhesap": 2500.00,
        "para_birimi": "TRY",
    }
}


def bakiye_goster(hesapNo):
    hesap = hesapAdı.get(hesapNo)
    hesapSifreDogrula = input("Hesap Şifrenizi Giriniz: ")
    if hesap and hesap["hesap_sifre"] == hesapSifreDogrula:
        print(f"Hesap Sahibi: {hesap['ad']}")
        print(f"Bakiye: {hesap['bakiye']} {hesap['para_birimi']}")
        print(f"Ek Hesap: {hesap['ekhesap']} {hesap['para_birimi']}")
        islem = input("Para çekmek ister misiniz? (E/H): ").upper()
        if islem == 'E':
            miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))
            para_cek(hesapNo, miktar)
        else:
            print("İşlem sonlandırıldı.")
    else:
        print("Hesap bulunamadı.")

def para_cek(hesapNo, miktar):
    hesap = hesapAdı.get(hesapNo)
    if hesap and miktar > 0:
        toplam_bakiye = hesap["bakiye"] + hesap["ekhesap"]
        if miktar <= toplam_bakiye:
            if miktar <= hesap["bakiye"]:
                hesap["bakiye"] -= miktar
            else:
                islem_mesaji = input("Yetersiz bakiye. Ek hesaptan kullanmak ister misiniz? (E/H): ").upper()
                if islem_mesaji != 'E':
                    print("İşlem sonlandırıldı.")
                    return
                ekhesap_kullanimi = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekhesap"] -= ekhesap_kullanimi
            print(f"{miktar} {hesap['para_birimi']} çekildi. Yeni bakiye: {hesap['bakiye']} {hesap['para_birimi']}, Ek Hesap: {hesap['ekhesap']} {hesap['para_birimi']}")
        else:
            print("Yetersiz bakiye.")
    else:
        print("Geçersiz işlem.")

hesapNoDogrula = input("Hesap Numaranızı Giriniz: ")
bakiye_goster(hesapNoDogrula)
