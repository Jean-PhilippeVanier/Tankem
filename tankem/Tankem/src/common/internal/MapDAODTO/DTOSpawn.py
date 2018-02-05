# -*- coding: utf-8 -*-

class DTOspawn:

    # Constructor
    def __init__(self, pos_x, pos_y, id_niveau, no_player):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.id_niveau = id_niveau
        self.no_player = no_player 

    # Getters
    def getX (self):
        return self.pos_x

    def getY (self):
        return self.pos_y

    def getIdNiveau (self):
        return self.id_niveau

    def getNoPlayer (self):
        return self.no_player
