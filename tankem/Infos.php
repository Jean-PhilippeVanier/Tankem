<?php
	require_once("action/InfosAction.php");

	$action = new InfosAction();

	$action->execute();

	require_once("Partial/header.php");
	
?>
<script type="text/javascript" src="js/InfosJS.js"></script>
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
		  <form class="" action ="Infos.php" method ="post">
			<div class="form-group w-25" id="labelEmail"> <label>Email address</label> <input type="email" id="editEmail" name="editEmail" class="form-control" placeholder="Enter email"> </div>
			<div class="form-group w-25" id="labelPrenom"> <label>Prenom<br></label> <input type="text" id="editPrenom" name="editPrenom" class="form-control" placeholder="Prenom"> </div>
			<div class="form-group w-25" id="labelPassword"> <label>Password</label> <input type="password" name="editPassword" class="form-control" placeholder="Password"> </div>
			<div class="form-group w-25" id="labelNom"> <label>Nom<br></label> <input type="text" id="editNom" name="editNom" class="form-control" placeholder="Nom"> </div>
			<div class="form-group w-25" id="labelReEnterPassword"> <label>Re-enter&nbsp;Password</label> <input type="password" name="editConfirmPassword" class="form-control" placeholder="Re-enter Password"> </div>
			<div class="form-group w-25" id="labelUsername"> <label>Nom utilisateur</label> <input type="text" id="editUsername" name="editUsername" class="form-control" placeholder="Nom utilisateur"> </div>
			<div class="form-group w-25" id="labelColor"> <label>Couleur de tank voulue</label> <input type="color" id="editColor" name="editColor" class="form-control"> </div> 
			<button type="submit" class="btn btn-primary">Update</button>
			</form>
		</div>
	  </div>
	</div>
  </div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js"></script>
  <script src="https://pingendo.com/assets/bootstrap/bootstrap-4.0.0-alpha.6.min.js"></script>
</body>

</html>