import argparse
from Users import MongoConnector


def argument():
    """
    à supprimer
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('arguments', nargs='+', help='entrer la methode à appeler et ses arguments ensuite')
    args = parser.parse_args()
    return args.arguments


class Permissions(MongoConnector):
    def __init__(self, id_p, name="", description=""):
        """
        prend en argument un id(int), un nom(str), une description(str)
        POST: instancie les variables passées en argument
              SI la BDD répond
        RAISE: lance une exception "error" si la BDD ne répond pas
        """
        if id_p is None:
            raise IdpIsNone("id_p obligatoire")
        super().__init__()

        self.__id_p = id_p
        self.__name = name
        self.__description = description

        try:
            with MongoConnector() as connector:
                self.__collection = connector.db["Permissions"]

        except Exception as error:
            print(error)

    @property
    def id_permission(self):
        return self.__id_p

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    # @name.setter
    def changer_nom(self, new_name):
        """
        appelle une requète qui change le nom d'une permission dans la BDD à partir de son nom actuel
        PRE : un string avec le nouveau nom
        POST : appelle une requète qui change le nom d'une permission par un nouveau nom dans la BDD
               à partir de son nom actuel
        """
        query = {"name": self.__name}

        new_values = {"$set": {
            "name": new_name
        }}

        self.db["Permissions"].update_one(query, new_values)

    # @description.setter
    def changer_desc(self, new_desc):
        """
        appelle une requète qui change la description d'une permission dans la BDD à partir de sa description actuelle
        PRE : un string avec la nouvelle description
        POST : appelle une requète qui change la description d'une permission par une nouvelle dans la BDD
               à partir de sa description actuelle
        """
        query = {"description": self.__description}
        new_values = {"$set": {"description": new_desc}}

        self.db["Permissions"].update_one(query, new_values)

    def add_db_perm(self):
        """
        appelle une requète qui ajoute une permission avec un id, un nom, une description dans la BDD
        PRE :
        POST : appelle une requète qui ajoute une permission avec un id, un nom, une description dans la BDD

        """
        query = {{"id_p": self.__id_p, "name": self.__name, "description": self.__description}}
        self.db["Permissions"].insert_one(query)

    def remove_perm(self):
        """
        appelle une requète qui supprime une permission dans la BDD à partir de son id
        PRE :
        POST : appelle une requète qui supprime une permission dans la BDD à partir de son id
        """
        query = {"id_p": self.__id_p}
        self.db["Permissions"].delete_one(query)


class IdpIsNone(Exception):
    pass


if __name__ == '__main__':
    """
    à supprimer
    """
    perm_test = Permissions(1080, "abdl", "perm de test")

    if argument()[0] == 'changer_nom':
        perm_test.changer_nom(argument())
    elif argument()[0] == 'changer_desc':
        perm_test.changer_desc(argument())
    elif argument()[0] == 'add_db_perm':
        perm_test.add_db_perm()
    elif argument()[0] == 'remove_perm':
        perm_test.remove_perm()



