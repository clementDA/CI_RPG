import unittest
from src.character_type.character import modele_character
from src.character_type.heros import Heros

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

class TestHeros(unittest.TestCase):
    def test_initialisation_heros(self):
        chevalier = Heros("Perceval", "Humain")
        self.assertEqual(chevalier.race, "Humain")
        self.assertEqual(chevalier.pv, 10)
        self.assertEqual(chevalier.pv_max, 10)
        self.assertEqual(chevalier.attaque, 1)
        self.assertEqual(chevalier.defense, 0)
        self.assertEqual(chevalier.magie, 10)
        self.assertEqual(chevalier.magie_max, 10)
        self.assertEqual(chevalier.xp, 0)
        self.assertEqual(chevalier.niveau, 1)

    def test_lvl_up(self):
        chevalier = Heros("Ivain le chevalier au lion", "Humain")
        chevalier.lvl_up()
        self.assertEqual(chevalier.niveau, 2)
        self.assertEqual(chevalier.pv_max, 15)
        self.assertEqual(chevalier.pv, 15)
        self.assertEqual(chevalier.attaque, 2)
        self.assertEqual(chevalier.defense, 1)
        self.assertEqual(chevalier.magie_max, 13)
        self.assertEqual(chevalier.magie, 13)
        self.assertEqual(chevalier.xp, 0)

    def test_lancer_sorts_avec_magie(self):
        mage = Heros("Merlin", "Demi demon")
        cible = modele_character("Lancelot", "Traitre")
        cible.defense = 2
        cible.pv = 10
        succes = mage.lancer_sorts(cible, 5)
        self.assertTrue(succes)
        self.assertEqual(mage.magie, 5)
        self.assertEqual(cible.pv, 7) 

    def test_lancer_sorts_pas_assez_magie(self):
        mage = Heros("Merlin", "Demi demon")
        cible = modele_character("Bandit", "Humain")
        mage.magie = 3

        succes = mage.lancer_sorts(cible, 5)
        self.assertFalse(succes)
        self.assertEqual(mage.magie, 3) 
        self.assertEqual(cible.pv, 10)  

    def test_lancer_sorts_degats_pas_negatifs(self):
        morg = Heros("Morgane", "Fee")
        cible = modele_character("soldat", "humain")
        cible.defense = 10
        
        succes = morg.lancer_sorts(cible, 5) 
        self.assertTrue(succes)
        self.assertEqual(cible.pv, 10)



if __name__ == '__main__':
    unittest.main()



