<?php

	require_once("action/DAO/Connection.php");

class DAOeditorOracle {
	private $connection;

	public function __construct() {
		$this->connection = Connection::getConnection();
	}

	public function create($DTOmap){
		// Creation map
		try{
			$statementMap = $this->connection->prepare("INSERT INTO editor_niveau (
														name,
														creation_date,
														status,
														size_x,
														size_y,
														item_delay_min,
														item_delay_max)
														VALUES (?,?,?,?,?,?,?)");


			$statementMap->bindParam(1,$DTOmap->name);
			$statementMap->bindParam(2,$DTOmap->creation_date);
			$statementMap->bindParam(3,$DTOmap->status);
			$statementMap->bindParam(4,$DTOmap->size_x);
			$statementMap->bindParam(5,$DTOmap->size_y);
			$statementMap->bindParam(6,$DTOmap->item_delay_min);
			$statementMap->bindParam(7,$DTOmap->item_delay_max);
			$statementMap->execute();

			// Avoir le id du tableau cree
			try{
				$statementId = $this->connection->prepare("SELECT id FROM editor_niveau
															WHERE name = ? and creation_date = ?");
				$statementId->bindParam(1,$DTOmap->name);
				$statementId->bindParam(2,$DTOmap->creation_date);
				$statementId->setFetchMode(PDO::FETCH_ASSOC);
				$statementId->execute();
				$DTOmap->id_niveau = array_values($statementId->fetch())[0];
			}catch(PDOException $e){
				echo 'id error';
			}
		}catch(PDOException $e){
			echo 'Valeurs invalides lors de la sauvegarde de la map';
			echo $e;
		}

		// Creation tuiles
		foreach( $DTOmap->array_tuiles as $tuile ){
			try{
				$statementTuiles = $this->connection->prepare("INSERT INTO editor_tuile (
															pos_x,
															pos_y,
															id_niveau,
															type_tuile,
															has_tree)
															VALUES (?,?,?,?,?)");
				$statementTuiles->bindParam(1,$tuile->posX);
				$statementTuiles->bindParam(2,$tuile->posY);
				$statementTuiles->bindParam(3,$DTOmap->id_niveau);
				$statementTuiles->bindParam(4,$tuile->type);
				$statementTuiles->bindParam(5,$tuile->hasTree);
				$statementTuiles->execute();
			}catch(PDOException $e){
				echo "Erreur tuile pos :" . $tuile->posX . "/" . $tuile->posY;
				echo $e;
			}
		}

		// Creation spawn
		foreach( $DTOmap->array_spawns as $spawn ){
			try{
				$statementSpawn = $this->connection->prepare("INSERT INTO editor_spawn (
															pos_x,
															pos_y,
															id_niveau,
															no_player)
															VALUES (?,?,?,?)");
				$statementSpawn->bindParam(1,$spawn->posX);
				$statementSpawn->bindParam(2,$spawn->posY);
				$statementSpawn->bindParam(3,$DTOmap->id_niveau);
				$statementSpawn->bindParam(4,$spawn->no_player);
				$statementSpawn->execute();
			}catch(PDOException $e){
				echo "Erreur spawn pos :" . $tuile->posX . "/" . $tuile->posY;
				echo $e;
			}
		}
	}
}
