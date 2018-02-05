## -*- coding: utf-8 -*-
from util import *
from entity import *

from direct.showbase import DirectObject
from panda3d.core import *
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import YUp
from direct.interval.IntervalGlobal import *
import random
import common
from common.internal.EnregistrementDAODTO.DAOEnregistrementOracle import DAOenregistrementOracle
from common.internal.EnregistrementDAODTO.DTOEnregistrementJoueur import DTOenregistrementJoueur
from common.internal.EnregistrementDAODTO.DTOEnregistrementPartie import DTOenregistrementPartie
from common.internal.EnregistrementDAODTO.DTOEnregistrementProjectile import DTOenregistrementProjectile
from common.internal.EnregistrementDAODTO.DTOEnregistrementArme import DTOenregistrementArme
from direct.gui.OnscreenText import OnscreenText #pour pouvoir ecrire du texte
from direct.gui.DirectGui import *  #pour pouvoir creer les les autres GUI
import time
import webbrowser
DAOMap = common.internal.MapDAODTO.DAOMapOracle.DAOmaporacle()
DTOlistmap = DAOMap.read()
DTOStats = common.internal.DTOStats.DTOStats()
DAOStats = common.internal.DAOStats.DAOStats()

#Module qui sert à la création des maps
class Map(DirectObject.DirectObject):
	def __init__(self, mondePhysique, dtoValues, idJoueur1, idJoueur2):
		
		#On garde le monde physique en référence
		self.mondePhysique = mondePhysique
		self.idJoueur1 = idJoueur1
		self.idJoueur2 = idJoueur2


		#On prends les infos du dto
		self.dtoValues = dtoValues

		self.tabJoueurs = None

		#initialisation des constantes utiles
		self.map_nb_tuile_x = 12
		self.map_nb_tuile_y = 12
		self.map_grosseur_carre = 2.0 #dimension d'un carré
		self.map_petite_valeur_carre = 0.05 #Afin de contourner des problèmes d'affichage, on va parfois décaler les carrés/animations d'une petite valeur. Par exmeple, on ne veut pas que les cubes animés passent dans le plancher.

		#On veut que le monde soit centré. On calcul donc le décalage nécessaire des tuiles
		self.position_depart_x = - self.map_grosseur_carre * self.map_nb_tuile_x / 2.0
		self.position_depart_y = - self.map_grosseur_carre * self.map_nb_tuile_y / 2.0

		#On déclare des listes pour les tanks, les items et les balles
		# Inkonsistanseh REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE list/liste
		self.listTank = []
		self.listeItem = []
		self.listeBalle = []

		#Dictionnaire qui contient des noeuds animés.
		#On pourra attacher les objets de notre choix à animer
		self.dictNoeudAnimation = {}
		self.creerNoeudAnimationImmobile() #Pour être consistant, on créé une animation... qui ne bouge pas
		self.creerNoeudAnimationVerticale() #Animation des blocs qui bougent verticalement
		self.creerNoeudAnimationVerticaleInverse() #Idem, mais décalé

		#Création de l'objet qui génèrera des arbres pour nous
		self.treeOMatic  = treeMaker.TreeOMatic()

		#Initialise le contenu vide la carte
		#On y mettra les id selon ce qu'on met
		self.endroitDisponible = [[True for x in range(self.map_nb_tuile_y)] for x in range(self.map_nb_tuile_x)]

		#Message qui permettent la création d'objets pendant la partie
		self.accept("tirerCanon",self.tirerCanon)
		self.accept("tirerMitraillette",self.tirerMitraillette)
		self.accept("lancerGrenade",self.lancerGrenade)
		self.accept("lancerGuide",self.lancerGuide)
		self.accept("deposerPiege",self.deposerPiege)
		self.accept("tirerShotgun",self.tirerShotgun)

		# variables pour l'enregistrement
		self.tick = 0
		self.time = 0
		self.delai = 6
		self.saved = False
		self.DAOEnregistrement = DAOenregistrementOracle()
		self.isDTOStatsSaved = False

	def libererEndroitGrille(self,i,j,doitBloquer):
		#print "bloque " + str(i) + " " + str(j)
		self.endroitDisponible[i][j] = doitBloquer

	def figeObjetImmobile(self):
		self.noeudOptimisation.flattenStrong()

	def construireMapChoisie(self,DTOmap,tabJoueurs):
		self.tabJoueurs = tabJoueurs
		maze = mazeUtil.MazeBuilder(self.map_nb_tuile_y, self.map_nb_tuile_x)
		maze.build()
		mazeTuiles = DTOmap.getArrayTuiles()
		mazeSpawns = DTOmap.getArraySpawns()
		DTOStats.idNiveau = DTOmap.id_niveau
		DTOStats.idJoueur1 = self.idJoueur1
		DTOStats.idJoueur2 = self.idJoueur2

		self.dtoPartie = DTOenregistrementPartie(DTOmap.id_niveau, self.idJoueur1, self.idJoueur2, time.strftime("%d/%m/%Y"))

		for tuile in mazeTuiles:
			# Tuile mur
			if(tuile.getType() >= 2):
				if(tuile.getType() == 2):
					animation = "AnimationMurImmobile"
				elif(tuile.getType() == 3):
					animation = "AnimationMurVerticale"
				else:
					animation = "AnimationMurVerticaleInverse"
				
				if(tuile.hasTree() == 1):
					noeudAAttacher = Arbre(self.mondePhysique,self.treeOMatic)
				else:
					noeudAAttacher = None

				self.creerMur(tuile.getX(), tuile.getY(), animation, noeudAAttacher)
		couleurs = [0,0,0,0]
		couleurs[0] = Vec3(0.1,0.1,0.1)
		couleurs[1] = Vec3(0.6,0.0,0.0)
		couleurs[2] = Vec3(0.0,0.6,0.0)
		couleurs[3] = Vec3(0.0,0.0,0.6)
		for idx,spawn in enumerate(mazeSpawns):
			if(idx < len(tabJoueurs)):
				self.creerChar(spawn.getX(),spawn.getY(),spawn.getNoPlayer()-1,couleurs[spawn.getNoPlayer()-1],tabJoueurs[idx])
				# print("spawn.getNoPlayer()-1: " + str(spawn.getNoPlayer()-1) + "         tabJoueurs[idx]" + str(tabJoueurs[idx].idJoueur))
			else: #S'il y a plus de tanks que de joueurs, la création de char ne prendra pas l'info d'un joueur
				self.creerChar(spawn.getX(),spawn.getY(),spawn.getNoPlayer()-1,couleurs[spawn.getNoPlayer()-1],None)

		self.genererItemParInterval(DTOmap.getItemDelayMin(),DTOmap.getItemDelayMax())


	def construireMapHasard(self):
		self.dtoPartie = DTOenregistrementPartie(None,time.strftime("%d/%m/%Y"))
		#Utilisation du module de création au hasard
		#Le module a un x et y inversé!
		maze = mazeUtil.MazeBuilder(self.map_nb_tuile_y, self.map_nb_tuile_x)
		maze.build()
		mazeArray = maze.refine(.6)

		#Interprétation du résultat de l'algo
		for row in mazeArray:
			for cell in row:
				if(cell.type == 1):
					typeMur = random.randint(0, 100)
					#On créé des éléments!
					#40% du temps un mur immobile (5% de chance d'avoir un arbre)
					#5% du temps un arbre seul
					#18% du temps un mur mobile (5% de chance d'avoir un arbre)
					#17% du temps un mur mobile inverse (5% de chance d'avoir un arbre)
					if(typeMur <= 40):
						noeudAnimationDuMur = "AnimationMurVerticale" if typeMur <= 20 else "AnimationMurVerticaleInverse"
						noeudAAttacher = None if random.randint(0, 20) != 0 else Arbre(self.mondePhysique,self.treeOMatic)
						self.creerMur(cell.row, cell.col, noeudAnimationDuMur, noeudAAttacher)
					elif(typeMur <= 45):
						self.creerArbre(cell.row, cell.col)
					else:
						noeudAAttacher = None if random.randint(0, 20) != 0 else Arbre(self.mondePhysique,self.treeOMatic)
						self.creerMur(cell.row, cell.col,"AnimationMurImmobile",noeudAAttacher)

		self.creerChar(6,6,0,Vec3(0.1,0.1,0.1),None) #Char noir
		self.creerChar(3,3,1,Vec3(0.6,0.6,0.5),None) #Char gris-jaune

		#Dans la carte par défaut, des items vont appraître constamment entre 10 et 20 secondes d'interval
		self.genererItemParInterval(3,8)

	def construireDecor(self, camera):
		modele = loader.loadModel("../asset/Skybox/skybox")
		modele.set_bin("background", 0);
		modele.set_two_sided(True);
		modele.set_depth_write(False);
		modele.set_compass();
		verticalRandomAngle = random.randint(0,45)
		modele.setHpr(0,verticalRandomAngle,-90)
		randomGrayScale = random.uniform(0.6,1.2)
		semiRandomColor = Vec4(randomGrayScale,randomGrayScale,randomGrayScale,1)
		modele.setColorScale(semiRandomColor)
		modele.setPos(0,0,0.5)
		#Et oui! Le ciel est parenté à la caméra!
		modele.reparentTo(camera)

	def construirePlancher(self):
		#Optimisation... on attache les objets statiques au même noeud et on utiliser
		#la méthode flattenStrong() pour améliorer les performances.
		self.noeudOptimisation = NodePath('NoeudOptimisation')
		self.noeudOptimisation.reparentTo(render)

		#Construction du plancher
		# On charge les tuiles qui vont former le plancher
		for i in range(0,self.map_nb_tuile_x):
			for j in range(0,self.map_nb_tuile_y):
				modele = loader.loadModel("../asset/Floor/Floor")
				# Reparentage du modèle à la racine de la scène
				modele.reparentTo(self.noeudOptimisation)
				self.placerSurGrille(modele,i, j)

		#Construction du plancher si on tombe
		#Un plan devrait marche mais j'ai un bug de collision en continu...
		shape = BulletBoxShape(Vec3(50,50,5))
		node = BulletRigidBodyNode('Frontfiere sol')
		node.addShape(shape)
		np = render.attachNewNode(node)
		np.setTag("EntiteTankem","LimiteJeu")
		np.setPos(Vec3(0,0,-9.0))
		self.mondePhysique.attachRigidBody(node)

		#Construction de l'aire de jeu sur laquelle on joue
		shape = BulletBoxShape(Vec3(-self.position_depart_x, -self.position_depart_y, 2))
		node = BulletRigidBodyNode('Plancher')
		node.addShape(shape)
		np = render.attachNewNode(node)
		np.setTag("EntiteTankem","Plancher")
		HACK_VALUE = 0.02 #Optimisation de collision, les masques ne marchent pas
		np.setZ(-2.00 - HACK_VALUE)
		self.mondePhysique.attachRigidBody(node)


	def placerSurGrille(self,noeud,positionX, positionY):
		# On place l'objet en calculant sa position sur la grille
		noeud.setX(self.position_depart_x + (positionX+0.5) * self.map_grosseur_carre)
		noeud.setY(self.position_depart_y + (positionY+0.5) * self.map_grosseur_carre)

	def tirerCanon(self, identifiantLanceur, position, direction):
		#Création d'une balle de physique
		someBalle = balle.Balle(identifiantLanceur,self.mondePhysique,self.dtoValues)
		self.listeBalle.append(someBalle)
		someBalle.projetter(position,direction)

	def tirerMitraillette(self, identifiantLanceur, position, direction):
		#Création d'une balle de physique
		someBalle = balle.Balle(identifiantLanceur,self.mondePhysique,self.dtoValues)
		self.listeBalle.append(someBalle)
		someBalle.projetterRapide(position,direction)

	def lancerGrenade(self, identifiantLanceur, position, direction):
		#Création d'une balle de physique
		someBalle = balle.Balle(identifiantLanceur, self.mondePhysique,self.dtoValues)
		self.listeBalle.append(someBalle)
		someBalle.lancer(position,direction,self.dtoValues.getValue("GRENADE_VITESSE_BALLE"))

	def lancerGuide(self, identifiantLanceur, position, direction):
		#Création d'une balle de physique
		someBalle = balle.Balle(identifiantLanceur, self.mondePhysique,self.dtoValues)
		self.listeBalle.append(someBalle)

		#On définit la position d'arrivé de missile guidé
		noeudDestination = self.listTank[0].noeudPhysique
		if(identifiantLanceur == 0):
			noeudDestination = self.listTank[1].noeudPhysique

		someBalle.lancerGuide(position,noeudDestination)

	def deposerPiege(self, identifiantLanceur, position, direction):
		#Création d'une balle de physique
		someBalle = balle.Balle(identifiantLanceur, self.mondePhysique,self.dtoValues)
		self.listeBalle.append(someBalle)
		someBalle.deposer(position,direction)

	def tirerShotgun(self, identifiantLanceur, position, direction):
		#Création d'une balle de physique
		someBalle = balle.Balle(identifiantLanceur,self.mondePhysique,self.dtoValues)
		self.listeBalle.append(someBalle)
		someBalle.projetterVariable(position,direction)

	#####################################################
	#Création des différentes entités sur la carte
	#####################################################

	def creerItem(self, positionX, positionY, armeId):
		#L'index dans le tableau d'item coincide avec son
		#itemId. Ça va éviter une recherche inutile pendant l'éxécution
		itemCourrant = item.Item()
		self.listeItem.append(itemCourrant)
		#On place le tank sur la grille
		self.placerSurGrille(itemCourrant.noeudPhysique,positionX,positionY)
		self.libererEndroitGrille(positionX, positionY,False)
		itemCourrant.initialisationComplete(armeId,self.mondePhysique , lambda : self.libererEndroitGrille(positionX, positionY,True))

	def creerItemHasard(self, positionX, positionY):
		listeItem = ["Mitraillette", "Shotgun", "Piege", "Grenade", "Guide","Spring"]
		itemHasard = random.choice(listeItem)
		self.creerItem(positionX, positionY,itemHasard)

	def creerItemPositionHasard(self):
		#Pas de do while en Python! Beurk...
		randomX = random.randrange(0,self.map_nb_tuile_x)
		randomY = random.randrange(0,self.map_nb_tuile_y)

		#Tant qu'on trouve pas d'endroit disponibles...
		while(not self.endroitDisponible[randomX][randomY]):
			randomX = random.randrange(0,self.map_nb_tuile_x)
			randomY = random.randrange(0,self.map_nb_tuile_y)

		#Quand c'est fait on met un item au hasard
		self.creerItemHasard(randomX,randomY)

	def genererItemParInterval(self, delaiMinimum, delaiMaximum):
		#Délai au hasard entre les bornes
		delai = random.uniform(delaiMinimum, delaiMaximum)
		intervalDelai = Wait(delai)
		intervalCreerItem = Func(self.creerItemPositionHasard)
		intervalRecommence = Func(self.genererItemParInterval,delaiMinimum,delaiMaximum)

		sequenceCreation = Sequence(intervalDelai,
									intervalCreerItem,
									intervalRecommence,
									name="Creation item automatique")
		#On le joue une fois et il se rappelera lui-même :-)
		sequenceCreation.start()

	def creerMur(self,positionX, positionY, strAnimation = None, appendObject = None):
		mur = Wall(self.mondePhysique)
		#On place le bloc sur la grille
		if(appendObject != None):
			#Décale l'objet de 1 unité pour être SUR le mur et non dedans
			appendObject.noeudPhysique.setZ(appendObject.noeudPhysique.getZ() + 1.0)
			appendObject.noeudPhysique.reparentTo(mur.noeudPhysique)
		self.placerSurGrille(mur.noeudPhysique,positionX,positionY)
		self.libererEndroitGrille(positionX,positionY,False)

		if(strAnimation):
			mur.animate(self.dictNoeudAnimation[strAnimation])

	def creerArbre(self,positionX, positionY):
		arbre = Arbre(self.mondePhysique,self.treeOMatic)
		#On place le bloc sur la grille
		self.placerSurGrille(arbre.noeudPhysique,positionX,positionY)
		self.libererEndroitGrille(positionX,positionY,False)

	def creerNoeudAnimationImmobile(self):
		noeudAnimationCourrant = NodePath("AnimationMurImmobile")
		self.dictNoeudAnimation["AnimationMurImmobile"] = noeudAnimationCourrant
		noeudAnimationCourrant.reparentTo(render)

	def creerNoeudAnimationVerticale(self):
		#Création d'un noeud vide
		noeudAnimationCourrant = NodePath("AnimationMurVerticale")
		tempsMouvement = self.dtoValues.getValue("TEMPS_MOUVEMENT_BLOCS")
		blocPosInterval1 = LerpPosInterval( noeudAnimationCourrant,
											tempsMouvement,
											Vec3(0,0,-self.map_grosseur_carre + self.map_petite_valeur_carre),
											startPos=Vec3(0,0,0))
		blocPosInterval2 = LerpPosInterval( noeudAnimationCourrant,
											tempsMouvement,
											Vec3(0,0,0),
											startPos=Vec3(0,0,-self.map_grosseur_carre + self.map_petite_valeur_carre))
		delai = Wait(1.2)
		# On créé une séquence pour bouger le bloc
		mouvementBloc = Sequence()
		mouvementBloc = Sequence(   blocPosInterval1,
									delai,
									blocPosInterval2,
									delai,
									name="mouvement-bloc")

		mouvementBloc.loop()

		noeudAnimationCourrant.reparentTo(render)
		#Ajout dans le dicitonnaire de l'animation
		self.dictNoeudAnimation["AnimationMurVerticale"] = noeudAnimationCourrant

	def creerNoeudAnimationVerticaleInverse(self):
		#Création d'un noeud vide
		noeudAnimationCourrant = NodePath("AnimationMurVerticaleInverse")
		tempsMouvement = self.dtoValues.getValue("TEMPS_MOUVEMENT_BLOCS")
		blocPosInterval1 = LerpPosInterval( noeudAnimationCourrant,
											tempsMouvement,
											Vec3(0,0,-self.map_grosseur_carre + self.map_petite_valeur_carre),
											startPos=Vec3(0,0,0))
		blocPosInterval2 = LerpPosInterval( noeudAnimationCourrant,
											tempsMouvement,
											Vec3(0,0,0),
											startPos=Vec3(0,0,-self.map_grosseur_carre + self.map_petite_valeur_carre))
		delai = Wait(1.2)
		# On créé une séquence pour bouger le bloc
		mouvementBloc = Sequence()
		mouvementBloc = Sequence(   blocPosInterval2,
									delai,
									blocPosInterval1,
									delai,
									name="mouvement-bloc-inverse")
		mouvementBloc.loop()

		noeudAnimationCourrant.reparentTo(render)
		#Ajout dans le dicitonnaire de l'animation
		self.dictNoeudAnimation["AnimationMurVerticaleInverse"] = noeudAnimationCourrant


	def creerChar(self,positionX, positionY, identifiant, couleur, infosJoueur):
		###################### ajout de -1 a l'id, ca marche pas sinon i don't know why ##############################
		someTank = tank.Tank(identifiant,couleur,self.mondePhysique,self.dtoValues, DTOStats, infosJoueur)
		#On place le tank sur la grille
		self.placerSurGrille(someTank.noeudPhysique,positionX,positionY)

		#Ajouter le char dans la liste
		self.listTank.append(someTank)

	def traiterCollision(self,node0, node1):
		#Pas très propre mais enfin...
		indiceTank = int(self.traiterCollisionTankAvecObjet(node0, node1,"Balle"))
		if(indiceTank != -1):
			tireurBalleId = int(self.trouverTag(node0, node1, "lanceurId"))
			balleId = int(self.trouverTag(node0, node1, "balleId"))
			#Prend 1 de dommage par défaut si la balle n'a pas été tirée par le tank
			self.listeBalle[balleId].exploser()
			if(tireurBalleId != indiceTank):
				dommage = 1.0
				tankQuiTire = 0
				if(indiceTank == 0):
					tankQuiTire = 1
				if(self.tabJoueurs[tankQuiTire] is not None):
					#print "Degat avant : " + str(dommage)
					dommage = int(dommage) / 100.0 * (100 + 10 * int(self.tabJoueurs[tankQuiTire].force))
					#print "Degat modifié : " + str(dommage)
				self.listTank[indiceTank].prendDommage(dommage,self.mondePhysique)
			return
		
		indiceTank = int(self.traiterCollisionTankAvecObjet(node0, node1,"Item"))
		if(indiceTank != -1):
			itemID = int(self.trouverTag(node0, node1, "itemId"))
			if(itemID != -1):
				#Avertit l'item et le tank de la récupération
				itemCourrant = self.listeItem[itemID]
				#print "détecte item touché!!!!"
				itemCourrant.recupere()
				self.listTank[indiceTank].recupereItem(itemCourrant.armeId)
				return

		indiceTank = int(self.traiterCollisionTankAvecObjet(node0, node1,"LimiteJeu"))
		if(indiceTank != -1):
			#Un tank est tombé. mouhahahadddddddddd
			self.listTank[indiceTank].tombe(self.mondePhysique)
			return


	#Méthode qui va retourner -1 si aucune collision avec un tank
	#Ou encore l'index du tank touché si applicable
	def traiterCollisionTankAvecObjet(self,node0,node1,testEntite):
		tag0 = node0.getTag("EntiteTankem")
		tag1 = node1.getTag("EntiteTankem")
		retour = -1
		if(tag0 == "Tank" and tag1 == testEntite):
			#print node1
			retour = node0.getTag("IdTank")

		if(tag0 == testEntite and tag1 == "Tank"):
			retour = node1.getTag("IdTank")
		return retour

	#Trouve si un des 2 noeuds a le tag indiqué
	def trouverTag(self,node0, node1, tag):
		retour = ""
		#On trouve l'ID de l'item qui a collisionné
		if(node0.getTag(tag) != ""):
			retour = node0.getTag(tag)

		if(node1.getTag(tag) != ""):
			retour = node1.getTag(tag)

		return retour

	#On met à jour ce qui est nécessaire de mettre à jour
	def update(self,tempsTot):
		self.tick+=1
		if(self.listTank[0].pointDeVie <= 0 or self.listTank[1].pointDeVie <= 0):
			self.analyseFinPartie()
		

		for tank in self.listTank:
			tank.traiteMouvement(tempsTot)

		# Sauvegarde
		if(self.dtoPartie.getIdMap() is not None):
			if(self.tick == self.delai):
				self.tick = 0
				if(self.listTank[0].etat == "actif" and self.listTank[1].etat == "actif"):
					self.sauvegardeDTO()
					self.time+=1
				elif(self.listTank[0].pointDeVie <= 0 or self.listTank[1].pointDeVie <= 0):
					if(not self.saved):
						self.saved = True
						self.DAOEnregistrement.create(self.dtoPartie)

				if(self.time == 600):
					self.delai = 12
				elif(self.time == 900):
					self.delai = 24

	# On sauvegarde les info du temps X dans le DTOPartie
	def sauvegardeDTO(self):
		dtoJoueur1 = DTOenregistrementJoueur(self.time,
											  self.listTank[0].noeudPhysique.getPos()[0],
											  self.listTank[0].noeudPhysique.getPos()[1],
											  self.listTank[0].noeudPhysique.getHpr()[0],
											  self.listTank[0].pointDeVie,1)
		self.dtoPartie.appendJoueur1(dtoJoueur1)

		dtoJoueur2 = DTOenregistrementJoueur(self.time,
											  self.listTank[1].noeudPhysique.getPos()[0],
											  self.listTank[1].noeudPhysique.getPos()[1],
											  self.listTank[1].noeudPhysique.getHpr()[0],
											  self.listTank[1].pointDeVie,1)
		self.dtoPartie.appendJoueur2(dtoJoueur2)

		for balle in self.listeBalle:
			if(balle.etat is not "Detruit"):
				en_mouvement = 0
				if(balle.etat is "actif"):
					en_mouvement = 1

				dtoProjectile = DTOenregistrementProjectile(self.time,
															balle.noeudPhysique.getPos()[0],
															balle.noeudPhysique.getPos()[1],
															en_mouvement)
				self.dtoPartie.appendProjectile(dtoProjectile)

		for arme in self.listeItem:
			if(arme.etat is not "detruit"):
				dtoArme = DTOenregistrementArme(self.time,
												arme.noeudPhysique.getPos()[0],
												arme.noeudPhysique.getPos()[1],
												arme.armeId)
				self.dtoPartie.appendArme(dtoArme)


	def analyseFinPartie(self):
		if(not self.isDTOStatsSaved):
			self.isDTOStatsSaved = True
			#set le gagnant
			if (self.listTank[0].pointDeVie <= 0):
				DTOStats.idGagnant = DTOStats.idJoueur2
				print "Joueur 2 a gagne"
			elif (self.listTank[1].pointDeVie <= 0):
				DTOStats.idGagnant = DTOStats.idJoueur1
				print "Joueur 1 a gagne"

			#affiche les stats de la partie
			# print("idJoueur1: "+str(DTOStats.idJoueur1))
			# print("idJoueur2: "+str(DTOStats.idJoueur2))
			# print("idMap: "+str(DTOStats.idNiveau))
			# print("idGagnant: "+str(DTOStats.idGagnant))
			# for i in range(6):
			# 	print ("NbUtil J1 Arme N"+str(DTOStats.DTOStatsArmeJ1[i].idArme)+" : "+str(DTOStats.DTOStatsArmeJ1[i].nbUtil))
			# 	print ("NbUtil J2 Arme N"+str(DTOStats.DTOStatsArmeJ2[i].idArme)+" : "+str(DTOStats.DTOStatsArmeJ2[i].nbUtil))
			DAOStats.create(DTOStats)
			#ajoute l'exp (si non favoris, voir DAOStats)
			if(DTOStats.idGagnant == DTOStats.idJoueur1):
				addedExp1 = 100+self.listTank[0].pointDeVie*2
				addedExp2 = (self.listTank[0].pointDeVieMax-self.listTank[0].pointDeVie)*2
			else:
				addedExp2 = 100+self.listTank[1].pointDeVie*2
				addedExp1 = (self.listTank[1].pointDeVieMax-self.listTank[1].pointDeVie)*2

			print("addedExp1: " + str(addedExp1))
			print("addedExp2: " + str(addedExp2))

			DAOStats.update(DTOStats, addedExp1, addedExp2)
			# print("-------------idJoueur1: "+str(DTOStats.idJoueur1))
			# print("-------------idJoueur2: "+str(DTOStats.idJoueur2))
			#DTO complet
			self.DTOStats = DTOStats
			# print ("username1: " + DTOStats.nomJ1)
			# print ("username2: " + DTOStats.nomJ2)

			#affiche les boutons pour aller sur le site web
			self.bP1 = DirectButton(text = ("Page Joueur1", "Page Joueur1", "Page Joueur1", "Page Joueur1"),
						  text_scale=(0.06,0.06),
						  borderWidth = (0.02, 0.02),
						  text_bg=(0.243,0.325,0.321,1),
						  frameColor=(0.243,0.325,0.321,1),
						  relief=2,
						  textMayChange = 1,
						  pad = (0,0),
						  command = self.openSiteP1,
						  pos = (-1.25,-1.4,-0.9))

			self.bP2 = DirectButton(text = ("Page Joueur2", "Page Joueur2", "Page Joueur2", "Page Joueur2"),
						  text_scale=(0.06,0.06),
						  borderWidth = (0.02, 0.02),
						  text_bg=(0.243,0.325,0.321,1),
						  frameColor=(0.243,0.325,0.321,1),
						  relief=2,
						  textMayChange = 1,
						  pad = (0,0),
						  command = self.openSiteP2,
						  pos = (1.25,-1.4,-0.9))

			#affiche les recap de l'exp
			if(DTOStats.idGagnant == DTOStats.idJoueur1):
				if(DTOStats.expJ1avantPartie > DTOStats.expJ2avantPartie):
					print("Experience J1: "+str(DTOStats.expJ1avantPartie)+"(experience avant partie) +  100xp(partie Gagnee) + "+str(self.listTank[0].pointDeVie)+"(vie restante)x2 = "+str(DTOStats.expJ1apresPartie)+"xp")
					print("Experience J2: "+str(DTOStats.expJ2avantPartie)+"(experience avant partie) +  "+str((self.listTank[0].pointDeVieMax-self.listTank[0].pointDeVie))+"(vie enlevée)x2 = "+str(DTOStats.expJ2apresPartie)+"xp")
				else:
					print("Experience J1: "+str(DTOStats.expJ1avantPartie)+"(experience avant partie) +  100xp(partie Gagnee) + 100xp(non favori) + "+str(self.listTank[0].pointDeVie)+"(vie restante)x2 = "+str(DTOStats.expJ1apresPartie)+"xp")
					print("Experience J2: "+str(DTOStats.expJ2avantPartie)+"(experience avant partie) +  "+str((self.listTank[0].pointDeVieMax-self.listTank[0].pointDeVie))+"(vie enlevée)x2 = "+str(DTOStats.expJ2apresPartie)+"xp")
			else:
				if(DTOStats.expJ2avantPartie > DTOStats.expJ1avantPartie):
					print("Experience J2: "+str(DTOStats.expJ2avantPartie)+"(experience avant partie) +  100xp(partie Gagnee) + "+str(self.listTank[1].pointDeVie)+"(vie restante)x2 = "+str(DTOStats.expJ2apresPartie)+"xp")
					print("Experience J1: "+str(DTOStats.expJ1avantPartie)+"(experience avant partie) +  "+str((self.listTank[1].pointDeVieMax-self.listTank[1].pointDeVie))+"(vie enlevée)x2 = "+str(DTOStats.expJ1apresPartie)+"xp")
				else:
					print("Experience J2: "+str(DTOStats.expJ2avantPartie)+"(experience avant partie) +  100xp(partie Gagnee) + 100xp(non favori) + "+str(self.listTank[1].pointDeVie)+"(vie restante)x2 = "+str(DTOStats.expJ2apresPartie)+"xp")
					print("Experience J1: "+str(DTOStats.expJ1avantPartie)+"(experience avant partie) +  "+str((self.listTank[1].pointDeVieMax-self.listTank[1].pointDeVie))+"(vie enlevée)x2 = "+str(DTOStats.expJ1apresPartie)+"xp")
			
			self.textLabel1 = TextNode('testLabel1')
			self.textLabel2 = TextNode('testLabel2')


			if(DTOStats.idGagnant == DTOStats.idJoueur1):
				if(DTOStats.expJ1avantPartie > DTOStats.expJ2avantPartie):
					self.textLabel1.setText("Exp J1: "+str(DTOStats.expJ1avantPartie)+" +  100xp + ("+str(self.listTank[0].pointDeVie)+")x2 = "+str(int(DTOStats.expJ1apresPartie))+"xp")
					self.textLabel2.setText("Exp J2: "+str(DTOStats.expJ2avantPartie)+" +  ("+str((self.listTank[0].pointDeVieMax-self.listTank[0].pointDeVie))+")x2 = "+str(int(DTOStats.expJ2apresPartie))+"xp")
				else:
					self.textLabel1.setText("Exp J1: "+str(DTOStats.expJ1avantPartie)+" +  100xp + 100xp(non favori) + ("+str(self.listTank[0].pointDeVie)+")x2 = "+str(int(DTOStats.expJ1apresPartie))+"xp")
					self.textLabel2.setText("Exp J2: "+str(DTOStats.expJ2avantPartie)+" +  ("+str((self.listTank[0].pointDeVieMax-self.listTank[0].pointDeVie))+")x2 = "+str(int(DTOStats.expJ2apresPartie))+"xp")
			else:
				if(DTOStats.expJ2avantPartie > DTOStats.expJ1avantPartie):
					self.textLabel2.setText("Exp J2: "+str(DTOStats.expJ2avantPartie)+" +  100xp + ("+str(self.listTank[1].pointDeVie)+"(vie restante)x2 = "+str(int(DTOStats.expJ2apresPartie))+"xp")
					self.textLabel1.setText("Exp J1: "+str(DTOStats.expJ1avantPartie)+" +  ("+str((self.listTank[1].pointDeVieMax-self.listTank[1].pointDeVie))+")x2 = "+str(int(DTOStats.expJ1apresPartie))+"xp")
				else:
					self.textLabel2.setText("Exp J2: "+str(DTOStats.expJ2avantPartie)+" +  100xp + 100xp(non favori) + ("+str(self.listTank[1].pointDeVie)+")x2 = "+str(int(DTOStats.expJ2apresPartie))+"xp")
					self.textLabel1.setText("Exp J1: "+str(DTOStats.expJ1avantPartie)+" +  ("+str((self.listTank[1].pointDeVieMax-self.listTank[1].pointDeVie))+")x2 = "+str(int(DTOStats.expJ1apresPartie))+"xp")



			self.textLabel1.setTextColor(0,0,0,1)
			self.textLabel1.setShadow(0.05,0.05)
			self.textLabel1.setShadowColor((200,200,200,0.8))
			self.textLabel1.setCardColor((255,255,255,0.3))
			self.textLabel1.setCardAsMargin(0, 0, 0, 0)
			self.textLabel1.setCardDecal(True)
			self.textLabel1.setAlign(TextNode.ACenter)
			self.nodeLabel1 = aspect2d.attachNewNode(self.textLabel1)
			self.nodeLabel1.setScale(0.10)
			self.nodeLabel1.setPos(0,0,1)
			
			self.textLabel2.setTextColor(0,0,0,1)
			self.textLabel2.setShadow(0.05,0.05)
			self.textLabel2.setShadowColor((200,200,200,0.8))
			self.textLabel2.setCardColor((255,255,255,0.3))
			self.textLabel2.setCardAsMargin(0, 0, 0, 0)
			self.textLabel2.setCardDecal(True)
			self.textLabel2.setAlign(TextNode.ACenter)
			self.nodeLabel2 = aspect2d.attachNewNode(self.textLabel2)
			self.nodeLabel2.setScale(0.10)
			self.nodeLabel2.setPos(0,0,1)

			self.sequence = Sequence (LerpPosInterval(self.nodeLabel1,1,(0,0,-0.2),blendType="easeIn"))
			self.sequence.start()
			self.sequence2 = Sequence (LerpPosInterval(self.nodeLabel2,1,(0,0,-0.5),blendType="easeIn"))
			self.sequence2.start()
			
			#animation lvlUp
			if(DTOStats.lvlJ1apresPartie > DTOStats.lvlJ1avantPartie):
				print "lvlUP J1"
				pos1Debut = self.listTank[0].modele.getPos()
				pos1Fin = pos1Debut+Point3(0,0,5)
				duree = 0.4
				intervalVictory1 = self.listTank[0].modele.posInterval(
					duree,
					pos1Fin,
					pos1Debut,
					blendType="easeIn"
				)

				intervalVictoryHPR = self.listTank[0].modele.hprInterval(
					duree,
					self.listTank[0].modele.getHpr()+Vec3(0,360,0)
				)

				intervalVictory2 = self.listTank[0].modele.posInterval(
					duree,
					pos1Debut,
					pos1Fin,
					blendType="easeOut"
				)
				mySequence = Sequence(intervalVictory1, intervalVictoryHPR, intervalVictory2)
				mySequence.loop()
				
			if(DTOStats.lvlJ2apresPartie > DTOStats.lvlJ2avantPartie):
				print "lvlUP J2"
				#animation lvlUp
				pos1Debut = self.listTank[1].modele.getPos()
				pos1Fin = pos1Debut+Point3(0,0,5)
				duree = 0.4
				intervalVictory1 = self.listTank[1].modele.posInterval(
					duree,
					pos1Fin,
					pos1Debut,
					blendType="easeIn"
				)

				intervalVictoryHPR = self.listTank[1].modele.hprInterval(
					duree,
					self.listTank[1].modele.getHpr()+Vec3(0,360,0)
				)

				intervalVictory2 = self.listTank[1].modele.posInterval(
					duree,
					pos1Debut,
					pos1Fin,
					blendType="easeOut"
				)
				mySequence = Sequence(intervalVictory1, intervalVictoryHPR, intervalVictory2)
				mySequence.loop()

	def openSiteP2(self):
		webbrowser.open_new("http://127.0.0.1/search.php?username='"+str(DTOStats.nomJ2)+"'")

	def openSiteP1(self):
		webbrowser.open_new("http://127.0.0.1/search.php?username='"+str(DTOStats.nomJ1)+"'")