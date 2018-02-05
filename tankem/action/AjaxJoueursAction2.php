<?php
	require_once("action/CommonAction.php");

	class AjaxJoueursAction extends CommonAction{
		public $result = "Rien ne s'est passé";

		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {
			try{
				$this->connection = Connection::getConnection();
				$statement = $this->connection->prepare("SELECT * from joueur");
				$statement->execute();
				$this->tab = $statement->fetchall(PDO::FETCH_ASSOC);
				$this->result = json_encode($this->tab);
			}catch(PDOException $e){
				echo "Échec lors de la connection : " + $e->getMessage();
			}
		}
	}
