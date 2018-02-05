<?php
	class DTOarme {
        public $type_arme;
        public $time_sec;
        public $pos_x;
        public $pos_y;

		public function __construct($type_arme, $time_sec, $pos_x, $pos_y) {
			$this->type_arme = $type_arme;
			$this->time_sec = $time_sec;
			$this->pos_x = $pos_x;
			$this->pos_y = $pos_y;
		}
	}