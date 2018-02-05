<?php
	require_once("action/AjaxEnregistrerStatsAction.php");

	$action = new AjaxEnregistrerStatsAction();
	$action->execute();

	echo $action->result;
