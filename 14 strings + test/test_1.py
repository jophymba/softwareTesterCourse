palindrom = input("Zadej palindrom: \n")
opak = palindrom[::-1]
if opak == palindrom:
    print("Ano, je to palindrom")
else:
    print("Ne, není to palindrom")    