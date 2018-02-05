const MAX_POINTS = 30;
const AJOUT_HP = 10;
const AJOUT_DEGAT = 10;
const AJOUT_DEP = 5;
const AJOUT_TIR = 10;

var joueur = null;

window.onload = function(){
	//Commence par loader les infos de joueur
	retrieveInfoJoueur();
}

function initStats(){
	document.querySelector(".niveauJ").innerHTML = joueur.niveau;
	retrieveHpTot(); //On peut pas retourner le hp total tout de suite vu que l'hp original des tanks se retrouve dans une autre table de BD
	document.getElementById("gpDEGATTotal").innerHTML = "BONUS DÉGAT : " + calcDegatTot().toFixed(2) + "%";
	document.getElementById("gpDEPTotal").innerHTML = "BONUS VITESSE DÉPLACEMENT : " + calcDepTot().toFixed(2) + "%";
	document.getElementById("gpTIRTotal").innerHTML = "BONUS VITESSE TIR : " + calcTirTot().toFixed(2) + "%";
	document.querySelector(".statModHP").innerHTML = joueur.hp;
	document.querySelector(".statModDEGAT").innerHTML = joueur.degat;
	document.querySelector(".statModDEP").innerHTML = joueur.deplacement;
	document.querySelector(".statModTIR").innerHTML = joueur.tir;
	document.querySelector(".ptsDispo").innerHTML = joueur.calcPtsDepenser();
}

/************************************
	FONCTIONS POUR MODIFIER LES STATS
************************************/

function modifHP(plus){
	if(plus && joueur.calcPtsDepenser() > 0 && joueur.hp < MAX_POINTS)
		joueur.modifHP(++joueur.hp);
	else if(!plus && joueur.hp > 0)
		joueur.modifHP(--joueur.hp);
	document.querySelector(".statModHP").innerHTML = joueur.hp;
	document.querySelector(".ptsDispo").innerHTML = joueur.calcPtsDepenser();
}

function modifDEGAT(plus){
	if(plus && joueur.calcPtsDepenser() > 0 && joueur.degat < MAX_POINTS)
		joueur.modifDEGAT(++joueur.degat);
	else if(!plus && joueur.degat > 0)
		joueur.modifDEGAT(--joueur.degat);
	document.querySelector(".statModDEGAT").innerHTML = joueur.degat;
	document.querySelector(".ptsDispo").innerHTML = joueur.calcPtsDepenser();
}

function modifDEP(plus){
	if(plus && joueur.calcPtsDepenser() > 0 && joueur.deplacement < MAX_POINTS)
		joueur.modifDEP(++joueur.deplacement);
	else if(!plus && joueur.deplacement > 0)
		joueur.modifDEP(--joueur.deplacement);
	document.querySelector(".statModDEP").innerHTML = joueur.deplacement;
	document.querySelector(".ptsDispo").innerHTML = joueur.calcPtsDepenser();
}

function modifTIR(plus){
	if(plus && joueur.calcPtsDepenser() > 0 && joueur.tir < MAX_POINTS)
		joueur.modifTIR(++joueur.tir);
	else if(!plus && joueur.tir > 0)
		joueur.modifTIR(--joueur.tir);
	document.querySelector(".statModTIR").innerHTML = joueur.tir;
	document.querySelector(".ptsDispo").innerHTML = joueur.calcPtsDepenser();
}

/************************************
	FONCTIONS POUR CALCULER LES STATS
************************************/

function calcHpTot(hp){
	return hp / 100 * (100 + AJOUT_HP * joueur.hp);
}

function calcDegatTot(){
	return AJOUT_DEGAT * joueur.degat;
}

function calcDepTot(){
	return AJOUT_DEP * joueur.deplacement;
}

function calcTirTot(){
	var tir = 100;
	for(var i = 0; i < joueur.tir; ++i){
		tir = tir / 100 * (100 - AJOUT_TIR);
	}
	return 100 - tir;
}

function retrieveHpTot(){
	//Recherche dans une autre table l'hp original des tanks
	var pts = 0
	$.ajax({
		type : "POST",
		url : "ajaxPtsVie.php",
		data : {

		}
	})
	.done(function(data){
		var pts = JSON.parse(data);
		document.getElementById("gpHPTotal").innerHTML = "HP TOTAL : " + calcHpTot(pts[0].VIE).toFixed(2);
	})
}

function retrieveInfoJoueur(){
	$.ajax({
		type : "POST",
		url : "ajaxStatsJoueur.php",
		data : {

		}
	})
	.done(function(data){
		//Quand tout est loader, créer un nouveau joueur et initier laffichage des stats
		var tmpJ = JSON.parse(data);
		joueur = new Joueur(parseInt(tmpJ[0].VIE), parseInt(tmpJ[0].FORCE), parseInt(tmpJ[0].AGILITE), parseInt(tmpJ[0].DEXTERITE), parseInt(tmpJ[0].NIVEAU));
		initStats();
	})
}

function enregistrerStats(){
	$.ajax({
		type : "POST",
		url : "ajaxEnregistrerStats.php",
		data : {
			hp : joueur.hp,
			degat : joueur.degat,
			deplacement : joueur.deplacement,
			tir : joueur.tir,
			niveau : joueur.niveau
		}
	})
	.done(function(data){
		document.querySelector(".messageStats").innerHTML = "Stats Joueur - Enregistré!";
		retrieveInfoJoueur();
		setTimeout(function(){
			document.querySelector(".messageStats").innerHTML = "Stats Joueur";
		},2000);
	})
}

/********************
 CLASSES
********************/

class Joueur{
	constructor(hp, degat, deplacement, tir, niveau){
		this.hp = hp;
		this.degat = degat;
		this.deplacement = deplacement;
		this.tir = tir;
		this.niveau = niveau;
	}

	modifHP(nouvHP){
		this.hp = nouvHP;
	}

	modifDEGAT(nouvDG){
		this.degat = nouvDG;
	}

	modifDEP(nouvDEP){
		this.deplacement = nouvDEP;
	}

	modifTIR(nouvTIR){
		this.tir = nouvTIR;
	}

	calcPtsDepenser(){
		var pts = this.niveau * 5 - (this.hp + this.degat + this.deplacement + this.tir);
		if(pts < 0)
			pts = 0;
		return pts;
	}
}

/*
TO-DO
Faire en sorte qu'on utilise les données du joueur pour voir les infos.
Mettre un bouton d'enregistrement et permettre au joueur d'renregistrer ces données.
Faire en sorte que seul ceux qui sont connectés au site peuvent accéder à cette page.
*/