<?php
	require_once("CommonAction.php");
	require_once("DAO/EnregistrementDAO.php");

	class AjaxEnregistrement extends CommonAction{
		public $result;

		 public function __construct() {
			 parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		 }

		 protected function executeAction() {
			 $this->DAO = new EnregistrementDAO();
			 $this->result = $this->DAO->read();
		}
	}