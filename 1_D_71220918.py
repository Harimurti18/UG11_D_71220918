print("Halo selamat datang di bioskop!")

def xxi():
    print("Dimanakah kamu ingin menonton?")
    print("1) XXI Empire")
    print("2) XXI Amplaz")
    print("3) XXI JCM")
    a = int(input("Masukan pilihanmu: "))
    if a == 4:
        print("Pilihan tidak tersedia")

def film():
    print("Mau menonton film apa nih? Ada film:")
    print("1. Frozen")
    print("2. Keramat")
    print("3) KKN di Desa Penari")
    a = int(input("Pilih nomor film: "))
    if a == 4:
        print("Pilihan tidak tersedia")

def layar():
    print("Mau nonton layar bioskop apa:")
    print("1. Reguler")
    print("2. Dolby Almos")
    print("3. Premiere")
    a = int(input("Pilih nomor tipe layar: "))

def waktu():
    print("Mau nonton jam berapa:")
    print("1. 12.35")
    print("2. 14.45")
    print("3. 16.55")
    print("4. 19.05")
    a = int(input("Masukan angka pilihan anda: "))
    if a == 1:
        print("Oke berhasil!, silahkan dinikmati di jam",12.35)
    elif a == 2:
        print("Oke berhasil!, silahkan dinikmati di jam",14.45)
    elif a == 3:
        print("Oke berhasil!, silahkan dinikmati di jam",16.55)
    elif a == 4:
        print("Oke berhasil!, silahkan dinikmati di jam",19.05)
xxi()
film()
layar()
a = int(input("Berapa banyak tiket? "))
waktu()