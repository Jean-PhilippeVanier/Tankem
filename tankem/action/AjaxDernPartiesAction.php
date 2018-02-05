<?php
	require_once("action/CommonAction.php");

	class AjaxDernPartiesAction extends CommonAction{
		public $result = "Aucun résultat des dernières parties";

		public function __construct() {
			parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		}

		protected function executeAction() {
			try{
				$this->connection = Connection::getConnection();
				$statement = $this->connection->prepare("SELECT editor_niveau.name NomNiveau, player1.username NomJoueur1, player1.couleurTank CouleurTank1, player2.username NomJoueur2, player2.couleurTank CouleurTank2, gagnant.username NomGagnant FROM partie JOIN editor_niveau ON partie.idNiveau = editor_niveau.id JOIN joueur player1 ON partie.idJoueur1 = player1.id JOIN joueur player2 ON partie.idJoueur2 = player2.id JOIN joueur gagnant ON partie.idGagnant = gagnant.id WHERE ROWNUM <= 5 ORDER BY partie.id DESC");
				$statement->execute();
				$this->rows = $statement->fetchall(PDO::FETCH_ASSOC);
				$this->result = json_encode($this->rows);
				Connection::closeConnection();
			}catch(PDOException $e){
				echo "Échec lors de la requête : " + $e->getMessage();
			}
		}
	}
