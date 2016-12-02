<?php
/**
 * Created by Alexander on 26-Nov-16.
 * This script will update the user password
 */

    include "connection/conn.php";
    session_start();

    $options = [
        'cost' => 12,
    ];
    $pass = password_hash($_POST["password"], PASSWORD_BCRYPT, $options);

    if (isset($_SESSION["recovery_process"])){

        $confirm_code = $_SESSION["recovery_process"];
        $new_recover = null;

        $statement = $dbh->prepare("UPDATE racers SET `password` = :new_password, `recover` = :recover WHERE `recover` = '$confirm_code'");
        $statement->bindParam(":new_password", $pass);
        $statement->bindParam(":recover", $new_recover);
        $statement->execute();

        echo "Password reset success";
        unset($_SESSION["recovery_process"]);
    }else{
        echo "Session failure";
    }