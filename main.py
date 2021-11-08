class Profile:
    """Une classe pour représenter un Profile d'utilisateur.

    La class Profile contient toutes les informations à propos d'un utilisateur.

    Args:
        pseudo (str): Le nom d'utilisateur.
        password (str): Le mot de passe.
        last_name (str): Le nom de famille.
        first_name (str): Le prénom.
        team (str): l'équipe.


    Attributes:
        __pseudo (str): Le nom d'utilisateur.
        __password (str): Le mot de passe.
        __last_name (str): Le nom de famille.
        __first_name (str): Le prénom.
        __team (str): l'équipe.


    Returns:
        str: Les données personnels d'un utilisateurs.
    """

    def __init__(self, pseudo, password, last_name, first_name, team):
        self.__pseudo = pseudo
        self.__password = password
        self.__last_name = last_name
        self.__first_name = first_name
        self.__team = team

    def __str__(self):
        return f"""
                ===========================
                Pseudo : {self.__pseudo}
                Password : {self.__password}
                Name : {self.__last_name}
                Surname : {self.__first_name}
                Team : {self.__team}
                ===========================
                """

    @property
    def pseudo(self):
        """retourne la valeur de l'attribut pseudo.

            Returns:
                str: valeur de l'attribut pseudo.
        """
        return self.__pseudo

    @property
    def password(self):
        """retourne la valeur de l'attribut password.

            Returns:
                str: valeur de l'attribut password.
        """
        return self.__password


def connection_infos():
    """retourne le pseudo et le mot de passe demander à l'utilisateur.

    Demander un pseudo et un mot de passe à l'utilisateur et les retourner.

    return:
        pseudo (str): Le nom d'utilisateur.
        password (str): Le mot de passe.

    """
    pseudo = input("What's your pseudo ?")
    password = input("What's you password ?")
    return pseudo, password


list_profile = [
    Profile("Chaos", "1234", "Meunier", "Arnaud", "2TM1"),
    Profile("Coco", "1234", "Jean", "Pierre", "2TM2"),
    Profile("Nono", "1234", "Van", "Noé", "2TM3")
]

if __name__ == '__main__':
    connexion = connection_infos()
    for profile in list_profile:
        if profile.pseudo == connexion[0] and profile.password == connexion[1]:
            print(f"Welcome {profile.pseudo}. Here are all your information : {profile}")
            exit(0)

    print("Invalid pseudo or password")
    exit(-1)
