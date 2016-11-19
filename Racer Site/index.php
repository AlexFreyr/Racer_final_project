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

            <div class="row">
                <div class="col l4 m12">
                    <div class="card cyan darken-4">
                        <div class="card-content white-text">
                            <span class="card-title">Compete against your friends</span>
                            <p>If you sign up, you can use compare scores against your friends when you race.</p>
                        </div>
                        <div class="card-action">
                            <a href="#">Sign up here</a>
                        </div>
                    </div>
                </div>
                <div class="col l4 m12">
                    <div class="card cyan darken-4">
                        <div class="card-content white-text">
                            <span class="card-title">Customize your car</span>
                            <p>You can add your unique identity to the streets by changing up the look on your car.</p>
                        </div>
                    </div>
                </div>
                <div class="col l4 m12">
                    <div class="card cyan darken-4">
                        <div class="card-content white-text">
                            <span class="card-title">See how you progress</span>
                            <p>Explore the scores that other people are getting and try to keep up with them, it's okay if you don't though, we still care for you :)</p>
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
</body>
</html>