class Spawn{
    constructor(idPlayer){
        this.x=0
        this.y=0
        this.idPlayer = idPlayer
        this.isActive=false
    }

    changePos(x,y){
        this.x=x
        this.y=y
    }

    tick(){
        if(this.isActive){
            var pixX = this.x * sizeTuile + debX + 2;
            var pixY = this.y * sizeTuile + debY + 2;
            switch(this.idPlayer){
                case 1:
                    ctx.strokeStyle = "blue"
                    break
                case 2:
                    ctx.strokeStyle = "red"
                    break
                case 3:
                    ctx.strokeStyle = "yellow"
                    break
                case 4:
                    ctx.strokeStyle = "green"
                    break
            }
            ctx.beginPath();
            ctx.moveTo(pixX,pixY);
            ctx.lineTo(pixX + sizeTuile - 4, pixY);
            ctx.lineTo(pixX + sizeTuile - 4, pixY + sizeTuile - 4);
            ctx.lineTo(pixX, pixY + sizeTuile - 4);
            ctx.lineTo(pixX, pixY);
            ctx.stroke();
        }
    }
}
