import re
from connexion_bdd import MongoConnector


class Users:
    def __init__(self, user_name, email, password, age="", first_name="", last_name="", security_question="",
                 security_answer=""):
        """
        PRE: prend en argument un pseudo(str), un mdp(str), un age(str), un prénom(str), un nom(str),
             une question de sécurité(str), une réponse de sécurité(str)
        POST: instancie les variables passées en argument
              SI la BDD répond
        RAISE: lance une exception "error" si la BDD ne répond pas
        """

        self.user_name = user_name
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.security_question = security_question
        self.security_answer = security_answer

        try:
            with MongoConnector() as connector:
                self.__collection = connector.db["users"]

        except Exception as error:
            print(error)

    def create(self):
        """
        Ajoute l'utilisateur dans la BDD.
        PRE:
        POST: appelle une requète qui ajoute un utilisateur avec toutes ses variables dans la BDD
        """
        query = {
            "user_name": self.user_name,
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "security_question": self.security_question,
            "security_answer": self.security_answer,
            "list_role": [22, 25, 50]
        }
        self.__collection.insert_one(query)

    def update(self, new_user_name, new_email, new_first_name, new_last_name, new_password, new_security_question,
               new_security_answer):
        """
        met à jour les données d'un utilisateur dans la BDD.
        PRE: prend en argument un nouveau pseudo(str), un nouvel email(str), un nouveau nom(str),
             un nouveau mot de passe(str), une nouvelle question de sécurité(str), une nouvelle réponse(str).
        POST: appelle une requète qui ajoute un utilisateur avec toutes ses variables dans la BDD
        """

        query = {"user_name": self.user_name}

        new_values = {"$set": {
            "user_name": new_user_name,
            "email": new_email,
            "first_name": new_first_name,
            "last_name": new_last_name,
            "password": new_password,
            "security_question": new_security_question,
            "security_answer": new_security_answer
        }}
        self.__collection.update_one(query, new_values)

    def delete(self):
        """
        Supprime l'utilisateur de la BDD.
        PRE:
        POST: appelle une requète qui supprime un utilisateur à partir de son pseudo dans la BDD
        """
        query = {"user_name": self.user_name}
        self.__collection.delete_one(query)

    def has_role(self, id_role):
        """
        Vérifie dans la BDD si l'Utilisateur dispose d'un rôle.
        PRE: prend en argument l'id du role qu'on souhaite chercher
        POST: retourne true si le rôle est dans la list de la BDD et sinon False
        """
        res = self.__collection.find_one({"user_name": self.user_name, "list_role": id_role})
        if res is None:
            return False
        else:
            return res

    def is_exist_user_name(self):
        """
        Vérifie si le nom d'utilisateur existe déjà dans la base de données.
        PRE:
        POST: True si le user_name courant existe dans la BDD et sinon False.
        """
        query = {"user_name": self.user_name}
        if self.__collection.count_documents(query):
            return True
        else:
            return False

    def is_exist_email(self):
        """
        Vérifie si le l'email de l'utilisateur existe déjà dans la base de données.
        PRE:
        POST: retourne true si l'email existe dans la BDD et sinon False.
        """
        query = {"email": self.email}
        if self.__collection.count_documents(query):
            return True
        else:
            return False

    def is_user_in_bdd(self):
        """
        Vérifie dans la BDD si l'Utilisateur existe et que son mot de passe est le même que dans la BDD.
        PRE: prend en argument l'id du role qu'on souhaite chercher
        POST: retourne true ainsi que la réponsede la BDD si le rôle est dans la list de la BDD et sinon False
              et un string informant d'une erreur
        """
        query = {"user_name": self.user_name, "password": self.password}
        res = self.__collection.find_one(query)
        if res is None:
            return False, "L'utilisateur n'existe pas ou MDP erroné !"
        else:
            return True, res
