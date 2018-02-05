<?php
	require_once("action/AjaxSearchAction.php");

	$action = new AjaxSearchAction();
	$action->execute();

	echo $action->result;
