print("Program zjistí, z čeho se skládá věta.")
zadana_veta = input("Zadejte větu: ")

# Převedeme větu na malá písmena. Původní větu si ponecháme v proměnné zadana_veta beze změny
veta = zadana_veta.lower()

#  Nastavíme výchozí počty proměnných
samohlasky = 0
souhlasky = 0
ostatni = 0
cisel = 0

#  Definujeme sady typů znaků
samohlasky_sada = "aáeéěiíoóuúůyý"
souhlasky_sada = "bcčdďfghjklmnňpqrřsštťvwxzž"
cisla_sada = "0123456789"

#  V hlavním cyklu programu analyzujeme druh a počet znaků
for znak in veta:
    if znak in samohlasky_sada:      # Nejprve samohlásky
        samohlasky += 1
    elif znak in souhlasky_sada:     # Pak souhlásky
        souhlasky += 1
    elif znak in cisla_sada:         # Poté čísla
        cisel += 1
    else:
        ostatni += 1        # Vše, co zbylo, jsou ostatní znaky (mezery, tečky atd...)

# Zde využijeme původní nezměněnou větu
print(f'Vaše věta: "{zadana_veta}" má:')
print("samohlásek:", samohlasky)
print("souhlásek:", souhlasky)
print("čísel:", cisel)
print("ostatních znaků:", ostatni)

input("\nAplikaci ukončíte stisknutím klávesy Enter...")