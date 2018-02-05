<?php
    require_once("action/SearchAction.php");
    $action = new SearchAction();
    $action->execute();
    require_once("partial/header.php");
?>
<script type="text/javascript" src="js/jquery-3.2.1.min.js"></script>
<script type="text/javascript" src="js/search.js"></script>
<script type="text/javascript" src="js/calculateName.js"></script>
        <div class="searchArea" style="text-align:center">
            <input type="text" id="searchBar"size="21" maxlength="120" placeholder="chercher un joueur">
            <input type="button", id="btnfind" value="find" onclick="search()">
        </div>
        <div id="searchResults">
        </div>
        <div class="buttonDiv">
            <input type="button", id="btnPrevious" style="float:left;margin-left:20%;" value="Previous" onclick="goPrevious()">
            <input type="button", id="btnNext" style="float:right;margin-right:20%;" value="Next" onclick="goNext()">
        </div>
        <div style="clear:both;">
            <!-- pour mettre des args dans l'URL -->
            <?php
                if(isset($_GET["username"])){
            ?>
                <script>
                    document.getElementById("searchBar").value = <?=$_GET["username"]; ?>;
                    search()
                </script>
            <?php
                }
            ?>
        </div>

        </div>
    </body>
</html>
