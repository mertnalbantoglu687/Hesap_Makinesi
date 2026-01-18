import random

virgul_sayisi = 0

nokta_sayisi = 0

def Sayı_Al(metin):
    global virgul_sayisi, nokta_sayisi
    sayi = input(metin)
    virgul_sayisi += sayi.count(",")
    nokta_sayisi += sayi.count(".")
    sayi = sayi.replace(",", ".")
    return float(sayi)

def Sonucu_Yazdır(sonuc):
    global virgul_sayisi, nokta_sayisi

    sonuc = str(sonuc)

    if virgul_sayisi > nokta_sayisi:
        sonuc = sonuc.replace(".", ",")

    elif virgul_sayisi < nokta_sayisi:
        sonuc = sonuc.replace(",", ".")

    else:
        if random.choice([True, False]):
            sonuc = sonuc.replace(".", ",")

        else:
            sonuc = sonuc.replace(",", ".")

    print("=", sonuc)

while True:
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
            print("Bir sayı sıfıra bölünemez.")

        else:
            print(sayi1, "÷", sayi2, end=" ")
            Sonucu_Yazdır(sayi1 / sayi2)

    elif secim == "5":
        sayi1 = Sayı_Al("Taban: ")
        print(" ")
        sayi2 = Sayı_Al("Üs: ")
        print(" ")
        print(sayi1, "^", sayi2, end=" ")
        Sonucu_Yazdır(sayi1 ** sayi2)

    elif secim == "6":
        sayi = Sayı_Al("Bir sayı giriniz: ")
        print(" ")
        if sayi < 0:
            print("Negatif sayının karekökü alınamaz.")

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
