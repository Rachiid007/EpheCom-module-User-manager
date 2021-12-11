from Users import Users
from connexion_bdd import MongoConnector
import re


def is_valid_pseudo(pseudo):
    """ Check if a a pseudo is valid
    :pre: pseudo str
    :post: return bool: True if the pseudo contains a character, a digit or _ - + @ and
        its size is between 4 and 25 otherwise False
    """
    if not re.match(r'\b[A-Za-z0-9._+-@]{4,25}\b', pseudo):
        return False, "Le Pseudo ne respect pas la norme !"
    else:
        return True


def is_valid_password(password):
    """ Check if a password is valid
    :pre: password str
    :post: return bool: True if the pseudo contains a character, a digit or _ - + @ and
        its size is between 7 and 25 otherwise False
    """
    if not re.match(r'\b[A-Za-z0-9._+-@]{7,25}\b', password):
        return False, "Le MDP ne respect pas la norme !"
    else:
        return True


def is_same_password(password, confimation_password):
    """ Check if a password is equal to the confirmation password
    :pre: password str, confimation_password str
    :post: return bool: True if the password is equal to the confirmation password otherwise False
    """

    if password != confimation_password:
        return False, "Les 2 MDP ne correspondent pas !"
    else:
        return True


def is_age_min_13_yeas(age):
    """ Check if the age os greater is greater than 13
    :pre: age str
    :post: return bool: True if the age is greater than 13 otherwise False
    """

    if int(age) < 13:
        return False, "Vous devez avoir minimum 13 ans !"
    else:
        return True


def is_valide_email(email):
    """ Check if the email address is valid
    :pre: email str
    :post: return bool: True if the email is valid otherwise False
    """

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if not re.fullmatch(regex, email):
        return False, "L'email n'est pas valide !"
    else:
        return True


def register_verify(user_name, email, age, password, confimation_password):
    """ Check if the register fields are valid
    :pre: user_name str, email str, age str, password str, confimation_password str
    :post: return bool: True if the fields are valid otherwise False
    """

    if is_valid_pseudo(user_name) and is_valid_password(password) and is_same_password(password,
                                                                confimation_password) and is_age_min_13_yeas(age):

        user_test = Users(user_name, email, password, age)

        if user_test.is_exist_user_name():
            return False, "Le nom d'utilisateur existe déjà !"

        if user_test.is_exist_email():
            return False, "L'adresse email existe déjà !"

        user_test.create()
        return True, "L'utilisateur a été créée"


def login_verify(user_name, password):
    """ Check if the user name and password exist in the DB
    :pre: user_name str, password str
    :post: return bool: True if the user name and password exist in the DB otherwise False
    """

    user_test = Users(user_name=user_name, email="", password=password, age="")
    return user_test.is_user_in_bdd()


"""
pas fini la modiff !
"""


def update_verify(current_user, new_email, new_first_name, new_last_name, new_password, new_password_confim,
                  new_security_question, new_security_answer):
    if is_valid_pseudo(n_user_name) and is_valide_email(new_email) and is_same_password(new_password,
                                                                                        new_password_confim):
        user_test = Users(current_user)
        user_test.update(new_user_name, new_email, new_first_name, new_last_name, new_password, new_security_question,
                         new_security_answer)


def get_all_users():
    try:
        with MongoConnector() as connector:
            collection = connector.db["users"]
            resultat = collection.find({})
            list_of_users = [x for x in resultat]
            return list_of_users

    except Exception as error:
        print(error)


if __name__ == '__main__':
    user1 = Users(user_name="Rachiid007", password="rachid1234", email="rachid@gmail.com", age="")
    # user1.create()
    print(user1.is_user_in_bdd())

    # print(user1.is_user_in_bdd())
    # il_est_dans_la_db = user1.is_user_in_bdd()[0]
    # print(il_est_dans_la_db)

    # list_users()
    # print(user1.is_exist_user_name())
