/**
 * Created by Alexander on 19-Nov-16.
 * This script handles all of the user input in the login site,
 * the script also handles all of the AJAX calls to the server.
 */

function unexpected_error(caught_error){
    $('#error-text').remove();

    $('.row').after($('' +
        '<div class="col s12 m6">' +
        '<div class="card grey lighten-5">' +
        '<div class="card-content red-text">' +
        '<span class="card-title">Fatal Error</span>' +
        '<p>If you are seeing this text it means that something has gone horribly wrong. Please be in contact at vorur.mail@gmail.com and send us the automatically generated error: </p>' +
        caught_error +
        '</div>' +
        '</div>' +
        '</div>'));
}

// Login form //
$('#login_button').on("click", function(){
    if($.trim($('#login_username').val()) != ""){
        if($.trim($('#login_password').val()) != "") {
            $(".parallax-container .container").after($('<div class="progress"><div class="indeterminate"></div></div>'));
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
            if(html == "Failure"){
                $('#error-text').remove();
                $("div.container + div.progress").remove();
                $('#login-form').append($("<p class='flow-text red-text' id='error-text'>Incorrect username/password</p>"))
            }else if(html == "Success"){
                $('#error-text').remove();
            }
        },
        failure: function(html) {
            unexpected_error(html);
        }
    });
};


// Sign up form //
$('#signup_button').on("click", function(){
    if($.trim($('#new_username').val()) != ""){
        if($.trim($('#new_email').val()) != "" && !$('#new_email').hasClass("invalid")) {
            if($.trim($('#new_password').val()) != ""){
                if($('#new_password').val() == $('#new_repassword').val()){
                    $(".parallax-container .container").after($('<div class="progress"><div class="indeterminate"></div></div>'));
                    signup($('#new_username').val(), $('#new_email').val(), $('#new_password').val());
                }else{
                    Materialize.toast("Passwords don't match", 4000);
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

function signup(username, email, password){
    $.ajax({
        url: "../php/signup.php",
        type: "POST",
        cache: false,
        data: {
            username: username,
            email: email,
            password: password
        },
        success: function(html) {
            if(html == "Email"){
                $('#error-text').remove();
                $("div.container + div.progress").remove();
                $('#signup-form').append($("<p class='flow-text red-text' id='error-text'>Email already in use</p>"));
            }else if(html == "Username"){
                $('#error-text').remove();
                $("div.container + div.progress").remove();
                $('#signup-form').append($("<p class='flow-text red-text' id='error-text'>Username already in use</p>"));
            }else if(html == "Success"){
                //Remove everything from page and let the user know to check their inbox
                $("div.container + div.progress").remove();
                $('.parallax-container .container').empty();
                $('.container').append($("<div class='card grey lighten-5'>" +
                    "<div class='card-content black-text'>" +
                    "<h2>Thanks</h2>" +
                    "<p class='flow-text'>We've sent a confirmation email at " + email + "</p>" +
                    "<p class='flow-text'>If you can't see the email please wait for a few mintues and check the spam in your inbox, sometimes it ends up there</p>" +
                    "</div></div>"));
            }
        },
        failure: function(html) {
            unexpected_error(html);
        }
    });
};