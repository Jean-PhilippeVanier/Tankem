window.onload = function(){
	ajaxDernParties();
}

function ajaxDernParties(){
	$.ajax({
		type : "POST",
		url : "ajaxDernParties.php",
		data : {

		}
	})
	.done(function(data){
		var template = document.querySelector("#mon-template").innerHTML;
		document.getElementById("contDernPart").innerHTML = "";
		var tabParties = JSON.parse(data);
		$(tabParties).each(function(i) {
			if(i == 5){
				return false;
			}
			var newElement = document.createElement("div");
			newElement.innerHTML = template;
			newElement.querySelector('.nomNiveau').innerHTML = "Nom du niveau : " + tabParties[i].NOMNIVEAU;
			newElement.querySelector('.nomJoueur1').innerHTML = "Nom du joueur 1 : " + tabParties[i].NOMJOUEUR1;
			newElement.querySelector('.couleurTank1').style="background-color:"+tabParties[i].COULEURTANK1;
			newElement.querySelector('.nomJoueur2').innerHTML = "Nom du joueur 2 : " + tabParties[i].NOMJOUEUR2;
			newElement.querySelector('.couleurTank2').style="background-color:"+tabParties[i].COULEURTANK2;			
			newElement.querySelector('.vainqueur').innerHTML = "Gagnant : " + tabParties[i].NOMGAGNANT;
			document.getElementById("contDernPart").appendChild(newElement);
		})
		setTimeout(function(){
			ajaxDernParties();
		}, 10000); //Reload la page chaque 10 secondes
	})
}