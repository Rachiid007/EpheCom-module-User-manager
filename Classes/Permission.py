import sys

# adding Classes to the system path
# sys.path.insert(0, '../Classes')

from Classes.Connection_to_DB import MongoConnector


class Permissions:
    def __init__(self, name: str = "", description: str = ""):
        """
        Initialization of the class Permissions
        PRE: name and description are string
        POST: Create a object Permissions with a name name and a description description
        """
        self.__name = name
        self.__description = description

        # To Update as said in the review
        try:
            with MongoConnector() as connector:
                self.__collection = connector.db["permissions"]

        except Exception as error:
            print(error)

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @name.setter
    def name(self, new_name: str):
        query = {"name": self.__name}
        new_values = {"$set": {"name": new_name}}

        self.__collection.update_one(query, new_values)

    @description.setter
    def description(self, new_desc: str):
        query = {"description": self.__description}
        new_values = {"$set": {"description": new_desc}}

        self.__collection.update_one(query, new_values)

    def add_db_perm(self) -> None:
        """
        Send the data of the Permissions into the database
        PRE:
        POST: The Permissions is now in the database
        """
        query = {"name": self.__name, "description": self.__description}
        self.__collection.insert_one(query)

    def remove_perm(self) -> None:
        """
        Send a delete request to database
        PRE:
        POST: The Permissions is deleted from the database
        """
        query = {"name": self.__name}
        self.__collection.delete_one(query)

    def list_perm(self) -> list:
        """
        Find and return a list with all permissions
        PRE:
        POST: return a list with all permission's names
        """
        list_perm = []
        tab = self.__collection.find()
        for line in tab:
            list_perm.append(line["name"])
        return list_perm
