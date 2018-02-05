// Variables globales
var canvas = null;
var ctx = null;
var scaleX = 0;
var scaleY = 0;
var game = null;
var play = false;
var iter = 0;
var tick = 0;

// Images
var block1 = new Image();
block1.src = "images/block1.png";
var block2 = new Image();
block2.src = "images/block2.jpg";
var block3 = new Image();
block3.src = "images/block3.jpg";
var block4 = new Image();
block4.src = "images/block4.png";

var tank1 = new Image();
tank1.src = "images/tank1.png";
var tank2 = new Image();
tank2.src = "images/tank2.png";
var projectile = new Image();
projectile.src = "images/projectile.png";
var explosion = new Image();
explosion.src = "images/explosion.png";

var mitraillette = new Image();
mitraillette.src = "images/mitraillette.png";
var shotgun = new Image();
shotgun.src = "images/shotgun.png";
var piege = new Image();
piege.src = "images/piege.png";
var guide = new Image();
guide.src = "images/guide.png";
var spring = new Image();
spring.src = "images/spring.png";
var grenade = new Image();
grenade.src = "images/grenade.png";

window.onload = function() {
	ajaxEnregistrement();
};

function ajaxEnregistrement() {
	$.ajax({
			type : "POST",
			url : "ajaxEnregistrement.php",
			data : {
			}
		})
		.done(function(data) {
			var listeParties = JSON.parse(data);
			var containerPage = document.getElementById("page-replay");
			containerPage.style.padding = "5%";
			console.log(listeParties);

			// Creation liste des parties
			var containerListe = document.createElement("ul");
			containerListe.style.width = "25%";
			containerListe.style.listStyle = "none";
			containerListe.style.float = "left";

			$(listeParties).each(function(i) {
				// Creation d'une nouvelle partie
				var partie = this;
				var nouvellePartie = document.createElement("li");
				var textNum = document.createTextNode("Partie #" + partie.id + " Map: " + partie.nom_map );
				var textDate = document.createTextNode("Crée le: " + partie.creation_date);
				nouvellePartie.appendChild(textNum);
				nouvellePartie.appendChild(document.createElement("br"));
				nouvellePartie.appendChild(textDate);

				//Style
				nouvellePartie.style.marginBottom = "1%";
				nouvellePartie.style.padding = "0.5%";
				nouvellePartie.style.color = "#fff";
				nouvellePartie.style.backgroundColor = "#666";
				nouvellePartie.onmouseover = function() {
					this.style.backgroundColor = "#333";
				}
				nouvellePartie.onmouseleave = function() {
					this.style.backgroundColor = "#666";
				}
				nouvellePartie.style.display = "block";

				// Event
				nouvellePartie.onmousedown = function(){updateGame(partie);}

				containerListe.appendChild(nouvellePartie);
			});

			containerPage.appendChild(containerListe);

			// Creation Canvas
			canvas = document.createElement("canvas");
			var canvasX = window.innerWidth*60/100
			var canvasY = window.innerHeight*80/100
			canvas.setAttribute("id", "canvas");
			canvas.setAttribute("width", canvasX);
			canvas.setAttribute("height", canvasY);
			canvas.style.backgroundColor = "#181818";
			canvas.style.float = "right";

			ctx = canvas.getContext('2d');

			containerPage.appendChild(canvas);

			// Modificateur du temps, play/slider
			var divTime = document.createElement("div");
			divTime.style.margin = "5% 0%";

			var button = document.createElement("button");
			button.setAttribute("id", "button");
			button.onclick = function(){buttonPlay();}
			button.innerHTML = "Play";
			button.style.width = "25%";

			var slider = document.createElement("input");
			slider.setAttribute("id", "slider");
			slider.setAttribute("type", "range");
			slider.setAttribute("min", "0");
			slider.setAttribute("max", "100");
			slider.setAttribute("value", "0");
			slider.style.margin = "0% 3%";
			slider.style.width = "69%"

			$(document).on('input', '#slider', function() {
				play = false;
				$("#button").html("Play");
				tick = this.value;
			});

			divTime.appendChild(button);
			divTime.appendChild(slider);
			containerListe.appendChild(divTime);
			
			// Info joueur
			var divInfos = document.createElement("ul");
			divInfos.style.margin = "5% 0%";

			var joueur1 = document.createElement("li");
			joueur1.setAttribute("id", "joueur1");
			joueur1.innerHTML = "Joueur 1, vie: 0/0";
			divInfos.appendChild(joueur1);

			var joueur2 = document.createElement("li");
			joueur2.setAttribute("id", "joueur2");
			joueur2.innerHTML = "Joueur 2, vie: 0/0";
			divInfos.appendChild(joueur2);

			containerListe.appendChild(divInfos);
			// Clear float
			var clear = document.createElement("p");
			clear.style.clear = "both";
			containerPage.appendChild(clear);
			drawGame();
		})
}

