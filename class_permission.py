import argparse
from connexion_bdd import MongoConnector


def argument():
    """
    à supprimer
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('arguments', nargs='+', help='entrer la methode à appeler et ses arguments ensuite')
    args = parser.parse_args()
    return args.arguments


class Permissions:
    def __init__(self, name="", description=""):
        """
        prend en argument un id(int), un nom(str), une description(str)
        POST: instancie les variables passées en argument
              SI la BDD répond
        RAISE: lance une exception "error" si la BDD ne répond pas
        """
        self.__name = name
        self.__description = description

        try:
            with MongoConnector() as connector:
                self.__collection = connector.db["Permissions"]

        except Exception as error:
            print(error)

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

        self.__collection.update_one(query, new_values)

    # @description.setter
    def changer_desc(self, new_desc):
        """
        PRE :
        POST :
        """
        query = {"description": self.__description}
        new_values = {"$set": {"description": new_desc}}

        self.__collection.update_one(query, new_values)

    def add_db_perm(self):
        """
        appelle la fctn qui va pull param: class en question avec son propre self, envoie les 3 args et ajoute la perm
        PRE :
        POST :
        """
        query = {{"name": self.__name, "description": self.__description}}
        self.__collection.insert_one(query)

    def remove_perm(self):
        """
        appelle la fctn qui envoye un delete request avec l id de ma perm a retirer dans mongodb
        PRE :
        POST :
        """
        query = {"name": self.__name}
        self.__collection.delete_one(query)

        # rajouter une check permissions (id p)


if __name__ == '__main__':
    """
    à supprimer
    """
    perm_test = Permissions("abdl", "perm de test")

    if argument()[0] == 'changer_nom':
        perm_test.changer_nom(argument())
    elif argument()[0] == 'changer_desc':
        perm_test.changer_desc(argument())
    elif argument()[0] == 'add_db_perm':
        perm_test.add_db_perm()
    elif argument()[0] == 'remove_perm':
        perm_test.remove_perm()



