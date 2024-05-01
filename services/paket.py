import os
import repository.paket as repo

def setPaket() -> None:
    print("="*10)
    print("MENU PAKET")
    print("="*10)
    print("\nAKSI")
    print("1. Lihat Paket ")
    print("2. Tambah Paket")
    print("3. Edit Paket")
    print("4. Hapus Paket")

def paket(aksi:str):
    match aksi:
        case "1":
            print()
        case "2":
            os.system('cls')
            jenis_baru = input("Masukkan nama jenis paket: ")
            harga = input("Masukkan harga paket: ")
            request = {
                'jenis':jenis_baru,
                'harga':harga
                }
            result = repo.create(request)
            if(result):
                print("PAKET BERHASIL DITAMBAHKAN!")
            else:
                print("PAKET GAGAL DITAMBAHKAN")
        case "3":
            print()
        case _:
            print()