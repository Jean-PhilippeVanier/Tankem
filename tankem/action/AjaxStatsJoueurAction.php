<?php
	require_once("action/CommonAction.php");

	class AjaxStatsJoueurAction extends CommonAction{
		public $result = "Aucune information du joueur connecté disponible";

		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {    
            try{
                $this->connection = Connection::getConnection();
                $statement = $this->connection->prepare("SELECT vie,force,agilite,dexterite,niveau FROM joueur WHERE username = ?");
                $statement->execute(Array($_SESSION["Username"]));
                $this->row = $statement->fetchall(PDO::FETCH_ASSOC);
				$this->row = json_encode($this->row);
				$this->result = $this->row;
				Connection::closeConnection();
            }catch(PDOException $e){
                echo 'Échec lors de la connexion : ' . $e->getMessage();
            }
		}
	}
