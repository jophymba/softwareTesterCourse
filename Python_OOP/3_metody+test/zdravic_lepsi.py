class Zdravic:
     """
     Trida reprezentuje zdravic, zdravi uzivatele
     """
     text = "Ahoj"
     """
     Atribut obsahujici vychozi text. Pokud neni specifikovan jiny pouzije se tento
     """
     def pozdrav(self, jmeno):
          return f"{self.text} {jmeno}"

zdravic = Zdravic()
zdravic.text = "Ahoj uzivateli"
zdravic.pozdrav("Karel")
zdravic.pozdrav("Petr")
zdravic.text = "Vitam te programatore"
zdravic.pozdrav("Richard")