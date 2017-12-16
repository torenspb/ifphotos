$(function() {

    var usernameForm = function() {
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            beforeSend: function() {
                form[0].reset();
                $('.arrow-container').html('');
                $('.custom-container').html('Downloading...');
            },
            success: function(data) {
                $('.custom-container').html(data.data);
            }

        })
        return false;
    };

    var about = function() {
        $.ajax({
            url: '/info/',
            type: 'get',
            dataType: 'json',
            beforeSend: function() {
                $('.arrow-container').html('');
                $('.custom-container').html('');
            },
            success: function(data) {
                $('.custom-container').html(data.data);
            }
        })

    }

    $('.about').click(about);
    $("#navbar-form").on("submit", ".username-form", usernameForm);

});