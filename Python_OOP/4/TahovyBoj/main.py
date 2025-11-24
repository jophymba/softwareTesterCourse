from bojovnik import Bojovnik
from kostka import Kostka

kostka = Kostka(10)
bojovnik = Bojovnik("Zalgoren", 100, 20, 10, kostka)
print("Život: {0}".format(bojovnik.graficky_zivot())) #test graficky_zivot()
#útok na našeho bojovníka
souper = Bojovnik("Shadow", 60, 18, 15, kostka)
souper.utoc(bojovnik)
print(souper.vrat_posledni_zpravu())
print(bojovnik.vrat_posledni_zpravu())
print("Život: {0}".format(bojovnik.graficky_zivot()))