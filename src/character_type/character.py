class modele_character:

    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.pv_max = 10
        self.pv = 10
        self.attaque = 1
        self.defense = 0



    #montant est un nombre ou "full" pour un soin total
    def soin(self, montant):
      if montant == "full":
        self.pv = self.pv_max
      elif isinstance(montant, int):
        self.pv += montant
        if self.pv > self.pv_max:
            self.pv = self.pv_max
      else:
          raise ValueError("L'argument est invalide, entrez un nombre ou 'full'")



    #les pv sont baissé d'une valeur egale a l'attaque moins la defense adverse
    def frappe(self, defenseur):
        degats = self.attaque - defenseur.defense
        if degats < 0:
            degats = 0
        defenseur.pv -= degats
