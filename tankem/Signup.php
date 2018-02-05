<?php
	require_once("action/signupAction.php");

	$action = new SignupAction();

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
  <div class="py-5 mx-auto text-center bg-faded" id="mainContainer">
	<div class="w-100 container">
	  <div class="row text-center w-100 mx-auto" id="fixedcontainer">
		<div class="col-md-11 text-center mx-auto">
		<?php
				if ($action->wrongInfo) {
		?>
				<div class="error"><strong>Erreur : </strong>"<?=$action->errorMessage?>"</div>
		<?php
				}
		?>
		<?php
				if ($action->rightInfo) {
		?>
				<div class="success"><strong>Succès! : </strong>"<?=$action->errorMessage?>"</div>
		<?php
				}
		?>

		  <form class="" action ="Signup.php" method ="post">
			<div class="form-group w-25" id="signupemail"> <label>Email address</label> <input type="email" name="fieldEmail" class="form-control" placeholder="Enter email"> </div>
			<div class="form-group w-25" id="signupPrenom"> <label>Prenom<br></label> <input type="text" name="fieldPrenom" class="form-control" placeholder="Prenom"> </div>
			<div class="form-group w-25" id="signupPassword"> <label>Password</label> <input type="password" name="fieldPassword" class="form-control" placeholder="Password"> </div>
			<div class="form-group w-25" id="nom"> <label>Nom<br></label> <input type="text" name="fieldNom" class="form-control" placeholder="Nom"> </div>
			<div class="form-group w-25" id="reEnterPassword"> <label>Re-enter&nbsp;Password</label> <input type="password" name="fieldConfirmPassword" class="form-control" placeholder="Re-enter Password"> </div>
			<div class="form-group w-25" id="signupUsername"> <label>Nom utilisateur</label> <input type="text" name="fieldUsername" class="form-control" placeholder="Nom utilisateur"> </div>
			<div class="form-group w-25" id="registerColor"> <label>Couleur de tank voulue</label> <input type="color" name="fieldColor" class="form-control"> </div> 
			<button type="submit" class="btn btn-primary">Register</button>
			</form>
		</div>
	  </div>
	</div>
  </div>
  <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js"></script>
  <script src="https://pingendo.com/assets/bootstrap/bootstrap-4.0.0-alpha.6.min.js"></script>
</body>

</html>