import mysql.connector as mysql


class settings():
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="n21217916",
        database="discord"
    )
    cursor = db.cursor()



