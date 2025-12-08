class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def _vykresli(self):
        """
        Vykreslí začátek textu.
        """
        self._vycisti_obrazovku()
        print("-------------- Aréna -------------- \n")
        print("Zdraví bojovníků: \n")
        print("{0} {1}".format(self._bojovnik_1,
                               self._bojovnik_1.graficky_zivot()))
        print("{0} {1}".format(self._bojovnik_2,
                               self._bojovnik_2.graficky_zivot()))

    def _vycisti_obrazovku(self):
        """
        Vymaže obrazovku konzole.
        """
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])

    def _vypis_zpravu(self, zprava):
        """
        Vypíše zprávu se zpožděním.
        """
        import time as _time
        print(zprava)
        _time.sleep(0.1)

    def zapas(self):
        """
        Simuluje zápas bojovníků.
        """
        import random as _random
        print("Vítejte v aréně!")
        print("Dnes se utkají {0} s {1}!".format(self._bojovnik_1,
                                                 self._bojovnik_2))
        print("Zápas může začít...", end=" ")
        input()
        # prohození bojovníků
        if _random.randint(0, 1):
            (self._bojovnik_1, self._bojovnik_2) = (self._bojovnik_2,
             self._bojovnik_1)
        # cyklus s bojem
        while (self._bojovnik_1.je_nazivu() and self._bojovnik_2.je_nazivu()):
            self._bojovnik_1.utoc(self._bojovnik_2)
            self._vykresli()
            self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())
            self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
            if self._bojovnik_2.je_nazivu():
                self._bojovnik_2.utoc(self._bojovnik_1)
                self._vykresli()
                self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
                self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())
            print("")