# -*- coding: utf-8 -*-
from SingletonDBConnection import SingletonDBConnection
from DTOEnregistrementArme import DTOenregistrementArme
from DTOEnregistrementJoueur import DTOenregistrementJoueur
from DTOEnregistrementPartie import DTOenregistrementPartie 
from DTOEnregistrementProjectile import DTOenregistrementProjectile 
import cx_Oracle

class DAOenregistrementOracle():

    def __init__(self):
		self.connection = SingletonDBConnection().getConnection()

    def create(self, DTOpartie):
        # Creation de la partie dans la BD
        cur = self.connection.cursor()
        statement = "INSERT INTO ENREGISTREMENT_PARTIE(ID_MAP, ID_JOUEUR1, ID_JOUEUR2, CREATION_DATE) VALUES(:id_map, :id_j1, :id_j2, :creation_date)"
        cur.execute(statement, { 'id_map':DTOpartie.getIdMap(), 'id_j1':DTOpartie.getIdJ1(), 'id_j2':DTOpartie.getIdJ2(), 'creation_date':DTOpartie.getDate() } )
        cur.close()
        self.connection.commit()

        # Avoir le ID de la partie cree
        curReadId = self.connection.cursor()
        curReadId = curReadId.execute("SELECT MAX(ID) FROM ENREGISTREMENT_PARTIE")
        idPartie = curReadId.fetchall()
        idPartie = idPartie[0][0]
        curReadId.close()

        # Insertion du joueur 1
        arrayJoueur1 = DTOpartie.getArrayJoueur1()
        arrayInsert = [(1,idPartie,dtoJoueur.getTime(),dtoJoueur.getX(),dtoJoueur.getY(),dtoJoueur.getOrientation(), dtoJoueur.getHealth(),dtoJoueur.isBallShot()) for dtoJoueur in arrayJoueur1]
        curJoueur = self.connection.cursor()
        statement = "INSERT INTO ENREGISTREMENT_JOUEUR(NO_JOUEUR, ID_PARTIE, TIME_SEC, POS_X, POS_Y, ORIENTATION, HEALTH, BALL_SHOT) VALUES(:1,:2,:3,:4,:5, :6, :7, :8)"
        curJoueur.bindarraysize = 5
        # curJoueur.setinputsizes(int,int,int,int,int)
        curJoueur.executemany(statement, arrayInsert)
        curJoueur.close()

        # Insertion du joueur 2
        arrayJoueur2 = DTOpartie.getArrayJoueur2()
        arrayInsert = [(2,idPartie,dtoJoueur.getTime(),dtoJoueur.getX(),dtoJoueur.getY(),dtoJoueur.getOrientation(), dtoJoueur.getHealth(),dtoJoueur.isBallShot()) for dtoJoueur in arrayJoueur2]
        curJoueur = self.connection.cursor()
        statement = "INSERT INTO ENREGISTREMENT_JOUEUR(NO_JOUEUR, ID_PARTIE, TIME_SEC, POS_X, POS_Y, ORIENTATION, HEALTH, BALL_SHOT) VALUES(:1,:2,:3,:4,:5, :6, :7, :8)"
        curJoueur.bindarraysize = 5
        curJoueur.executemany(statement, arrayInsert)
        curJoueur.close()

        # Insertion arme
        arrayArme = DTOpartie.getArrayArme()
        arrayInsert = [(dtoArme.getType(),idPartie,dtoArme.getTime(),dtoArme.getX(),dtoArme.getY()) for dtoArme in arrayArme]
        curArme = self.connection.cursor()
        statement = "INSERT INTO ENREGISTREMENT_ARME(TYPE_ARME, ID_PARTIE, TIME_SEC, POS_X, POS_Y) VALUES(:1,:2,:3,:4,:5)"
        curArme.bindarraysize = 5
        curArme.executemany(statement, arrayInsert)
        curArme.close()

        # Insertion projectile
        arrayProjectile = DTOpartie.getArrayProjectile()
        arrayInsert = [(idPartie,dtoProjectile.getTime(),dtoProjectile.getX(),dtoProjectile.getY(),dtoProjectile.getEnMouvement()) for dtoProjectile in arrayProjectile]
        curProjectile = self.connection.cursor()
        statement = "INSERT INTO ENREGISTREMENT_PROJECTILE(ID_PARTIE, TIME_SEC, POS_X, POS_Y, EN_MOUVEMENT) VALUES(:1,:2,:3,:4,:5)"
        curProjectile.bindarraysize = 6
        curProjectile.executemany(statement, arrayInsert)
        curProjectile.close()

        # Commit
        self.connection.commit()

        # ----------------------------------------------------------------------
        # Verification qu'il n'y a que 5 parties dans la BD

        # Avoir le nombre de parties
        curReadNb = self.connection.cursor()
        curReadNb = curReadNb.execute("SELECT COUNT(ID) FROM ENREGISTREMENT_PARTIE")
        nbParties = curReadNb.fetchall()
        nbParties = nbParties[0][0]

        if(nbParties > 5):
            # Avoir le id de la plus petite partie
            curReadId = self.connection.cursor()
            curReadId = curReadId.execute("SELECT MIN(ID) FROM ENREGISTREMENT_PARTIE")
            idPartie = curReadId.fetchall()
            idPartie = idPartie[0][0]
            curReadId.close()

            self.delete(idPartie)
        
        SingletonDBConnection().closeConnection()

    def delete(self, idPartie):
        # Delete Joueurs
        cur = self.connection.cursor()
        statement = 'DELETE FROM ENREGISTREMENT_JOUEUR WHERE ID_PARTIE = :ID'
        cur.execute(statement, {'ID':idPartie})
        cur.close()

        # Delete Arme
        cur = self.connection.cursor()
        statement = 'DELETE FROM ENREGISTREMENT_ARME WHERE ID_PARTIE = :ID'
        cur.execute(statement, {'ID':idPartie})
        cur.close()

        # Delete Projectile
        cur = self.connection.cursor()
        statement = 'DELETE FROM ENREGISTREMENT_PROJECTILE WHERE ID_PARTIE = :ID'
        cur.execute(statement, {'ID':idPartie})
        cur.close()

        # Delete Partie
        cur = self.connection.cursor()
        statement = 'DELETE FROM ENREGISTREMENT_PARTIE WHERE ID = :ID'
        cur.execute(statement, {'ID':idPartie})
        cur.close()

        # Commit
        self.connection.commit()

# TEST
#testDao = DAOenregistrementOracle()
#testDTOp = DTOenregistrementPartie("4/20/2017")
#testDTOj1 = DTOenregistrementJoueur(0,10,10)
#testDTOj2 = DTOenregistrementJoueur(0,4,4)
#testDTOa = DTOenregistrementArme(0,8,8,1)
#
#testDTOp.appendJoueur1(testDTOj1)
#testDTOp.appendJoueur2(testDTOj2)
#testDTOp.appendArme(testDTOa)
#
#testDao.create(testDTOp)
