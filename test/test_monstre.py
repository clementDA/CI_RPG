import unittest
from src.character_type.monstre import monstre

class TestMonstre(unittest.TestCase):

    def test_initialisation_monstre_normal(self):
        gobelin = monstre("Bzog", "Gobelin")
        self.assertFalse(gobelin.elite)
        self.assertEqual(gobelin.pv_max, 10)
        self.assertEqual(gobelin.attaque, 1)
        self.assertEqual(gobelin.defense, 0)

    def test_initialisation_monstre_elite(self):
        dragon = monstre("Smaug", "Dragon", elite=True)
        self.assertTrue(dragon.elite)

    def test_mise_au_rang_non_elite(self):
        orc = monstre("Kraztet", "Orc", elite=False)
        orc.mise_au_rang(2)
        self.assertEqual(orc.attaque, 5) 
        self.assertEqual(orc.defense, 4)  
        self.assertEqual(orc.pv_max, 18)
        self.assertEqual(orc.pv, 18)  


    def test_mise_au_rang_elite(self):
        unogre = monstre("Mangtruc", "Ogre", elite=True)
        unogre.mise_au_rang(2)
        self.assertEqual(unogre.attaque, 5) 
        self.assertEqual(unogre.defense, 4) 
        self.assertEqual(unogre.pv_max, 26)
        self.assertEqual(unogre.pv, 26)  

if __name__ == '__main__':
    unittest.main()
