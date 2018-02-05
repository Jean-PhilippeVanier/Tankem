<?php
	require_once("action/CommonAction.php");

	class AjaxNiveauFavori extends CommonAction{
		public $result = "Aucun niveau préféré";

		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {
			$id = $_POST["idJoueur"];
			try{
				$this->connection = new PDO("oci:dbname=DECINFO", "e1384492", "C");
                $this->connection->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
                $this->connection->setAttribute(PDO::ATTR_EMULATE_PREPARES,false);
				$statement = $this->connection->prepare("SELECT COUNT(idNiveau) Count, idNiveau FROM partie WHERE IdJoueur1 = ? or IdJoueur2 = ? GROUP BY idNiveau ORDER by Count DESC");
				$statement->execute(Array($id, $id));
				$this->row = $statement->fetchall(PDO::FETCH_ASSOC);
				// $this->result = json_encode($this->row);
				// if($this->row == null){
				// 	$this->result = null;
				// }else{
					$this->idMostUsed = json_encode($this->row);
					// $this->idMostUsed = $this->row;
					$this->result = $this->idMostUsed;
					// print_r($this->result)

				// }
			}catch(PDOException $e){
				echo 'Échec lors de la connection : ' + $e->getMessage();
			}
		}
	}
