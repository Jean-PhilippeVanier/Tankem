var ctx = null
var niveau = null
var sizeTuile =50;
var longueurGrid = null;
var hauteurGrid = null;
var debX = null;
var debY = null;
var imgblock1 = new Image()
var imgblock2 = new Image()
var imgblock3 = new Image()
var imgblock4 = new Image()
var imgtree = new Image()
var selector = null;
var span = null;
var txtFocus = false;

window.onload = function(){

	ctx = document.getElementById("canvas").getContext("2d")
	niveau = new Niveau(12,12)
	document.getElementById("tailleX").value=niveau.tailleX
	document.getElementById("tailleY").value=niveau.tailleY
	span = document.getElementsByClassName("close")[0];

	imgblock1.src="images/block1.png"
	imgblock2.src="images/block2.jpg"
	imgblock3.src="images/block3.jpg"
	imgblock4.src="images/block4.png"
	imgtree.src="images/treeAlpha.png"

	longueurGrid = sizeTuile * niveau.tailleX;
	hauteurGrid = sizeTuile * niveau.tailleY;
	debX = (document.getElementById("canvas").width - longueurGrid) / 2;
	debY = (document.getElementById("canvas").height - hauteurGrid) / 2;

	selector = new Selector(0,0,sizeTuile);

	tick()
}

function tick(){

	ctx.clearRect(0,0,document.getElementById("canvas").width,document.getElementById("canvas").height)
	drawTiles();
	drawGrid();
	selector.tick();
	for (var i = 0; i < niveau.tabSpawn.length; i++) {
		niveau.tabSpawn[i].tick();
	}

	window.requestAnimationFrame(tick)
}

document.onkeydown = function (e) {
	if(document.activeElement.className != "input"){
		selector.updatePosition(e)
	}
}

function afficherErreur(erreur){
	var modal = document.getElementById("myModal");
	var message = document.getElementById("messageErreur");

	modal.style.display = "block";
	message.innerHTML = erreur;
}

window.onclick = function(e) {
	var result = null;
	if(e.target == span){
		var modal = document.getElementById("myModal");
		modal.style.display = "none";
	}
	else if(e.target == document.getElementById("sauvegarder")){
		result = envoyerTables();
	}

	if(result != null){
		if(typeof result == "string"){
			afficherErreur(result);
		}
		else{
			$.ajax({
				url: 'ajax.php',
				type: 'POST',
				data: {
					value:JSON.stringify(result)}
				}
			)
			.done(function() {
				afficherErreur == "Le niveau a été sauvegarder correctement!";
				console.log(JSON.stringify(result)); //ICI POUR LE DÉBUT DAO / DTO / PHP / WHATEVER
				console.log("success");
			})


		}
	}
}

function drawGrid(){
	ctx.strokeStyle = "black"
	for(var i = 0; i <= niveau.tailleY; ++i){
		ctx.beginPath();
		ctx.moveTo(debX,debY + sizeTuile * i);
		ctx.lineTo(debX + sizeTuile * niveau.tailleX, debY + sizeTuile * i);
		ctx.stroke();
	}
	for(var i = 0; i <= niveau.tailleX; ++i){
		ctx.beginPath();
		ctx.moveTo(debX + sizeTuile * i, debY);
		ctx.lineTo(debX + sizeTuile * i, debY + sizeTuile * niveau.tailleY);
		ctx.stroke();
	}
}

