class Bojovnik:
    """
    Třída reprezentující bojovníka do arény.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        """
        jmeno - jméno bojovníka
        zivot - maximální život bojovníka
        utok - útok bojovníka
        obrana - obrana bojovníka
        kostka - instance kostky
        """
        self._jmeno = jmeno
        self._zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = kostka
        self._zprava = ""

    def __str__(self):
        """
        Vrátí jméno bojovníka.
        """
        return str(self._jmeno)

    def __repr__(self):
        """
        Vrací v řetězci kód konstruktoru pro funkci eval().
        """
        return str("Bojovnik({0}, {1}, {2}, {3}, {4})".format(self._jmeno,
                                                              self._max_zivot,
                                                              self._utok,
                                                              self._obrana,
                                                              self._kostka))
    

    def je_nazivu(self):
        """
        Vrátí True, pokud je bojovník naživu.
        Jinak vrátí False.
        """
        return self._zivot > 0

    def graficky_zivot(self):
        """
        Vrátí řetězec s grafickým životem.
        """
        celkem = 20
        pocet = int(self._zivot / self._max_zivot * celkem)
        if (pocet == 0 and self.je_nazivu()):
            pocet = 1
        return "[{0}{1}]".format("#"*pocet, " "*(celkem-pocet))

    def bran_se(self, uder):
        """
        Simuluje bránění bojovníka.
        Parametr úder je velikost útoku nepřítele.
        """
        zraneni = uder - (self._obrana + self._kostka.hod())
        if zraneni > 0:
            zprava = "{0} utrpěl poškození {1} hp.".format(self._jmeno,
                                                            zraneni)
            self._zivot = self._zivot - zraneni
            if self._zivot < 0:
                self._zivot = 0
                zprava = zprava[:-1] + " a zemřel."
        else:
            zprava = "{0} odrazil útok.".format(self._jmeno)
        self._nastav_zpravu(zprava)

    def utoc(self, souper):
        """
        Simuluje útok bojovníka.
        Parametr soupeř je instance druhého bojovníka.
        """
        uder = self._utok + self._kostka.hod()
        zprava = "{0} útočí s úderem za {1} hp.".format(self._jmeno, uder)
        self._nastav_zpravu(zprava)
        souper.bran_se(uder)
        

    def _nastav_zpravu(self, zprava):
        """
        Nastaví text zprávy.
        """
        self._zprava = zprava

    def vrat_posledni_zpravu(self):
        """
        Vrátí poslední zprávu.
        """
        return self._zprava