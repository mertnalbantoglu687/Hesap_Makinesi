import random

son_ondalik_ayrac = None

def Sayı_Al(metin):
    global son_ondalik_ayrac

    sayi = input(metin)

    if "," in sayi:
        son_ondalik_ayrac = ","

    elif "." in sayi:
        son_ondalik_ayrac = "."

    sayi = sayi.replace(",", ".")

    return float(sayi)

def Binlik_Ayraç_Ekle(sayi, ondalik_ayrac, binlik_ayrac):
    if ondalik_ayrac in sayi:
        tam, ondalik = sayi.split(ondalik_ayrac)

    else:
        tam, ondalik = sayi, ""

    tam = tam[::-1]

    parcalar = [tam[i:i+3] for i in range(0, len(tam), 3)]

    tam = binlik_ayrac.join(parcalar)[::-1]

    if ondalik:
        return tam + ondalik_ayrac + ondalik

    else:
        return tam

def Sonucu_Yazdır(sonuc):
    global son_ondalik_ayrac

    if isinstance(sonuc, float):
        if sonuc.is_integer():
            sonuc = int(sonuc)
            sonuc = str(sonuc)

        else:
            sonuc = f"{sonuc:.10f}".rstrip("0").rstrip(".")

    else:
        sonuc = str(sonuc)

    if son_ondalik_ayrac == ",":
        ondalik = ","
        binlik = "."

    elif son_ondalik_ayrac == ".":
        ondalik = "."
        binlik = ","

    else:
        ondalik = None
        binlik = "."

    if ondalik:
        sonuc = sonuc.replace(".", ondalik)

    sonuc = Binlik_Ayraç_Ekle(
        sonuc,
        ondalik if ondalik else ".",
        binlik
    )

    print("=", sonuc)

print(" ")

while True:
    virgul_sayisi = 0

    nokta_sayisi = 0

    secim = input(
        "Toplama: 1\n"
        "Çıkarma: 2\n"
        "Çarpma: 3\n"
        "Bölme: 4\n"
        "Üs Alma: 5\n"
        "Karekök: 6\n"
        "Çıkış: 7\n\n"
        "Lütfen bir sayı seçiniz(1/2/3/4/5/6/7): "
    )

    print(" ")

    if secim == "1":
        sayi1 = Sayı_Al("Birinci sayı: ")
        print(" ")
        sayi2 = Sayı_Al("İkinci sayı: ")
        print(" ")
        print(sayi1, "+", sayi2, end=" ")
        Sonucu_Yazdır(sayi1 + sayi2)

    elif secim == "2":
        sayi1 = Sayı_Al("Birinci sayı: ")
        print(" ")
        sayi2 = Sayı_Al("İkinci sayı: ")
        print(" ")
        print(sayi1, "-", sayi2, end=" ")
        Sonucu_Yazdır(sayi1 - sayi2)

    elif secim == "3":
        sayi1 = Sayı_Al("Birinci sayı: ")
        print(" ")
        sayi2 = Sayı_Al("İkinci sayı: ")
        print(" ")
        print(sayi1, "x", sayi2, end=" ")
        Sonucu_Yazdır(sayi1 * sayi2)

    elif secim == "4":
        sayi1 = Sayı_Al("Birinci sayı: ")
        print(" ")
        sayi2 = Sayı_Al("İkinci sayı: ")
        print(" ")
        if sayi2 == 0:
            print("Bir sayı 0'a bölünemez.")

        else:
            print(sayi1, "÷", sayi2, end=" ")
            Sonucu_Yazdır(sayi1 / sayi2)

    elif secim == "5":
        sayi1 = Sayı_Al("Taban: ")

        print(" ")

        sayi2 = int(Sayı_Al("Üs: "))

        print(" ")

        if abs(sayi2) > 1000:
            print("Lütfen 1000'den küçük bir üs giriniz.")

        else:
            print(sayi1, "^", sayi2, end=" ")

            try:
                Sonucu_Yazdır(int(sayi1) ** sayi2)

            except OverflowError:
                print("Sonuç hesaplanılamadı.")

    elif secim == "6":
        sayi = Sayı_Al("Bir sayı giriniz: ")
        print(" ")
        if sayi < 0:
            print("Negatif sayıların karekökü alınamaz.")

        else:
            print("√(" + str(sayi) + ")", end=" ")
            Sonucu_Yazdır(sayi ** 0.5)

    elif secim == "7":
        print("Çıkış yapıldı.")
        print(" ")
        break

    else:
        print(" ")
        print("Böyle bir seçenek yok.")

    print(" ")
