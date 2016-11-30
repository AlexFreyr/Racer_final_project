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
                            <div class="input-field col l6 m8 s12">
                                <i class="material-icons prefix">search</i>
                                <input class="search" type="text" id="score-search">
                                <label for="score-search">Search</label>
                            </div>
                        </div>
                        <div>
                            <table>
                                <thead>
                                    <tr>
                                        <th>User</th>
                                        <th>Score</th>
                                    </tr>
                                </thead>

                                <tbody id="score-table">

                                </tbody>
                            </table>
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