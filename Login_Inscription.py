from settings import settings
import mysql

class Authentification():
    def __init__(self):
        pass 
    
    def login(self, email, password_hash):
        try:
            sql = "SELECT id, password_hash, role FROM users WHERE email = %s"
            settings.cursor.execute(sql, (email,))
            user = settings.cursor.fetchone()

            if user:
                id, db_password_hash, role = user
                if password_hash == db_password_hash:
                    return {"success": True, "id": id, "role": role}
                else:
                    return {"success": False, "message": "Mot de passe incorrect"}
            else:
                return {"success": False, "message": "Utilisateur non trouvé"}
        except mysql.connector.Error as err:
            print("Erreur lors de l'authentification:", err)
            return {"success": False, "message": "Erreur lors de l'authentification"}
        
    def register(self, first_name, name, email, password_hash):
        try:
            if not email.endswith("@laplateforme.io"):
                return {"success": False, "message": "L'adresse e-mail doit se terminer par '@laplateforme.io'"}
        
            sql_check = "SELECT id FROM users WHERE email = %s"
            settings.cursor.execute(sql_check, (email,))
            existing_user = settings.cursor.fetchone()
            if existing_user:
                return {"success": False, "message": "Cet email est déjà associé à un compte"}
            
            sql_insert = "INSERT INTO users (first_name, name, email, password_hash) VALUES (%s, %s, %s, %s)"
            settings.cursor.execute(sql_insert, (first_name, name, email, password_hash))
            
            sql_update_username = "UPDATE users SET username = CONCAT(LEFT(first_name, 3), LEFT(name, 3))"
            settings.cursor.execute(sql_update_username)
            
            settings.db.commit()
            
            return {"success": True, "message": "Utilisateur enregistré avec succès"}
        except mysql.connector.Error as err:
            print("Erreur lors de l'enregistrement de l'utilisateur:", err)
            return {"success": False, "message": "Erreur lors de l'enregistrement de l'utilisateur"}

            
        
    def change_password_hash(self, email, old_password_hash, new_password_hash):
        login_result = self.login(email, old_password_hash)
        if login_result["success"]:
            try:
                sql = "UPDATE users SET password_hash = %s WHERE email = %s"
                settings.cursor.execute(sql, (new_password_hash, email))
                settings.db.commit()
                return {"success": True, "message": "Mot de passe mis à jour avec succès"}
            except mysql.connector.Error as err:
                print("Erreur lors de la mise à jour du mot de passe:", err)
                return {"success": False, "message": "Erreur lors de la mise à jour du mot de passe"}
        else:
            return {"success": False, "message": login_result["message"]}
        
    def get_user_info(self, email):
        try:
            sql = "SELECT id, first_name, name, email, username, role FROM users WHERE email = %s"
            settings.cursor.execute(sql, (email,))
            user_info = settings.cursor.fetchone()
            if user_info:
                id, first_name, name, email, username, role = user_info
                return {"id": id, "first_name": first_name, "name": name, "email": email, "username": username, "role": role}
            else:
                return None
        except mysql.connector.Error as err:
            print("Erreur lors de la récupération des informations de l'utilisateur:", err)
            return None
