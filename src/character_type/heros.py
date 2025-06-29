from src.character_type.character import modele_character

class Heros(modele_character):
    def __init__(self, nom, race):
        super().__init__(nom, race)
        self.magie_max = 10
        self.magie = 10
        self.xp = 0
        self.niveau = 1

    def lvl_up(self):
        self.niveau += 1
        self.pv_max += 5
        self.attaque += 1
        self.defense += 1
        self.magie_max += 3
        self.magie +=3
        self.pv +=5
        self.xp = 0

    def lancer_sorts(self, cible ,cout_magie):
        if self.magie >= cout_magie:
            self.magie -= cout_magie
            degats = cout_magie - cible.defense
            if degats < 0:
                     degats = 0
            cible.pv -= degats
            return True
        else:
            return False
