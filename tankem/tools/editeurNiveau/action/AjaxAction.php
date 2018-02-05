<?php
	require_once("action/CommonAction.php");
	require_once("action/DTO/DTOMap.php");
	require_once("action/DAO/DAOeditorOracle.php");

	class AjaxAction extends CommonAction{
		 public function __construct() {
			 parent::__construct(CommonAction::$VISIBILITY_PUBLIC);
		 }

			 protected function executeAction() {

				 $this->result = json_decode($_POST["value"]);
				//  $this->result = $this->result[0]->sizeX;
				 $this->DTOmap = new DTOmap(0,$this->result[0]->name,
					 $this->result[0]->date,
				 	 $this->result[0]->status,
				 	 $this->result[0]->sizeX,
				 	 $this->result[0]->sizeY,
				 	 $this->result[0]->itemDelMin,
				 	 $this->result[0]->itemDelMax,
				 	 $this->result[1],
					 $this->result[2]
				 );
				 $this->DAO = new DAOeditorOracle();
				 $this->DAO->create($this->DTOmap);

				//  $this->result = $this->DTOmap;
		 }
	}
