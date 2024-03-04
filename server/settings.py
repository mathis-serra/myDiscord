import mysql.connector as mysql


db = mysql.connect(
    host="localhost",
    user="root",
    passwd="dominique59",
    database="discord"
)
cursor = db.cursor()



