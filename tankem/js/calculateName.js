function calculateName(player){

    var maxStat = 30
    var qualificatifA = ""
    var qualificatifB = ""
    var bestStat1 = Array()
    bestStat1[0] = [-1, 0]
    var bestStat2 = Array()
    bestStat2[0]=[-1, 0]
    // StatsJoueur: 0 = vie, 1 = force, 2 = agilite, 3 = dexterite
    var statsJoueur = Array()
    statsJoueur[0]=player.VIE
    statsJoueur[1]=player.FORCE
    statsJoueur[2]=player.AGILITE
    statsJoueur[3]=player.DEXTERITE

    //test si tt les stats sont au max
    if(player.VIE == maxStat && player.FORCE == maxStat && player.AGILITE == maxStat && player.DEXTERITE == maxStat){
        return "le dominateur"
    }

    //calcule le stat le plus grand
    $(statsJoueur).each(function(index, el) {
        if(statsJoueur[index] > bestStat1[0][1]){
            bestStat1 = []
            bestStat1.push([index, statsJoueur[index]])
        }
        else if((statsJoueur[index] == bestStat1[0][1]) && statsJoueur[index] > 0 ) {
            bestStat1.push([index, statsJoueur[index]])
        }
    });
    bestStat1 = bestStat1[Math.floor(bestStat1.length * Math.random())]

    //calcule le 2eme stat le plus grand
    $(statsJoueur).each(function(index, el) {
        if (index != bestStat1[0]) {
            if(statsJoueur[index] > bestStat2[0][1]){
                bestStat2 = []
                bestStat2.push([index, statsJoueur[index]])
            }
            else if((statsJoueur[index] == bestStat2[0][1]) && statsJoueur[index] > 0 ) {
                bestStat2.push([index, statsJoueur[index]])
            }
        }
    });
        bestStat2 = bestStat2[Math.floor(bestStat2.length * Math.random())]

    //calcule l'adjectif correspondant au stat le plus grand
    if(bestStat1[0] == 0){
        if(bestStat1[1] >= 1) {
            qualificatifA = "le fougeux"
        }
        if(bestStat1[1]>=5){
            qualificatifA = "le petulant"
        }
        if(bestStat1[1]>=10){
            qualificatifA = "l'immortel"
        }
    }
    else if(bestStat1[0]==1) {
        if(bestStat1[1] >= 1) {
            qualificatifA = "le crossfiter"
        }
        if(bestStat1[1]>=5){
            qualificatifA = "le Hulk"
        }
        if(bestStat1[1]>=10){
            qualificatifA = "le tout puissant"
        }
    }
    else if(bestStat1[0]==2) {
        if(bestStat1[1] >= 1) {
            qualificatifA = "le prompt"
        }
        if(bestStat1[1]>=5){
            qualificatifA = "le lynx"
        }
        if(bestStat1[1]>=10){
            qualificatifA = "le foudroyant"
        }
    }
    else if(bestStat1[0]==3) {
        if(bestStat1[1] >= 1) {
            qualificatifA = "le precis"
        }
        if(bestStat1[1]>=5){
            qualificatifA = "l'habile"
        }
        if(bestStat1[1]>=10){
            qualificatifA = "le chirurgien"
        }
    }

    //calcule l'adjectif correspondant au second stat le plus grand
    if(bestStat2[0] == 0){
        if(bestStat2[1] >= 1) {
            qualificatifB = "fougeux"
        }
        if(bestStat2[1]>=5){
            qualificatifB = "petulant"
        }
        if(bestStat2[1]>=10){
            qualificatifB = "immortel"
        }
    }
    else if(bestStat2[0]==1) {
        if(bestStat2[1] >= 1) {
            qualificatifB = "qui fait du crossfit"
        }
        if(bestStat2[1]>=5){
            qualificatifB = "brutal"
        }
        if(bestStat2[1]>=10){
            qualificatifB = "tout puissant"
        }
    }
    else if(bestStat2[0]==2) {
        if(bestStat2[1] >= 1) {
            qualificatifB = "prompt"
        }
        if(bestStat2[1]>=5){
            qualificatifB = "lynx"
        }
        if(bestStat2[1]>=10){
            qualificatifB = "foudroyant"
        }
    }
    else if(bestStat2[0]==3) {
        if(bestStat2[1] >= 1) {
            qualificatifB = "precis"
        }
        if(bestStat2[1]>=5){
            qualificatifB = "habile"
        }
        if(bestStat2[1]>=10){
            qualificatifB = "chirurgien"
        }
    }

    return qualificatifA + " " + qualificatifB
}
