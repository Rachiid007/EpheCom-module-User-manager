import re

from pymongo import MongoClient


class MongoConnector:

    def __init__(self):
        certificat_path = "2TM1-G2.pem"
        uri = "mongodb+srv://cluster0.5i6qo.gcp.mongodb.net/ephecom?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE"
        client = MongoClient(uri, tls=True, tlsCertificateKeyFile=certificat_path)
        self.db = client['ephecom']

    def __enter__(self):
        return self

    def __exit__(self):
        self.db.close()


def list_users():
    connector = MongoConnector()

    collection = connector.db["users"]

    return [print(x) for x in collection.find()]


class Users(MongoConnector):

    def __init__(self, user_name, email, password, first_name="", last_name="", age=13, q_securite="", ans_securite=""):
        super().__init__()

        self.user_name = user_name
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.q_securite = q_securite
        self.ans_securite = ans_securite

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
        self.db["users"].insert_one(query)

    def is_exist_user_name(self):
        """ Vérifiez si le nom d'utilisateur existe déjà dans la base de données.
        :return: True si le user_name courant existe dans la BDD et sinon False.
        """
        query = {"user_name": self.user_name}
        if self.db["users"].count_documents(query):
            return True
        else:
            return False

    def is_exist_email(self):
        """ Vérifiez si le nom d'utilisateur existe déjà dans la base de données.
        :return: True si le user_name courant existe dans la BDD et sinon False.
        """
        query = {"email": self.email}
        if self.db["users"].count_documents(query):
            return True
        else:
            return False

    def update(self, new_user_name, new_email, new_first_name, new_last_name, new_password, new_q_securite,
               new_ans_securite):
        """ Modifie les données de l'utilisateur qui sont dans la BDD.
        :param new_user_name:
        :param new_email:
        :param new_first_name:
        :param new_last_name:
        :param new_password:
        :param new_q_securite:
        :param new_ans_securite:
        :return:
        """

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
        self.db["users"].update_one(query, new_values)

    def delete(self):
        """
        Supprime l'utilisateur de la BDD.
        :return:
        """
        query = {"user_name": self.user_name}
        self.db["users"].delete_one(query)

    def has_role(self, id_role):
        """ Vérifie si l'Utilisateur dispose d'un rôle.
        parcourt la list "list_role" -> True si il a le role
        :param id_role: l'ID du role qu'on souhaite
        :return: True si le rôle est dans la list et sinon False
        """
        res = self.db["users"].find_one({"user_name": self.user_name, "list_role": id_role})
        if res is None:
            return False
        else:
            return res

    def is_user_in_bdd(self) :
        query = {"user_name": self.user_name, "password": self.password}
        res = self.db["users"].find_one(query)
        if res is None:
            return False, "L'utilisateur n'existe pas ou MDP erroné !"
        else:
            return True, res


def register_verify(user_name, email, password, confirm_password, age):
    if not re.match(r'\b[A-Za-z0-9._+-@]{7,25}\b', password):
        return False, "Le MDP ne respect pas la norme !"

    if password != confirm_password:
        return False, "Les 2 MDP ne correspondent pas !"

    if age < 13:
        return False, "Vous devez avoir minimum 13 ans !"

    user_test = Users(user_name, email, password)

    if not user_test.is_exist_user_name():
        return False, "Le nom d'utilisateur existe déjà !"

    if not user_test.is_exist_email():
        return False, "L'adresse email existe déjà !"

    user_test.create()
    return True


if __name__ == '__main__':

    try:
        user1 = Users(user_name="Rachiid007", password="rachid1234", email="rachid@gmail.com")
        # user1.create()
        # print(user_in_bdd("Abderrachid", "rachid1234"))

        # print(user1.is_user_in_bdd())
        il_est_dans_la_db = user1.is_user_in_bdd()[0]
        print(il_est_dans_la_db)

        # list_users()
        # print(user1.is_exist_user_name())

    except Exception as e:
        print(e)
