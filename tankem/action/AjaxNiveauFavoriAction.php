<?php
	require_once("action/CommonAction.php");

	class AjaxNiveauFavoriAction extends CommonAction{
		public $result = "Aucun niveau préféré";

		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {
			$id = $_POST["idJoueur"];
			try{
				$this->connection = Connection::getConnection();
				$statement = $this->connection->prepare("SELECT editor_niveau.name NomNiveau FROM editor_niveau WHERE editor_niveau.id = (SELECT idNiveau FROM partie WHERE IdJoueur1 = ? OR IdJoueur2 = ? GROUP BY idNiveau ORDER BY COUNT(idNiveau) DESC FETCH FIRST 1 ROWS ONLY)");
				$statement->execute(Array($id, $id));
				$this->row = $statement->fetchall(PDO::FETCH_ASSOC);
				$this->idMostUsed = json_encode($this->row);
				$this->result = $this->idMostUsed;
				Connection::closeConnection();
			}catch(PDOException $e){
				echo 'Échec lors de la connection : ' + $e->getMessage();
			}
		}
	}