// button function
function buttonPlay(){
	if( game != null){
		if(play){
			play = false;
			$("#button").html("Play");
		}
		else {
			play = true;
			$("#button").html("Pause");
		}
	}
}

// Change les infos du replay pour avior celle de la derniere partie choisie.
function updateGame(partie){
	tick = 0;
	play = false;
	game = partie;
	$("#button").html("Play");
	$("#slider").attr({"max" : getGameMaxTime(game)});
}

// Tick. Loop qui dessinne chaque element du replay.
function drawGame(){
	iter++;
	$("#slider").val(tick);
	if(game != null && iter >= 5){
		iter = 0;
		drawMap(game.map);
		drawPlayerOne(game, tick);
		drawPlayerTwo(game, tick);
		drawWeapon(game,tick);
		drawProjectiles(game,tick);
		if(play){
			tick++;
		}
	}
	window.requestAnimationFrame(drawGame);
}

// Dessine la map dans le canvas selon les infos donnees
function drawMap(map){
	scaleX = ctx.canvas.width/map[0].length;
	scaleY = ctx.canvas.height/map.length;


	$(map).each(function(i){
		var y = this;
		$(y).each(function(j){
			var valeur = this[0];
			// case vide
			if(valeur == 1){
				ctx.drawImage(block1,j*scaleX,i*scaleY,scaleX,scaleY);
			}
			else if(valeur == 2){
				ctx.drawImage(block2,j*scaleX,i*scaleY,scaleX,scaleY);
			}
			else if(valeur == 3){
				ctx.drawImage(block3,j*scaleX,i*scaleY,scaleX,scaleY);
			}
			else if(valeur == 4){
				ctx.drawImage(block4,j*scaleX,i*scaleY,scaleX,scaleY);
			}

		});
	});
}

// Dessinne le joueur 1 ainsi que mettre a jour sa vie
function drawPlayerOne(game, time_sec){
	var arrayJoueur1 = game.arrayJoueur1;

	// Trouver infos au bon temps
	var joueur = infoAtTick(arrayJoueur1, tick);

	// afficher infos
	if(joueur){
		var orientation = joueur.orientation.replace(",",".");
		orientation = parseFloat(orientation);
		ctx.save();
		ctx.translate(positionX(joueur.pos_x, game.map[0].length),
						 positionY(joueur.pos_y, game.map.length));
		ctx.rotate((orientation*Math.PI/180) * 1);
		ctx.drawImage(tank1,
					-scaleX/2,
					-scaleY/2,
					scaleX,scaleY)
		ctx.restore();
		$("#joueur1").html("Tank rouge: " + game.nom_joueur1 + "<br/> vie: " + joueur.health + "/" + arrayJoueur1[0].health);
	}
	else{
		$("#joueur1").html("Tank rouge: " + game.nom_joueur1 + "<br/> vie: " + "0" + "/" + arrayJoueur1[0].health);
	}

}

// Dessinne le joueur 2 ainsi que mettre a jour sa vie
function drawPlayerTwo(game, time_sec){
	var arrayJoueur2 = game.arrayJoueur2;

	// Trouver infos au bon temps
	var joueur = infoAtTick(arrayJoueur2, tick);

	// afficher infos
	if(joueur){
		var orientation = joueur.orientation.replace(",",".");
		orientation = parseFloat(orientation);
		ctx.save();
		ctx.translate(positionX(joueur.pos_x, game.map[0].length),
						 positionY(joueur.pos_y, game.map.length));
		ctx.rotate((orientation*Math.PI/180) * 1);
		ctx.drawImage(tank2,
					-scaleX/2,
					-scaleY/2,
					scaleX,scaleY)
		ctx.restore();
		$("#joueur2").html("Tank bleu: " + game.nom_joueur2 + "<br/> vie: " + joueur.health + "/" + arrayJoueur2[0].health);
	}
	else{
		$("#joueur2").html("Tank bleu: " + game.nom_joueur2 + "<br/> vie: " + "0" + "/" + arrayJoueur2[0].health);
	}

}

