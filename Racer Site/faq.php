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
                <div class="card grey lighten-5">
                    <div class="card-content black-text">
                        <div class="row">

                            <img class="bannerFAQ responsive-img fullscreen" src="./images/FAQ3.png">
                            <ul class="collapsible popout" data-collapsible="accordion">
                                <li>
                                  <div class="collapsible-header"><i class="material-icons">place</i>Where can i get the game?</div>
                                  <div class="collapsible-body"><p>Well currently the only way to play the game is to go to the front page and click the github link at the bottom and there you can download the game and play. In the future we hope to get a download up and running on our site so you don't have to fork the github</p></div>
                                </li>
                                <li>
                                  <div class="collapsible-header"><i class="material-icons">games</i>Do I need to make an account to play the game?</div>
                                  <div class="collapsible-body"><p>Yes you do you have to make an account with us, you can do that by going over the sign in / sign up tab at the top of the website and making an account there. You will be sent a comformation email to the email address you provided confirming that you did indeed make an account with us. After that you´re ready to start playing, good luck :)</p></div>
                                </li>
                                <li>
                                  <div class="collapsible-header"><i class="material-icons">whatshot</i>On your main page you advertise multiplayer and car customization but they don't seem to be in a the game?</div>
                                  <div class="collapsible-body"><p>These are things we hope to add into the game in the future as dlc, currently we are working on the core of the game.</p></div>
                                </li>
                                 <li>
                                  <div class="collapsible-header"><i class="material-icons">games</i>What do you in the game?</div>
                                  <div class="collapsible-body"><p>You avoid oncoming traffic and try to find your wife</p></div>
                                </li>
                            </ul>
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
    <script src="javascript/score.js"></script>
    <script src="https://use.fontawesome.com/0f8675ccce.js"></script>

</body>
</html>