<?php
	class DTOmap {
        public $id_niveau;
        public $name;
        public $creation_date;
        public $status;
        public $size_x;
        public $size_y;
        public $item_delay_min;
        public $item_delay_max;
        public $array_tuiles;
        public $array_spawns;

		public function __construct($id_niveau, $name, $creation_date, $status,
									$size_x, $size_y, $item_delay_min,
									$item_delay_max, $array_tuiles,
									$array_spawns) {
			$this->id_niveau = $id_niveau;
			$this->name = $name;
			$this->creation_date = $creation_date;
			$this->status = $status;
			$this->size_x = $size_x;
			$this->size_y = $size_y;
			$this->item_delay_min = $item_delay_min;
			$this->item_delay_max = $item_delay_max;
			$this->array_tuiles = $array_tuiles;
			$this->array_spawns = $array_spawns;
		}
	}
