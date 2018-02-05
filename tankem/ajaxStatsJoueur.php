<?php
	require_once("action/AjaxStatsJoueurAction.php");

	$action = new AjaxStatsJoueurAction();
	$action->execute();

	echo $action->result;
