from abc import ABC
from datetime import datetime

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def jellemzok(self):
        return "Egyágyas szoba"
    
class KetagyasSzoba(Szoba):
    def jellemzok(self):
        return "Kétágyas szoba"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def hozzaad_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglal(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return szoba.ar
        return None

    
    def lemond(self, foglal):
        if foglal in self.foglalasok:
            self.foglalasok.remove(foglal)

    def listaz(self):
        print("Egyágyas szobák: 1, 2; Kétágyas szoba: 3.")
        for foglalas in self.foglalasok:
            print(f"A(z) {foglalas.datum} napon a(z) {foglalas.szoba.szobaszam}-s szoba foglalt!")

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

def main():
    #szoba létrehozása
    szalloda1 = Szalloda("Hotel Austrianski Pingwin & Bóbr") #meg lehet adni több szállodát is
    szobak = EgyagyasSzoba(1, "10.000 Ft/fő/éj"), EgyagyasSzoba(2, "10.000 Ft/fő/éj"), KetagyasSzoba(3, "15.000 Ft/fő/éj")
    for szoba in szobak:
        szalloda1.hozzaad_szoba(szoba)
    #foglalások
    meglevofoglalas = [(1, "2024-5-30"), (1, "2025-5-30"), (2, "2024-5-30"), (2, "2024-6-1"), (3, "2024-5-30")]
    for fogl in meglevofoglalas:
        szalloda1.foglal(fogl[0], fogl[1])
    #felh. interface
    print(f"Szia! Üdvözöllek a {szalloda1.nev} szobafoglalási rendszerében! \n")
    while True:
        print("Kérlek válassz a műveletek közül! \n 1. Foglalás \n 2. Foglalás lemondása \n 3. Foglalások megjelenítése \n 0. Kilépés \n")
        #Létrehozunk segédváltozókat:
        #segedvaltozo1: kiválasztott menü lehetőség
        #segedvaltozo2: lefoglalni kívánt szoba
        #segedvaltozo3: lefoglalni kívánt dátum
        segedvaltozo1 = input("Választott lehetőség: ")
        try:

            if segedvaltozo1 == "1":
                print("Egyágyas szobák: 1, 2 \nKétágyas szoba: 3 \n")
                segedvaltozo2 = int(input("Melyik szobát szeretnéd lefoglalni? Kérlek írd be a számát: "))
                if segedvaltozo2 == 1 or 2 or 3:
                    print("Szoba elmentve!")
                    datum = input("Kérlek add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
                    try:
                        segedvaltozo3 = datetime.strptime(datum, "%Y-%m-%d")
                        if segedvaltozo3 > datetime.now():
                            segedvaltozo3 = segedvaltozo3.strftime("%Y-%m-%d")
                            foglalas_sikeres = szalloda1.foglal(segedvaltozo2, segedvaltozo3)
                            print(f"Sikeres volt a foglalásod! Fizetendő összeg: {foglalas_sikeres}")
                        else:
                            print("Múltbéli időpontra nem lehet szobát foglalni.")
                    except ValueError:
                        print("Hibás dátum formátumot adtál meg!")
                else:
                    print("Nem létezik a megadott szoba, próbáld újra elérhető szoba számával!")

            elif segedvaltozo1 == "2":
                print("Jelenlegi foglalások:\n")
                szalloda1.listaz()
                lemond_szobaszam = int(input("Kérlek add meg a lemondani kívánt foglaláshoz tartozó szoba számát: "))
                lemond_datum = input("Kérlek add meg a lemondani kívánt foglalás időpontját (YYYY-MM-DD): ")

                lemondas_siker = None
                for foglal in szalloda1.foglalasok:
                    if foglal.szoba.szobaszam == lemond_szobaszam and foglal.datum == lemond_datum:
                        lemondas_siker = foglal
                        break
                if lemondas_siker:
                    szalloda1.lemond(lemondas_siker)
                    print("Foglalás sikeresen törölve.")
                else:
                    print("Nem található foglalás a megadott paraméterekkel.")

            elif segedvaltozo1 == "3":
                szalloda1.listaz()

            elif segedvaltozo1 == "0":
                print("Kilépés a programból...")
                break

            else:
                print("Nem található az általad választott lehetőség. :(")

        #általános hibakezelés
        except Exception as e:
            print("Sajnálom, hiba történt:\n", str(e), "\n:( Próbáld újra!")
            

main()


