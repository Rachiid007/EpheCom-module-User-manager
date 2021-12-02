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
