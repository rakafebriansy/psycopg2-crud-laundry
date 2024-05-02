from services import dashboard, paket, karyawan, transaksi
import os


def main():
    while True:
        dashboard.menuDashboard()
        menu = input("Pilih menu: ")
        match menu:
            case "1":
                transaksi.buatTransaksi()
            case "2":
                transaksi.lihatTransaksi()
            case "3":
                aksi = paket.menuPaket()
                paket.paket(aksi)
            case "4":
                aksi = karyawan.menuKaryawan()
                karyawan.karyawan(aksi)
            case "0":
                break

if __name__ == "__main__":
    main()
    
