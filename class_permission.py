# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
import pymongo

def argument():
    """Functions that manage all the arguments' script"""
    parser = argparse.ArgumentParser()
    parser.add_argument('arguments', nargs='+', help='entrer la methode à appeler et ses arguments ensuite')
    args = parser.parse_args()
    return args.arguments

class permission:

    def __init__(self, id_p, name, description):

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

    #@name.setter
    def name(self, new_name):
        """
        recup chaine de carac (pseudo) et chaine (new name) remplace
        PRE :
        POST : self.__newnme --> name
        """
        query = {"name": self.__name}

        new_values = {"$set": {
            "name": new_name
        }}

        self.db["users"].update_one(query, new_values)

    #@description.setter
    def description(self, new_desc):
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
        query = {"id_p": self.__id_p}

        values = {"$set": {"id_p": self.__id_p, "name": self.__name, "description": self.__description}}
        self.db["permissions"].insert_one(query, values)

    def remove_perm(self):
        """
        appelle la fctn qui envoye un delete request avec l id de ma perm a retirer dans mongodb
        PRE :
        POST :
        """
        query = {"id_p": self.__id_p}

        values = {"$set": {"id_p": self.__id_p, "name": self.__name, "description": self.__description}}
        self.db["permissions"].delete_one(query, values)
        pass


    
if __name__ == '__main__':
    if argument()[0] == 'changer_nom':
        permission.changer_nom(argument())
    elif argument()[0] == 'changer_desc':
        permission.changer_desc(argument())
    elif argument()[0] == 'add_db_perm':
        permission.add_db_perm()
    elif argument()[0] == 'remove_perm':
        permission.remove_perm()



