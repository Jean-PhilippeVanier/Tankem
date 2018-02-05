<?php
	require_once("action/CommonAction.php");
	require_once("action/DAO/UserDAO.php");
	class InfosAction extends CommonAction {
		
		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_MEMBER);
			
		}

		protected function executeAction() {
			$row = $_SESSION["Row"];
			if(isset($_POST["editEmail"]) && isset($_POST["editPrenom"]) && isset($_POST["editEmail"]) && isset($_POST["editNom"]) && isset($_POST["editUsername"])){
				if($row["USERNAME"] != $_POST["editUsername"] || $row["NAME"] != $_POST["editNom"] || $row["SURNAME"] != $_POST["editPrenom"] || $row["EMAIL"] != $_POST["editEmail"] || $row["COULEURTANK"] != $_POST["editColor"]){
					$username = $_POST["editUsername"];
					$name = $_POST["editNom"];
					$prenom = $_POST["editPrenom"];
					$email = $_POST["editEmail"];
					$color = $_POST["editColor"];
					UserDAO::updateProfile($email,$prenom,$name,$username,$color);
					if($_SESSION["Success"]){
						$_SESSION["Username"] = $username;
					}
				}
			}
	}
}
