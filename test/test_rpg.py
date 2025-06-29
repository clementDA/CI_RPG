import unittest
from src.character_type.character import modele_character

class TestRpg(unittest.TestCase):
    def test_true_equals_true(self):
        self.assertTrue(True)

        import unittest

class TestPersonnage(unittest.TestCase):

    def test_initialisation_char(self):
        p = modele_character("Robert","Homme")
        self.assertEqual(p.race, "Homme")
        self.assertEqual(p.pv, 10)
        self.assertEqual(p.pv_max, 10)
        self.assertEqual(p.attaque, 1)
        self.assertEqual(p.defense, 0)

    def test_attaque_char(self):
        attaquant =modele_character("Gork","orc")
        defenseur =modele_character("Roland","humain")
        attaquant.frappe(defenseur)
        self.assertEqual(defenseur.pv,9)

    def test_soin_char(self):
        blesse =modele_character("patient","humain")
        blesse.pv -= 5
        blesse.soin("full")
        self.assertEqual(blesse.pv,10)

    def test_soin_char(self):
        blesse =modele_character("patient","humain")
        blesse.pv -= 5
        blesse.soin(2)
        self.assertEqual(blesse.pv,7)


if __name__ == '__main__':
    unittest.main()



