<?php
	require_once("action/AjaxPtsVieAction.php");

	$action = new AjaxPtsVieAction();
	$action->execute();

	echo $action->result;
