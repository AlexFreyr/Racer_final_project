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
                <img src="http://www.hdcarwallpapers.com/walls/super_sports_cars-HD.jpg">
            </div>
            <div class="container">
                <div class="row">
                    <div class="col s12 m6">
                        <div class="card grey lighten-5">
                            <div class="card-content black-text" id="login-form">
                                <span class="card-title">Login</span>
                                <input placeholder="Enter Username" id="login_username" type="text" class="validate">
                                <input placeholder="Enter Password" id="login_password" type="password" class="validate">
                                <a class="waves-effect waves-light btn" id="login_button"><i class="material-icons right">send</i>Continue</a>
                            </div>
                        </div>
                    </div>
                    <div class="col s12 m6">
                        <div class="card grey lighten-5">
                            <div class="card-content black-text">
                                <span class="card-title">Sign up</span>
                                <input placeholder="Enter New Username" id="new_username" type="text" class="validate">
                                <input placeholder="Enter Email" id="new_email" type="text" class="validate">
                                <input placeholder="Enter Password" id="new_password" type="password" class="validate">
                                <input placeholder="Re-Enter Password" id="new_repassword" type="password" class="validate">
                                <a class="waves-effect waves-light btn" id="signup_button"><i class="material-icons right">send</i>Submit</a>
                            </div>
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
    <script src="javascript/login.js"></script>
</body>
</html>