import sys
# adding Classes to the system path
sys.path.insert(0, '..\Classes')

from Connection_to_DB import MongoConnector
from datetime import date
import re
import hashlib


class Users:
    """this Classes collects all information about a user"""

    def __init__(self, pseudo: str, email: str, password: str, age: int = "", first_name: str = "", last_name: str = "",
                 security_question: str = "", security_answer: str = ""):
        """ This builds a User based on user name, email, password, age, first name, last name, security question,
                 security answer
        :pre: pseudo str, email str, password str, age int, first_name str, last_name str, security_question str,
                 security_answer str
        :post: object user created
        """

        self.pseudo = pseudo
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.security_question = security_question
        self.security_answer = security_answer

        try:
            with MongoConnector() as connector:
                self.__collection = connector.db["users"]

        except Exception as error:
            print(error)

    def create(self):
        """ Insert a user in the DB
        :pre
        :post: user inserted in the DB
        """
        query = {
            "pseudo": self.pseudo,
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "security_question": self.security_question,
            "security_answer": self.security_answer,
            "list_role": [22, 25, 50]
        }
        self.__collection.insert_one(query)

    def has_role(self, id_role):
        """ Vérifie si l'Utilisateur dispose d'un rôle.
        parcourt la list "list_role" -> True si il a le role
        :param id_role: l'ID du role qu'on souhaite
        :return: True si le rôle est dans la list et sinon False
        """
        res = self.__collection.find_one({"pseudo": self.pseudo, "list_role": id_role})
        if res is None:
            return False
        else:
            return res


class PasswordOrUsernameNotCorrect(Exception):
    pass


class PseudoNotValid(Exception):
    pass


class PasswordNotValid(Exception):
    pass


class PasswordsNotSame(Exception):
    pass


class AgeNotValid(Exception):
    pass


class EmailNotValid(Exception):
    pass


class SecurityQuestionNotCorrect(Exception):
    pass


class SecurityAnswerNotCorrect(Exception):
    pass


class NameNotValid(Exception):
    pass


class ValidationsInfosUsers:

    @staticmethod
    def is_valid_pseudo(pseudo: str):
        """ Check if a a pseudo is valid
        :pre: pseudo str
        :post: return bool: True if the pseudo contains a character, a digit or _ - + @ and
            its size is between 4 and 25 otherwise False
        """
        try:
            pseudo_ok = str(pseudo)
        except ValueError:
            raise PseudoNotValid("Le Pseudo doit etre un String")

        if not re.match("([A-z]{4,})([0-9_@]*)", pseudo_ok):
            raise PseudoNotValid("Le Pseudo ne respect pas la norme !")

        return True

    @staticmethod
    def is_valid_password(password: str):
        """ Check if a password is valid
        :pre: password str
        :post: return bool: True if the pseudo contains a character, a digit or _ - + @ and
            its size is between 7 and 25 otherwise False
        """
        if not re.match(r'\b[A-z0-9._+-@]{7,25}\b', password):
            raise PasswordNotValid("Le MDP ne respect pas la norme !")

        return True

    @staticmethod
    def is_same_password(password: str, confimation_password: str):
        """ Check if a password is equal to the confirmation password
        :pre: password str, confimation_password str
        :post: return bool: True if the password is equal to the confirmation password otherwise False
        """

        if password != confimation_password:
            raise PasswordsNotSame("Les 2 MDP ne correspondent pas !")

        return True

    @staticmethod
    def is_age_min_13_yeas(self, birthdate: str):
        """ Check if the age os greater is greater than 13
        :pre: age int
        :post: return bool: True if the age is greater than 13 otherwise False
        """
        try:
            age = self.claculate_age(birthdate)

        except ValueError:
            raise AgeNotValid("chaine de l'age pas bon !!")

        if age < 13:
            raise AgeNotValid("Vous devez avoir minimum 13 ans !")

        return True

    @staticmethod
    def is_valide_email(email: str):
        """ Check if the email address is valid
        :pre: email str
        :post: return bool: True if the email is valid otherwise False
        """
        try:
            email_ok = str(email)
        except ValueError:
            return EmailNotValid("L'email doit être un String !")

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not re.fullmatch(regex, email_ok):
            raise EmailNotValid("L'email n'est pas valide !")

        return True

    @staticmethod
    def is_valid_name(name: str):
        """ Check if a a pseudo is valid
        :pre: pseudo str
        :post: return bool: True if the pseudo contains a character, a digit or _ - + @ and
            its size is between 4 and 25 otherwise False
        """
        try:
            name_ok = str(name)
        except ValueError:
            raise NameNotValid("Le Pseudo doit etre un String")

        if not re.match("([A-z]{3,})", name_ok):
            raise NameNotValid("Le nom/prenom ne respect pas la norme !")

        return True

    @staticmethod
    def is_valide_securite_question(security_question: str):
        """ check si la question et la réponse de sécurité sont correct
        :pre: password must be string
        :post: return str: The encrypted password
        """
        try:
            security_question_ok = str(security_question)

        except ValueError:
            raise SecurityQuestionNotCorrect("La question de sécurité doit être un String")

        if 5 <= len(security_question_ok) <= 50:
            return True

        raise SecurityQuestionNotCorrect("La question de sécurité doit être entre 5 et 50 caractères")

    @staticmethod
    def is_valide_securite_answer(security_answer: str):
        """ check si la question et la réponse de sécurité sont correct
        :pre: password must be string
        :post: return str: The encrypted password
        """
        try:
            security_answer_ok = str(security_answer)

        except ValueError:
            raise SecurityQuestionNotCorrect("La réponse de sécurité doit être un String")

        if 5 <= len(security_answer_ok) <= 50:
            return True

        raise SecurityQuestionNotCorrect("La réponse de sécurité doit être entre 5 et 50 caractères")

    @staticmethod
    def password_encryption(password: str):
        """ password encryption
        :pre: password must be string
        :post: return str: The encrypted password
        """
        password = password.encode("utf-8")
        hash_object = hashlib.sha512(password)
        hex_dig = hash_object.hexdigest()
        return hex_dig

    @staticmethod
    def claculate_age(birthdate):
        today = date.today()

        # A bool that represents if today's day/month precedes the birth day/month
        one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))

        # Calculate the difference in years from the date object's components
        year_difference = today.year - birthdate.year

        age = year_difference - one_or_zero

        return age


