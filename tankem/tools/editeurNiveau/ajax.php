<?php
    require_once("action/AjaxAction.php");

    $action = new AjaxAction();
    $action->execute();

	echo json_encode($action->result);
?>
