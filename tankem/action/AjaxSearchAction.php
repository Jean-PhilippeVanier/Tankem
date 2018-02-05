<?php
	require_once("action/CommonAction.php");

	class AjaxSearchAction extends CommonAction{
		public $result = "result";

		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {
            $this->result = $_POST["searchKey"];
            $str = $_POST["searchKey"]."%";
            try{
                $this->connection = Connection::getConnection();
                $statement = $this->connection->prepare("SELECT * FROM joueur WHERE upper(username) LIKE upper(?)");
                $statement->execute(Array($str));
                $this->row = $statement->fetchall(PDO::FETCH_ASSOC);
				if(isset($_SESSION["Username"])){
					$this->result = json_encode([$this->row,$_SESSION["Username"]]);
				}else{
					$this->result = json_encode([$this->row]);
				}
				Connection::closeConnection();
            }catch(PDOException $e){
                echo 'Échec lors de la connexion : ' . $e->getMessage();
            }
		}
	}