class UsersOperations:

    def __init__(self):
        try:
            with MongoConnector() as connector:
                self.__collection = connector.db["users"]

        except Exception as error:
            print(error)

    def get_all_users(self):
        """ get all users in DB
        :pre:
        :post: return bool: dictionaire with all Users
        """
        resultat = self.__collection.find({})
        return [x for x in resultat]

    def get_infos_user(self, pseudo):
        """ get infos from this user
        :pre: pseudo str
        :post: return bool: dictionaire with data of this user
        """
        query = {"pseudo": pseudo}
        res = self.__collection.find_one(query)
        if res is None:
            raise PseudoNotValid("Le Pseudo n'est pas correct !")

        return res

    def get_id_user(self, pseudo: str):
        myquery = {"pseudo": pseudo}
        resultat = self.__collection.find_one(myquery)
        return resultat["_id"]

    def is_not_exist_pseudo(self, pseudo: str):
        """ Vérifiez si le nom d'utilisateur existe déjà dans la base de données.
        :return: True si le pseudo courant existe dans la BDD et sinon False.
        """
        query = {"pseudo": pseudo}
        if self.__collection.count_documents(query):
            raise PseudoNotValid("Le nom d'utilisateur existe déjà !")

        return True

    def is_not_exist_email(self, email: str):
        """ Vérifiez si le nom d'utilisateur existe déjà dans la base de données.
        :return: True si le pseudo courant existe dans la BDD et sinon False.
        """
        query = {"email": email}
        if self.__collection.count_documents(query):
            raise EmailNotValid("L'email existe déjà !")

        return True

    def is_user_in_db(self, pseudo: str, password: str):
        """ Vérifiez si l'utilisateur existe dans la base de données.
        :return: True si le user courant existe dans la BDD avec un Dictionnaire des données de l'User et sinon False.
        """
        query = {"pseudo": pseudo, "password": password}
        res = self.__collection.find_one(query)
        if res is None:
            raise PasswordOrUsernameNotCorrect("Le Pseudo ou le Mdp est incorrecte !")

        return res

    def update(self, current_pseudo, new_pseudo, new_email, new_first_name, new_last_name, new_password,
               new_security_question, new_security_answer):
        """ Update a user in the DB
        :pre new_pseudo str: a new user name , new_email str : a new email, new_first_name str: a new first name,
            new_last_name str: a new last name, new_security_question str: a new security question,
                 new_security_answer str: a new security answer
        :post: user updated in the DB
        """

        query = {"pseudo": current_pseudo}

        new_values = {"$set": {
            "pseudo": new_pseudo,
            "email": new_email,
            "first_name": new_first_name,
            "last_name": new_last_name,
            "password": new_password,
            "security_question": new_security_question,
            "security_answer": new_security_answer
        }}
        self.__collection.update_one(query, new_values)

    def delete_specific_user(self, pseudo):
        query = {"pseudo": pseudo}
        self.__collection.delete_one(query)

    def delete_all_users(self):
        self.__collection.delete_many({})


