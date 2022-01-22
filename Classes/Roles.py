import sys

# adding Classes to the system path
sys.path.insert(0, '../Classes')

from Users import *


class AlreadyExistException(Exception):
    pass


class DoesNotExistException(Exception):
    pass


class Role:
    """this class collects all information about a role"""

    def __init__(self, id_role: int, name: str, description: str, id_user: int, perm_list: list):
        """ This builds a Role based on id role, role name , description , id user and permission list
        :pre:
        :post: object role created
        """
        self.__id_role = id_role
        self.__name = name
        self.__description = description
        self.__id_user = id_user
        self.__perm_list = perm_list

    def __str__(self) -> str:

        """string representation of a role.
        : pre:
        : post: return str : textual representation of a role
        """
        return f"id Role : {self.__id_role} | Name : {self.__name} | Description : {self.__description} " \
               f"| id_user : {self.__id_user} | Permission list : {self.__perm_list}"

    @property
    def id_role(self):
        return self.__id_role

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def id_user(self):
        return self.__id_user

    @property
    def perm_list(self):
        return self.__perm_list

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @id_user.setter
    def id_user(self, new_id_user):
        self.__id_user = new_id_user

    def add_perm(self, permission_id):
        """add a permission_id to the role
        pre: permission_id: int permission_id
        post: a permission_id is added to the list of permissions
        raises: AlreadyExistException if the permission already exist
        """
        if self.__perm_list.count(permission_id) > 0:
            raise AlreadyExistException("Permission already exist in this Role")

        self.__perm_list.append(permission_id)

    def remove_perm(self, permission_id):
        """remove a permission_id from the role
        pre: permission: int permission_id
        post: a permission_id is removed from the list of permissions
        raises: DoesNotExistException if the permission_id doesn't exist
        """

        if self.__perm_list.count(permission_id) == 0:
            raise DoesNotExistException("Permission_id doesn't exist in this Role")

        self.__perm_list.remove(permission_id)


