<?php
/**
 * Created by Alexander on 19-Nov-16.
 * This script creates a new user and inserts them into the database
 */


try {
    include "connection/conn.php";
    $username = $_POST['username'];
    $email = $_POST["email"];
    $password = $_POST['password'];

    $sql = "SELECT `username` FROM `racers` WHERE `username`='$username'";

    foreach ($dbh->query($sql) as $row) {
        $user_exists = $row["username"];
    }

    if (isset($user_exists)) {
        echo "Username";
    } else {
        $sql = "SELECT `email` FROM `racers` WHERE `email`='$email'";
        foreach ($dbh->query($sql) as $row) {
            $user_exists = $row["email"];
        }
        if (isset($user_exists)) {
            echo "Email";
        } else {
            $key = sha1($username);
            $statement = $dbh->prepare("INSERT INTO racers(username, email, password, confirm_code, confirmed) 
                                        VALUES(:username, :email, :password, :confirm_code, :confirmed)");
            $statement->execute(array(
                "username" => $username,
                "email" => $email,
                "password" => $password,
                "confirm_code" => (string)$key,
                "confirmed" => 0
            ));

            $subject = 'Racer confirmation email';
            $message = '
                        <html>
                        <head>
                          <title>Racer Confirmation page</title>
                        </head>
                        <body>
                           <h2>Thank you for signing up with Racer.</h2>
                           <p>Please click <a href="http://vorur.info/confirmation.php">this link</a> to activate your account and get started competing with your friends.</p>
                        </body>
                        </html>
                        ';

            // To send HTML mail, the Content-type header must be set
            $headers  = 'MIME-Version: 1.0' . "\r\n";
            $headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";

            if(mail($email, $subject, $message, $headers)){
                echo "Success";
            }
        }
    }
}catch (Exception $e){
    echo $e->getMessage();
}

?>