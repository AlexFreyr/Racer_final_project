<?php
/**
 * Created by Alexander on 19-Nov-16.
 * This script creates a new user and inserts them into the database
 * called from: login.js
 */


try {
    include "connection/conn.php";

    //Get the information needed
    $username = $_POST['username'];
    $email = $_POST["email"];
    $password = $_POST['password'];

    //Check if there is a user that already has that username
    $sql = "SELECT `username` FROM `racers` WHERE `username`='$username'";

    foreach ($dbh->query($sql) as $row) {
        $user_exists = $row["username"];
    }

    if (isset($user_exists)) {
        echo "Username"; //Return this if username is in use, the js file handles the rest
    } else {
        //Check if email is in use
        $sql = "SELECT `email` FROM `racers` WHERE `email`='$email'";
        foreach ($dbh->query($sql) as $row) {
            $user_exists = $row["email"];
        }
        if (isset($user_exists)) {
            echo "Email"; //Return this if email is in use, the js file handles the rest
        } else {
            $options = [
                'cost' => 12,
            ];
            $hashed_password = password_hash($password, PASSWORD_BCRYPT, $options); //Make a password hash

            //Make a verification key that will be sent to the email provided
            $key = sha1($username);

            // Insert the user information into the database
            $statement = $dbh->prepare("INSERT INTO racers(username, email, password, confirm_code, confirmed) 
                                        VALUES(:username, :email, :password, :confirm_code, :confirmed)");
            $statement->execute(array(
                "username" => $username,
                "email" => $email,
                "password" => $hashed_password,
                "confirm_code" => (string)$key,
                "confirmed" => 0
            ));

            //Set the user score as 0
            $racer_id = null;
            $score = 0;
            $sql = "SELECT id FROM racers WHERE username='$username'";
            foreach ($dbh->query($sql) as $row)
            {
                $racer_id = $row["id"];
            }

            $statement = $dbh->prepare("INSERT INTO scores(score, racer_id)
                                        VALUES(:score, :racer_id)");
            $statement->execute(array(
                "score" => $score,
                "racer_id" => $racer_id
            ));

            //Email information
            $subject = 'Racer confirmation email';
            $message = "
                        <html>
                        <head>
                          <title>Racer Confirmation page</title>
                        </head>
                        <body>
                           <h2>Thank you for signing up with Racer.</h2>
                           <p>Please click <a href='http://vorur.info/confirmation.php?n=$username&code=$key'>this link</a> to activate your account and get started competing with your friends.</p>
                        </body>
                        </html>
                        ";

            // To send HTML mail, the Content-type header must be set
            $headers  = 'MIME-Version: 1.0' . "\r\n";
            $headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";

        }
        if(mail($email, $subject, $message, $headers)){
            echo "Success"; //If email was sent successfully
        }else{
            echo "Invalid"; //Return this if there was a problem sending the email, the js file handles the rest.
            //TODO: Make the js handle this exception
        }
    }
}catch (Exception $e){
    echo $e->getMessage();
}

?>