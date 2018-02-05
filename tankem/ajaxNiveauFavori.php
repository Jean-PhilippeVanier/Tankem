<?php
	require_once("action/AjaxNiveauFavoriAction.php");

	$action = new AjaxNiveauFavoriAction();
	$action->execute();

	echo $action->result;
