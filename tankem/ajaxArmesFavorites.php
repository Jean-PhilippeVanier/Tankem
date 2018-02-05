<?php
	require_once("action/AjaxArmesFavoritesAction.php");

	$action = new AjaxArmesFavoritesAction();
	$action->execute();

	echo $action->result;
