import server.settings as settings
import mysql.connector

class User:
    def __init__(self, user_id=None, email=None):
        self.user_id = user_id
        self.email = email
        self.first_name = None
        self.last_name = None
        self.username = None
        self.password_hash = None

    def generate_username(self):
        if self.first_name and self.last_name:
            first_three_letters = self.first_name[:3].lower()
            last_three_letters = self.last_name[:3].lower()
            self.username = first_three_letters + last_three_letters
        else:
            self.username = None

    def fetch_user_by_email(self):
        try:
            sql = "SELECT * FROM users WHERE email = %s"
            settings.cursor.execute(sql, (self.email,))
            user_data = settings.cursor.fetchone()
            if user_data:
                self.user_id = user_data[0]
                self.first_name = user_data[2]
                self.last_name = user_data[3]
                self.generate_username()
                self.password_hash = user_data[5]
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("Erreur lors de la récupération des données de l'utilisateur par email:", err)
            return False
