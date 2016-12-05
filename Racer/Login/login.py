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

    def login(self, username, password):
        with self.connection.cursor() as cursor:
            sql = "SELECT `id`,`username`,`password` FROM `racers` WHERE `username`=%s"
            cursor.execute(sql, (username))
            result = cursor.fetchone()
            print(result)

            sqlHighScore = "SELECT `score` FROM `scores` WHERE `racer_id`=%s"
            cursor.execute(sqlHighScore, (result["id"]))
            highscoreResult = cursor.fetchone()
            print(highscoreResult)


            if result != None:
                hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                print(hashed)
                if bcrypt.hashpw(password.encode('utf-8'), result['password'].encode('utf-8')) == result['password'].encode('utf-8'):
                    print('Hola')
                else:
                    print('Fuck')

                self.id = result["id"]
                self.user = result["username"]
                self.highscore = highscoreResult["score"]
                self.connection.close()
                return True
            return False


