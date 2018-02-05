<?php
	session_start();
	require_once("action/DAO/Connection.php");

	abstract class CommonAction {
		public static $VISIBILITY_MEMBER = 1;
		public static $VISIBILITY_PUBLIC = 0;

		private $visibility = null;

		public function __construct($visibility) {
			$this->visibility = $visibility;
		}

		public function execute() {
			if (isset($_GET["logout"])) {
				session_unset();
				session_destroy();
				session_start();
			}

			if ($this->visibility > CommonAction::$VISIBILITY_PUBLIC) {
				if (!isset($_SESSION["key"])) {
					header("location:index.php");
					exit;
				}
			}

			$this->executeAction();
			Connection::closeConnection();
		}

		abstract protected function executeAction();
	}
