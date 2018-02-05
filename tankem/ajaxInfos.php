<?php
	require_once("action/AjaxInfosAction.php");

	$action = new AjaxInfosAction();
	$action->execute();

	echo json_encode($action->result);
