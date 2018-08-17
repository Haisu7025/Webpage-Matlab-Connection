jQuery(document).ready(function() {

    /*
        Fullscreen background
    */

});

$(function() {
    $("#b1").click(function() {
        var a = $("#i1").val();
        var b = $("#i2").val();
        $.post('http://127.0.0.1:5000/matlab', {
                'a': a,
                'b': b,
            },
            function(data) {
                alert(JSON.stringify(data));
            });
    });


});