$(function() {
    $('#btn-submit').click(function() {
 
        $.ajax({
            url: '/add',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});