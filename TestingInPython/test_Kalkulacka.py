from unittest import TestCase

from Kalkulacka import Kalkulacka

class TestKalkulacka(TestCase):
    def setUp(self):
        self.kalkulacka = Kalkulacka()

    def test_scitani(self):
        self.assertEqual(2, self.kalkulacka.secti(1, 1))
        self.assertAlmostEqual(1.42, self.kalkulacka.secti(3.14, -1.72), places=3)
        self.assertAlmostEqual(2.0 / 3, self.kalkulacka.secti(1.0 / 3, 1.0 / 3), places=3)

    def test_odcitani(self):
        self.assertEqual(0, self.kalkulacka.odecti(1, 1))
        self.assertAlmostEqual(4.86, self.kalkulacka.odecti(3.14, -1.72), places=3)
        self.assertAlmostEqual(2.0 / 3, self.kalkulacka.odecti(1.0 / 3, -1.0 / 3), places=3)
        self.assertFalse(2 == 8)

    def test_nasobeni(self):
        self.assertEqual(2, self.kalkulacka.vynasob(1, 2))
        self.assertAlmostEqual(-5.4008, self.kalkulacka.vynasob(3.14, -1.72), places=4)
        self.assertAlmostEqual(0.111, self.kalkulacka.vynasob(1.0 / 3, 1.0 / 3), places=3)

    def test_deleni(self):
        self.assertEqual(2, self.kalkulacka.vydel(4, 2))
        self.assertAlmostEqual(-1.826, self.kalkulacka.vydel(3.14, -1.72), places=3)
        self.assertEqual(1, self.kalkulacka.vydel(1.0 / 3, 1.0 / 3))

    def test_deleni_vyjimka(self):
        with self.assertRaises(ValueError):
            self.kalkulacka.vydel(2, 0)