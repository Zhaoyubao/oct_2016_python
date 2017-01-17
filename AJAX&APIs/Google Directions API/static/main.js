$(document).ready(function() {
    $('form').submit(function(e) {
        e.preventDefault()
        var origin = $(this).children('input#from').val().replace(/\s/g,'');
        var dest = $(this).children('input#to').val().replace(/\s/g,'');
        // console.log("Origin:", origin);
        // console.log("Destination:", dest);
        $('span#msg_from').text('');
        $('span#msg_to').text('');
        if(origin == '') {
            $('span#msg_from').text('Please Input The Origin!');
        }
        if(dest == '') {
            $('span#msg_to').text('Please Input The Destination!');
        }
        if(origin != '' && dest != '') {
            // console.log("Url:", $(this).attr('action'));
            // console.log("Serialized:", $(this).serialize());
            $.post($(this).attr('action'), $(this).serialize(), function(res) {
                // console.log("Response:",res);
                $('div#directions').html(res);
            });
            $(this).children('input#from').val("");
            $(this).children('input#to').val("");
        }
    });
});
