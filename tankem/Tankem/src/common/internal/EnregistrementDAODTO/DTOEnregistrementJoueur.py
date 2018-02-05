#-*- coding: utf-8 -*-
class DTOenregistrementJoueur:
    def __init__(self, time_sec, pos_x, pos_y,orientation,health,ball_shot):
        self.time_sec = time_sec
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.orientation = orientation
        self.health = health
        self.ball_shot = ball_shot

    def getTime(self):
        return self.time_sec

    def getX(self):
        return self.pos_x

    def getY(self):
        return self.pos_y

    def getOrientation(self):
        return self.orientation

    def getHealth(self):
        return self.health

    def isBallShot(self):
        return self.ball_shot