// Dessinne les armes que les joueurs peuvent ramasser
function drawWeapon(game, time_sec){
	var arrayArmes = game.arrayArmes;

	// Trouver infos au bon temps
	var arme = infoAtTick(arrayArmes, tick);

	// afficher infos
	if(arme){
		if(arme.type_arme == "Mitraillette"){
			ctx.drawImage(mitraillette,
						positionX(arme.pos_x, game.map[0].length)-(scaleX/2),
						positionY(arme.pos_y, game.map.length)-(scaleY/2),
						scaleX,scaleY)
		}
		else if(arme.type_arme == "Guide"){
			ctx.drawImage(guide,
						positionX(arme.pos_x, game.map[0].length)-(scaleX/2),
						positionY(arme.pos_y, game.map.length)-(scaleY/2),
						scaleX,scaleY)
		}
		else if(arme.type_arme == "Piege"){
			ctx.drawImage(piege,
						positionX(arme.pos_x, game.map[0].length)-(scaleX/2),
						positionY(arme.pos_y, game.map.length)-(scaleY/2),
						scaleX,scaleY)
		}
		else if(arme.type_arme == "Shotgun"){
			ctx.drawImage(shotgun,
						positionX(arme.pos_x, game.map[0].length)-(scaleX/2),
						positionY(arme.pos_y, game.map.length)-(scaleY/2),
						scaleX,scaleY)
		}
		else if(arme.type_arme == "Spring"){
			ctx.drawImage(spring,
						positionX(arme.pos_x, game.map[0].length)-(scaleX/2),
						positionY(arme.pos_y, game.map.length)-(scaleY/2),
						scaleX,scaleY)
		}
		else if(arme.type_arme == "Grenade"){
			ctx.drawImage(grenade,
						positionX(arme.pos_x, game.map[0].length)-(scaleX/2),
						positionY(arme.pos_y, game.map.length)-(scaleY/2),
						scaleX,scaleY)
		}
		else{
			ctx.fillStyle="#333";
			ctx.fillRect(positionX(arme.pos_x, game.map[0].length)-(scaleX/4),
						positionY(arme.pos_y, game.map.length)-(scaleY/4),
						scaleX/2,scaleY/2)
		}

	}

}
// Dessinne les projectiles et leurs explosion
 function drawProjectiles(game, time){
	 var arrayProjectiles = game.arrayProjectiles;
	 var projectiles = [];

	 for(var i=0; i<arrayProjectiles.length; i++){
		 if(arrayProjectiles[i].time_sec == time){
			 projectiles.push(arrayProjectiles[i]);
		 }
	 }

	 if(projectiles.length > 0){
		 for(var j=0; j<projectiles.length; j++){
			 if(projectiles[j].en_mouvement == "1"){
				ctx.drawImage(projectile,
							positionX(projectiles[j].pos_x, game.map[0].length)-(scaleX/8),
							positionY(projectiles[j].pos_y, game.map.length)-(scaleY/8),
							scaleX/4,scaleY/4)
			 }
			 else{
				ctx.drawImage(explosion,
							positionX(projectiles[j].pos_x, game.map[0].length)-(scaleX/2),
							positionY(projectiles[j].pos_y, game.map.length)-(scaleY/2),
							scaleX,scaleY)
			 }
		 }
	 }
 }

// Retourne l'object d'un array au tick voulut
function infoAtTick(array, time){
	var result = false;

	for(var i=0; i<array.length; i++){
		if(array[i].time_sec == time){
			result = array[i];
			break;
		}
	}

	return result;

}

// Traduit la position X de Tankem pour qu'elle soit cmopatible avec le canvas
function positionX(posX,lengthX){
	var posX = posX.replace(",", ".");
	var totalX = parseFloat(posX) + lengthX;
	var width = ctx.canvas.width;

	return totalX*width/(lengthX*2);
}

// Traduit la position Y de Tankem pour qu'elle soit cmopatible avec le canvas
function positionY(posY,lengthY){
	var posY = posY.replace(",", ".");
	var totalY = parseFloat(posY) + lengthY;
	var height = ctx.canvas.height;

	return totalY*height/(lengthY*2);
}

// Retourte le nombre maximal de tick d'une partie
function getGameMaxTime(game){
	var result = 0;

	for( var i=0; i<game.arrayJoueur1.length; i++){
		var time = parseInt(game.arrayJoueur1[i].time_sec);
		if(result < time){
			result = time;
		}
	}

	for( var i=0; i<game.arrayJoueur2.length; i++){
		var time = parseInt(game.arrayJoueur2[i].time_sec);
		if(result < time){
			result = time;
		}
	}

	return result
}
