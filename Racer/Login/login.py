# coding=utf-8
"""
Login script that gets the user id, username and score from the database
"""
import pymysql
import pymysql.cursors
import bcrypt


class Login:
    """
    Makes the connection to the database
    """
    def __init__(self):
        self.connection = pymysql.connect(host='hostname',
                                          user='developer',
                                          password='Vorur-dev123',
                                          db='racer',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.id = None
        self.user = None
        self.highscore = None

    def login(self, username, password):
        """
        This function returns true or false if the user enters
        the correct username and password to an account
        """
        with self.connection.cursor() as cursor:
            sql = "SELECT `id`,`username`,`password` FROM `racers` WHERE `username`=%s"
            cursor.execute(sql, username)
            result = cursor.fetchone()

            if result is not None:
                sql_highscore = "SELECT `score` FROM `scores` WHERE `racer_id`=%s"
                cursor.execute(sql_highscore, (result["id"]))
                highscore_result = cursor.fetchone()

                self.id = result["id"]
                self.user = result["username"]
                self.highscore = highscore_result["score"]
                self.connection.close()

                login_result = result['password'].encode('utf-8')
                if bcrypt.hashpw(password.encode('utf-8'), login_result) == login_result:
                    return True
        return False
