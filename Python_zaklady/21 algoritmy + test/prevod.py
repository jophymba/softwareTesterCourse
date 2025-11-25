znaky_soustavy = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cislo = int(input("Číslo v desítkové soustavě: \n").strip())

while True:
    ciselna_soustava = int(input("Číselná soustava (2-16): \n").strip())
    if ciselna_soustava in [2,16]:
        break
    else:
        print("Neplatná volba. Zadej pouze 2 nebo 16.")

vysledek = ""

match ciselna_soustava:
    case 2|16:
        while cislo > 0:
            zbytek = cislo % ciselna_soustava
            cislo = cislo //ciselna_soustava
            vysledek = str(znaky_soustavy[zbytek]) + vysledek

print(f"Číslo ve zvolené soustavě: {vysledek}")