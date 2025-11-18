zelenina = ["zelí", "okurka", "rajče", "paprika", "ředkev", "mrkev", "brokolice"]
ovoce = ["jablko", "hruška", "pomeranč", "jahoda", "banán", "kiwi", "malina"]
a = 0
b = "ano"
while b == "ano":
   zapis =input("Zadej název libovolného ovoce nebo zeleniny:")
   if zapis in zelenina:
    print("Zadal jsi zeleninu")
   elif zapis in ovoce:
    print ("Zadal jsi ovoce")
   else: print ("Tvoje slovo nemám v seznamu")
   a +=1
   b = input("Přeješ si zadat další slovo? (ano/ne) ")
print("Zadal jsi", a, "slov")