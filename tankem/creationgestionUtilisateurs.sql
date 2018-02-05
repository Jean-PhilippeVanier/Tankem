--Supression des tables
DROP TABLE joueur_arme;
DROP TABLE joueur_map;
DROP TABLE arme;
DROP TABLE joueur;
--sqlplus e1384492@\"10.57.4.60/DECINFO.edu\"
--Création des tables
CREATE TABLE joueur (
	id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
	username VARCHAR2(20) NOT NULL,
	name VARCHAR2(30) NOT NULL,
	surname VARCHAR2(30) NOT NULL,
	couleurTank VARCHAR2(20) NOT NULL,
	password VARCHAR2(100) NOT NULL,
	email VARCHAR2(50) NOT NULL,
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

--INSERT INTO joueur (ingamename, name, surname, couleurTank, password, email, niveau, experience, vie, force, agilite, dexterite, partieJoue, partieGagne) VALUES ('Test4','Test4Nom','Test4Prenom','Rouge','AAAaaa111','nicolas.martin1996@yahoo.com',1,0,0,0,0,0,0,0);

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

--Insertion des infos
INSERT INTO arme (name) VALUES ('Canon');
INSERT INTO arme (name) VALUES ('Grenade');
INSERT INTO arme (name) VALUES ('Mitraillette');
INSERT INTO arme (name) VALUES ('Piege');
INSERT INTO arme (name) VALUES ('Shotgun');
INSERT INTO arme (name) VALUES ('Guide');

--Fin
COMMIT;