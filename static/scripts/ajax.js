$(document).on('submit', '#user_form', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: "/accounts/register/",
        data: {
            name: $('#name').val(),
            email: $('#email').val(),
            phone: $('#phone').val(),
            username: $('#username').val(),
            password: $('#password').val(),
            confirm_password: $('#confirm_password').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data) {
            if (data.message[0] == 'error') {
                $('.message-alert').removeClass('alert-success');
                $('.message-alert').addClass('alert-danger');
            }
            else if (data.message[0] == 'success') {
                $('.message-alert').removeClass('alert-danger');
                $('.message-alert').addClass('alert-success');
                setTimeout(function () {
                    window.location.href = '/accounts/login';
                }, 1000);
            }
            $('#alert-message').html(data.message[1]);
            $('.message-alert').css("display", "block");
            $('.message-alert').removeClass('alert-hide');
            $('.message-alert').addClass('alert-show');
            setTimeout(function () {
                $('.message-alert').addClass('alert-hide');
                $('.message-alert').removeClass('alert-show');
            }, 5000) //alert fadeOut

        },
        error: function () {
            alert('failed')
        }
    })
})


$(document).on('submit', '#login-form', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/accounts/login/',
        data: {
            username: $('#username').val(),
            password: $('#password').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            console.log(data.message[0])
            if (data.message[0] == 'error') {
                $('.message-alert').removeClass('alert-success');
                $('.message-alert').addClass('alert-danger');
            }
            else if(data.message[0] == 'success'){
                $('.message-alert').removeClass('alert-danger');
                $('.message-alert').addClass('alert-success');
                setTimeout(function () {
                    window.location.href = '/';
                }, 1000);
            }
            $('#alert-message').html(data.message[1]);
            $('.message-alert').css("display", "block");
            $('.message-alert').removeClass('alert-hide');
            $('.message-alert').addClass('alert-show');

            setTimeout(function () {
                $('.message-alert').addClass('alert-hide');
                $('.message-alert').removeClass('alert-show');
            }, 5000) //alert fadeOut
        },
        error: function(error){
            alert("error")
        }
    })
})


