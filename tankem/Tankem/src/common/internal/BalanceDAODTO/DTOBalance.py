# -*- coding: utf-8 -*-

class DTObalance:
    #####
    # Constructeur

    def __init__(self):
        self.values = {}

    # Ajouter une valeur au dictionnaire
    def setValue (self, key, value):
        key = key.upper()
        self.values[key] = value

    # Avoir une valeur dans le dictionnaire
    def getValue (self, key):
        key = key.upper()
        return self.values[key]

    def getDictionary (self):
        return self.values