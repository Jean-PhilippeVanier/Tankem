<?php
	require_once("action/indexAction.php");

	$action = new IndexAction();

	$action->execute();

	require_once("partial/header.php");
?>

  <div class="py-5">
	<div class="container">
	  <div class="row">
		<div class="col-md-12">
		  <h1 class="display-1 text-center">Tank'Em<br></h1>
		</div>
	  </div>
	</div>
  </div>
  <div class="py-5 text-center">
	<div class="container">
	  <div class="row text-center">
		<div class="col-md-3 text-center mx-auto">
		  <form class="text-center" action ="index.php" method ="post">
	  		<?php 
				if ($action->wrongLogin) {
				?>
					<div class="error"><strong>Erreur : </strong>Connexion erronée</div>
					<?php
			  }
				if($action->banned){			
					?>
						<div class="error"><strong>Erreur : </strong>User is banned</div>
					<?php
					}
					?>
		
			<div class="form-group text-center w-100" id="login-email" > <label>Username</label> <input type="text" name = "username" class="form-control" placeholder="Enter Username"> </div>
			<div class="form-group text-center w-100" id="login-password" > <label class="text-center">Password</label> <input type="password" name = "pwd" class="form-control" placeholder="Password"> </div> 
	  <button type="submit" class="btn btn-primary text-center">Login</button>
	  </form>
			<p>Oublier votre mot de passe? Clickez <a href = "reset.php">ici!</a></p>
		  <p class="">Êtes-vous un nouvel utilisateur? Enregistrez-vous, c'est gratuit!<br></p><a href="Signup.php" class="btn btn-primary">Signup<br></a></div>
	  </div>
	</div>
  </div>

<?php
	require_once("partial/footer.php");