def register_verify(pseudo: str, email: str, age: int, password: str, confimation_password: str,
                    security_question: str, security_answer: str):
    """ Check if the register fields are valid
    :pre: pseudo str, email str, age int, password str, confimation_password str
    :post: return bool: True if the fields are valid otherwise False
    """

    try:
        ValidationsInfosUsers().is_valid_pseudo(pseudo)
        ValidationsInfosUsers().is_valid_password(password)
        ValidationsInfosUsers().is_valide_email(email)
        ValidationsInfosUsers().is_same_password(password, confimation_password)
        ValidationsInfosUsers().is_age_min_13_yeas(age)
        ValidationsInfosUsers().is_valide_securite_question(security_question)
        ValidationsInfosUsers().is_valide_securite_answer(security_answer)
        security_answer.lower()

        UsersOperations().is_not_exist_pseudo(pseudo)
        UsersOperations().is_not_exist_email(email)

        password_encrypt = ValidationsInfosUsers().password_encryption(password)

        user = Users(pseudo=pseudo, email=email, password=password_encrypt, age=age,
                     security_question=security_question, security_answer=security_answer)
        user.create()
        return True

    except Exception as e:
        print(e)


def login_verify(pseudo, password):
    """ Check if the user name and password exist in the DB
    :pre: pseudo str, password str
    :post: return bool: True if the user name and password exist in the DB otherwise False
    """

    try:
        password_encrypt = ValidationsInfosUsers().password_encryption(password)

        user_info = UsersOperations().is_user_in_db(pseudo, password_encrypt)
        return user_info

    except Exception as e:
        print(e)


def update_verify(current_pseudo, current_password, new_pseudo, new_email, new_first_name, new_last_name, new_password,
                  new_password_confim, new_security_question, new_security_answer):
    try:
        user_infos = UsersOperations().get_infos_user(current_pseudo)

        if new_pseudo != current_pseudo or new_pseudo != "":
            """
            si c un nvx check si il est dispo et correspond à la norme
            """
            ValidationsInfosUsers().is_valid_pseudo(new_pseudo)
            UsersOperations().is_not_exist_pseudo(new_pseudo)
        else:
            new_pseudo = current_pseudo

        if new_email != user_infos["email"] or new_email != "":
            """
            si c un nvx check si il est dispo et correspond à la norme
            """
            ValidationsInfosUsers().is_valide_email(new_email)
            UsersOperations().is_not_exist_email(new_email)
        else:
            new_email = user_infos["email"]

        if new_first_name != "":
            ValidationsInfosUsers().is_valid_name(new_first_name)

        if new_last_name != "":
            ValidationsInfosUsers().is_valid_name(new_last_name)

        current_password_encrypt = ValidationsInfosUsers().password_encryption(current_password)
        if not current_password_encrypt == user_infos["password"]:
            return "current Password not correct !"

        if new_password != "" or new_password_confim != "":
            ValidationsInfosUsers().is_valid_password(new_password)
            ValidationsInfosUsers().is_same_password(new_password, new_password_confim)
        else:
            new_password = user_infos["password"]

        ValidationsInfosUsers().is_valide_securite_question(new_security_question)
        ValidationsInfosUsers().is_valide_securite_answer(new_security_answer)
        new_security_answer.lower()

        UsersOperations().update(current_pseudo, new_pseudo, new_email, new_first_name, new_last_name, new_password,
                                 new_security_question, new_security_answer)
        return True

    except Exception as e:
        print(e)


def delete_user(pseudo: str):
    UsersOperations().delete_specific_user(pseudo)


def recup_password(pseudo: str):
    try:
        user_infos = UsersOperations().get_infos_user(pseudo)

        return user_infos["security_question"]

    except Exception as e:
        print(e)


def check_if_correct_answers(pseudo: str, security_answer):
    try:
        user_infos = UsersOperations().get_infos_user(pseudo)

        if user_infos["security_answer"] == security_answer.lower():
            return True

        return False

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # UsersOperations().delete_all_users()
    print(register_verify("totototo", "toto@gmail.com", 36, "totototo", "totototo", "C qui ToTo ?",
                          "c'est toto"))

    print(register_verify("rachid007", "bellaalirachid@gmail.com", 48, "abdel1234", "abdel1234", "C quoi Django ?",
                          "Framework"))

    print(update_verify(current_pseudo="Abdel1080", current_password="abdel1234", new_pseudo="rachid007",
                        new_email="bellaalirachid@gmail.com", new_first_name="Rachid", new_last_name="BELLAALI",
                        new_password="", new_password_confim="",
                        new_security_question="C'est quoi mon meilleur langage de progra ?",
                        new_security_answer="Python"))

    user_test = UsersOperations()
    print(user_test.get_all_users())