function drawTiles() {
	for(var y = 0; y < niveau.tailleY; ++y){
		for(var x = 0; x < niveau.tailleX; ++x){
			switch(niveau.tabTile[x][y].type){
				case 0:
					ctx.fillStyle = "grey"
					ctx.fillRect(debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile)
					break
				case 1:
					ctx.drawImage(imgblock1,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
					break
				case 2:
					ctx.drawImage(imgblock2,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
					break
				case 3:
					ctx.drawImage(imgblock3,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
					break
				case 4:
					ctx.drawImage(imgblock4,debX + x * sizeTuile, debY + y * sizeTuile, sizeTuile, sizeTuile )
					break
			}
			if(niveau.tabTile[x][y].hasTree){
				ctx.drawImage(imgtree, sizeTuile/4+ debX + x * sizeTuile, sizeTuile/4+ debY + y * sizeTuile, sizeTuile/2, sizeTuile/2)
			}
		}
	}
}

function clickButton(){
	var tailleXinput = parseInt(document.getElementById("tailleX").value)
	var tailleYinput = parseInt(document.getElementById("tailleY").value)

	if(tailleXinput < 6 || tailleXinput > 12 || isNaN(tailleXinput)){
		afficherErreur("La taille X doit être un nombre de 6 à 12!");
	} else if(tailleYinput < 6 || tailleYinput > 12 || isNaN(tailleYinput)){
		afficherErreur("La taille Y doit être un nombre de 6 à 12!");
	} else {
		niveau.setSize(tailleXinput, tailleYinput);
		longueurGrid = sizeTuile * niveau.tailleX;
		hauteurGrid = sizeTuile * niveau.tailleY;
		debX = (document.getElementById("canvas").width - longueurGrid) / 2;
		debY = (document.getElementById("canvas").height - hauteurGrid) / 2;
	}
}

function envoyerTables(){
	var dtoNiveau; //Le niveau qu'on envoie à la BD
	var dtoTuile; //La table de tuiles que l'on envoie à la BD
	var dtoSpawn; //la table de spawn que on envoit à la BD
	var tabReturn = null; //La table que l'on return qui contient les infos des 2 variables précédentes

	//Création du'ne variable de la date actuelle pour Oracle
	var date = new Date();
	date = date.getUTCFullYear() + '-' +
		('00' + (date.getUTCMonth()+1)).slice(-2) + '-' +
		('00' + date.getUTCDate()).slice(-2) + ' ' +
		('00' + date.getUTCHours()).slice(-2) + ':' +
		('00' + date.getUTCMinutes()).slice(-2) + ':' +
		('00' + date.getUTCSeconds()).slice(-2);

	dtoNiveau = new DTONiveau(
		document.getElementById("nomNiveau").value,
		date,
		document.getElementById("status").value,
		niveau.tailleX,
		niveau.tailleY,
		parseInt(document.getElementById("itemDelMin").value),
		parseInt(document.getElementById("itemDelMax").value)
	)

	dtoTuile = [];
	for (var i = 0; i < niveau.tailleY; ++i){
		for(var j = 0; j < niveau.tailleX; ++j){
			if(niveau.tabTile[i][j].type != 0){
				dtoTuile.push(new DTOTuile(niveau.tabTile[i][j].x,niveau.tabTile[i][j].y,niveau.tabTile[i][j].type,niveau.tabTile[i][j].hasTree));
			}
		}
	}

	dtoSpawn = [];
	for(var i = 0; i < niveau.tabSpawn.length; ++i){
		if(niveau.tabSpawn[i].isActive){
			dtoSpawn.push(new DTOSpawn(niveau.tabSpawn[i].x, niveau.tabSpawn[i].y, niveau.tabSpawn[i].idPlayer));
		}
	}

	//Algorithme pour mettre a jour l'id des joueurs
	for(var i = 0; i < dtoSpawn.length; ++i){
		var present = false;
		for(var j = 0; j < dtoSpawn.length; ++j){
			if(dtoSpawn[j].no_player == i + 1){
				present = true;
			}
		}
		if(present == false){
			for(var j = i; j < dtoSpawn.length; ++j){
				--dtoSpawn[j].no_player;
			}
		}
	}

	//Vérifications
	if(dtoNiveau.name == ""){
		tabReturn = "Votre niveau a besoin d'un nom!";
	} else if(dtoNiveau.length > 20){
		tabReturn = "Votre nom de niveau doit être moins de 20 caractères!";  
	} else if(dtoNiveau.itemDelMin == ""){
		tabReturn = "Votre niveau a besoin d'un délai minimal des objets!";
	} else if(isNaN(dtoNiveau.itemDelMin)){
		tabReturn = "Votre délai minimal des objets doit être un nombre!";
	} else if(dtoNiveau.itemDelMax == ""){
		tabReturn = "Votre niveau a besoin d'un délai maximal des objets!";
	} else if(isNaN(dtoNiveau.itemDelMax)){
		tabReturn = "Votre délai maximal des objets doit être un nombre!";
	} else if (parseInt(dtoNiveau.itemDelMin) > parseInt(dtoNiveau.itemDelMax)){
		tabReturn = "Votre délai maximal des objets doit être plus grand que votre délai minimal des objets";
	} else if(dtoSpawn.length < 2){
		tabReturn = "Il n'y a pas assez de joueur sur le terrain!";
	}

	//S'il n'y a pas de strings dans tabReturn, il n'y a donc pas de problème, tabReturn sera un tableau des infos
	if(tabReturn == null){
		tabReturn = [dtoNiveau, dtoTuile, dtoSpawn];
	}

	return tabReturn;
}
