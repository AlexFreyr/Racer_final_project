<?php
/**
 * Created by Alexander on 26-Nov-16.
 * This script will send the recover email and update the database information
 */
    include "connection/conn.php";
    $email = $_POST["email"];
    $sql = "SELECT `username` FROM `racers` WHERE `email`='$email'";

    foreach ($dbh->query($sql) as $row) {
        $user_exists = $row["username"];
    }

    if(isset($user_exists)){

        $key = password_hash($email, PASSWORD_BCRYPT);
        $subject = 'Racer recovery email';
        $message = "
                        <html>
                        <head>
                          <title>Racer recovery email</title>
                        </head>
                        <body>
                           <h2>Lost password ?</h2>
                           <p>Please click <a href='http://vorur.info/recover.php?n=$user_exists&code=$key'>this link</a> to change the password to your account.</p>
                           <p>If you do not recognize sending this email, please ignore it</p>
                        </body>
                        </html>
                        ";

        // To send HTML mail, the Content-type header must be set
        $headers  = 'MIME-Version: 1.0' . "\r\n";
        $headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";

        if(mail($email, $subject, $message, $headers)){
            $statement = $dbh->prepare("UPDATE racers SET `recover` = :recover WHERE `username` = '$user_exists'");
            $statement->bindParam(":recover", $key);
            $statement->execute();

            echo "Success";
        }
    }else{
        echo "Email fail";
    }