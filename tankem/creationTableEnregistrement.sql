DROP TABLE enregistrement_projectile;
DROP TABLE enregistrement_arme;
DROP TABLE enregistrement_joueur;
DROP TABLE enregistrement_partie;

CREATE TABLE enregistrement_partie (
	id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
	id_map NUMBER NOT NULL,
	id_joueur1 NUMBER NOT NULL,
	id_joueur2 NUMBER NOT NULL,
	creation_date VARCHAR2(50) NOT NULL
);

CREATE TABLE enregistrement_joueur (
	no_joueur NUMBER NOT NULL,
	id_partie NUMBER NOT NULL,
	time_sec NUMBER NOT NULL,
	pos_x REAL NOT NULL,
	pos_y REAL NOT NULL,
	orientation NUMBER NOT NULL,
	health NUMBER NOT NULL,
	ball_shot NUMBER(1) NOT NULL,
	CONSTRAINT pk_erg_joueur PRIMARY KEY (no_joueur, id_partie, time_sec),
	CONSTRAINT fk_erg_partie_joueur FOREIGN KEY (id_partie) REFERENCES enregistrement_partie(id)
);

CREATE TABLE enregistrement_arme (
	type_arme VARCHAR2(50) NOT NULL,
	id_partie NUMBER NOT NULL,
	time_sec NUMBER NOT NULL,
	pos_x NUMBER NOT NULL,
	pos_y NUMBER NOT NULL,
	CONSTRAINT pk_erg_arme PRIMARY KEY (id_partie, time_sec, pos_x, pos_y),
	CONSTRAINT fk_erg_partie_arme FOREIGN KEY (id_partie) REFERENCES enregistrement_partie(id)
);

-- A MODIFIER PEUT-ETRE
CREATE TABLE enregistrement_projectile (
	id_partie NUMBER NOT NULL,
	time_sec NUMBER NOT NULL,
	pos_x NUMBER NOT NULL,
	pos_y NUMBER NOT NULL,
	en_mouvement NUMBER(1) NOT NULL,
	CONSTRAINT pk_erg_projectile PRIMARY KEY (id_partie, time_sec, pos_x, pos_y),
	CONSTRAINT fk_erg_partie_projectile FOREIGN KEY (id_partie) REFERENCES enregistrement_partie(id)
);
