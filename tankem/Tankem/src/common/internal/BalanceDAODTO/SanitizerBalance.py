# -*- coding: utf-8 -*-
# from itertools import *
import itertools
from DTOBalance import DTObalance

class SanitizerBalance():
    #####
    # Constructeur

    def __init__(self, dtoValues, feedback, rewrite):
        self.dtoValues = dtoValues
        self.feedback = feedback
        self.rewrite = rewrite

        # Constantes
        self.keysList = self.initKeysList()
        self.dtoMin = self.initDtoMin()
        self.dtoMax = self.initDtoMax()

    #####
    # Init Hardcoded shizzles

    # KeysList
    def initKeysList(self):
        tmpList = []

        tmpList.append("vitesse_char")
        tmpList.append("vitesse_rotation")
        tmpList.append("vie")
        tmpList.append("temps_mouvement_blocs")
        tmpList.append("canon_vitesse_balle")
        tmpList.append("canon_reload")
        tmpList.append("mitraillette_vitesse_balle")
        tmpList.append("mitraillette_reload")
        tmpList.append("grenade_vitesse_balle")
        tmpList.append("grenade_reload")
        tmpList.append("shotgun_vitesse_balle")
        tmpList.append("shotgun_reload")
        tmpList.append("shotgun_spread")
        tmpList.append("piege_vitesse_balle")
        tmpList.append("piege_reload")
        tmpList.append("missile_vitesse_balle")
        tmpList.append("missile_reload")
        tmpList.append("spring_vitesse_saut")
        tmpList.append("spring_reload")
        tmpList.append("rayon_explosion")
        tmpList.append("message_acceuil_duree")
        tmpList.append("message_countdown_duree")

        return tmpList

    # DTO Min
    def initDtoMin(self):
        tmpDTO = DTObalance()
        minList = []

        # initMinList
        minList.append(4)    # vitesse_char
        minList.append(1000) # vitesse_rotation
        minList.append(100)  # vie
        minList.append(0.2)  # temps_mouvement_blocs
        minList.append(4)    # canon_vitesse_balle
        minList.append(0.2)  # canon_reload
        minList.append(4)    # mitraillette_vitesse_balle
        minList.append(0.2)  # mitraillette_reload
        minList.append(10)   # grenade_vitesse_balle
        minList.append(0.2)  # grenade_reload
        minList.append(4)    # shotgun_vitesse_balle
        minList.append(0.2)  # shotgun_reload
        minList.append(0.1)  # shotgun_spread
        minList.append(0.2)  # piege_vitesse_balle
        minList.append(0.2)  # piege_reload
        minList.append(20)   # missile_vitesse_balle
        minList.append(0.2)  # missile_reload
        minList.append(6)    # spring_vitesse_saut
        minList.append(0.2)  # spring_reload
        minList.append(1)    # rayon_explosion
        minList.append(1)    # message_acceuil_duree
        minList.append(0)    # message_countdown_duree

        # init tmpDTO
        for key,min in itertools.izip(self.keysList, minList):
            tmpDTO.setValue(key,min)

        return tmpDTO

    # DTO max
    def initDtoMax(self):
        tmpDTO = DTObalance()
        maxList = []

        # initMaxList
        maxList.append(12)   # vitesse_char
        maxList.append(2000) # vitesse_rotation
        maxList.append(2000) # vie
        maxList.append(2)    # temps_mouvement_blocs
        maxList.append(30)   # canon_vitesse_balle
        maxList.append(10)   # canon_reload
        maxList.append(30)   # mitraillette_vitesse_balle
        maxList.append(10)   # mitraillette_reload
        maxList.append(25)   # grenade_vitesse_balle
        maxList.append(10)   # grenade_reload
        maxList.append(30)   # shotgun_vitesse_balle
        maxList.append(10)   # shotgun_reload
        maxList.append(1.5)  # shotgun_spread
        maxList.append(4)    # piege_vitesse_balle
        maxList.append(10)   # piege_reload
        maxList.append(40)   # missile_vitesse_balle
        maxList.append(10)   # missile_reload
        maxList.append(20)   # spring_vitesse_saut
        maxList.append(10)   # spring_reload
        maxList.append(30)   # rayon_explosion
        maxList.append(10)   # message_acceuil_duree
        maxList.append(10)   # message_countdown_duree

        # init tmpDTO
        for key,max in itertools.izip(self.keysList, maxList):
            tmpDTO.setValue(key,max)

        return tmpDTO

    #####
    # Verifie si les valeurs respectent les min/max

    def sanitizeDto(self):
        isValid = True
        for key in self.keysList:
            value = self.dtoValues.getValue(key)
            min = self.dtoMin.getValue(key)
            max = self.dtoMax.getValue(key)

            if(value < min):
                isValid = False
                if(self.feedback):
                    print key + " est en dessous du minimum " + str(value) + "/" + str(min)
                if(self.rewrite):
                   self.dtoValues.setValue(key,min)

            if(value > max):
                isValid = False
                if(self.feedback):
                    print key + " est au dessus du maximum " + str(value) + "/" + str(max)
                if(self.rewrite):
                   self.dtoValues.setValue(key,max)
                
        return isValid
