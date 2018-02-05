<?php
	require_once("action/DernieresPartiesAction.php");

	$action = new DernieresPartiesAction();

	$action->execute();

	require_once("partial/header.php");
?>

<script id="mon-template" type="x-template">
	<div class="row rowInfoPartie">
		<div class="col-md-12">
			<h4 class="text-center nomNiveau"></h4>
			<div class="row">
				<div class="col-md-6 cold-md-push-6 blocPartieJoueur">
					<p class="text-center nomJoueur1"></p>
					<img class="couleurTank1" src="images/tankAlpha.png" width="100px" height="100px"></img>
				</div>
				<div class="col-md-6 cold-md-pull-6 blocPartieJoueur">
					<p class="text-center nomJoueur2"></p>
					<img class="couleurTank2"  src="images/tankAlpha.png" width="100px" height="100px"></img>
				</div>
			</div>
			<h4 class="text-center vainqueur"></h4>
		</div>
	</div>
</script>

<script type="text/javascript" src="js/dernieresPartiesJS.js"></script>

<div class="container">
	<h1>Dernières Parties</h1>
	<div id="contDernPart">
		<!--<div class="row rowInfoPartie">
			<div class="col-md-12">
				<h4 class="text-center">NOM DU NIVEAU</h4>
				<div class="row">
					<div class="col-md-6 cold-md-push-6 blocPartieJoueur">
						<p class="text-center">NOM DU JOUEUR1</p>
						<p>TANK ET COULEUR DU JOUEUR1</p>
					</div>
					<div class="col-md-6 cold-md-pull-6 blocPartieJoueur">
						<p class="text-center">NOM DU JOUEUR2</p>
						<p>TANK ET COULEUR DU JOUEUR2</p>
					</div>
				</div>
				<h4 class="text-center">VAINQUEUR</h4>
			</div>
		</div>-->
	</div>
</div>

<?php
	require_once("partial/footer.php");