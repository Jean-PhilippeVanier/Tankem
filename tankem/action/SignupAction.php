<?php
	require_once("action/CommonAction.php");
	class SignupAction extends CommonAction {
		public $wrongInfo = false;
		public $rightInfo = false;
		public $errorMessage = "";
		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {

			$connection = Connection::getConnection();
			$execute = true;
			if(isset($_POST["fieldUsername"])){

				$statement = $connection->prepare("INSERT INTO joueur (username,name,surname,couleurTank,password,banned,bannedStart,logCounter,email,niveau,experience,vie,force,agilite,dexterite,partieJoue,partieGagne) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)");
				if($_POST["fieldUsername"] != ""){
					$statement2 = $connection->prepare("SELECT * FROM joueur WHERE username = ?");
					$statement2->bindParam(1,$_POST["fieldUsername"]);
					$statement2->setFetchMode(PDO::FETCH_ASSOC);
					$statement2->execute();

					if ($row = $statement2->fetch()){	
						$execute = false;
						$this->wrongInfo = true;
						$this->errorMessage = "Ce nom d'utilisateur est déjà utilisé";
					}
					else{
						$statement->bindParam(1, $_POST["fieldUsername"]);
					}
				}
				else{
					$execute = false;
					$this->wrongInfo = true;
					$this->errorMessage = "Veuillez entrer un username";
				}
				if($_POST["fieldEmail"] != ""){
					$statement2 = $connection->prepare("SELECT * FROM joueur WHERE email = ?");
					$statement2->bindParam(1,$_POST["fieldEmail"]);
					$statement2->setFetchMode(PDO::FETCH_ASSOC);
					$statement2->execute();
					if($row = $statement2->fetch()){
						$execute = false;
						$this->wrongInfo = true;
						$this->errorMessage = "Cet email est déjà utilisé";
						
					}
					else if($execute){
						$statement->bindParam(9, $_POST["fieldEmail"]);
					}
				}
				else if($execute){
					$execute = false;
					$this->wrongInfo = true;
					$this->errorMessage = "Veuillez entrer un email";
				}
				if($_POST["fieldNom"] != ""){
					$statement->bindParam(2, $_POST["fieldNom"]);
				}
				else if($execute){
					$execute = false;
					$this->wrongInfo = true;
					$this->errorMessage = "Veuillez entrer un nom ";
				}
				if($_POST["fieldPrenom" ] != ""){
					$statement->bindParam(3, $_POST["fieldPrenom"]);
				}
				else if($execute){
					$execute = false;
					$this->wrongInfo = true;
					$this->errorMessage = "Veuillez entrer un prenom ";
				}
				$statement->bindParam(4, $_POST["fieldColor"]);
				if($_POST["fieldPassword"] != ""){
					if($_POST["fieldPassword"] == $_POST["fieldConfirmPassword"]){
						$hashedPwd = password_hash($_POST["fieldPassword"], PASSWORD_BCRYPT);
						$statement->bindParam(5,$hashedPwd);
					}
					else if($execute){
						$execute = false;
						$this->wrongInfo = true;
						$this->errorMessage ="Les mots de passe ne sont pas les mêmes ";
					}
				}
				else if($execute){
					$execute = false;
					$this->wrongInfo = true;
					$this->errorMessage = "Veuillez entrer un mot de passe ";
				}
				if($execute){
					$tmp = 0;
					$notBanned = null;
					$statement->bindParam(6, $tmp);
					$statement->bindParam(7, $notBanned);
					$statement->bindParam(8, $tmp);
					$statement->bindParam(10, $tmp);
					$statement->bindParam(11, $tmp);
					$statement->bindParam(12, $tmp);
					$statement->bindParam(13, $tmp);
					$statement->bindParam(14, $tmp);
					$statement->bindParam(15, $tmp);
					$statement->bindParam(16, $tmp);
					$statement->bindParam(17, $tmp);

					$statement->execute();

					$this->rightInfo = true;
					$this->errorMessage = "L'enregistrement s'est bien effectué";
				}
			}
			Connection::closeConnection();
		}
}
