-- Mettre un commentaire
-- Pour exécuter ce script dans sqlplus: start creationTable.sql (ou chemin relatif)
--DROP TABLE tankem_values;
--DROP TABLE tankem_text;
CREATE TABLE tankem_values(
	id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
	vitesse_char REAL NOT NULL CHECK (vitesse_char >= 4 AND vitesse_char <= 12 ),
	vitesse_rotation REAL NOT NULL CHECK (vitesse_rotation >= 1000 AND vitesse_rotation <= 2000 ),
	vie REAL NOT NULL CHECK (vie >= 100 AND vie <= 2000),
	temps_mouvement_blocs REAL NOT NULL CHECK (temps_mouvement_blocs >= 0.2 AND temps_mouvement_blocs <= 2),
	canon_vitesse_balle REAL NOT NULL CHECK (canon_vitesse_balle >= 4 AND canon_vitesse_balle <= 30),
	canon_reload REAL NOT NULL CHECK (canon_reload >= 0.2 AND canon_reload <= 10),
	mitraillette_vitesse_balle REAL NOT NULL CHECK (mitraillette_vitesse_balle >= 4 AND mitraillette_vitesse_balle <= 30),
	mitraillette_reload REAL NOT NULL CHECK (mitraillette_reload >= 0.2 AND mitraillette_reload <= 10),
	grenade_vitesse_balle REAL NOT NULL CHECK (grenade_vitesse_balle >= 10 AND grenade_vitesse_balle <= 25),
	grenade_reload REAL NOT NULL CHECK (grenade_reload >= 0.2 AND grenade_reload <= 10),
	shotgun_vitesse_balle REAL NOT NULL CHECK (shotgun_vitesse_balle >= 4 AND shotgun_vitesse_balle <= 30),
	shotgun_reload REAL NOT NULL CHECK (shotgun_reload >= 0.2 AND shotgun_reload <= 10),
	shotgun_spread REAL NOT NULL CHECK (shotgun_spread >= 0.1 AND shotgun_spread <= 1.5),
	piege_vitesse_balle REAL NOT NULL CHECK (piege_vitesse_balle >= 0.2 AND piege_vitesse_balle <= 4),
	piege_reload REAL NOT NULL CHECK (piege_reload >= 0.2 AND piege_reload <= 10),
	missile_vitesse_balle REAL NOT NULL CHECK (missile_vitesse_balle >= 20 AND missile_vitesse_balle <= 40),
	missile_reload REAL NOT NULL CHECK (missile_reload >= 0.2 AND missile_reload <= 10),
	spring_vitesse_saut REAL NOT NULL CHECK (spring_vitesse_saut >= 6 AND spring_vitesse_saut <= 20),
	spring_reload REAL NOT NULL CHECK (spring_reload >= 0.2 AND spring_reload <= 10),
	rayon_explosion REAL NOT NULL CHECK (rayon_explosion >= 1 AND rayon_explosion <= 30),
	message_acceuil_duree REAL NOT NULL CHECK (message_acceuil_duree >= 1 AND message_acceuil_duree <= 10),
	message_countdown_duree REAL NOT NULL CHECK (message_countdown_duree >= 0 AND message_countdown_duree <= 10)
);
CREATE TABLE tankem_text(
	id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
	message_acceuil VARCHAR2(60),
	message_start VARCHAR2(50),
	message_fin VARCHAR2(70)
);
-- Insertion de valeurs dans la table
INSERT INTO tankem_values (vitesse_char,vitesse_rotation,vie,temps_mouvement_blocs,
canon_vitesse_balle,canon_reload,mitraillette_vitesse_balle,mitraillette_reload,
grenade_vitesse_balle,grenade_reload,shotgun_vitesse_balle,shotgun_reload,shotgun_spread,
piege_vitesse_balle,piege_reload,missile_vitesse_balle,missile_reload,spring_vitesse_saut,
spring_reload,rayon_explosion,message_acceuil_duree,message_countdown_duree)
VALUES (7,1500,200,0.8,14,1.2,18,0.4,16,0.8,13,1.8,0.4,1,0.8,30,3,10,0.5,8,3,3);
INSERT INTO tankem_text (message_acceuil,message_start,message_fin) VALUES ('PEPE!','Darth Vader did nothing wrong!','Jai pas de jokes :c');


-- Ne pas oublier le commit pour que les données soient vraiment dans la table

-- requête pour voir les tables
SELECT table_name FROM user_tables;

-- Destruction de table
-- DROP TABLE tankem_values;
COMMIT;