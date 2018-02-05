# -*- coding: utf-8 -*-
from DTOStatsArme import DTOStatsArme

class DTOStats():
    # def __init__(self, idJoueur1, idJoueur2, idGagnant, idNiveau):
    def __init__(self):
        self.idJoueur1 = None
        self.nonJ1 = None
        self.nomJ2 = None
        self.idJoueur2 = None
        self.idGagnant = None
        self.idNiveau = None
        self.expJ1avantPartie = None
        self.expJ2avantPartie = None
        self.lvlJ1avantPartie = None
        self.lvlJ2avantPartie = None
        self.expJ1apresPartie = None
        self.expJ2apresPartie = None
        self.lvlJ1apresPartie = None
        self.lvlJ2apresPartie = None
        # self.idJoueur1 = idJoueur1
        # self.idJoueur2 = idJoueur2
        # self.idGagnant = None
        # self.idNiveau = idNiveau
        self.DTOStatsArmeJ1 = []
        self.DTOStatsArmeJ2 = []
        for i in range(6):
            self.DTOStatsArmeJ1.append(DTOStatsArme(i+1, 0))
            self.DTOStatsArmeJ2.append(DTOStatsArme(i+1, 0))
