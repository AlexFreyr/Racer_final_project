import pymysql

# if self.lastScore > self.highscore:
#    with self.connection.cursor() as cursor:
#       updateScore = "UPDATE `scores` SET `score`=%s WHERE `racer_id`=%s"
#       cursor.execute(updateScore, (self.lastScore, self.user_id))
#       updateResult = cursor.fetchone()