class RolesDBManagement:

    def __init__(self):
        """  Builds roles DB Management object
        :pre:
        :post: DB connection established, roles loaded
        :raises: Exception if DB connection fails
        """
        try:
            with MongoConnector() as connector:
                self.__collection = connector.db["roles"]

        except Exception as error:
            print(error)

    def is_role_existing_in_db(self, role):
        """ Check if a role exist in the DB
        :pre: role Role: a role object
        :post: return bool: True if the role exist, otherwise False
        """

        my_query = {"name": role.name, "id_user": role.id_user}
        my_doc = self.__collection.find(my_query)

        return len(list(my_doc.clone())) > 0

    def is_role_name_id_user_existing_in_db(self, name, id_user):
        """ Check if a role exist in the DB
        :pre: name str, id_user str
        :post: return bool: True if the role exist, otherwise False
        """

        my_query = {"name": name, "id_user": id_user}
        my_doc = self.__collection.find(my_query)

        return len(list(my_doc.clone())) > 0

    def get_all_roles_from_db(self):
        """ Get the list of roles from the DB
        :pre:
        :post: roles_List list of Role: the list of roles collected from the DB
        :raises:DoesNotExistException if no role found in the DB
        """
        """
        roles_list = []
        for x in self.__collection.find():
            roles_list.append(Role(x["_id"], x["name"], x["description"],
                                   x["id_user"], x["perm_list"]))"""

        roles_list = [Role(x["_id"], x["name"], x["description"], x["id_user"], x["perm_list"])
                      for x in self.__collection.find()]

        if len(roles_list) == 0:
            raise DoesNotExistException("There are no Roles in the DB")

        return roles_list

    def generate_list_role(self, query):
        roles_list = []

        for x in self.__collection.find(query):
            roles_list.append(Role(x["_id"], x["name"], x["description"], x["id_user"],
                                   x["perm_list"]))

        if len(roles_list) == 0:
            raise DoesNotExistException("Role doesn't exist in the DB")

        return roles_list

    def get_roles_by_name(self, name):

        """ Get the list of roles that have the name given in the param
        :pre: name str: the name of the role
        :post: list_roles list: the list of roles that have the name given in the param
        :raises:DoesNotExistException if no role found in the DB
        """
        my_query = {"name": name}
        return self.generate_list_role(my_query)

    def get_roles_by_id_user(self, id_user):

        """ Get the list of roles that have the id_user given in the param
        :pre: id_user int: the id_user of a user
        :post: list_roles list: the list of roles that have the user_id given in the param
        :raises: Does no ExistException if no role found in the DB
        """
        my_query = {"id_user": id_user}
        return self.generate_list_role(my_query)

    def get_roles_by_pseudo(self, pseudo):

        """ Get the list of roles that have the pseudo given in the param
        :pre: pseudo str: the pseudo of a user
        :post: list_roles list: the list of roles that have the pseudo given in the param
        :raises: DoesNotExistException if no role found in the DB
        """
        obj_user_operation = UsersOperations()
        return self.get_roles_by_id_user(obj_user_operation.get_id_user(pseudo))

    def get_role_by_name_user_id(self, name, id_user):
        """ Get the list of roles that have the name and id_user given in the param
        :pre: name str: the name of the role, id_user int : the id of a user
        :post: Role: a role object as per the information collected from the DB
        :raises:DoesNotExistException if no role found in the DB
        """

        my_query = {"name": name, "id_user": id_user}
        my_doc = self.__collection.find(my_query)
        if len(list(my_doc.clone())) == 0:
            raise DoesNotExistException("get_role_by_name_user_id Role-User doesn't exist in the DB")

        return Role(my_doc[0]["_id"], my_doc[0]["name"], my_doc[0]["description"], my_doc[0]["id_user"],
                    my_doc[0]["perm_list"])

    def update_role_in_db(self, role):
        """ Update a role in the DB
        :pre: role Role: a role object
        :post: str : the role updated in the DB
        :raises:Exception in case of failure
        """
        if not self.is_role_existing_in_db(role):
            raise DoesNotExistException("Role doesn't exist in the DB")

        my_query = {"name": role.name, "id_user": role.id_user}
        new_values = {"$set": {"name": role.name, "description": role.description, "id_user": role.id_user,
                               "perm_list": role.perm_list}}
        try:
            self.__collection.update_one(my_query, new_values)
        except Exception as error:
            return error

        return "Role updated in the DB"

    def insert_role_in_db(self, role):
        """ Insert a role in the DB
        :pre: role Role: a Role object
        :post: str: role inserted in the DB
        """
        if self.is_role_existing_in_db(role):
            raise AlreadyExistException("Role already exist in the DB")

        my_dict = {"name": role.name, "description": role.description, "id_user": role.id_user,
                   "perm_list": role.perm_list}
        try:
            self.__collection.insert_one(my_dict)
        except Exception as error:
            return error

        return "Role inserted in the DB"

    def delete_role_from_db(self, name, id_user):
        """ Delete a role from the DB
        :pre: name str , id_user str
        :post: str the role deleted from the DB
        :raises:Exception in case of failure
        """
        if not self.is_role_name_id_user_existing_in_db(name, id_user):
            raise DoesNotExistException("Role doesn't exist in the DB")

        my_query = {"name": name, "id_user": id_user}

        try:
            self.__collection.delete_one(my_query)
        except Exception as error:
            return error

        return "Role deleted from the DB"


if __name__ == '__main__':
    print("Test Class Role and Role DB Management")
    try:
        role_mgt = RolesDBManagement()
        list_role1 = role_mgt.get_roles_by_name("admin")
        print(list_role1)
        role1 = role_mgt.get_role_by_name_user_id("admin", 1080)
        role1.name = "admin3"
        role1.id_user = "100130"
        print(role_mgt.insert_role_in_db(role1))
        # print(role_mgt.get_roles_by_pseudo("arnaud"))
        # print(role1)
        # print(role_mgt.get_all_roles_from_db())

    except Exception as e:
        print(e)
