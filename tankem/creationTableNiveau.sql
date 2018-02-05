DROP TABLE editor_spawn;
DROP TABLE editor_tuile;
DROP TABLE editor_niveau;

CREATE TABLE editor_niveau (
	id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
	name VARCHAR2(50) NOT NULL ,
	creation_date VARCHAR2(50) NOT NULL,
	status VARCHAR2(10) NOT NULL,
	size_x NUMBER NOT NULL,
	size_y NUMBER NOT NULL,
	item_delay_min REAL NOT NULL,
	item_delay_max REAL NOT NULL
);

CREATE TABLE editor_tuile (
	pos_x NUMBER NOT NULL,
	pos_y NUMBER NOT NULL,
	id_niveau NUMBER NOT NULL,
	type_tuile NUMBER NOT NULL,
	has_tree NUMBER(1) NOT NULL,
	CONSTRAINT pk_tuile PRIMARY KEY (pos_x, pos_y,id_niveau),
	CONSTRAINT fk_niveau_tuile FOREIGN KEY (id_niveau) REFERENCES editor_niveau(id)
);

CREATE TABLE editor_spawn (
	pos_x NUMBER NOT NULL,
	pos_y NUMBER NOT NULL,
	id_niveau NUMBER NOT NULL,
	no_player NUMBER NOT NULL,
	CONSTRAINT pk_spawn PRIMARY KEY (pos_x, pos_y,id_niveau),
	CONSTRAINT fk_niveau_spawn FOREIGN KEY (id_niveau) REFERENCES editor_niveau(id)
);
