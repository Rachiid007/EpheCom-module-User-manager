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

    for x in collection.find():
        print(x)


def user_in_bdd(user_name, password):
    connector = MongoConnector()

    collection = connector.db["users"]

    query_all = {"user_name": user_name, "password": password}
    if collection.count_documents(query_all):
        return True
    else:
        return False


class Users(MongoConnector):

    def __init__(self, user_name, email, password, first_name="", last_name="", q_securite="", ans_securite=""):
        super().__init__()

        self.user_name = user_name
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
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


if __name__ == '__main__':

    try:
        user1 = Users(user_name="Rachiid007", password="rachid1234", email="rachid@gmail.com")
        # user1.create()

        # print(user_in_bdd("Abderrachid", "rachid1234"))
        list_users()
        # print(user1.is_exist_user_name())

    except Exception as e:
        print(e)
