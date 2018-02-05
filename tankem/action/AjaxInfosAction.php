<?php
	require_once("action/CommonAction.php");

	class AjaxInfosAction extends CommonAction{
		public $result = "";
		public $answer;
		public $error;
		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {

			$connection = Connection::getConnection();	
			$statement = $connection->prepare("SELECT username,email,name,surname,couleurTank,password FROM joueur WHERE username = ?");
			$statement->bindParam(1,$_SESSION["Username"]);
			$statement->setFetchMode(PDO::FETCH_ASSOC);
			$success = $statement->execute();
			$_SESSION["Success"] = $success;
			$answer = $statement->fetch();
			$this->result = $answer;
			Connection::closeConnection();
		}
	}