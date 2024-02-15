import mysql.connector

class DatabaseConnect():
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "n21217916"
        self.database = "discord"
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connexion")
        except mysql.connector.Error as err:
            print("Erreur de connexion :", err)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Deconnexion")


test = DatabaseConnect()
test.connect()