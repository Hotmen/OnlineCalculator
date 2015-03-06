$(function () {
    $(".calculator").on("click", "a.butt", handler);


function handler(evt) {
    evt.preventDefault();
    var text = $(this).text();
    var lcd = $("#input")
    if ( text == "C" ) {
            lcd.text("");
        }
        else if ( text == "BS" ) {
            lcd.text(lcd.text().slice(0,lcd.text().length-1));
        }
        else if ( text == "=" ) { calc();}
        else {
            lcd.text(lcd.text() + text);
        }
}

function calc() {
    $.get("calc", {"s": $("#input").text()}, function (data) {
        $("#input").text(data);
    });
}
});