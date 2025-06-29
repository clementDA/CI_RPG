from src.character_type.character import modele_character

class monstre(modele_character):
    def __init__(self, nom, race, elite=False):
        super().__init__(nom, race)
        self.elite = elite

    def mise_au_rang(self, multiplicateur):
        if not isinstance(multiplicateur, int) or multiplicateur <= 0:
            raise ValueError("Le multiplicateur doit être un entier positif.")

        self.attaque += (2*multiplicateur)
        self.defense += (2*multiplicateur)
        if self.elite:
            self.pv_max += multiplicateur * 80
        else:
            self.pv_max += multiplicateur * 4
        self.pv = self.pv_max
