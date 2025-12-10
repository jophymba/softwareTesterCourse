print("Zadej jméno: ")
jmeno = input()

print("Zadej příjmení: ")
prijmeni = input()

print("Zadej svůj věk: ")
vek = input()
vek = int(vek)

print(jmeno.upper() + " " + prijmeni.upper())
print("Za rok ti bude", vek + 1, "let.")

# druhy zpusob rešení

print("Zadej jméno: ")
jmeno = input()

print("Zadej příjmení: ")
prijmeni = input()

print("Zadej svůj věk: ")
vek = int(input())

print(f"{jmeno.upper()} {prijmeni.upper()}")

print(f"Za rok ti bude {vek + 1 } let.")