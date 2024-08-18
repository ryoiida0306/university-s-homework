let diff_iida = 0;
let diff_ando = 10;
let diff_asai = 100;

function setdiff(name, score){
    if (name == "iida"){
        diff_iida = score;
    }
    if (name == "ando"){
        diff_ando = score;
    }
    if (name == "asai"){
        diff_asai = score;
    }
}
function diff(name){
    if (name == "iida"){return diff_iida;}
    if (name == "ando"){return diff_ando;}
    if (name == "asai"){return diff_asai;}
    return -1;
}

function anothers(name){
    if (name == "ando"){
        array = ["asai","iida"];
        return array;
    }
    if (name == "asai"){
        array = ["ando","iida"];
        return array;
    }
    if (name == "iida"){
        array = ["ando","asai"];
        return array;
    }
    return 0;


}

function rank_from_name(name){
    var rank = 1;
    if (diff(name) < diff(anothers(name)[0])){
        rank++;
    }
    if (diff(name) < diff(anothers(name)[1])){
        rank++;
    }
    return rank;
}


function name_from_rank(num){
    // array = [["","",""],["","",""],["","",""]];

    // array[rank_from_name("asai")-1][0] = "asai";
    // array[rank_from_name("ando")-1][1] = "ando";
    // array[rank_from_name("iida")-1][2] = "iida";
    // return array;

    if (rank_from_name("asai") == num){
        return "asai";
    }
    if (rank_from_name("ando") == num){
        return "ando";
    }
    if (rank_from_name("iida") == num){
        return "iida";
    }
    return "";
}


// name_disp(){
//     var elem = document.getElementById("first");
//     elem 
// }

function ack(you1, read1, you2, read2, from,to){
    if (from == "asai"){
        if(to == "ando"){
            if(you1 == "ando"){return read1;}
            if(you2 == "ando"){return read2;}
        }
        if(to == "iida"){
            if(you1 == "iida"){return read1;}
            if(you2 == "iida"){return read2;}
        }
    }
    if (from == "ando"){
        if (to == "asai"){
            if(you1 == "asai"){return read1;}
            if(you2 == "asai"){return read2;}
        }
        if (to == "iida"){
            if(you1 == "iida"){return read1;}
            if(you2 == "iida"){return read2;}
        }
    }
    if (from == "iida"){
        if (to == "asai"){
            if(you1 == "asai"){return read1;}
            if(you2 == "asai"){return read2;}
        }
        if (to == "ando"){
            if(you1 == "ando"){return read1;}
            if(you2 == "ando"){return read2;}
        }
    }
    return -1;
}


function ack_disp(you1, read1, you2, read2, to){//nameは英語
    var elem = document.getElementById(to+"_button");
    var ack_num = ack(you1, read1, you2, read2, Me(),to);
    if(ack_num != 0)
        elem.setAttribute("value",elem.getAttribute("value")+" ("+ack_num+")");
    elem.setAttribute("style","color: rgb("+ack_num*10+", 0, 0);");

}

function all_ack_disp(you1, read1, you2, read2){
    try{
       ack_disp(you1, read1, you2, read2, "ando");
    }catch{}
    try{
       ack_disp(you1, read1, you2, read2, "asai");
    }catch{}
    try{
       ack_disp(you1, read1, you2, read2, "iida");
    }catch{}

    
}

function eng_to_jp(name){
    if (name == "iida"){
        return "飯田";
    }
    if (name == "asai"){
        return "浅井";
    }
    if (name == "ando"){
        return "安藤";
    }
    return "error";
}


function mes_from_rank(num){
    if(num == 1){
        return "もっと早く返そう";
    }
    if(num == 2){
        return "まずまずの早さだね";
    }
    if(num == 3){
        return "この調子でどんどん返そう！";
    }
    return "エラー";


}
