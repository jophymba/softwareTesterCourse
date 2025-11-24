from kalkulacka import Kalkulacka


kalkulacka = Kalkulacka()
print("Zadej 1. číslo: ", end="")
prvni = float(input())
kalkulacka.prvni = prvni
print("Zadej 2. číslo: ", end="")
druhe = float(input())
kalkulacka.druhe = druhe


print(f"Součet: {kalkulacka.scitani()}")
print(f"Rozdíl: {kalkulacka.odcitani()}")
print(f"Součin: {kalkulacka.nasobeni()}")
print(f"Podíl: {kalkulacka.deleni()}")