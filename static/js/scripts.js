$("form[name=signup_form").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
    console.log(data)
    var signupUType= document.getElementById('signupUserType').value;
    if(signupUType === 'requestor'){
    $.ajax({
        url: "/user/signup",
        type: "POST",
        data : data,
        dataType: "json",
        success : function(resp){
            console.log(resp);
            window.location.href ="/requestorDashboard"
        },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
        });
    }else{
        $.ajax({
            url: "/user/signup",
            type: "POST",
            data : data,
            dataType: "json",
            success : function(resp){
                console.log(resp);
                window.location.href ="/workerDashboard"
            },
            error: function(resp){
                console.log(resp);
                $error.text(resp.responseJSON.error).removeClass("error--hidden");
            }
            });
    }
    e.preventDefault();
})

$("form[name=login_form").submit(function(e){
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
    var loginUType= document.getElementById('loginUserType').value;
    if(loginUType === 'requestor'){
    $.ajax({
        url: "/user/login",
        type: "POST",
        data : data,
        dataType: "json",
        success : function(resp){
            console.log(resp);
            window.location.href ="/requestorDashboard"
        },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
        });
    }else{
        $.ajax({
            url: "/user/login",
            type: "POST",
            data : data,
            dataType: "json",
            success : function(resp){
                console.log(resp);
                window.location.href ="/workerDashboard"
            },
            error: function(resp){
                console.log(resp);
                $error.text(resp.responseJSON.error).removeClass("error--hidden");
            }
            });
    }
    e.preventDefault();
})