import settings as settings
import mysql

class Authentification():
    def __init__(self):
        self.db = mysql.connect()
        self.db.connect()
    
    def login(self, email, password):
        try:
            sql = "SELECT id, password, role FROM users WHERE email = %s"
            self.db.cursor.execute(sql, (email,))
            user = self.db.cursor.fetchone()

            if user:
                user_id, db_password, role = user
                if password == db_password:
                    return {"success": True, "user_id": user_id, "role": role}
                else:
                    return {"success": False, "message": "Mot de passe incorrect"}
            else:
                return {"success": False, "message": "Utilisateur non trouvé"}
        except mysql.connector.Error as err:
            print("Erreur lors de l'authentification:", err)
            return {"success": False, "message": "Erreur lors de l'authentification"}
        
    def register(self, nom, prenom, email, password):
        try:
            sql_check = "SELECT id FROM users WHERE email = %s"
            self.db.cursor.execute(sql_check, (email,))
            existing_user = self.db.cursor.fetchone()
            if existing_user:
                return {"success": False, "message": "Cet email est déjà associé à un compte"}
            
            sql_insert = "INSERT INTO users (nom, prenom, email, password) VALUES (%s, %s, %s, %s)"
            self.db.cursor.execute(sql_insert, (nom, prenom, email, password))
            self.db.connection.commit()
            return {"success": True, "message": "Utilisateur enregistré avec succès"}
        except mysql.connector.Error as err:
            print("Erreur lors de l'enregistrement de l'utilisateur:", err)
            return {"success": False, "message": "Erreur lors de l'enregistrement de l'utilisateur"}
        
    def change_password(self, email, old_password, new_password):
        login_result = self.login(email, old_password)
        if login_result["success"]:
            try:
                sql = "UPDATE users SET password = %s WHERE email = %s"
                self.db.cursor.execute(sql, (new_password, email))
                self.db.connection.commit()
                return {"success": True, "message": "Mot de passe mis à jour avec succès"}
            except mysql.connector.Error as err:
                print("Erreur lors de la mise à jour du mot de passe:", err)
                return {"success": False, "message": "Erreur lors de la mise à jour du mot de passe"}
        else:
            return {"success": False, "message": login_result["message"]}