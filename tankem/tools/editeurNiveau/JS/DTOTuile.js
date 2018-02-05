class DTOTuile{
	constructor(posX, posY, type, hasTree){
		this.posX = posX;
		this.posY = posY;
		this.idNiveau = 0;
		this.type = type;
		this.hasTree = hasTree;
	}

	setId(id){
		this.idNiveau = id;
	}
}