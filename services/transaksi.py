import os
import repository.transaksi as repoTransaksi
import repository.paket as repoPaket
import repository.karyawan as repoKaryawan
import datetime

def lihatTransaksi() -> None:
    os.system("cls")
    print("LIHAT TRANSAKSI")
    df_transaksi = repoTransaksi.findAll()
    print(df_transaksi)
    input("\nKlik apapun untuk melanjutkan.")
def buatTransaksi() -> bool:
    os.system("cls")
    print("BUAT TRANSAKSI")
    print("Masukkan data dibawah!\n")
    nama_pelanggan = input("Nama pelanggan: ")
    no_telp_pelanggan = input("Nomor telepon pelanggan: ")
    df_paket = repoPaket.findAll()
    print(df_paket)
    paket = input("Id paket: ")
    df_karyawan = repoKaryawan.findAll()
    print(df_karyawan)
    karyawan = input("Id karyawan: ")
    id_paket, id_karyawan = repoKaryawan.findOne(paket)[0], repoKaryawan.findOne(karyawan)[0]
    request = {
        'tanggal_transaksi': datetime.datetime.today(),
        'nama_pelanggan':nama_pelanggan,
        'no_telp_pelanggan':no_telp_pelanggan,
        'id_paket':id_paket,
        'id_karyawan':id_karyawan,
    }
    result = repoTransaksi.create(request)
    if(result):
        print("TRANSAKSI BERHASIL DIBUAT!\n")
    else:
        print("TRANSAKSI GAGAL DIBUAT\n")
    exit()
