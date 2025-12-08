class Kostka:
    """
    Třída reprezentuje hrací kostku.
    """
    
    def __init__(self, pocet_sten=6):
        """
        pocet_sten - počet stěn kostky
        """
        self._pocet_sten = pocet_sten

    def __str__(self):
        """
        Vrací textovou reprezentaci kostky.
        """
        return str("Kostka s {0} stěnami".format(self._pocet_sten))

    def __repr__(self):
        """
        Vrací v řetězci kód konstruktoru pro funkci eval().
        """
        return str("Kostka({0})".format(self.__pocet_sten))

    def vrat_pocet_sten(self):
        return self.__pocet_sten

    def hod(self):
        """
        Vykoná hod kostkou a vrátí číslo od 1 do
        počtu stěn.
        """
        import random as _random
        return _random.randint(1, self._pocet_sten)