# -*- coding: utf-8 -*-
class DTOmap:

	# Constructor
	def __init__(self, id_niveau, name, creation_date, status,
				 size_x, size_y, item_delay_min, item_delay_max):

		self.id_niveau = id_niveau
		self.name = name
		self.creation_date = creation_date
		self.status = status
		self.size_x = size_x
		self.size_y = size_y
		self.item_delay_min = item_delay_min
		self.item_delay_max = item_delay_max
		self.array_tuiles = []
		self.array_spawns = []

	# Append arrays
	def appendTuile(self,DTOtuile):
		self.array_tuiles.append(DTOtuile)

	def appendSpawn(self,DTOspawn):
		self.array_spawns.append(DTOspawn)

	# Getters

	def getId(self):
		return self.id_niveau

	def getName(self):
		return self.name

	def getDate(self):
		return self.creation_date

	def getStatus(self):
		return self.status

	def getSizeX(self):
		return self.size_x

	def getSizeY(self):
		return self.size_y

	def getItemDelayMin(self):
		return self.item_delay_min

	def getItemDelayMax(self):
		return self.item_delay_max

	def getArrayTuiles(self):
		return self.array_tuiles

	def getArraySpawns(self):
		return self.array_spawns
