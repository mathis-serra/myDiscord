import mysql.connector as mysql

#all the infos for the Database 
class settings():
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="n21217916",
        database="discord"
    )
    cursor = db.cursor()



