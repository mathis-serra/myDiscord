import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="dominique59",
    database="myDiscord"
)
cursor = db.cursor()
