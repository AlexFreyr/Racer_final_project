# coding=utf-8
"""
Updates the user score with the highscore that the user gets
"""
import pymysql
import pymysql.cursors


class Update:
    """
    Update class that sets the connection to the database
    """
    def __init__(self):
        self.connection = pymysql.connect(host='vorur.info',
                                          user='developer',
                                          password='Vorur-dev123',
                                          db='racer',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def run_update(self, highscore, last_score, user_id):
        """
        Update the information with a update query to the database
        """
        if last_score > highscore:
            with self.connection.cursor() as cursor:
                update_score = "UPDATE `scores` SET `score`=%s WHERE `racer_id`=%s"
                cursor.execute(update_score, (last_score, user_id))
                cursor.close()
                self.connection.commit()
                self.connection.close()
                print("Score updated")
