from DTOStats import DTOStats
from SingletonDBConnection import SingletonDBConnection
import cx_Oracle


class DAOStats():

	def __init__(self):
		self.connection = SingletonDBConnection().getConnection()

	def create(self, DTOStats):
		cur = self.connection.cursor()
		#insert les infos de la partie
		statement = "INSERT INTO partie(IdJoueur1, IdJoueur2, IdNiveau, IdGagnant) VALUES(:1, :2, :3, :4)"
		result = cur.execute(statement, (DTOStats.idJoueur1, DTOStats.idJoueur2, DTOStats.idNiveau, DTOStats.idGagnant))
		self.connection.commit()
		# print("insert into partie done!")

		#recup l'id de la partie
		result2 = cur.execute("SELECT MAX(Id) FROM partie")
		for i in result2:
			idPartie = i[0]

		try:
			#insert les Stats des armes
			for i in range(6):
				#StatsArmesJ1
				statement = "INSERT INTO joueur_arme_partie(IdPartie, IdJoueur, IdArme, NbFoisUtilArme) VALUES(:1, :2, :3, :4)"
				cur.execute(statement, (idPartie, DTOStats.idJoueur1, DTOStats.DTOStatsArmeJ1[i].idArme, DTOStats.DTOStatsArmeJ1[i].nbUtil))
				#StatsArmesJ2
				statement = "INSERT INTO joueur_arme_partie(IdPartie, IdJoueur, IdArme, NbFoisUtilArme) VALUES(:1, :2, :3, :4)"
				cur.execute(statement, (idPartie, DTOStats.idJoueur2, DTOStats.DTOStatsArmeJ2[i].idArme, DTOStats.DTOStatsArmeJ2[i].nbUtil))
			self.connection.commit()
			# print"insert into joueur_arme_partie done"
		except cx_Oracle.DatabaseError as e:
			error, = e.args
			print("Erreur d'insert")
			print(error.code)
			print(error.message)
			print(error.context)


	def update(self, DTOStats, addedExp1, addedExp2):
		cur = self.connection.cursor()


		#recup des usernames
		result = cur.execute("SELECT username FROM joueur where ID=:1", (str(DTOStats.idJoueur1)))
		for i in result:
			DTOStats.nomJ1 = i[0]
		result = cur.execute("SELECT username FROM joueur where ID=:1", (str(DTOStats.idJoueur2)))
		for i in result:
			DTOStats.nomJ2 = i[0]

		#recup de l'exp
		result = cur.execute("SELECT experience FROM joueur where ID=:1", (str(DTOStats.idJoueur1)))
		for i in result:
			exp1 = i[0]

		result = cur.execute("SELECT experience FROM joueur where ID=:1", (str(DTOStats.idJoueur2)))
		for i in result:
			exp2 = i[0]

		#ajoute l'expavantPartie dans le DTO
		DTOStats.expJ1avantPartie = exp1
		DTOStats.expJ2avantPartie = exp2


		#ajoute 100 si gagnant pas favori
		if(DTOStats.idGagnant == DTOStats.idJoueur1 and exp1<exp2):
			exp1 += 100
			print "J1 non favori"
		if(DTOStats.idGagnant == DTOStats.idJoueur2 and exp2<exp1):
			exp2 += 100
			print "J2 non favori"

		#update l'experience
		exp1 += addedExp1
		exp2 += addedExp2
		result = cur.execute("UPDATE joueur SET experience = :1 WHERE ID=:2", (exp1, DTOStats.idJoueur1))
		result = cur.execute("UPDATE joueur SET experience = :1 WHERE ID=:2", (exp2, DTOStats.idJoueur2))
		self.connection.commit()
		# print("experience updated")

		#ajoute l'exp apres partie dans DTOStats
		DTOStats.expJ1apresPartie = exp1
		DTOStats.expJ2apresPartie = exp2

		#recupere le niveau
		result = cur.execute("SELECT niveau FROM joueur where ID=:1", (str(DTOStats.idJoueur1)))
		for i in result:
			lvlP1 = i[0]

		result = cur.execute("SELECT niveau FROM joueur where ID=:1", (str(DTOStats.idJoueur2)))
		for i in result:
			lvlP2 = i[0]

		#ajoute niveau dans DTOStats
		DTOStats.lvlJ1avantPartie = lvlP1
		DTOStats.lvlJ2avantPartie = lvlP2

		#calcul le niveau
		seuilInfLvlP1 = 0
		seuilInfLvlP2 = 0
		if(lvlP1 > 0):
			seuilInfLvlP1 = 100*(lvlP1)+50*((lvlP1-1)*(lvlP1-1))
		if(lvlP2 > 0):
			seuilInfLvlP2 = 100*(lvlP2)+50*((lvlP2-1)*(lvlP2-1))

		while(exp1 > seuilInfLvlP1):
			lvlP1 +=1
			seuilInfLvlP1 = 100*(lvlP1)+50*((lvlP1-1)*(lvlP1-1))
			exp1 = exp1 - seuilInfLvlP1
			# print("experienceRestante1: "+str(exp1))

		while(exp2 > seuilInfLvlP2):
			lvlP2 +=1
			seuilInfLvlP2 = 100*(lvlP2)+50*((lvlP2-1)*(lvlP2-1))
			exp2 = exp2 - seuilInfLvlP2
			# print("experienceRestante2: "+str(exp2))

		DTOStats.lvlJ1apresPartie = lvlP1
		DTOStats.lvlJ2apresPartie = lvlP2

		result = cur.execute("UPDATE joueur SET niveau = :1 WHERE ID=:2", (lvlP1, DTOStats.idJoueur1))
		result = cur.execute("UPDATE joueur SET niveau = :1 WHERE ID=:2", (lvlP2, DTOStats.idJoueur2))
		self.connection.commit()
		# print"levels updated"


		#update des stats de la table joueur(parties gagnees/jouees):
		if(DTOStats.idGagnant == DTOStats.idJoueur1):
			result = cur.execute("UPDATE joueur SET partieGagne = partieGagne+1, partieJoue = partieJoue+1 WHERE ID=:1", (str(DTOStats.idJoueur1)))
			result = cur.execute("UPDATE joueur SET partieJoue = partieJoue+1 WHERE ID=:1", (str(DTOStats.idJoueur2)))
		else:
			result = cur.execute("UPDATE joueur SET partieJoue = partieJoue+1 WHERE ID=:1", (str(DTOStats.idJoueur1)))
			result = cur.execute("UPDATE joueur SET partieGagne = partieGagne+1, partieJoue = partieJoue+1 WHERE ID=:1", (str(DTOStats.idJoueur2)))
		self.connection.commit()
		# print "stats nbParties Jouees/gagnees updated"

		SingletonDBConnection().closeConnection()








