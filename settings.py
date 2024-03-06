import mysql.connector as mysql

<<<<<<< HEAD
class settings:
   
=======

class settings():
>>>>>>> server
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="dominique59",
        database="discord"
    )
    cursor = db.cursor()


<<<<<<< HEAD

=======
>>>>>>> server
