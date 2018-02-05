# -*- coding:utf-8 -*-
class DTOJoueur:
	def __init__(self, idJoueur, username, name, surname, couleurTank,
				 password, email, banned, bannedStart, logCounter, 
				 niveau, experience, vie, force, agilite,
				 dexterite, partieJoue, partieGagne):
		self.idJoueur = idJoueur
		self.username = username
		self.name = name
		self.surname = surname
		self.couleurTank = couleurTank
		self.password = password
		self.email = email
		self.banned = banned
		self.bannedStart = bannedStart
		self.logCounter = logCounter
		self.niveau = niveau
		self.experience = experience
		self.vie = vie
		self.force = force
		self.agilite = agilite
		self.dexterite = dexterite
		self.partieJoue = partieJoue
		self.partiegagne = partieGagne

	def getId(self):
		return self.idJoueur

	def getUsername(self):
		return self.username

	def getStats(self):
		self.stats = []
		self.stats.append(self.vie)
		self.stats.append(self.force)
		self.stats.append(self.agilite)
		self.stats.append(self.dexterite)
		return self.stats