print("zadej cilso:")
b = int(input())
if (b == 6):
    print( b, "je stejne cislo jako 6")
elif(b > 6):
    print( b, "je vetsi cislo nez 6")    
else:
    print(b, "je mensi cislo nez 6")    



print("zadej cislo mezi 10 a 20 nebo 30 a 40")
a = int(input())    
if (a >= 10 and a<= 20) or(a >= 30 and a <= 40):
    print("spravne")
else:
    print("nespravne")    