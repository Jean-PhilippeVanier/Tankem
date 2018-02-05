<?php
	require_once("action/CommonAction.php");

	class AjaxEnregistrerStatsAction extends CommonAction{
		public $result = "Aucune information du joueur connecté disponible";

		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {    
            try{
                $this->connection = Connection::getConnection();
                $statement = $this->connection->prepare("UPDATE joueur SET vie = ?, force = ?, agilite = ?, dexterite = ?, niveau = ? WHERE username = ?");
                $statement->execute(Array($_POST["hp"],$_POST["degat"],$_POST["deplacement"],$_POST["tir"],$_POST["niveau"],$_SESSION["Username"]));
				Connection::closeConnection();
            }catch(PDOException $e){
                echo 'Échec lors de la connexion : ' . $e->getMessage();
            }
		}
	}
