import re
from connexion_bdd import MongoConnector


class Users:
    def __init__(self, user_name, email, password, age, first_name="", last_name="", q_securite="", ans_securite=""):

        self.user_name = user_name
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.q_securite = q_securite
        self.ans_securite = ans_securite

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
            "q_securite": self.q_securite,
            "ans_securite": self.ans_securite,
            "list_role": [22, 25, 50]
        }
        self.__collection.insert_one(query)

    def update(self, new_user_name, new_email, new_first_name, new_last_name, new_password, new_q_securite,
               new_ans_securite):

        query = {"user_name": self.user_name}

        new_values = {"$set": {
            "user_name": new_user_name,
            "email": new_email,
            "first_name": new_first_name,
            "last_name": new_last_name,
            "password": new_password,
            "q_securite": new_q_securite,
            "ans_securite": new_ans_securite
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


def register_verify(user_name, email, age, password, confirm_password):
    if not re.match(r'\b[A-Za-z0-9._+-@]{7,25}\b', password):
        return False, "Le MDP ne respect pas la norme !"

    if password != confirm_password:
        return False, "Les 2 MDP ne correspondent pas !"

    if age < 13:
        return False, "Vous devez avoir minimum 13 ans !"

    user_test = Users(user_name, email, password, age)

    if not user_test.is_exist_user_name():
        return False, "Le nom d'utilisateur existe déjà !"

    if not user_test.is_exist_email():
        return False, "L'adresse email existe déjà !"

    user_test.create()
    return True


def login_verify(user_name, password):
    user_test = Users(user_name=user_name, email="", password=password, age="")
    return user_test.is_user_in_bdd()


if __name__ == '__main__':
    user1 = Users(user_name="Rachiid007", password="rachid1234", email="rachid@gmail.com", age="")
    # user1.create()
    print(user1.is_user_in_bdd())

    # print(user1.is_user_in_bdd())
    # il_est_dans_la_db = user1.is_user_in_bdd()[0]
    # print(il_est_dans_la_db)

    # list_users()
    # print(user1.is_exist_user_name())

    pass
