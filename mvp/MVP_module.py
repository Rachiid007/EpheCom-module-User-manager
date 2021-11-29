import argparse
import json
import re


def argument():
    """cette fonction permet de gérer les arguments

    Return: le dictionnaire des arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("pseudo", help="Pseudo du compte")
    parser.add_argument("password", help="Mot de passe du compte")
    parser.add_argument("path", help="Le chemin d'accès vers le fichier reprennant tout les comptes")
    return parser.parse_args()


class WrongPasswordOrPseudo(Exception):
    pass


def valid_psd(password: str) -> str:
    """fait ça!

    PRE: prend en argument un mot de passe
    POST: Si le mot de passe est conforme, il est renvoyé.
    RAISE: si MPD est faux!exception
    """

    if not re.match(r'\b[A-Za-z0-9._+-@]{7,25}\b', password):
        raise WrongPasswordOrPseudo("Le mot de passe ne respecte pas la norme")
    return password


def print_account(account: dict) -> str:
    """Cette fonction renvoie les propriétés d'un utilisateur

    PRE: prend en argument un dictionnaire d'un compte
    POST: renvoie une string avec toutes les informations du dictionnaire (users)
    """
    return (f"""
    Bonjour {account["pseudo"]}, voici toutes les informations qu'on a à votre sujet :
        ===========================
        Pseudo : {account["pseudo"]} 
        Password : {account["password"]}  
        Name : {account["last_name"]} 
        Surname : {account["first_name"]}  
        Team : {account["team"]} 
        ===========================
        """)


def open_file(path: str):
    """Cette fonction permet d'ouvrir un fichier.

    PRE: path (str): le chemin du fichier
    POST: le dictionnaire du fichier ou un message d'erreur si il n'existe pas
    """
    """PRE: prend en argument une string avec le chemin d'accès vers le fichier des comptes
       POST: renvoie le fichier ouvert
    """
    try:
        return open(path)

    except IOError:
        print("Le fichier n'a pas été trouvé")
        exit(-1)


class Utilisateur:
    """Une classe pour la gestion des utilisateurs.
    La class Profile contient toutes les informations à propos d'un utilisateur.
    Args:
        pseudo (str): Le nom d'utilisateur.
        password (str): Le mot de passe.
        team (str): l'équipe.
    Attributes:
        __pseudo (str): le nom d'utilisateur.
        __password (str): le mot de passe.
        __dict_accounts (dict): liste des utilisateurs.
    """

    def __init__(self, pseudo: str, password: str, path: str):
        self.__pseudo = pseudo
        self.__password = password
        self.__dict_accounts = json.load(open_file(path))

    @property
    def pseudo(self):
        """Cette fonction permet de renvoyer le pseudo d'un utilisateur
        Returns:
            pseudo (str): le pseudo de l'utilisateur
        PRE: un objet défini
       POST: retourne une string de la valeur de l'attribut pseudo"""
        return self.__pseudo

    @property
    def password(self):
        """Cette fonction permet de renvoyer le mot de passe
        Returns:
            password (str): le mot de passe
        PRE: un objet défini
        POST: retourne une string de la valeur de l'attribut password
        """
        return self.__password

    def check_infos(self):
        """Cette fonction permet de valider le pseudo et le mot de passe
        Returns:
            les propriétés d'un utilisateur (str) ou une erreur si le pseudo ou le mot de passe est invalide
        PRE: prend en argument un dictionnaire avec un pseudo, un password et un dictionnaire de comptes
        POST: renvoie une string avec toutes les informations du compte du pseudo entré
        """
        for account in self.__dict_accounts.values():
            if account["pseudo"] == self.__pseudo and account["password"] == self.__password:
                return print_account(account)

        raise WrongPasswordOrPseudo("Le mot de passe ou le pseudo est incorrecte ")


if __name__ == '__main__':
    args = argument()
    try:
        x = Utilisateur(args.pseudo, valid_psd(args.password), args.path)
        print(x.check_infos())
    except WrongPasswordOrPseudo as e:
        print(e)
