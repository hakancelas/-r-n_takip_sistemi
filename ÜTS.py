# Ürün takip sistemi için gerekli modüller yüklendi.
# Bu sistemde yalnızca Python'un temel özellikleri kullanılacak.
import sys  # Programın çıkış yapmasını sağlamak için kullanılan bir modül.

# Ürün bilgilerini saklamak için bir sözlük (dictionary) oluşturuldu.
# Sözlük yapısı şu şekildedir:
# {
#    "urun_id": {"urun_adi": "Ürün Adı", "stok_adedi": 10, "fiyat": 99.99}
# }
urun_listesi = {}

# Yeni ürün eklemek için fonksiyon tanımlandı.
def urun_ekle():
    """
    Kullanıcının sisteme yeni bir ürün eklemesini sağlar.
    Ürün bilgileri kullanıcıdan alınır ve urun_listesi sözlüğüne kaydedilir.
    """
    print("\nYeni Ürün Ekle")  # Kullanıcıya bilgi verilir.
    
    # Ürün için benzersiz bir ID istenir.
    urun_id = input("Ürün ID'sini girin: ")  
    
    # Girilen ID'nin zaten mevcut olup olmadığını kontrol ediyoruz.
    if urun_id in urun_listesi:
        print("Bu ID'ye sahip bir ürün zaten mevcut! Lütfen başka bir ID girin.")
        return  # İşlemi iptal ederek ana menüye döneriz.

    # Kullanıcıdan ürün adı istenir.
    urun_adi = input("Ürün adını girin: ")  
    
    # Stok miktarını kontrol ederek, sayısal bir değer girmesi sağlanır.
    while True:
        try:
            stok_adedi = int(input("Stok adedini girin (sadece tam sayı): "))
            break  # Doğru bir değer girilirse döngüden çıkılır.
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")  # Geçersiz giriş durumunda uyarı verir.

    # Ürün fiyatını kontrol ederek, sayısal bir değer girmesi sağlanır.
    while True:
        try:
            fiyat = float(input("Ürün fiyatını girin (ör. 49.99): "))
            break  # Doğru bir değer girilirse döngüden çıkılır.
        except ValueError:
            print("Lütfen geçerli bir fiyat girin!")  # Geçersiz giriş durumunda uyarı verir.

    # Kullanıcının girdiği bilgiler sözlüğe eklenir.
    urun_listesi[urun_id] = {
        "urun_adi": urun_adi,
        "stok_adedi": stok_adedi,
        "fiyat": fiyat,
    }
    
    # Kullanıcıya işlemin başarılı olduğu bilgisi verilir.
    print(f"Ürün '{urun_adi}' başarıyla eklendi! (ID: {urun_id})")

# Mevcut ürünleri güncellemek için fonksiyon tanımlandı.
def urun_guncelle():
    """
    Mevcut bir ürünün bilgilerini günceller.
    Kullanıcı, yalnızca değiştirmek istediği alanları güncelleyebilir.
    """
    print("\nÜrün Güncelle")
    
    # Kullanıcıdan güncellenecek ürünün ID'si istenir.
    urun_id = input("Güncellemek istediğiniz ürünün ID'sini girin: ")
    
    # Girilen ID'nin var olup olmadığını kontrol ederiz.
    if urun_id not in urun_listesi:
        print("Bu ID'ye sahip bir ürün bulunamadı!")
        return  # İşlemi iptal ederek ana menüye döneriz.

    # Mevcut ürün bilgileri kullanıcıya gösterilir.
    print(f"Mevcut ürün bilgileri: {urun_listesi[urun_id]}")

    # Kullanıcıdan yeni ürün adı istenir. Boş bırakılırsa eski değer korunur.
    urun_adi = input("Yeni ürün adını girin (boş bırakmak için Enter'a basın): ")
    
    # Stok miktarını güncellemek için giriş kontrolü yapılır.
    while True:
        stok_adedi = input("Yeni stok adedini girin (boş bırakmak için Enter'a basın): ")
        if stok_adedi == "":  # Kullanıcı boş bırakırsa döngüden çıkarız.
            break
        try:
            stok_adedi = int(stok_adedi)
            break
        except ValueError:
            print("Lütfen geçerli bir stok adedi girin!")

    # Ürün fiyatını güncellemek için giriş kontrolü yapılır.
    while True:
        fiyat = input("Yeni fiyatı girin (boş bırakmak için Enter'a basın): ")
        if fiyat == "":  # Kullanıcı boş bırakırsa döngüden çıkarız.
            break
        try:
            fiyat = float(fiyat)
            break
        except ValueError:
            print("Lütfen geçerli bir fiyat girin!")

    # Kullanıcı boş bırakmadıysa, ilgili alanlar güncellenir.
    if urun_adi:
        urun_listesi[urun_id]["urun_adi"] = urun_adi
    if stok_adedi != "":
        urun_listesi[urun_id]["stok_adedi"] = stok_adedi
    if fiyat != "":
        urun_listesi[urun_id]["fiyat"] = fiyat

    print("Ürün başarıyla güncellendi!")  # Kullanıcıya bilgi verilir.

# Ürün silmek için fonksiyon tanımlandı.
def urun_sil():
    """
    Kullanıcının bir ürünü sistemden tamamen silmesini sağlar.
    """
    print("\nÜrün Sil")
    
    # Kullanıcıdan silinecek ürünün ID'si istenir.
    urun_id = input("Silmek istediğiniz ürünün ID'sini girin: ")
    
    # Girilen ID'nin var olup olmadığını kontrol ederiz.
    if urun_id in urun_listesi:
        # Sözlükten ürün silinir.
        del urun_listesi[urun_id]
        print("Ürün başarıyla silindi!")
    else:
        print("Bu ID'ye sahip bir ürün bulunamadı!")

# Tüm ürünleri listelemek için fonksiyon tanımlandı.
def urunleri_listele():
    """
    Sistemdeki tüm ürünleri kullanıcıya listeler.
    """
    print("\nÜrün Listesi")
    
    # Eğer ürün listesi boşsa, kullanıcıya bilgi verilir.
    if not urun_listesi:
        print("Hiç ürün bulunmamaktadır.")
        return

    # Tüm ürünler bir döngü ile listelenir.
    for urun_id, bilgiler in urun_listesi.items():
        print(f"ID: {urun_id}, Ad: {bilgiler['urun_adi']}, "
              f"Stok: {bilgiler['stok_adedi']}, Fiyat: {bilgiler['fiyat']} TL")

# Ana menü fonksiyonu
def ana_menu():
    """
    Kullanıcıya bir menü sunar ve seçime göre işlemleri gerçekleştirir.
    """
    while True:
        # Ana menü seçeneklerini ekrana yazdırır.
        print("\nÜrün Takip Sistemi")
        print("1. Ürün Ekle")
        print("2. Ürün Güncelle")
        print("3. Ürün Sil")
        print("4. Ürünleri Listele")
        print("5. Çıkış")

        # Kullanıcıdan seçim yapılması istenir.
        secim = input("Bir seçenek girin (1-5): ")

        # Seçime göre ilgili işlemleri gerçekleştirir.
        if secim == "1":
            urun_ekle()
        elif secim == "2":
            urun_guncelle()
        elif secim == "3":
            urun_sil()
        elif secim == "4":
            urunleri_listele()
        elif secim == "5":
            print("Çıkış yapılıyor...")
            sys.exit()  # Programı sonlandırır.
        else:
            print("Geçersiz bir seçenek girdiniz! Lütfen tekrar deneyin.")

# Programın başlangıç noktası.
if __name__ == "__main__":
    ana_menu()
