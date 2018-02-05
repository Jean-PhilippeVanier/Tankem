<?php
	require_once("action/GestionPointsAction.php");

	$action = new GestionPointsAction();

	$action->execute();

	require_once("partial/header.php");
?>

<script type="text/javascript" src="js/gestionPoints.js"></script>

<div class="container">
	<h1>Gestion des Attributs</h1>
	<div class="row">
		<div class="col-md-8 gpStatsJoueur">
			<h4 class="text-center messageStats">Stats Joueur</h4>
			<div class="row">
				<div class="col-md-6 cold-md-push-6">
					<p id="gpHPTotal">/p>
				</div>
				<div class="col-md-6 cold-md-pull-6">
					<p id="gpDEGATTotal"></p>
				</div>
			</div>
			<div class="row">
				<div class="col-md-6 cold-md-push-6">
					<p id="gpDEPTotal"></p>
				</div>
				<div class="col-md-6 cold-md-pull-6">
					<p id="gpTIRTotal"></p>
				</div>
			</div>
		</div>

		<div class="col-md-6 gpModifStats">
			<h4 class="text-center">Modifications des Stats</h4>
			<div class="row">
				<div class="col-md-6 text-right">
					<p>Points disponibles : </p>
				</div>
				<div class="cold-md-6 text-left ptsDispo">
				</div>
			</div>
			<div class="row">
				<div class="col-md-6 text-right">
					<p>Niveau du joueur : </p>
				</div>
				<div class="cold-md-6 text-left niveauJ">
				</div>
			</div>
			<div class="row gpRowModifStat">
				<div class="col-md-1">
					<button class="btn btn-secondary" type="submit" onclick="modifHP(false)">-</button>
				</div>
				<div class="col-md-5">
					<p class="text-right">HP : </p>
				</div>
				<div class="col-md-5 text-left statModHP">
				</div>
				<div class="cold-md-1">
					<button class="btn btn-secondary" type="submit" onclick="modifHP(true)">+</button>
				</div>
			</div>
			<div class="row gpRowModifStat">
				<div class="col-md-1">
					<button class="btn btn-secondary" type="submit" onclick="modifDEGAT(false)">-</button>
				</div>
				<div class="col-md-5">
					<p class="text-right">DEGAT : </p>
				</div>
				<div class="col-md-5 text-left statModDEGAT">
				</div>
				<div class="cold-md-1">
					<button class="btn btn-secondary" type="submit" onclick="modifDEGAT(true)">+</button>
				</div>
			</div>
			<div class="row gpRowModifStat">
				<div class="col-md-1">
					<button class="btn btn-secondary" type="submit" onclick="modifDEP(false)">-</button>
				</div>
				<div class="col-md-5">
					<p class="text-right">DEPLACEMENT : </p>
				</div>
				<div class="col-md-5 text-left statModDEP">
				</div>
				<div class="cold-md-1">
					<button class="btn btn-secondary" type="submit" onclick="modifDEP(true)">+</button>
				</div>
			</div>
			<div class="row gpRowModifStat">
				<div class="col-md-1">
					<button class="btn btn-secondary" type="submit" onclick="modifTIR(false)">-</button>
				</div>
				<div class="col-md-5">
					<p class="text-right">VITESSE TIR : </p>
				</div>
				<div class="col-md-5 text-left statModTIR">
				</div>
				<div class="cold-md-1">
					<button class="btn btn-secondary" type="submit" onclick="modifTIR(true)">+</button>
				</div>
			</div>
			<button class="btn btn-primary col-md-10" type="submit" onclick="enregistrerStats()">Enregistrer les stats</button>
		</div>
	</div>
</div>

<?php
	require_once("partial/footer.php");