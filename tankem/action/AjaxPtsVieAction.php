<?php
	require_once("action/CommonAction.php");

	class AjaxPtsVieAction extends CommonAction{
		public $result = "Aucune donnée pour les points de vie";

		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {
			try{
				$this->connection = Connection::getConnection();
				$statement = $this->connection->prepare("SELECT vie FROM tankem_values");
				$statement->execute();
				$this->row = $statement->fetchall(PDO::FETCH_ASSOC);
				$this->row = json_encode($this->row);
				$this->result = $this->row;
				Connection::closeConnection();
			}catch(PDOException $e){
				echo 'Échec lors de la connection : ' + $e->getMessage();
			}
		}
	}