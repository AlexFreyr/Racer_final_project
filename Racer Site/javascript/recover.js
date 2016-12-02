/**
 * Created by Alexander on 30-Nov-16.
 * This script handles the recovery progress
 */

$(document).ready(function() {
    $("#new_password_button").on("click", function(){
        var password = $("#new_password").val();
        var confirm_password = $("#confirm_new_password").val();

        if (password == confirm_password){
            $.ajax({
                type: "POST",
                url: "../php/recover.php",
                cache: false,
                data: {
                    password: password
                },
                success: function(html){
                    if(html == "Password reset success"){
                        $("#change_password").empty();
                        $("#change_password").append("<p class='flow-text'>Password reset succcessful, you can now log in</p>")
                    }else if(html == "Session failure"){
                        $("#change_password").empty();
                        $("#change_password").append("<p class='flow-text'>There was a mismatch detected and password was not reset</p>")
                    }
                },
                failure: function(html){

                }
            });
        }else{
            //TODO: Notify user that passwords do not match
        }
    });
});