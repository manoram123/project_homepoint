
// Ajax Register
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



// Ajax Login
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
                    window.location.href = '/user/dashboard/';
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

//Ajax Hostel Listing
$(document).ready(function(){
    $("").submit(function(e){
        e.preventDefault()
        $.ajax({
            type: 'POST',
            url: "/hostels/listhostel/",
            dataType: "json",
            processData: false,
            contentType: false,
            // data: {
            //     // title: $("#title").val(),
            //     // address: $("#search_input_address").val(),
            //     // price: $("#price").val(),
            //     // description: $("#title").val(),
            //     csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            // },
            success: function (data) {
                if (data.message[0] == 'error') {
                    // $('.message-alert').removeClass('alert-success');
                    // $('.message-alert').addClass('alert-danger');
                }
                else if (data.message[0] == 'success') {
                    $('.message-alert').removeClass('alert-danger');
                    $('.message-alert').addClass('alert-success');
                    // setTimeout(function () {
                    //     window.location.href = '/user/dashboard';
                    // }, 1000);
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
            error: function (error) {
                alert(error.responseText)
            }
        })
    })   
}) 


$(document).ready(function(){
    setTimeout(function(){
        $('.message-alert').css.display = 'none'
    }, 5000)
})