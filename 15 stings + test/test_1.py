print("Výpočet průměru známek")
print("Zadejte známky oddělené čárkou: ")

vstup = input()

oddeleni = vstup.split(",")
oddeleni = [int(x.strip()) for x in oddeleni]

prumer = sum(oddeleni) / len(oddeleni)

print("Průměr:", prumer)


