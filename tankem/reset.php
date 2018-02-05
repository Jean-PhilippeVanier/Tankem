<?php
	require_once("action/resetAction.php");

	$action = new ResetAction();

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
		  <form class="text-center" action ="reset.php" method ="post">
	  		<?php 
				if ($action->wrongEmail) {
				?>
					<div class="error-div"><strong>Erreur : </strong>Cette adresse e-mail n'est pas dans nos données.</div><p></p>
					<?php
			  }			
				?>
			<?php 
			if ($action->rightEmail) {
			?>
				<div class="error-div"><strong>Nous avons bien reçu votre demande, vous devriez recevoir un message avc votre nouveau mot de passe.</strong></div><p></p>
				<?php
			}			
			?>

			<div class="form-group text-center w-100" id="resetEmail" > <label>E-mail</label> <input type="email" id = "resetEmail" name = "resetEmail" class="form-control" placeholder="Enter your email"> </div>
	 		<button type="submit" class="btn btn-primary text-center">Submit</button>
	  </form>
	  </div>
	</div>
  </div>

<?php
	require_once("partial/footer.php");