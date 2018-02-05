DROP TABLE partie;
DROP TABLE joueur_arme_partie;

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
	CONSTRAINT PK_Id PRIMARY KEY (IdPartie, IdJoueur),
	CONSTRAINT FK_IdPartie FOREIGN KEY (IdPartie) REFERENCES partie(Id),
	CONSTRAINT FK_IdJoueur FOREIGN KEY (IdJoueur) REFERENCES joueur(Id),
	CONSTRAINT FK_IdArme FOREIGN KEY (IdArme) REFERENCES arme(Id)
);