print("Zadejte delší slovo: ")
delsi_slovo = input()

print("Zadejte kratší slovo: ")
kratsi_slovo = input()

a = (len(delsi_slovo))
b = (len(kratsi_slovo))

c = a - b

print("Slova se liší délkou o", c, "znaků")

# Druhý způsob řešení

print("Zadejte delší slovo: ")
delsi_slovo = input()

print("Zadejte kratší slovo: ")
kratsi_slovo = input()

delka_slov = len(delsi_slovo) - len(kratsi_slovo)
print(f"Slova se liší délkou o {delka_slov} znaků")