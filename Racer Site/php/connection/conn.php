<?php
/**
 * By: Alexander
 * Date: 19-Nov-16
 * Time: 3:44 AM
 * Description: This is class that contains the connection to the database
 */
$hostname='localhost';
$username='developer';
$password='Vorur-dev123';


try {
    $dbh = new PDO("mysql:host=$hostname;dbname=racer",$username,$password);
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}
catch(PDOException $e)
{
    echo $e->getMessage();
}

?>