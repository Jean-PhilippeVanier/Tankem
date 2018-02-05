# -*- coding: utf-8 -*-
class DTOlistmap:

	# Constructor
	def __init__(self):
		self.array_maps = []

	# Getters
	def appendList(self, DTOmap):
		self.array_maps.append(DTOmap)

	def getArrayMaps(self):
		return self.array_maps

	def getMap(self, id):
		for map in self.array_maps:
			if(map.getId() == id):
				return map
