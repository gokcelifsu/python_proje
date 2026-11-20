# Bankamatik (ATM) Uygulaması - 1. Hafta Mini Proje

class Kullanici:
    """Kullanıcı bilgilerini ve şifre doğrulamasını tutan sınıf."""
    def __init__(self, ad_soyad, pin_kodu):
        self.ad_soyad = ad_soyad
        self.pin_kodu = pin_kodu

    def pin_dogrula(self, girilen_pin):
        # Girilen şifrenin doğruluğunu kontrol eder
        return self.pin_kodu == girilen_pin


class BankaHesabi:
    """Bakiye, para yatırma ve çekme işlemlerini yöneten sınıf."""
    def __init__(self, kullanici, baslangic_bakiye=0):
        self.kullanici = kullanici
        self.bakiye = baslangic_bakiye

    def bakiye_goster(self):
        print(f"\nSayın {self.kullanici.ad_soyad}, güncel bakiyeniz: {self.bakiye} TL")

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Hata: Geçerli bir tutar giriniz.")

    def para_cek(self, miktar):
        if miktar <= 0:
            print("Hata: Geçerli bir tutar giriniz.")
        elif miktar > self.bakiye:
            print("Hata: Yetersiz bakiye!")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL")


def atm_baslat():
    """Ana program akışını ve kullanıcı menüsünü yöneten fonksiyon."""
    musteri = Kullanici("Gökçe Elif", "1234")
    hesap = BankaHesabi(musteri, 1500)

    print("=== TALOS BANK ATM'YE HOŞ GELDİNİZ ===")
    sifre = input("Lütfen 4 haneli PIN kodunuzu giriniz: ")

    if not musteri.pin_dogrula(sifre):
        print("Hatalı PIN! Kartınız güvenlik nedeniyle iade edildi.")
        return

    while True:
        print("\n--- İŞLEM MENÜSÜ ---")
        print("1. Bakiye Sorgula\n2. Para Yatır\n3. Para Çek\n4. Çıkış")
        secim = input("Seçiminiz (1-4): ")

        if secim == "1":
            hesap.bakiye_goster()
        elif secim == "2":
            tutar = float(input("Yatırılacak tutar: "))
            hesap.para_yatir(tutar)
        elif secim == "3":
            tutar = float(input("Çekilecek tutar: "))
            hesap.para_cek(tutar)
        elif secim == "4":
            print("Çıkış yapılıyor. İyi günler dileriz!")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")


# Programı çalıştır
atm_baslat()