import argparse
from Users import MongoConnector


def argument():
    """test Functions that manage all the arguments' script"""
    parser = argparse.ArgumentParser()
    parser.add_argument('arguments', nargs='+', help='entrer la methode à appeler et ses arguments ensuite')
    args = parser.parse_args()
    return args.arguments


class Permissions(MongoConnector):
    def __init__(self, id_p, name, description):
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
        recup chaine de carac (pseudo) et chaine (new name) remplace
        PRE :
        POST : self.__newnme --> name
        """
        query = {"name": self.__name}

        new_values = {"$set": {
            "name": new_name
        }}

        self.db["permissions"].update_one(query, new_values)

    # @description.setter
    def changer_desc(self, new_desc):
        """
        PRE :
        POST :
        """
        query = {"description": self.__description}
        new_values = {"$set": {"description": new_desc}}

        self.db["permissions"].update_one(query, new_values)

    def add_db_perm(self):
        """
        appelle la fctn qui va pull param: class en question avec son propre self, envoie les 3 args et ajoute la perm
        PRE :
        POST :
        """
        query = {{"id_p": self.__id_p, "name": self.__name, "description": self.__description}}
        self.db["permissions"].insert_one(query)

    def remove_perm(self):
        """
        appelle la fctn qui envoye un delete request avec l id de ma perm a retirer dans mongodb
        PRE :
        POST :
        """
        query = {"id_p": self.__id_p}
        self.db["permissions"].delete_one(query)


if __name__ == '__main__':
    perm_test = Permissions(1080, "abdl", "perm de test")

    if argument()[0] == 'changer_nom':
        perm_test.changer_nom(argument())
    elif argument()[0] == 'changer_desc':
        perm_test.changer_desc(argument())
    elif argument()[0] == 'add_db_perm':
        perm_test.add_db_perm()
    elif argument()[0] == 'remove_perm':
        perm_test.remove_perm()



