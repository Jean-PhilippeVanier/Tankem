DROP TABLE joueur_arme_partie;
DROP TABLE joueur_arme;
DROP TABLE joueur_map;
DROP TABLE partie;
DROP TABLE arme;
DROP TABLE joueur;

CREATE TABLE joueur (
	id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
	username VARCHAR2(20) NOT NULL UNIQUE,
	name VARCHAR2(30) NOT NULL,
	surname VARCHAR2(30) NOT NULL,
	couleurTank VARCHAR2(20) NOT NULL,
	password VARCHAR2(100) NOT NULL,
	banned NUMBER NOT NULL,
	bannedStart NUMBER,
	logCounter NUMBER NOT NULL,
	email VARCHAR2(70) NOT NULL UNIQUE,
	niveau NUMBER NOT NULL,
	experience NUMBER NOT NULL,
	vie NUMBER NOT NULL,
	force NUMBER NOT NULL,
	agilite NUMBER NOT NULL,
	dexterite NUMBER NOT NULL,
	partieJoue NUMBER NOT NULL,
	partieGagne NUMBER NOT NULL,
	CONSTRAINT pk_joueur PRIMARY KEY (id)
);

--INSERT INTO joueur (username, name, surname, couleurTank, password, email, niveau, experience, vie, force, agilite, dexterite, partieJoue, partieGagne) VALUES ('Test2','Test2Nom','Test2Prenom','#FFFF00','AAAaaa111','nicknclank@yahoo.com',1,0,0,0,0,0,0,0);

CREATE TABLE arme (
	id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
	name VARCHAR2(20),
	CONSTRAINT pk_arme PRIMARY KEY (id)
);

CREATE TABLE joueur_map (
	idJoueur NUMBER,
	idMap NUMBER,
	nbFoisJouer NUMBER,
	CONSTRAINT pk_joueur_map PRIMARY KEY (idJoueur, idMap),
	CONSTRAINT fk_joueurJOUEUR_MAP FOREIGN KEY (idJoueur) REFERENCES joueur(id),
	CONSTRAINT fk_mapJOUEUR_MAP FOREIGN KEY (idMap) REFERENCES editor_niveau(id)
);

CREATE TABLE joueur_arme (
	idJoueur NUMBER,
	idArme NUMBER,
	nbFoisUtilise NUMBER,
	CONSTRAINT pk_joueur_arme PRIMARY KEY (idJoueur, idArme),
	CONSTRAINT fk_joueurJOUEUR_ARME FOREIGN KEY (idJoueur) REFERENCES joueur(id),
	CONSTRAINT fk_armeJOUEUR_ARME FOREIGN KEY (idArme) REFERENCES arme(id)
);

CREATE TABLE partie(
	Id Number GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
	IdJoueur1 Number NOT NULL,
	IdJoueur2 Number NOT NULL,
	IdNiveau Number NOT NULL,
	Idgagnant Number NOT NULL,
	CONSTRAINT PK_Id PRIMARY KEY (Id),
	CONSTRAINT FK_IdJoueur1 FOREIGN KEY (IdJoueur1) REFERENCES joueur(Id),
	CONSTRAINT FK_IdJoueur2 FOREIGN KEY (IdJoueur2) REFERENCES joueur(Id),
	CONSTRAINT FK_IdNiveau FOREIGN KEY (IdNiveau) REFERENCES editor_niveau(Id),
	CONSTRAINT Fk_Idgagnant FOREIGN KEY (IdGagnant) REFERENCES joueur(Id)
);


CREATE TABLE joueur_arme_partie(
	IdPartie Number NOT NULL,
	IdJoueur Number NOT NULL, 
	IdArme Number NOT NULL,
	NbFoisUtilArme Number,
	CONSTRAINT PK_Id_JAP PRIMARY KEY (IdPartie, IdJoueur, IdArme),
	CONSTRAINT FK_IdPartie FOREIGN KEY (IdPartie) REFERENCES partie(Id),
	CONSTRAINT FK_IdJoueur FOREIGN KEY (IdJoueur) REFERENCES joueur(Id),
	CONSTRAINT FK_IdArme FOREIGN KEY (IdArme) REFERENCES arme(Id)
);

--Insertion des infos
INSERT INTO arme (name) VALUES ('Canon');
INSERT INTO arme (name) VALUES ('Grenade');
INSERT INTO arme (name) VALUES ('Mitraillette');
INSERT INTO arme (name) VALUES ('Piege');
INSERT INTO arme (name) VALUES ('Shotgun');
INSERT INTO arme (name) VALUES ('Guide');

INSERT INTO joueur(username, name, surname, couleurTank, password, banned, bannedStart, logCounter, email, niveau, experience, vie, force, agilite, dexterite, partieJoue, partieGagne) VALUES('Test1','Test1Nom','Test1Prenom','#FFFF00','AAAaaa111', 0, NULL, 0, 'nicknclank@yahoo.com',1,0,0,0,0,0,0,0);
INSERT INTO joueur(username, name, surname, couleurTank, password, banned, bannedStart, logCounter, email, niveau, experience, vie, force, agilite, dexterite, partieJoue, partieGagne) VALUES('Test2','Test2Nom','Test2Prenom','#FF0000','AAAaaa111', 0, NULL, 0, 'nicknclank666@yahoo.com',1,0,0,0,0,0,0,0);
INSERT INTO joueur(username, name, surname, couleurTank, password, banned, bannedStart, logCounter, email, niveau, experience, vie, force, agilite, dexterite, partieJoue, partieGagne) VALUES('Patate','PatateNom','PatatePrenom','#00FF00','AAAaaa111', 0, NULL, 0, 'nicknclank420@yahoo.com',1,0,0,0,0,0,0,0);


--Fin;
COMMIT;