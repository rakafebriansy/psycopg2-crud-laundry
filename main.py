from services import dashboard, paket
import os


def main():
    while True:
        dashboard.setDashboard()
        menu = input("Pilih menu: ")
        match menu:
            case "1":
                print()
            case "2":
                print()
            case "3":
                aksi = paket.setPaket()
                paket.paket(aksi)
            case "5":
                break

if __name__ == "__main__":
    main()
    
