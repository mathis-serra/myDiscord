import mysql.connector as mysql

#all the infos for the Database 
class settings():
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="dominique59",
        database="discord"
    )
    cursor = db.cursor()



