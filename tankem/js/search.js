var resultSearch = null
var mapFavorites = []
var weaponsFavorites = []
var weaponsFavoritesName = []
var tabJoueur = []
var currentPage = 0
var usernameLoggedIn = null


function search(){
    var searchbar = document.getElementById("searchBar")
    $.ajax({
        url: 'ajaxSearch.php',
        type: 'POST',
        data: {searchKey: searchbar.value}
    })
    .done(function(r) {
        document.getElementById("searchResults").innerHTML=""
        resultSearch = JSON.parse(r)[0]
        usernameLoggedIn = JSON.parse(r)[1]
        // console.log(resultSearch);
        getFavoritWeapons()
        ajaxJoueurs()
        getFavoritMap()
    })
}

function getFavoritMap(){
    $(resultSearch).each(function(index, el) {
        $.ajax({
            type : "POST",
            url : "ajaxNiveauFavori.php",
            data : {
                idJoueur: resultSearch[index].ID
            }
        })
        .done(function(favouritmap) {
            mapFavorites[index] = JSON.parse(favouritmap)
            displayInfos()
        })
    })
}


function getFavoritWeapons(){
    $(resultSearch).each(function(index, el) {
        $.ajax({
            type : "POST",
            url : "ajaxArmesFavorites.php",
            data : {
                idJoueur: resultSearch[index].ID
            }
        })
        .done(function(r) {
            weaponsFavorites[index] = JSON.parse(r)
            weaponsFavoritesName[index] = ["None", "None"]
            for (var i = 0; i < weaponsFavorites[index].length; i++) {
                switch (weaponsFavorites[index][i].IDARME) {
                    case "1":
                        weaponsFavoritesName[index][i] = "Canon"
                        break;
                    case "2":
                        weaponsFavoritesName[index][i] = "Grenade"
                        break;
                    case "3":
                        weaponsFavoritesName[index][i] = "Mitraillette"
                        break;
                    case "4":
                        weaponsFavoritesName[index][i] = "Piege"
                        break;
                    case "5":
                        weaponsFavoritesName[index][i] = "Shotgun"
                        break;
                    case "6":
                        weaponsFavoritesName[index][i] = "Guide"
                        break;
                }
            }
        })
    });
}

function ajaxJoueurs() {
	$.ajax({
		type : "POST",
		url : "ajaxJoueurs.php",
		data : {

		}
	})
	.done(function(data) {
		tabJoueur = JSON.parse(data);
		tabJoueur = quickSort(tabJoueur, 0, tabJoueur.length-1);
		tabJoueur.reverse(); //Pour inverser l'array
	})
}

function isHallOfFamous(a){
    for (var i = 0; i < tabJoueur.length; i++) {
        if(tabJoueur[i].USERNAME == a){
            return i
        }
    }
    return -1
}



