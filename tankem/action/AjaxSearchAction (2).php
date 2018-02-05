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
                $this->connection = new PDO("oci:dbname=DECINFO", "e1384492", "C");
                $this->connection->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
                $this->connection->setAttribute(PDO::ATTR_EMULATE_PREPARES,false);
                $statement = $this->connection->prepare("SELECT * FROM joueur WHERE ingamename LIKE ?");
                $statement->execute(Array($str));
                $this->row = $statement->fetchall(PDO::FETCH_ASSOC);
                // $this->result = $str;
                $this->result = json_encode($this->row);
            }catch(PDOException $e){
                echo 'Échec lors de la connexion : ' . $e->getMessage();
            }
		}
	}
