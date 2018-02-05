<?php
	require_once("action/HallOfFameAction.php");

	$action = new HallOfFameAction();

	$action->execute();

	require_once("partial/header.php");
?>

<script id="mon-template" type="x-template">
    <div class="row rowInfoJoueur">
		<div class="col-md-12">
			<div class="row">
				<div class="col-md-1 cold-md-push-11">
					<h4 class="numero"></h4>
				</div>
				<div class="col-md-11 cold-md-pull-1">
					<h4 class="text-center nomJoueur"></h4>
				</div>
			</div>
			<div class="row">
				<div class="col-md-6 cold-md-push-6">
					<p class="niveauFavori"></p>
					<p class="ratio"></p>
					<p class="nbPartiesJoues"></p>
				</div>
				<div class="col-md-6 cold-md-push-6">
					<img class="text-center imageTank" src="images/tankAlpha.png" width="100px" height="100px"></img>
				</div>
			</div>
		</div>
	</div>
</script>

<script type="text/javascript" src="js/hallOfFameJS.js"></script>
<script type="text/javascript" src="js/calculateName.js"></script>


<div class="container">
	<h1>Hall of Fame</h1>
	<div id="contHallOfFame">
	</div>
</div>

<?php
	require_once("partial/footer.php");