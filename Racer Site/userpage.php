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
                        <div class="card-content black-text grey lighten-4">
                            <h4>Statistics</h4>
                            <p class="flow-text">
                                <strong>Your highscore:</strong>
                                <?php
                                    session_start();
                                    include "php/connection/conn.php";

                                    $id = $_SESSION["id"];
                                    $sql = "SELECT score
                                            FROM scores
                                            WHERE racer_id = '$id'";

                                    $score = null;
                                    foreach ($dbh->query($sql) as $row) {
                                        $score = $row["score"];
                                        echo $row["score"];
                                    }
                                ?>
                            </p>
                            <p class="flow-text">
                                You have higher score than
                                <?php
                                    $sql = "SELECT count(score) as baseline
                                            FROM scores 
                                            WHERE score > '$score'";

                                    $baseline = null;
                                    foreach ($dbh->query($sql) as $row) {
                                        $baseline = $row["baseline"];
                                    }

                                    $sql = "SELECT count(score) as everyone
                                                FROM scores";

                                    $all = null;
                                    foreach ($dbh->query($sql) as $row) {
                                        $all = $row["everyone"];
                                    }

                                    if(($all - $baseline - 1) == 1){
                                        echo $all - $baseline - 1 . " person";
                                    }else{
                                        echo $all - $baseline - 1 . " persons";
                                    }

                                    if (($all - 1) == 1){
                                        echo " / " . ($all - 1) . " person";
                                    }else{
                                        echo " / " . ($all - 1) . " persons";
                                    }
                                ?>
                            </p>

                            <h4>Account Details</h4>
                            <p class="flow-text">
                                <strong>Username:</strong>
                                <?php
                                    echo $_SESSION["username"];
                                ?>
                            </p>
                            <p class="flow-text">
                                <strong>Email:</strong>
                                <?php
                                    $sql = "SELECT email
                                                FROM racers
                                                WHERE id = '$id'";

                                    foreach ($dbh->query($sql) as $row) {
                                        echo $row["email"];
                                    }
                                ?>
                            </p>
                        </div>
                        <br>
                        <a class="btn red" id="logout">Logout</a>
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