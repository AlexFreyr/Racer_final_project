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
            <div class="card grey lighten-5">
                <div class="card-content black-text">
                    <div class="row">
                        <h4>
                            Your profile
                        </h4>
                        <div class="card-content black-text grey lighten-4">
                            <p class="flow-text">Statistics</p>
                            <p class="flow-text"></p>
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
<script src="javascript/score.js"></script>

</body>
</html>