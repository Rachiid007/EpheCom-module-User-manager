from Users import Users
from connexion_bdd import MongoConnector
import re
import hashlib


class UsersOperations(object):

    def __init__(self):
        try:
            with MongoConnector() as connector:
                self.__collection = connector.db["users"]

        except Exception as error:
            print(error)

    def get_all_users(self):
        resultat = self.__collection.find({})
        return [x for x in resultat]

    def get_id_user(self, pseudo):
        myquery = {"user_name": pseudo}
        resultat = self.__collection.find_one(myquery)
        return resultat["_id"]

    def delete_specific_user(self, user_name):
        query = {"user_name": user_name}
        self.__collection.delete_one(query)

    def delete_all_users(self):
        self.__collection.delete_many({})

    def is_exist_user_name(self, user_name):
        """ Vérifiez si le nom d'utilisateur existe déjà dans la base de données.
        :return: True si le user_name courant existe dans la BDD et sinon False.
        """
        query = {"user_name": user_name}
        if self.__collection.count_documents(query):
            return True
        else:
            return False

    def is_exist_email(self, email):
        """ Vérifiez si le nom d'utilisateur existe déjà dans la base de données.
        :return: True si le user_name courant existe dans la BDD et sinon False.
        """
        query = {"email": email}
        if self.__collection.count_documents(query):
            return True
        else:
            return False

    def is_user_in_bdd(self, user_name, password):
        """ Vérifiez si l'utilisateur existe dans la base de données.
        :return: True si le user courant existe dans la BDD avec un Dictionnaire des données de l'User et sinon False.
        """
        query = {"user_name": user_name, "password": password}
        res = self.__collection.find_one(query)
        if res is None:
            return False, "L'utilisateur n'existe pas ou MDP erroné !"
        else:
            return True, res


def is_valid_pseudo(pseudo):
    """ Check if a a pseudo is valid
    :pre: pseudo str
    :post: return bool: True if the pseudo contains a character, a digit or _ - + @ and
        its size is between 4 and 25 otherwise False
    """
    if not re.match(r'\b[A-Za-z0-9._+-@]{5,25}\b', pseudo):
        return False, "Le Pseudo ne respect pas la norme !"
    else:
        return True, "pseudo ok"


def is_valid_password(password):
    """ Check if a password is valid
    :pre: password str
    :post: return bool: True if the pseudo contains a character, a digit or _ - + @ and
        its size is between 7 and 25 otherwise False
    """
    if not re.match(r'\b[A-Za-z0-9._+-@]{7,25}\b', password):
        return False, "Le MDP ne respect pas la norme !"
    else:
        return True, "MDP ok"


def is_same_password(password, confimation_password):
    """ Check if a password is equal to the confirmation password
    :pre: password str, confimation_password str
    :post: return bool: True if the password is equal to the confirmation password otherwise False
    """

    if password != confimation_password:
        return False, "Les 2 MDP ne correspondent pas !"
    else:
        return True, "Les 2 MDP ok !"


def is_age_min_13_yeas(age):
    """ Check if the age os greater is greater than 13
    :pre: age str
    :post: return bool: True if the age is greater than 13 otherwise False
    """

    if isinstance(age, int):
        if age < 13:
            return False, "Vous devez avoir minimum 13 ans !"
        else:
            return True, "age ok"
    else:
        return False, "L'age doit etre un entier"


def is_valide_email(email):
    """ Check if the email address is valid
    :pre: email str
    :post: return bool: True if the email is valid otherwise False
    """

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if not re.fullmatch(regex, email):
        return False, "L'email n'est pas valide !"
    else:
        return True, "email ok"


def password_encryption(password: str):
    """ password encryption
    :pre: password must be string
    :post: return str: The encrypted password
    """
    password = password.encode("utf-8")
    hash_object = hashlib.sha512(password)
    hex_dig = hash_object.hexdigest()
    return hex_dig


def register_verify(user_name, email, age, password, confimation_password):
    """ Check if the register fields are valid
    :pre: user_name str, email str, age str, password str, confimation_password str
    :post: return bool: True if the fields are valid otherwise False
    """

    if user_name == "" or email == "" or age == "" or password == "" or confimation_password == "":
        return False, "Un ou plusieurs champs ne sont pas complétés !"

    user_name_ok = is_valid_pseudo(user_name)
    email_ok = is_valide_email(email)
    password_ok = is_valid_password(password)
    two_passwd_ok = is_same_password(password, confimation_password)
    age_ok = is_age_min_13_yeas(age)

    if user_name_ok[0]:
        if email_ok[0]:
            if password_ok[0]:
                if two_passwd_ok[0]:
                    if age_ok[0]:

                        password_encrypt = password_encryption(password)

                        user_exist = UsersOperations().is_exist_user_name(user_name)
                        if user_exist:
                            return False, "Le nom d'utilisateur existe déjà !"

                        email_exist = UsersOperations().is_exist_email(email)
                        if email_exist:
                            return False, "L'adresse email existe déjà !"

                        user = Users(user_name, email, password_encrypt, age)
                        user.create()
                        return True, "L'utilisateur a été créé"

                    else:
                        return age_ok
                else:
                    return two_passwd_ok
            else:
                return password_ok
        else:
            return email_ok
    else:
        return user_name_ok


def login_verify(user_name, password):
    """ Check if the user name and password exist in the DB
    :pre: user_name str, password str
    :post: return bool: True if the user name and password exist in the DB otherwise False
    """

    password_encrypt = password_encryption(password)

    user_info = UsersOperations().is_user_in_bdd(user_name, password_encrypt)
    return user_info


def update_verify(current_user, new_user_name, new_email, new_first_name, new_last_name, new_password,
                  new_password_confim, new_security_question, new_security_answer):
    if is_valid_pseudo(new_user_name)[0] and is_valide_email(new_email)[0] and \
            is_same_password(new_password, new_password_confim)[0]:

        user_test = Users(user_name=current_user, email="", password="")
        user_test.update(new_user_name, new_email, new_first_name, new_last_name, new_password, new_security_question,
                         new_security_answer)
        return True, "Vos informations ont bien été modifiées !"
    else:
        return False, "Un ou plusieurs champs ne respecte pas la norme !!"


def delete_user(user_name):
    UsersOperations().delete_specific_user(user_name)


if __name__ == '__main__':

    user_opera1 = UsersOperations()

    # print(login_verify("rachid1080", "abdel1234"))

    # register_verify("rachid007", "bellaalirachid@gmail.com", 36, "abdel1234", "abdel1234")

    # delete_user("ChaosArnhug")

    # print(update_verify("rachid1080", "", "tarek@oliphant.com", "Tarek", "Chaabi", "tarek123", "tarek123", "date de naissance ?", "21-04-1998"))

    # user_opera1.delete_all_users()

    print(user_opera1.get_all_users())
