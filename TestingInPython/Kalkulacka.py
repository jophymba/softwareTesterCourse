class Kalkulacka:
     def secti(self, a, b):
          return a + b
     
     def odecti(self, a, b):
          return a - b
     
     def vynasob(self, a, b):
          return a * b

     def vydel(self, a, b):
          if b == 0:
               raise ValueError("Nelze delit nulou")
          return a / b 