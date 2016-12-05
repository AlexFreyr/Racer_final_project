import pymysql
import pymysql.cursors
import bcrypt


class Login:
    def __init__(self):
        self.connection = pymysql.connect(host='vorur.info',
                                          user='developer',
                                          password='Vorur-dev123',
                                          db='racer',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.id = None
        self.user = None
        self.highscore = None

    def login(self, username, password):
        with self.connection.cursor() as cursor:
            sql = "SELECT `id`,`username`,`password` FROM `racers` WHERE `username`=%s"
            cursor.execute(sql, username)
            result = cursor.fetchone()

            sql_highscore = "SELECT `score` FROM `scores` WHERE `racer_id`=%s"
            cursor.execute(sql_highscore, (result["id"]))
            highscore_result = cursor.fetchone()

            if result is not None:
                self.id = result["id"]
                self.user = result["username"]
                self.highscore = highscore_result["score"]
                self.connection.close()
                if bcrypt.hashpw(password.encode('utf-8'), result['password'].encode('utf-8')) == result['password'].encode('utf-8'):
                    return True
            return False
