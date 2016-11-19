/**
 * Created by Alexander on 19-Nov-16.
 * This script handles all of the user input in the login site,
 * the script also handles all of the AJAX calls to the server.
 */

// Login form //
$('#login_button').on("click", function(){
    if($.trim($('#login_username').val()) != ""){
        if($.trim($('#login_password').val()) != "") {
            login($('#login_username').val(), $('#login_password').val());
        }else{
            Materialize.toast('Password required', 4000);
        }
    }else{
        Materialize.toast('Username required', 4000);
    }
});

function login(username, password){
    $.ajax({
        url: "../php/login.php",
        type: "POST",
        cache: false,
        data: {
            username: username,
            password: password
        },
        success: function(html) {

        },
        failure: function(html) {

        }
    });
};


// Sign up form //
$('#signup_button').on("click", function(){
    if($.trim($('#new_username').val()) != ""){
        if($.trim($('#new_email').val()) != "") {
            if($.trim($('#new_password').val()) != ""){
                if($.trim($('#new_repassword').val()) != ""){
                    if($('#new_password').val() == $('#new_repassword').val()){

                    }else{
                        Materialize.toast("Passwords don't match", 4000);
                    }
                }else{
                    Materialize.toast('Password re-enter missing', 4000);
                }
            }else{
                Materialize.toast('Password required', 4000);
            }
        }else{
            Materialize.toast('Email required', 4000);
        }
    }else{
        Materialize.toast('Username required', 4000);
    }
});