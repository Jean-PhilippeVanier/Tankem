from DAOMap import DAOmaporacle

dao = DAOmaporacle()
listemaps = dao.read()

for map in listemaps.getArrayMaps():
	print(map.getName())