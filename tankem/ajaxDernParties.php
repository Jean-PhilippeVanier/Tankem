<?php
	require_once("action/AjaxDernPartiesAction.php");

	$action = new AjaxDernPartiesAction();
	$action->execute();

	echo $action->result;