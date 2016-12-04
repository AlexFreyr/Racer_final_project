import pymysql
import pymysql.cursors
import bcrypt

class Update:
    def __init__(self):
        self.connection = pymysql.connect(host='vorur.info',
                                          user='developer',
                                          password='Vorur-dev123',
                                          db='racer',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

   def runupdate(self, highscore, lastScore, user_id):
    if lastScore > highscore:
      with self.connection.cursor() as cursor:
          updateScore = "UPDATE `scores` SET `score`=%s WHERE `racer_id`=%s"
          cursor.execute(updateScore, (lastScore, user_id))
          print("Sucess")
    else:
        print("Fuck")