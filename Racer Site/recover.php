<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <!--Import Google Icon Font-->
    <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/css/materialize.min.css">
    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <!--Custom css scripts go below this comment-->
    <link type="text/css" rel="stylesheet" href="css/style.css">

</head>

<body>
<main>
    <?php
    include "static/header.php";
    ?>
    <div class="parallax-container">
        <div class="parallax">
            <img src="images/bg.jpg">
        </div>
        <div class="container">
            <div class="row">
                <div class="col s12">
                    <div class="card grey lighten-5">
                        <?php
                            if(isset($_GET["n"]) && isset($_GET["code"])){
                                session_start();
                                include "php/connection/conn.php";

                                $username = $_GET["n"];
                                $recovery_code = $_GET["code"];

                                $sql = "SELECT `recover`, `confirmed` FROM `racers` WHERE `username`='$username'";
                                $confirmed = null;

                                foreach ($dbh->query($sql) as $row)
                                {
                                    $recovery_confirm = $row["recover"];
                                    $confirmed = $row["confirmed"];
                                }

                                if ($confirmed == 1){
                                    if ($recovery_code == $recovery_confirm){
                                        $_SESSION["recovery_process"] = $recovery_code;
                                        echo "<div class='card-content black-text' id='change_password'>
                                        <span class='card-title'>Enter new password</span>
                                        <input placeholder='New Password' type='password' id='new_password' class='validate'>
                                        <input placeholder='Confirm new password' type='password' id='confirm_new_password' class='validate'>
                                        <a class='waves-effect waves-light btn' id='new_password_button'><i class='material-icons right'>send</i>Submit</a>
                                      </div>";
                                    } else{
                                        echo "<div class=\"card-content black-text\" id=\"recovery_card\">
                                        <span class=\"card-title\">Password recovery</span>
                                        <input placeholder=\"Enter your email\" id=\"recover_email\" type=\"email\" class=\"validate\">
                                        <a class=\"waves-effect waves-light btn\" id=\"recovery_button\"><i class=\"material-icons right\">send</i>Continue</a>
                                        <div id=\"failure\">
                                        </div>
                                      </div>";
                                    }
                                }else{
                                    echo "<div class=\"card-content black-text\" id=\"recovery_card\">
                                        <span class=\"card-title\">Password recovery</span>
                                        <input placeholder=\"Enter your email\" id=\"recover_email\" type=\"email\" class=\"validate\">
                                        <a class=\"waves-effect waves-light btn\" id=\"recovery_button\"><i class=\"material-icons right\">send</i>Continue</a>
                                        <div id=\"failure\">
                                        </div>
                                      </div>";
                                }
                            }else{
                                echo "<div class=\"card-content black-text\" id=\"recovery_card\">
                                        <span class=\"card-title\">Password recovery</span>
                                        <input placeholder=\"Enter your email\" id=\"recover_email\" type=\"email\" class=\"validate\">
                                        <a class=\"waves-effect waves-light btn\" id=\"recovery_button\"><i class=\"material-icons right\">send</i>Continue</a>
                                        <div id=\"failure\">
                                        </div>
                                      </div>";
                            }
                        ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
</main>

<!--Footer goes outside the main tag to make sure it stays on the bottom of the page-->
<?php
include "static/footer.php";
?>

<!--Import jQuery before materialize.js-->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<!-- Compiled and minified JavaScript -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/js/materialize.min.js"></script>
<!--Custom javascript files go below this comment-->
<script src="javascript/start.js"></script>
<?php
    if(isset($_GET["n"]) && isset($_GET["code"])) {
        echo "<script src=\"javascript/recover.js\"></script>";
    }
?>
echo "<script src='javascript/recovery.js'></script>";
</body>
</html>