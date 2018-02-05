<?php
	class DTOjoueur {
        public $time_sec;
        public $pos_x;
        public $pos_y;
        public $orientation;
        public $health;
        public $ball_shot;

		public function __construct($time_sec, $pos_x, $pos_y, $orientation, $health, $ball_shot) {
			$this->time_sec = $time_sec;
			$this->pos_x = $pos_x;
			$this->pos_y = $pos_y;
			$this->orientation = $orientation;
			$this->health = $health;
			$this->ball_shot = $ball_shot;
		}
	}