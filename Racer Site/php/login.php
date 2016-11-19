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

    $con = new PDOConnection();
    $con = $con->dbh();
    echo $con;

?>