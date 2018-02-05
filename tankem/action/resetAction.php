<?php
	require_once("action/CommonAction.php");
	class ResetAction extends CommonAction {
		public $wrongEmail = false;
		public $rightEmail = false;
		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
			
		}
		protected function randomPassword() {
			$alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890';
			$pass = array();
			$alphaLength = strlen($alphabet) - 1;
			for ($i = 0; $i < 8; $i++) {
				$n = rand(0, $alphaLength);
				$pass[] = $alphabet[$n];
			}
			return implode($pass); //retourne une string
		}

		protected function executeAction() {
			if(isset($_POST["resetEmail"])) {
				$connection = Connection::getConnection();
				$userEmail = $_POST["resetEmail"];
				$statement = $connection->prepare("SELECT EMAIL FROM joueur WHERE EMAIL = ?");
				$statement->bindParam(1, $userEmail);
				$statement->setFetchMode(PDO::FETCH_ASSOC);
				$statement->execute();

				if($row = $statement->fetch()){
					$this->rightEmail = true;
					// the message
					$newPswd = $this->randomPassword();
					$newPswdHashed = password_hash($newPswd, PASSWORD_BCRYPT);
					$header = "Content-Type: text/html; charset=UTF-8";
					$msg = "Vous avez récemment demandé une réinitialisation de mot de passe.\nVotre nouveau mot de passe est : " . $newPswd;

					// use wordwrap() if lines are longer than 70 characters
					$msg = wordwrap($msg,70);
					// send email
					mail($userEmail,"Password reset for Tank'em",$msg,$header);

					$statement = $connection->prepare("UPDATE joueur SET password = ? where email = ?");
					$statement->bindParam(1,$newPswdHashed);
					$statement->bindParam(2,$userEmail);
					$statement->execute();
				}
				else{
					$this->wrongEmail = true;
				}
			}
		}
		
	}
