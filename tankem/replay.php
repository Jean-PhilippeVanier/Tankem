<?php
	require_once("action/replayAction.php");

	$action = new ReplayAction();

	$action->execute();

	require_once("partial/header.php");
?>
<script type="text/javascript" src="js/replay.js"></script>
<div id="page-replay"></div>
<?php
	require_once("partial/footer.php");
?>