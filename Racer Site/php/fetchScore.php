<?php
/**
 * Created by Michael Jes Þórsson on 21-Nov-16.
 * Description: Load the data when page loads
 */
    include "connection/conn.php";

    $sql = "SELECT racers.username AS username, scores.score AS score
            FROM racers
            INNER JOIN scores
            ON racers.id = scores.racer_id
            ORDER BY scores.score DESC
            LIMIT 10";

    $counter = 0;
    foreach ($dbh->query($sql) as $row)
    {
        $username = $row["username"];
        $score = $row["score"];
        if($counter % 2 == 0){
            echo "<tr><td> $username </td><td> $score </td></tr>";
        }else{
            echo "<tr class='grey lighten-3'><td> $username </td><td> $score </td></tr>";
        }
        $counter += 1;
    }
?>