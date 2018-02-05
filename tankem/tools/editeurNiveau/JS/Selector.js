class Selector{
    constructor(x,y,size){
        this.x = x;
        this.y = y;
        this.size = size;
    }

    tick(){
        var pixX = this.x * this.size + debX;
        var pixY = this.y * this.size + debY;
        ctx.strokeStyle = "red";
        ctx.beginPath();
        ctx.moveTo(pixX,pixY);
        ctx.lineTo(pixX + this.size, pixY);
        ctx.lineTo(pixX + this.size, pixY + this.size);
        ctx.lineTo(pixX, pixY + this.size);
        ctx.lineTo(pixX, pixY);
        ctx.stroke();
    }

    updatePosition(e){
        switch (e.key) {
            case "ArrowRight":
                if(this.x<niveau.tailleX-1){
                    ++this.x;
                }
                break
            case "ArrowLeft":
                if (this.x>0) {
                    --this.x;
                }
                break
            case "ArrowDown":
                if(this.y<niveau.tailleY-1){
                    ++this.y;
                }
                break
            case "ArrowUp":
                if (this.y>0) {
                    --this.y;
                }
                break
            case "0":
                if(niveau.isSpawnHere(this.x, this.y, 0)){
                    afficherErreur("On ne peut pas changer un terrain où qu'un joueur est placé!");
                } else if(niveau.tabTile[this.x][this.y].hasTree){
                    afficherErreur("On ne peut pas enlever un terrain où qu'un arbre est placé!")
                } else {
                    niveau.setTile(this.x, this.y, 0)
                }
                break;
            case "1":
                niveau.setTile(this.x, this.y, 1)
                break;
            case "2":
                if(niveau.isSpawnHere(this.x, this.y, 0)){
                    afficherErreur("On ne peut pas changer un terrain où qu'un joueur est placé!");
                } else {
                    niveau.setTile(this.x, this.y, 2)
                }
                break;
            case "3":
                if(niveau.isSpawnHere(this.x, this.y, 0)){
                    afficherErreur("On ne peut pas changer un terrain où qu'un joueur est placé!");
                } else {
                    niveau.setTile(this.x, this.y, 3)
                }
                break;
            case "4":
                if(niveau.isSpawnHere(this.x, this.y, 0)){
                    afficherErreur("On ne peut pas changer un terrain où qu'un joueur est placé!");
                } else {
                    niveau.setTile(this.x, this.y, 4)
                }
                break;
            case "q":
                if(niveau.isSpawnHere(this.x, this.y, 0)){
                    afficherErreur("On ne peut pas placer un arbre sur joueur!");
                } else if(niveau.tabTile[this.x][this.y].type == 0){
                    afficherErreur("On peut seulement placer un arbre sur une case qui existe!")
                } else{
                    niveau.toggleTree(this.x, this.y)
                }
                break
            case "a":
                var spawn = niveau.tabSpawn[0]
                if(niveau.tabTile[this.x][this.y].hasTree){
                    afficherErreur("On ne peut pas placer un joueur sur un arbre!");
                }
                else if(niveau.isSpawnHere(this.x, this.y, 1)){
                    afficherErreur("On ne peut pas placer un joueur sur un autre joueur!");
                }
                else if(niveau.tabTile[this.x][this.y].type != 1){
                    afficherErreur("Le joueur doit être placer sur une case sol!")
                }
                else{
                    if(spawn.x == this.x && spawn.y == this.y){
                        spawn.isActive = ! spawn.isActive
                    } else{
                        spawn.isActive = true;
                    }
                    niveau.tabSpawn[0].changePos(this.x, this.y)
                }
                break
            case "s":
                var spawn = niveau.tabSpawn[1]
                if(niveau.tabTile[this.x][this.y].hasTree){
                    afficherErreur("On ne peut pas placer un joueur sur un arbre!");
                }
                else if(niveau.isSpawnHere(this.x, this.y, 2)){
                    afficherErreur("On ne peut pas placer un joueur sur un autre joueur!");
                }
                else if(niveau.tabTile[this.x][this.y].type != 1){
                    afficherErreur("Le joueur doit être placer sur une case sol!")
                }
                else{
                    if(spawn.x == this.x && spawn.y == this.y){
                        spawn.isActive = ! spawn.isActive
                    } else {
                        spawn.isActive = true;
                    }
                    niveau.tabSpawn[1].changePos(this.x, this.y)
                }
                break
            case "d":
                var spawn = niveau.tabSpawn[2]
                if(niveau.tabTile[this.x][this.y].hasTree){
                    afficherErreur("On ne peut pas placer un joueur sur un arbre!");
                }
                else if(niveau.isSpawnHere(this.x, this.y, 3)){
                    afficherErreur("On ne peut pas placer un joueur sur un autre joueur!");
                }
                else if(niveau.tabTile[this.x][this.y].type != 1){
                    afficherErreur("Le joueur doit être placer sur une case sol!")
                }
                else{
                    if(spawn.x == this.x && spawn.y == this.y){
                        spawn.isActive = ! spawn.isActive
                    } else {
                        spawn.isActive = true;
                    }
                    niveau.tabSpawn[2].changePos(this.x, this.y)
                }
                break
            case "f":
                var spawn = niveau.tabSpawn[3]
                if(niveau.tabTile[this.x][this.y].hasTree){
                    afficherErreur("On ne peut pas placer un joueur sur un arbre!");
                }
                else if(niveau.isSpawnHere(this.x, this.y, 4)){
                    afficherErreur("On ne peut pas placer un joueur sur un autre joueur!");
                }
                else if(niveau.tabTile[this.x][this.y].type != 1){
                    afficherErreur("Le joueur doit être placer sur une case sol!")
                }
                else{
                    if(spawn.x == this.x && spawn.y == this.y){
                        spawn.isActive = ! spawn.isActive
                    } else {
                        spawn.isActive = true;
                    }
                    niveau.tabSpawn[3].changePos(this.x, this.y)
                }
                break
            default:
                break
        }
    }
}
