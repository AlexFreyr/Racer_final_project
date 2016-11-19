<?php
/**
 * By: Alexander
 * Date: 19-Nov-16
 * Time: 3:44 AM
 * Description: This is class that contains the connection to the database
 */
    class PDOConnection
    {
        protected $dbh;

        public function __construct()
        {
            try {

                $db_host = 'localhost';
                $db_name = 'racer';
                $db_user = 'developer';
                $user_pw = "Vorur-dev123";

                $con = new PDO('mysql:host='.$db_host.'; dbname='.$db_name, $db_user, $user_pw);
                $con->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION );
                $con->exec("SET CHARACTER SET utf8");  //  return all sql requests as UTF-8
            }
            catch (PDOException $err) {
                echo $err->getMessage();
                die();  //  terminate connection
            }
        }

        public function dbh()
        {
            return $this->dbh();
        }

        public function insert($command)
        {

        }
    }



?>