<?php
/**
 * Created by Alexander Freyr on 21-Nov-16.
 * Description: Allows the player to search through all of the scores.
 */
    include "connection/conn.php";
    session_start();
    $user_input = $_POST['user_input'];

    $sql = "SELECT racers.username AS username, scores.score AS score
            FROM racers
            INNER JOIN scores
            ON racers.id = scores.racer_id
            WHERE racers.username LIKE '%$user_input%'
            OR scores.score LIKE '$user_input%'
            ORDER BY username, score DESC
            LIMIT 10";

    $counter = 0;
    foreach ($dbh->query($sql) as $row)
    {
        $username = $row["username"];
        $score = $row["score"];
        if($counter % 2 == 0){
            if (strtolower($username) == strtolower($_SESSION["username"])){
                echo "<tr class='green-text'><td> $username </td><td> $score </td></tr>";
            }else{
                echo "<tr><td> $username </td><td> $score </td></tr>";
            }
        }else{
            if (strtolower($username) == strtolower($_SESSION["username"])) {
                echo "<tr class='green-text grey lighten-3'><td> $username </td><td> $score </td></tr>";
            }else{
                echo "<tr class='grey lighten-3'><td> $username </td><td> $score </td></tr>";
            }
        }
        $counter += 1;
    }

    if($counter == 0){
        echo "<tr><td class='red-text'>No data found</td></tr>";
    }

?>