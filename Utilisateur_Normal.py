from Utilisateur import User

class NormalUser(User):
    def __init__(self, id, nom, prenom,password, email,role):
        super().__init__(id, nom, prenom,password, email,role)