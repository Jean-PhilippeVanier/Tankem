# -*- coding: utf-8 -*-

class DTOtuile:

    # Constructor
    def __init__(self, pos_x, pos_y, id_niveau, type_tuile, has_tree):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.id_niveau = id_niveau
        self.type_tuile = type_tuile
        self.has_tree = has_tree

    # Getters
    def getX (self):
        return self.pos_x

    def getY (self):
        return self.pos_y

    def getIdNiveau (self):
        return self.id_niveau

    def getType (self):
        return self.type_tuile

    def hasTree (self):
        return self.has_tree
