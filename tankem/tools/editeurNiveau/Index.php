<?php
    require_once("action/IndexAction.php");

    $action = new IndexAction();
    $action->execute();
?>

<!DOCTYPE html>
<html>
    <head>
        <script src="JS/jquery.js"></script>
        <script src="JS/spawn.js"></script>
        <script src="JS/Tile.js"></script>
        <script src="JS/Niveau.js"></script>
        <script src="JS/main.js"></script>
        <script src="JS/Selector.js"></script>
        <script src="JS/DTONiveau.js"></script>
        <script src="JS/DTOTuile.js"></script>
        <script src="JS/DTOSpawn.js"></script>
        <link rel="stylesheet" href="style.css" type="text/css"/>
        <title>Éditeur de niveau</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    </head>
    <body>
        <main>
            <div>
                Nom du niveau: <input type="text" id="nomNiveau" class="input"/>
                Taille X: <input type="text" id="tailleX" size="2" class="input"/>
                Taille Y: <input type="text" id="tailleY" size="2" class="input"/>
                <input type="button" id="tailleTuile" value="Nouvelle taille" OnClick="clickButton()"/>
                <input type="button" id="sauvegarder" value="Sauvegarder" OnClick="envoyerTables()"/>
            </div>
            <div>
                Status: <select name="status" id="status">
                    <option value="1" selected>actif</option>
                    <option value="2">test</option>
                    <option value="3">inactif</option>
                </select>
                Delai minimum des objets: <input type="text" id="itemDelMin" class="input" value="3"/>
                Delai maximum des objets: <input type="text" id="itemDelMax" class="input" value="20"/>
            </div>
            <div style="float:left;margin:5%;">
                <table class="controles">
                    <div class="bold">Controles:</div>
                    <tr>
                        <td>Fleches:</td>
                        <td>Deplacer le selecteur</td>
                    </tr>
                    <tr>
                        <td>0:</td>
                        <td>Enleve tuile</td>
                    </tr>
                    <tr>
                        <td>1:</td>
                        <td>Place tuile sol</td>
                    </tr>
                    <tr>
                        <td>2:</td>
                        <td>Place tuile mur</td>
                    </tr>
                    <tr>
                        <td>3:</td>
                        <td>Place tuile mobile</td>
                    </tr>
                    <tr>
                        <td>4:</td>
                        <td>Place tuile mobile avec rythme inversé</td>
                    </tr>
                    <tr>
                        <td>Q:</td>
                        <td>Place/enleve arbre</td>
                    </tr>
                    <tr>
                        <td>A:</td>
                        <td>Place spawn Joueur1</td>
                    </tr>
                    <tr>
                        <td>S:</td>
                        <td>Place spawn Joueur2</td>
                    </tr>
                    <tr>
                        <td>D:</td>
                        <td>Place spawn Joueur3</td>
                    </tr>
                    <tr>
                        <td>F:</td>
                        <td>Place spawn Joueur4</td>
                    </tr>
                </table>
                <table class="legende">
                    <div class="bold">Legende:</div>
                    <tr>
                        <td><div style="border:2px solid red;width:30px;height:30px;"></div></td>
                        <td>Selector</td>
                    </tr>
                    <tr>
                        <td><div style="border:2px solid blue;width:30px;height:30px;"></div></td>
                        <td>Spawn Joueur1</td>
                    </tr>
                    <tr>
                        <td><div style="border:2px solid orange;width:30px;height:30px;"></div></td>
                        <td>Spawn Joueur2</td>
                    </tr>
                    <tr>
                        <td><div style="border:2px solid yellow;width:30px;height:30px;"></div></td>
                        <td>Spawn Joueur3</td>
                    </tr>
                    <tr>
                        <td><div style="border:2px solid green;width:30px;height:30px;"></div></td>
                        <td>Spawn Joueur4</td>
                    </tr>
                    <tr>
                        <td><img src="images/block1.png" width="30" height="30"></td>
                        <td>Tuile sol</td>
                    </tr>
                    <tr>
                        <td><img src="images/block2.jpg" width="30" height="30"></td>
                        <td>Tuile mur</td>
                    </tr>
                    <tr>
                        <td><img src="images/block3.jpg" width="30" height="30"></td>
                        <td>Tuile mobile</td>
                    </tr>
                    <tr>
                        <td><img src="images/block4.png" width="30" height="30"></td>
                        <td>Tuile mobile avec rythme inversé</td>
                    </tr>
                </table>
            </div>
            <canvas height="800", width="800" id="canvas"></canvas>
        </main>

        <!--Boit te dialogue-->
        <div id="myModal" class="modal">
            <div class="modal-content">
                <span class="close">&times;</span>
                <p id="messageErreur">ERROR</p>
            </div>
        </div>

    </body>
</html>
