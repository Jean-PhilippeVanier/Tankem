<?php
	require_once("action/AjaxJoueursAction.php");

	$action = new AjaxJoueursAction();
	$action->execute();

	echo $action->result;