#-*- coding: utf-8 -*-
class DTOenregistrementPartie:
    def __init__(self, idMap, idJoueur1, idJoueur2, creation_date):
        self.idMap = idMap
        self.idJoueur1 = idJoueur1
        self.idJoueur2 = idJoueur2
        self.creation_date = creation_date
        self.array_joueur1 = []
        self.array_joueur2 = []
        self.array_arme = []
        self.array_projectile = []

    def appendJoueur1(self,DTOenregistrementJoueur):
        self.array_joueur1.append(DTOenregistrementJoueur)

    def appendJoueur2(self,DTOenregistrementJoueur):
        self.array_joueur2.append(DTOenregistrementJoueur)

    def appendArme(self,DTOenregistrementArme):
        self.array_arme.append(DTOenregistrementArme)

    def appendProjectile(self, DTOenregistrementProjectile):
        self.array_projectile.append(DTOenregistrementProjectile)


    def getIdMap(self):
        return self.idMap

    def getIdJ1(self):
        return self.idJoueur1

    def getIdJ2(self):
        return self.idJoueur2

    def getDate(self):
        return self.creation_date

    def getArrayJoueur1(self):
        return self.array_joueur1

    def getArrayJoueur2(self):
        return self.array_joueur2

    def getArrayArme(self):
        return self.array_arme

    def getArrayProjectile(self):
        return self.array_projectile
