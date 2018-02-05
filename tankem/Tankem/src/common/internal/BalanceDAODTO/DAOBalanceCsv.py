# -*- coding: utf-8 -*-
from DAOBalance import DAOBalance
from DTOBalance import DTObalance
import csv

class DAOBalanceCsv(DAOBalance):
	def read(self,csvfile):
		DTO = DTObalance()
		with open(csvfile) as csvfile :
			reader = csv.DictReader(csvfile,delimiter=";")
			for row in reader:
				print(row['Name'], row['Value'])
				if((row['Value'] != "TANKEM_VALUES") and row['Value']!= ""):
					DTO.setValue((row['Name']),float(row['Value']))
				else:
					DTO.setValue((row['Name']),row['Value'])
		return DTO

	def update(self, file, dto):
		DTO = dto.getDictionary()
		with open(file,"wb") as csvfile :
			csvwriter = csv.writer(csvfile,delimiter=";")
			csvwriter.writerow(["Name","Value"])
			for key, value in DTO.iteritems():
				csvwriter.writerow([key,value])