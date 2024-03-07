import mysql.connector as mysql


class settings():

    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="dominique59",
        database="discord"
    )
    cursor = db.cursor()


