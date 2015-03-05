function main(){
    var b = document.getElementsByClassName("butt");
    var i;
    for (i=0; i < b.length; i++){
        b[i].addEventListener("click", cl);
    }
    function cl() {
        var el = this;
        if ( el.innerHTML == "C" ) {
            document.getElementById("input").innerHTML = "";
        }
        else if ( el.innerHTML == "BS" ) {
            var str = document.getElementById("input").innerHTML;
            document.getElementById("input").innerHTML = str.slice(0,str.length-1);
        }
        else if ( el.innerHTML == "=" ) { calc();}
        else {
            document.getElementById("input").innerHTML += el.innerHTML;
        }
}}
function calc() {
    var xmlhttp;
    xmlhttp=new XMLHttpRequest();
    xmlhttp.onreadystatechange=function() {
      if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
        document.getElementById("input").innerHTML = xmlhttp.responseText;
        }
      }
    var data = document.getElementById("input").innerHTML
    xmlhttp.open("GET", "calc?s="+encodeURIComponent(data) ,true);
    xmlhttp.send();
}