from pymongo import MongoClient


class MongoConnector:

    def __init__(self):
        """
        Create a new instance MongoClient

        PRE:
        POST: Create a connection with the database through a certificate, a uri and a developer account
        """

        certificate_path = "2TM1-G2.pem"
        uri = "mongodb+srv://cluster0.5i6qo.gcp.mongodb.net/ephecom?authSource=%24external" \
              "&authMechanism=MONGODB-X509&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE"
        client = MongoClient(uri,
                             tls=True,
                             tlsCertificateKeyFile=certificate_path)
        self.db = client['ephecom']

    def __enter__(self):
        return self

    def __exit__(self):
        self.db.close()
