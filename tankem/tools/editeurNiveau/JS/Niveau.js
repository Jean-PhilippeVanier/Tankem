class Niveau{
    constructor(x,y){
        this.tailleX = x
        this.tailleY = y
        this.itemDelay = 10
        this.tabTile= []
        this.tabSpawn = []
        this.maxSpawn=4
        this.nbtree=0
        this.maxTree=4
        for (var x = 0; x < this.tailleX; x++) {
            this.tabTile[x] = new Array()
            for (var y = 0; y < this.tailleY; y++) {
                this.tabTile[x][y] = new Tile(x,y)
            }
        }
        for (var i = 0; i < this.maxSpawn; i++) {
            this.tabSpawn.push(new Spawn(i+1))
        }
        // this.tabTile[1][1].type = 1
        // this.tabTile[2][2].type = 2
        // this.tabTile[3][3].type = 3
        // this.tabTile[4][4].type = 4
        // this.tabTile[2][2].hasTree = 1
        // this.tabTile[4][4].hasTree = 1
        // this.tabTile[1][1].hasTree = 1
    }
    setSize(x,y){
        this.tailleX = x
        this.tailleY = y
    }
    setTile(x,y,type){
        this.tabTile[x][y].type=type
    }
    toggleTree(x,y){
        if(this.tabTile[x][y].hasTree) {
            this.tabTile[x][y].hasTree = 0
            this.nbtree--
        } else if(this.nbtree>=this.maxTree) {
            afficherErreur("On ne peut pas avoir plus que " + this.maxTree + " arbres sur le terrain!");
        }else if(this.nbtree<this.maxTree){
            this.tabTile[x][y].hasTree = 1
            this.nbtree++
        }
    }
    addSpawn(x,y,idPlayer){
        this.tabSpawn(x,y,idPlayer);
    }
    isSpawnHere(x,y,id){
        var playerOnCase = false

        for (var i = 0; i < this.tabSpawn.length; i++) {
            if(this.tabSpawn[i].idPlayer != id){
                if(this.tabSpawn[i].x == x && this.tabSpawn[i].y == y && this.tabSpawn[i].isActive){
                    playerOnCase = true
                }
            }
        }

        return playerOnCase
    }
}
