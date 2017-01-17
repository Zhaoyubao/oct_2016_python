$(document).ready(function() {
    $('input').blur(function() {
        var tagName = $(this).attr('name');
        var value = $(this).val();
        console.log("Blur: %s, Value: %s", tagName, value);
        var data = $('form').serialize();
        console.log("Serialize:", data);
        if($(this).siblings("input[type='date']").val() != '') {
            $.post('/show/1', data, function(res) {
                $('div#leads').html(res);
            });
        }
        else {
            console.log("Invalid Input!");
        }
    });

    $('div#leads').on('click', 'li', function() {
        var page = $(this).attr('id');
        var data = $('form').serialize();
        console.log("Page:",page);
        console.log("Serialize:", data);
        var url = '/show/' + page;
        $.post(url, data, function(res) {
            $('div#leads').html(res);
        });
    });
});
