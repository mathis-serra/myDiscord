import mysql.connector as mysql


class Config:
    
    def db_connect(self):
        try:
            db = mysql.connect(
                host="localhost",
                user="root",
                passwd="dominique59",
                database="myDiscord"
            )
            cursor = db.cursor()
