/**
 * Created by Alexander on 26-Nov-16.
 * This script will send the recovery email
 */

$("#recovery_button").on("click", function(){
    $email = $("#recover_email").val();

    $.ajax({
        type: "POST",
        url: "../php/recovery.php",
        data:{
            email: $email
        },
        success: function(html){
            if(html == "Email fail"){
                $("#failure").empty();
                $("#failure").append("<p class='flow-text red-text'>This email does not exist</p>")
            }else if(html == "Success"){
                $("#recovery_card").empty();
                $("#recovery_card").append($("<p class='flow-text'>Email has been sent at " + $email +" with further instructions</p>"));
            }
        }
    });
});