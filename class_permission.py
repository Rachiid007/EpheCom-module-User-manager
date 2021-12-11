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
    def __init__(self, id_p, name, description):
        """
        instancie l'objet permission avec un id, un nom, une description
        """
        super().__init__()

        self.__id_p = id_p
        self.__name = name
        self.__description = description

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
        appelle une requète qui change le nom d'une permission dans la database
        PRE : un string avec le nouveau nom
        POST :
        """
        query = {"name": self.__name}

        new_values = {"$set": {
            "name": new_name
        }}

        self.db["permissions"].update_one(query, new_values)

    # @description.setter
    def changer_desc(self, new_desc):
        """
        appelle une requète qui change la description d'une permission dans la database
        PRE : un string avec la nouvelle description
        POST :
        """
        query = {"description": self.__description}
        new_values = {"$set": {"description": new_desc}}

        self.db["permissions"].update_one(query, new_values)

    def add_db_perm(self):
        """
        appelle une requète qui ajoute une permission avec un id, un nom, une description dans la database
        PRE :
        POST :
        """
        query = {{"id_p": self.__id_p, "name": self.__name, "description": self.__description}}
        self.db["permissions"].insert_one(query)

    def remove_perm(self):
        """
        appelle une requète qui supprime une permission dans la database à partir de son id
        PRE :
        POST :
        """
        query = {"id_p": self.__id_p}
        self.db["permissions"].delete_one(query)


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



