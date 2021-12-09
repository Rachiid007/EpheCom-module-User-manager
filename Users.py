import re
from connexion_bdd import MongoConnector


class Users:
    def __init__(self, user_name, email="", password="", age="", first_name="", last_name="", security_question="",
                 security_answer=""):

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
        """ Ajoute l'utilisateur dans la BDD.
        :return:
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
        :return:
        """
        query = {"user_name": self.user_name}
        self.__collection.delete_one(query)

    def has_role(self, id_role):
        """ Vérifie si l'Utilisateur dispose d'un rôle.
        parcourt la list "list_role" -> True si il a le role
        :param id_role: l'ID du role qu'on souhaite
        :return: True si le rôle est dans la list et sinon False
        """
        res = self.__collection.find_one({"user_name": self.user_name, "list_role": id_role})
        if res is None:
            return False
        else:
            return res

    def is_exist_user_name(self):
        """ Vérifiez si le nom d'utilisateur existe déjà dans la base de données.
        :return: True si le user_name courant existe dans la BDD et sinon False.
        """
        query = {"user_name": self.user_name}
        if self.__collection.count_documents(query):
            return True
        else:
            return False

    def is_exist_email(self):
        """ Vérifiez si le nom d'utilisateur existe déjà dans la base de données.
        :return: True si le user_name courant existe dans la BDD et sinon False.
        """
        query = {"email": self.email}
        if self.__collection.count_documents(query):
            return True
        else:
            return False

    def is_user_in_bdd(self):
        query = {"user_name": self.user_name, "password": self.password}
        res = self.__collection.find_one(query)
        if res is None:
            return False, "L'utilisateur n'existe pas ou MDP erroné !"
        else:
            return True, res
