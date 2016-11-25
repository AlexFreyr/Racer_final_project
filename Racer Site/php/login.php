<?php
/**
 * By: Alexander
 * Date: 19-Nov-16
 * Time: 3:39 AM
 * Description: This script is called from 'javascript/login.js' and will verify user information
 *              and log them in if correct information is supplied.
 */
    include "connection/conn.php";
    $username = $_POST['username'];
    $password = $_POST['password'];

    $password_hash = null;
    $confirmed = null;
    $sql = "SELECT `password`, `confirmed` FROM `racers` WHERE `username`='$username'";

    foreach ($dbh->query($sql) as $row)
    {
        $password_hash = $row["password"];
        $confirmed = $row["confirmed"];
    }

    if(password_verify($password, $password_hash) && $confirmed == 1){
        print "Success";
    }else{
        print "Failure";
    }