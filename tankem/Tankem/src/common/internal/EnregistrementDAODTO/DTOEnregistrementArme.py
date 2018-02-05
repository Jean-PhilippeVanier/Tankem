#-*- coding: utf-8 -*-
class DTOenregistrementArme:
    def __init__(self, time_sec, pos_x, pos_y, type_arme):
        self.time_sec = time_sec
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.type_arme = type_arme

    def getTime(self):
        return self.time_sec

    def getX(self):
        return self.pos_x

    def getY(self):
        return self.pos_y

    def getType(self):
        return self.type_arme
