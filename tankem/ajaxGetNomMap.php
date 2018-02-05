<?php
	require_once("action/AjaxGetNomMapAction.php");

	$action = new AjaxGetNomMapAction();
	$action->execute();

	echo json_encode($action->result);
