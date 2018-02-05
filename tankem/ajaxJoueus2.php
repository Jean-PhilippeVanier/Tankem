<?php
	require_once("action/AjaxJoueursAction2.php");

	$action = new AjaxJoueursAction2();
	$action->execute();

	echo $action->result;