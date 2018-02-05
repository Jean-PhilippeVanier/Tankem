<?php
	class DTOpartie {
        public $id;
        public $id_map;
		public $id_joueur1;
		public $id_joueur2;
        public $nom_map;
		public $nom_joueur1;
		public $nom_joueur2;
        public $creation_date;
        public $arrayJoueur1;
        public $arrayJoueur2;
        public $arrayProjectiles;
        public $arrayArmes;
        public $map;
		public $arbres;

		public function __construct($id, $id_map, $id_joueur1, $id_joueur2, $creation_date) {
			$this->id = $id;
			$this->id_map = $id_map;
			$this->id_joueur1 = $id_joueur1;
			$this->id_joueur2 = $id_joueur2;
			$this->nom_map = "Une map";
			$this->nom_joueur1 = "Joueur 1";
			$this->nom_joueur2 = "Joueur 2";
			$this->creation_date = $creation_date;
			$this->arrayJoueur1 = [];
			$this->arrayJoueur2 = [];
			$this->arrayProjectiles = [];
			$this->arrayArmes = [];
			$this->map = [];
			$this->arbres = [];
		}
	}
