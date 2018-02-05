<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" type="text/css">
  <link rel="stylesheet" href="css/Untitled.css" type="text/css"> </head>
	<script type="text/javascript" src="js/jquery-3.2.1.min.js"></script>
	<script type="text/javascript">
		if (top != self) top.location.replace(self.location.href); 
	</script> 
<body class="mx-auto">
  <nav class="navbar navbar-expand-md navbar-light bg-faded">
	<div class="container">
	  <a class="navbar-brand" href="#"><br></a> <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				  <span class="navbar-toggler-icon"></span>
			   </button>
	  <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
		<ul class="navbar-nav ">
			<?php
				if($action->isLoggedIn()){
				?>
		  		<li class="nav-item"> <p class="nav-link"> Bienvenue, <?=$_SESSION["Username"]?>! </p> </li>
					<li class="nav-item"> <a class="nav-link" href="Infos.php">Infos</a> </li>
			 		<li class="nav-item"> <a class="nav-link" href="gestionPoints.php">Gestion des Attributs</a> </li>
				<?php
				}
				else{
				?>
		  		<li class="nav-item"> <a class="nav-link" href="index.php">Home</a> </li>
				<?php
				}
			?>
			<li class="nav-item"> <a class="nav-link" href="hallOfFame.php">Hall of Fame</a> </li>
			<li class="nav-item"> <a class="nav-link" href="dernieresParties.php">Dernières Parties</a> </li>
		  <li class="nav-item"> <a class="nav-link" href="replay.php">Replay</a> </li>
  		<li class="nav-item"> <a class="nav-link" href="search.php">Recherche</a> </li>
			<?php
					if ($action->isLoggedIn()) {
			?>
					<li class ="nav-item"><a class="nav-link"href="?logout=true">Logout</a></li>
			<?php
					}
			?>
		</ul>
	  </div>
	</div>
  </nav>
