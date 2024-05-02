import os
import repository.karyawan as repo

def menuKaryawan() -> None:
    os.system("cls")
    print("="*10)
    print("MENU KARYAWAN")
    print("="*10)
    print("\nAKSI")
    print("1. Lihat Karyawan ")
    print("2. Tambah Karyawan")
    print("3. Edit Karyawan")
    print("4. Hapus Karyawan")
    aksi = input()
    return aksi

def karyawan(aksi:str):
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
            nama = input("Masukkan nama karyawan: ")
            no_telp = input("Masukkan nomor telepon karyawan: ")
            request = {
                'nama':nama,
                'no_telp':no_telp
                }
            result = repo.create(request)
            os.system("cls")
            if(result):
                print("KARYAWAN BERHASIL DITAMBAHKAN!\n")
            else:
                print("KARYAWAN GAGAL DITAMBAHKAN\n")
        case "3":
            os.system("cls")
            print("UBAH DATA\n")
            df_paket = repo.findAll()
            print(df_paket)
            column_name = input("Masukkan nama kolom: ")
            id = input("Masukkan id baris: ")
            new_value = input("Masukkan baru: ")
            request = {
                'column':column_name,
                'new_value':new_value,
                'id':id
            }
            result = repo.edit(request)
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