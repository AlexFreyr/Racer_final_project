import pymysql
import pymysql.cursors

class Login:
    def __init__(self):
        self.connection = pymysql.connect(host='vorur.info',
                                          user='developer',
                                          password='Vorur-dev123',
                                          db='racer',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.id = None

    def login(self, username, password):
        with self.connection.cursor() as cursor:
            sql = "SELECT `id` FROM `racers` WHERE `username`=%s AND `password`=%s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()

            self.connection.close()

            if result != None:
                self.id = result["id"]
                return True
            return False