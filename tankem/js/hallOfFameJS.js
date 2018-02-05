window.onload = function(){
	//Commence par cherche les infos nécessaires des joueurs
	ajaxJoueurs();
}

function afficherJoueurs(tabJoueur) {
	var template = document.querySelector("#mon-template").innerHTML;
	document.getElementById("contHallOfFame").innerHTML = "";
	$(tabJoueur).each(function(i) {
		if(i == 10){
			return false;
		}
		var newElement = document.createElement("div");
		newElement.innerHTML = template;
		newElement.querySelector('.numero').innerHTML = i + 1;
		var nomCalc = calculateName(tabJoueur[i]);
		if(nomCalc != " ") //Si le calculateName ne renvoit pas un vide, rajoute une virgule
			nomCalc = ", " + nomCalc;
		newElement.querySelector('.nomJoueur').innerHTML = "Nom : " + tabJoueur[i].USERNAME + nomCalc;
		newElement.querySelector('.ratio').innerHTML = "Ratio victoires/défaites : " + (ratio(tabJoueur[i]) * 100).toFixed(2) + "%";
		newElement.querySelector('.nbPartiesJoues').innerHTML = "Parties jouées : " + tabJoueur[i].PARTIEJOUE;
		newElement.querySelector('.imageTank').style="background-color:"+tabJoueur[i].COULEURTANK;
		document.getElementById("contHallOfFame").appendChild(newElement);
		ajaxNiveauFavori(tabJoueur[i].ID, i); //Fait un autre appel pour le niveau favori de joueur
	});
}

function ajaxNiveauFavori(id, idNode) {
	$.ajax({
		type : "POST",
		url : "ajaxNiveauFavori.php",
		data : {
			idJoueur: id
		}
	})
	.done(function(data){
		var niveauPref = JSON.parse(data);
		console.log(niveauPref);
		if(niveauPref.length == 0){
			niveauPref = "Aucun niveau préféré!"
		}
		else{
			niveauPref = "Niveau préféré : " + niveauPref[0].NOMNIVEAU;
		}
		document.getElementById("contHallOfFame").children[idNode].querySelector('.niveauFavori').innerHTML = niveauPref;
	})
}

function ajaxJoueurs() {
	//Affiche tous les infos des joueurs
	$.ajax({
		type : "POST",
		url : "ajaxJoueurs.php",
		data : {

		}
	})
	.done(function(data) {
		//Quicksort pour voir quel joueur à le meilleur ratio
		tabJoueur = JSON.parse(data);
		tabJoueur = quickSort(tabJoueur, 0, tabJoueur.length-1);
		tabJoueur.reverse(); //Pour inverser l'array
		afficherJoueurs(tabJoueur); //Afficher sur la page les joueurs
	})
}


//SImple fonction pour retourner le ratio victoires/parties sans diviser par zéro :)
function ratio(joueur){
	if(joueur.PARTIEJOUE == 0)
		return 0;
	else
		return joueur.PARTIEGAGNE / joueur.PARTIEJOUE;
}

//Quicksort (yaaaay)
function swap(items, firstIndex, secondIndex){
    var temp = items[firstIndex];
    items[firstIndex] = items[secondIndex];
    items[secondIndex] = temp;
}

function partition(items, left, right) {
	var pivot = ratio(items[Math.floor((right + left) / 2)]);
	var i = left;
    var j = right;

    while (i <= j) {
		while (ratio(items[i]) < pivot) {
            i++;
        }
		while (ratio(items[j]) > pivot) {
            j--;
        }
        if (i <= j) {
            swap(items, i, j);
            i++;
            j--;
        }
    }
    return i;
}

function quickSort(items, left, right) {
    var index;

    if (items.length > 1) {
        index = partition(items, left, right);
        if (left < index - 1) {
            quickSort(items, left, index - 1);
        }
        if (index < right) {
            quickSort(items, index, right);
        }
    }

    return items;
}

//TO-DO : faire un select dans une autre table (Joueur-Niveau)