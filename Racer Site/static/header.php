
<!--
 * By: Alexander
 * Date: 19-Nov-16
 * Time: 1:18 AM
 * Description: This is the static header for the website
 -->

<nav>
    <div class="nav-wrapper cyan darken-4">
        <a href="index.php" class="brand-logo center"><i class="material-icons">directions_car</i>Racer</a>
        <a href="#" data-activates="mobile-demo" class="button-collapse"><i class="material-icons">menu</i></a>
        <ul class="right hide-on-med-and-down">

            <?php
                session_start();

                if(isset($_SESSION["user_token"])){
                    echo '<li><a href="../userpage.php"><i class="material-icons left">perm_identity</i>Your page</a></li>';
                }else{
                    echo '<li><a href="../login.php"><i class="material-icons left">perm_identity</i>Login / signup</a></li>';
                }
            ?>
            <li><a href="../scores.php"><i class="material-icons left">assessment</i>All scores</a></li>

        </ul>
        <ul class="left hide-on-med-and-down">
            <li><a href="../faq.php"><i class="material-icons left">flag</i>FAQ</a></li>
        </ul>

        <ul class="side-nav" id="mobile-demo">
            <?php
                if(isset($_SESSION["user_token"])){
                    echo '<li><a href="../userpage.php"><i class="material-icons left">perm_identity</i>Your page</a></li>';
                }else{
                    echo '<li><a href="../login.php"><i class="material-icons left">perm_identity</i>Login / signup</a></li>';
                }
            ?>
            <li><a href="../scores.php"><i class="material-icons left">assessment</i>All scores</a></li>
            <li><a href="../faq.php"><i class="material-icons left">flag</i>FAQ</a></li>
        </ul>
    </div>
</nav>
