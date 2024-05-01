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
                os.system('cls')
                paket.setPaket()
                aksi = input()
                paket.paket(aksi)
            case "5":
                break



if __name__ == "__main__":
    main()
    