function displayInfos(){
    document.getElementById("searchResults").innerHTML=""
    // $(resultSearch).each(function(index) {
    for (var i = 0; i < 5; i++) {
            if(resultSearch[5*currentPage+i] != null){

                /////////////AJAX PRINCIPAL///////////
                node = document.createElement("div")
                node.className = "container"
                node.style="background-color:F0F0F0; padding:1%; margin:1% auto;"
                row1 = document.createElement("div")
                row1.className="row"
                row2 = document.createElement("div")
                row2.className="row"


                //row1
                colName = document.createElement("div")
                colName.className="col-sm-12"
                txtname = document.createElement("h4")
                txtname.className="text-center"
                if(resultSearch[5*currentPage+i].USERNAME == usernameLoggedIn){
                    texte = document.createTextNode(""+resultSearch[5*currentPage+i].USERNAME + " " + calculateName(resultSearch[5*currentPage+i]) + " ("+resultSearch[5*currentPage+i].SURNAME+" "+resultSearch[5*currentPage+i].NAME+")")
                }else {
                    texte = document.createTextNode(""+resultSearch[5*currentPage+i].USERNAME + " " + calculateName(resultSearch[5*currentPage+i]))
                }
                txtname.appendChild(texte)
                colName.appendChild(txtname)
                row1.appendChild(colName)
                row1.style="background-color:E0E0E0;border:1px solid black"


                //row2
                colImg = document.createElement("div")
                img = document.createElement("img")
                colImg.className="col-sm-2"
                img.src="images/tankAlpha.png"
                img.style="width:150px; height:150px; background-color:"+resultSearch[5*currentPage+i].COULEURTANK
                colImg.appendChild(img)

                //col1 Stats
                col1Stats = document.createElement("div")
                col1Stats.className="col-sm-4"
                col1Stats.style="font-weight:bold;font-size:17px;line-height:35px;padding-top:5px;border-left: 1px solid black; border-right: 1px solid black; padding-left:3%; margin-left:3%;"
                col1Stats.appendChild(document.createTextNode("Niveau: "+resultSearch[5*currentPage+i].NIVEAU))
                col1Stats.appendChild(document.createElement("br"))
                col1Stats.appendChild(document.createTextNode("Parties gagnees: "+resultSearch[5*currentPage+i].PARTIEGAGNE))
                col1Stats.appendChild(document.createElement("br"))
                col1Stats.appendChild(document.createTextNode("Parties jouees: "+resultSearch[5*currentPage+i].PARTIEJOUE))
                col1Stats.appendChild(document.createElement("br"))
                if(resultSearch[5*currentPage+i].PARTIEJOUE == 0){
                    col1Stats.appendChild(document.createTextNode("Ratio victoire: 0%"))
                }else{
                    col1Stats.appendChild(document.createTextNode("Ratio victoire: "+((resultSearch[5*currentPage+i].PARTIEGAGNE/resultSearch[5*currentPage+i].PARTIEJOUE)*100).toFixed(2)+"%"))
                }

                //col2Stats
                col2Stats = document.createElement("div")
                col2Stats.className="col-sm-4"
                col2Stats.style="font-weight:bold;font-size:17px;line-height:35px;padding-top:5px;"

                if(mapFavorites[5*currentPage+i].length > 0){
                    col2Stats.appendChild(document.createTextNode("Map favorite: "+mapFavorites[5*currentPage+i][0].NOMNIVEAU))
                }else{
                    col2Stats.appendChild(document.createTextNode("Map favorite: "+"None"))
                }
                col2Stats.appendChild(document.createElement("br"))
                col2Stats.appendChild(document.createTextNode("Arme principale: "+weaponsFavoritesName[5*currentPage+i][0]))
                col2Stats.appendChild(document.createElement("br"))
                col2Stats.appendChild(document.createTextNode("Arme secondaire: "+weaponsFavoritesName[5*currentPage+i][1]))


                col3 = document.createElement("div")
                col3.className="col-sm-1"
                if(isHallOfFamous(resultSearch[5*currentPage+i].USERNAME) < 10){
                    col3.style="background-image: url('images/badge.png');background-position: center;background-size: 100%;background-repeat: no-repeat; font-size: 3em;text-align:center;padding-top:2%;"
                    col3.appendChild(document.createTextNode(isHallOfFamous(resultSearch[5*currentPage+i].USERNAME)+1))
                }


                row2.appendChild(colImg)
                row2.appendChild(col1Stats)
                row2.appendChild(col2Stats)
                row2.appendChild(col3)

                node.appendChild(row1)
                node.appendChild(row2)
                document.getElementById("searchResults").appendChild(node)
            }
        }

    // });
}


function goPrevious(){
    if(currentPage > 0){
        currentPage--
        displayInfos()
    }
}

function goNext(){
    if((currentPage+1) < (resultSearch.length/5)){
        currentPage++
        displayInfos()
    }
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

function swap(items, firstIndex, secondIndex){
    var temp = items[firstIndex];
    items[firstIndex] = items[secondIndex];
    items[secondIndex] = temp;
}

function ratio(joueur){
	if(joueur.PARTIEJOUE == 0)
		return 0;
	else
		return joueur.PARTIEGAGNE / joueur.PARTIEJOUE;
}
