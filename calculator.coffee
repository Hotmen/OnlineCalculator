$ ->
	Calculate = ->
		$('.calculator').on 'click', 'a.butt', handler

	handler = (evt) ->
		evt.preventDefault()
		text = $(this).text()
		lcd = $ "#input"
		if  text is "C"
            lcd.text("")
        else if text is "BS"
            lcd.text lcd.text().slice 0,lcd.text().length-1
        else if text is "="
        	calc()
        else
            lcd.text lcd.text() + text
        return evt

	calc = ->
    	$.get "calc", {"s": $("#input").text()}, (data) ->
        	$("#input").text data

    Calculate()