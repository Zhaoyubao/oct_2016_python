$(document).ready(function() {
// Add notes...
    $('form').submit(function() {
        var title = $(this).children('input').val();
        if(title.replace(/\s/g, '')) {
            $.ajax({
                method: 'POST',
                url: '/notes/create',
                data: $(this).serialize(),
                success: function(res){
                            $('div#notes').html(res);
                         }
            })
        }
        $(this).children('input').val("");
        return false;
    })
// Delete notes..
    $('div#notes').on('click', 'b', function() {
        if (confirm("Confirm Delete?")) {
            var id = $(this).attr('id');
            var url = "/notes/" + id + "/delete";
            $.ajax({
                method: 'GET',
                url: url,
                success: function(res) {
                            $('div#notes').html(res);
                         }
            })
        }
    })
// Update notes...
    var oldValue = "";
    $('div#notes').on('focus', 'input, textarea', function() {
        if($(this).attr('name') === 'title') {
            $(this).css("border-bottom","1px solid silver");
        }
        oldValue = $(this).val();
        $(this).attr("id","focused");
    })

    $('div#notes').on('blur', 'input, textarea', function() {
        if($(this).attr('name') === 'title') {
            $(this).css("border-bottom","none");
        }
        $(this).attr("id","");
    })

    $('div#notes').on('change', 'input, textarea', function() {
        var id = $(this).parent().attr('id');
        var url = "/notes/" + id + "/update";
        var data = $(this).parent('form').serialize();
        if($(this).val().replace(/\s/g, '')) {
            $.ajax({
                method: 'POST',
                url: url,
                data: data,
                success: function(res){
                            $('div#notes').html(res);
                         }
            })
        }
        else {
            // console.log("No input!");
            $(this).val(oldValue);
        }
    })

// Mouseover functions:
    $('div#notes').on('mouseenter', 'input, textarea', function() {
        if($(this).attr('id') != 'focused') $('#tip').fadeIn('fast');
    })

    $('div#notes').on('mousemove', 'input, textarea', function(e) {
        var top = e.pageY + 8;
        var left = e.pageX + 8;
        $('#tip').css({
            'top' : top + 'px',
            'left' : left + 'px'
        })
        $('div#notes').on('focus', 'input, textarea', function() {
            $('#tip').hide()
        })
    })

    $('div#notes').on('mouseleave', 'input, textarea', function() {
        $('#tip').hide()
    })
})
