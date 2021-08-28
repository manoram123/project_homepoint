const defaultBtn1 = document.querySelector("#image1");
const defaultBtn1Alt = document.querySelector("#image1-alt");
const defaultBtn2 = document.querySelector("#image2");
const defaultBtn3 = document.querySelector("#image3");
const defaultBtn4 = document.querySelector("#image4");
const defaultBtn5 = document.querySelector("#image5");
const defaultBtn6 = document.querySelector("#image6");

const customBtn1 = document.querySelector("#add1").style;
const customBtn2 = document.querySelector("#add2").style;
const customBtn3 = document.querySelector("#add3").style;
const customBtn4 = document.querySelector("#add4").style;
const customBtn5 = document.querySelector("#add5").style;
const customBtn6 = document.querySelector("#add6").style;


function clickDefault(val){
        if(val == 1){
        defaultBtn1.click();
        }
        else if(val == 11){
        defaultBtn1Alt.click();
        }
        else if(val == 2){
        defaultBtn2.click();
        }
        else if(val == 3){
        defaultBtn3.click();
        }
        else if(val == 4){
        defaultBtn4.click();
        }
        else if(val == 5){
        defaultBtn5.click();
        }
        else if(val == 6){
        defaultBtn6.click()
        }
    }

    function removeImage(val){
    if(val == 1){
        var preview = document.querySelector('#image-preview1').style;
        var delBtn = document.querySelector('#del1').style;
        var img = document.querySelector('#image1').value = null;
        preview.background = 'none';
        // document.querySelector('.slot1').style.display = 'none'
        customBtn1.display = 'block'
        delBtn.display = 'none';
    }

    if(val == 2){
        var preview = document.querySelector('#image-preview2').style;
        var delBtn = document.querySelector('#del2').style;
        var img = document.querySelector('#image2').value = null;
        preview.background = 'none';
        // document.querySelector('.slot2').style.display = 'none'
        customBtn2.display = 'block';
        delBtn.display = 'none';
    }
    if(val == 3){
        var preview = document.querySelector('#image-preview3').style;
        var delBtn = document.querySelector('#del3').style;
        var img = document.querySelector('#image3').value = null;
        preview.background = 'none';
        // document.querySelector('.slot3').style.display = 'none'
        customBtn3.display = 'block';
        delBtn.display = 'none';
    }
    if(val == 4){
        var preview = document.querySelector('#image-preview4').style;
        var delBtn = document.querySelector('#del4').style;
        var img = document.querySelector('#image4').value = null;
        preview.background = 'none';
        // document.querySelector('.slot4').style.display = 'none'
        customBtn4.display = 'block'
        delBtn.display = 'none';
    }
    if(val == 5){
        var preview = document.querySelector('#image-preview5').style;
        var delBtn = document.querySelector('#del5').style;
        var img = document.querySelector('#image5').value = null;
        preview.background = 'none';
        // document.querySelector('.slot5').style.display = 'none'
        customBtn5.display = 'block'
        delBtn.display = 'none';
    }
    if(val == 6){
        var preview = document.querySelector('#image-preview6').style;
        var delBtn = document.querySelector('#del6').style;
        var img = document.querySelector('#image6').value = null;
        preview.background = 'none';
        customBtn6.display = 'block'
        delBtn.display = 'none';
    }
}


function showPreview(event, ind){
    if(event.target.files.length>0){
        var src = URL.createObjectURL(event.target.files[0]);

        if(ind == 1){
            var delBtn = document.querySelector('#del1').style;
            var preview = document.querySelector('#image-preview1').style;
            preview.background = "url('"+src+"')";
            preview.backgroundSize = 'cover';
            customBtn1.display = 'none';
            delBtn.display = 'block';
            document.querySelector('.slot1').style.display = 'block';
        }

        if(ind == 2){
            var delBtn = document.querySelector('#del2').style;
            var preview = document.querySelector('#image-preview2').style;
            preview.background = "url('"+src+"')";
            preview.backgroundSize = 'cover'
            customBtn2.display = 'none';
            delBtn.display = 'block';
            document.querySelector('.slot2').style.display = 'block'
        }
        if(ind == 3){
            var delBtn = document.querySelector('#del3').style;
            var preview = document.querySelector('#image-preview3').style;
            preview.background = "url('"+src+"')";
            preview.backgroundSize = 'cover'
            customBtn3.display = 'none';
            delBtn.display = 'block';
            document.querySelector('.slot3').style.display = 'block'
        }
            if(ind == 4){
            var delBtn = document.querySelector('#del4').style;
            var preview = document.querySelector('#image-preview4').style;
            preview.background = "url('"+src+"')";
            preview.backgroundSize = 'cover'
            customBtn4.display = 'none';
            delBtn.display = 'block';
            document.querySelector('.slot4').style.display = 'block'
        }
        if(ind == 5){
            var delBtn = document.querySelector('#del5').style;
            var preview = document.querySelector('#image-preview5').style;
            preview.background = "url('"+src+"')";
            preview.backgroundSize = 'cover'
            customBtn5.display = 'none';
            delBtn.display = 'block';
            document.querySelector('.slot5').style.display = 'block'
        }
        if(ind == 6){
            var delBtn = document.querySelector('#del6').style;
            var preview = document.querySelector('#image-preview6').style;
            preview.background = "url('"+src+"')";
            preview.backgroundSize = 'cover';
            customBtn6.display = 'none';
            delBtn.display = 'block';
        }
    }
}


//Validation
$(document).on('submit', "#p-form",function(e){
    // e.preventDefault();
    i = document.querySelector('.img-slot1').value;
    console.log(i)
    title = $('#title').val();
    address = $('#search_input_address').val();
    price = $('#price').val();

    function alert(msg){
        $('.message-alert').removeClass('alert-success');
        $('.message-alert').addClass('alert-danger');
        $('#alert-message').html(msg);
        $('.message-alert').css("display", "block");
        $('.message-alert').removeClass('alert-hide');
        $('.message-alert').addClass('alert-show');
        setTimeout(function () {
            $('.message-alert').addClass('alert-hide');
            $('.message-alert').removeClass('alert-show');
        }, 5000) //alert fadeOut
    }

    if(title == ""){
        e.preventDefault();
        alert("Please fill all the required fields!")
    }

    if(address == ""){
        e.preventDefault();
        alert("Please fill all the required fields!")
    }

    if(price == ""){
        e.preventDefault();
        alert("Please fill all the required fields!")
    }

    if(i == ""){
        e.preventDefault();
        alert("Upload at least one Image!")  
    }

})