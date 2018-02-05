<?php
    require_once("action/AjaxEnregistrement.php");

    $action = new AjaxEnregistrement();
    $action->execute();

	echo json_encode($action->result);