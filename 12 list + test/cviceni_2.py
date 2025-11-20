cisla = [2, 9, 1, 4, 2, 3, 3]

print(cisla, "cely seznam")

# zobrazeni male casti seznamu

print(cisla[0], "jedna polozka")

print(cisla[0:3], "polozka od do")

print(cisla[5:], "polozky od 5 a vyse")

print(cisla[::-1], "vsehny polozky prevracene")

cisla.insert(0, 1)
print(cisla, "vlozi cislo 1")

cisla.append(33)
print(cisla, "vlozi cislo 33 na konec")

cisla.remove(33)
print(cisla, "vymaze cislo 33")

dalsi_cisla = [44, 56]
cisla.extend(dalsi_cisla)

cisla.count(2)
print(cisla, "spocita mnozstvi cisla 2")

cisla.reverse()
print(cisla, "vypise prevracene")




# zde jsou funkce =========

a = min(cisla)
print(a, 'vypise minimalni hodnotu')

b = sum(cisla)
print(b, "secte vsechna cisla")

c = sorted(cisla)
print(c, "srovna dle cisel a abecedy")

e = len(cisla)
print(e, "spocita pocet polozek")




# seznam s funkci range ====

range_cisla = list(range(0,11))

print(range_cisla)

# vypsani cisel ze seznamu

for cislo in range_cisla:
    print(cislo, end = " ")

print()
# uprava obsahu seznamu


for i in range(len(range_cisla)):
    range_cisla[i] += 2
print(range_cisla)   


# seznamy s hodnotou string

uzivatel = ["Bilbo", "Pytlik", "10.7.1875" , "0858676767"]
print(uzivatel)

print(uzivatel[0:2])

for i in uzivatel:
    print(i, end= " ")

print()    
 # seznam vypis s pomoci enumerate   

for i, polozka in enumerate(uzivatel):
    print(i, polozka)

