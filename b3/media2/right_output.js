function right_change(num){
    var elem = document.getElementById("chatpage");
    if(num == -1){
        elem.setAttribute("src","../rankhub.html");
    }else{
        elem.setAttribute("src","right"+num+".html");
    }
}