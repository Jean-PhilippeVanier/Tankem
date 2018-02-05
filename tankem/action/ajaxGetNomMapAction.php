<?php
	require_once("action/CommonAction.php");

	class AjaxGetNomMapAction extends CommonAction{
		public $result = "QWERTYUIOP";

		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {
			$id = $_POST["idNiveau"];
			try{
				$this->connection = new PDO("oci:dbname=DECINFO", "e1384492", "C");
                $this->connection->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
                $this->connection->setAttribute(PDO::ATTR_EMULATE_PREPARES,false);
				$statement = $this->connection->prepare("SELECT Name FROM editor_niveau WHERE id = ?");
				$statement->execute(Array($id));
				$this->row = $statement->fetchall(PDO::FETCH_ASSOC);
                $this->result = $this->row;
				Connection::closeConnection();
			}catch(PDOException $e){
				echo 'Échec lors de la connection : ' + $e->getMessage();
			}
		}
	}
