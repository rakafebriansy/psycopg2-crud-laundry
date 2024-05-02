import os
import repository.paket as repo

def setPaket() -> None:
    os.system("cls")
    print("="*10)
    print("MENU PAKET")
    print("="*10)
    print("\nAKSI")
    print("1. Lihat Paket ")
    print("2. Tambah Paket")
    print("3. Edit Paket")
    print("4. Hapus Paket")
    aksi = input()
    return aksi

def paket(aksi:str):
    match aksi:
        case "1":
            os.system("cls")
            print("LIHAT DATA\n")
            df_paket = repo.findAll()
            print(df_paket)
            input('\nTekan apa saja untuk melanjutkan!')
        case "2":
            os.system("cls")
            print("TAMBAH DATA\n")
            jenis = input("Masukkan nama jenis paket: ")
            harga = input("Masukkan harga paket: ")
            request = {
                'jenis':jenis,
                'harga':harga
                }
            result = repo.create(request)
            os.system("cls")
            if(result):
                print("PAKET BERHASIL DITAMBAHKAN!\n")
            else:
                print("PAKET GAGAL DITAMBAHKAN\n")
        case "3":
            os.system("cls")
            print("UBAH DATA\n")
            df_paket = repo.findAll()
            print(df_paket)
            column_name = input("Masukkan nama kolom: ")
            id = input("Masukkan id baris: ")
            new_value = input("Masukkan baru: ")
            result = repo.edit(column_name, new_value, id)
        case "4":
            os.system("cls")
            print("HAPUS DATA\n")
            df_paket = repo.findAll()
            print(df_paket)
            id = input("Masukkan id baris: ")
            result = repo.delete(id)
        case _:
            os.system("cls")
            print("Pilihan tidak tersedia!")
            input("Klik apapun untuk melanjutkan.")