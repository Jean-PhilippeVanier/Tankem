<?php
	class DTOprojectile {
        public $time_sec;
        public $pos_x;
        public $pos_y;
        public $en_mouvement;

		public function __construct($time_sec, $pos_x, $pos_y, $en_mouvement) {
			$this->time_sec = $time_sec;
			$this->pos_x = $pos_x;
			$this->pos_y = $pos_y;
			$this->en_mouvement = $en_mouvement;
		}
	}