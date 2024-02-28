class User():
    def __init__(self, nom, prenom,password, email, role=1):
        self.nom = nom
        self.prenom = prenom
        self.password=password
        self.email = email
        self.role = role

    def all_user_info(self):
        return f"Utilisateur: {self.nom} {self.prenom} ({self.email}) [{self.password}]- Rôle: {self.role}"
    
    def get_nom(self):
        return self.nom
    
    def get_prenom(self):
        return self.prenom
   
    def get_password(self):
        return self.password
    
    def get_email(self):
        return self.email
    
    def get_role(self):
        return self.role
    
    def set_role(self, nouveau_role):
        self.role = nouveau_role