
b = document.getElementsByClassName("butt")
for i in [0..b.length]
	b[i].addEventListener("click", cl)
cl = ->
	el = $ this
	if el.innerHTML is "C"
        document.getElementById("input").innerHTML = ""        
    else if el.innerHTML is "BS"
        str = document.getElementById("input").innerHTML
        document.getElementById("input").innerHTML = str[0..str.length-1]
    else if el.innerHTML is "="
    	calc()
    else
        document.getElementById("input").innerHTML += el.innerHTML
calc = ->
	xmlhttp = new XMLHttpRequest()
	xmlhttp.onreadystatechange = ->
		if xmlhttp.readyState==4 && xmlhttp.status==200
			document.getElementById("input").innerHTML = xmlhttp.responseText
	data = document.getElementById("input").innerHTML
	xmlhttp.open("GET", "calc?s="+encodeURIComponent(data) ,true)
	xmlhttp.send()
    