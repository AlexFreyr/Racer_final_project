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
                <div class="col s12">
                    <div class="card grey lighten-5">
                        <div class="card-content black-text">
                            <?php
                                include "php/connection/conn.php";

                                try{
                                    $name = $_GET['n'];
                                    $code = $_GET['code'];

                                    $sql = "SELECT `id`, `confirm_code`, `confirmed` FROM `racers` WHERE `username`='$name'";

                                    foreach ($dbh->query($sql) as $row)
                                    {
                                        if($row['confirm_code'] == $code){
                                            $userid = $row['id'];
                                            $updatequery = $dbh->prepare("UPDATE `racers` SET `confirmed`='1', `confirm_code`='0' WHERE `id`='$userid'");
                                            $updatequery->execute();

                                            echo '<h3 class="center-align">Email confirmation success!</h3><p class="flow-text center-align">Email confirmation was successful, you can now log in.</p>';
                                        }else{
                                            echo "<h3 class='center-align'>Email confirmation failure!</h3><p class='flow-text center-align'>Email confirmation failed, if you're having problem confirming your email try contacting us at vorur.mail@gmail.com and we'll try our best to resolve the issue.</p>";
                                        }
                                    }
                                }catch(Exception $e){
                                    echo $e->getMessage();
                                }
                            ?>
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
</body>
</html>