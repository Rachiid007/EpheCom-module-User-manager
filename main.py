#! python3
# coding: utf-8

from argparse import ArgumentParser
from platform import system
from re import match
import subprocess
import sys


def check_filename(filename: str) -> bool:
    """Verifier si le nom du fichier est correct.

    Verifier si le nom du fichier est correct (retourne True ou sinon False).


    Parameters:
            filename (str): un nom de fichier

    Returns:
            boolean (bool): Booléen si le nom du fichier est correct ou non
    """
    regex = r'\b[A-Za-z0-9._+-]+\.[A-Z|a-z]{2,6}\b'

    if match(regex, filename):
        return True

    else:
        return False


def check_args() -> str:
    """Verifier les arguments de la ligne de commande

    Configuration des arguments de ligne de commande. Verifier si le nom du fichier reçu via arguments de ligne
    de commande est bien un nom de fichier.


    Returns:
            Nom du fichier (str): Si nom de fichier, retourne le nom du fichier ou erreur dans le cas échéant
    """
    parser = ArgumentParser(prog="Ping hostname", description="Tester la joignabilité d'un site.")
    parser.add_argument('filename', type=str, help='Le nom du fichier contenant la liste des noms des sites.')
    args = parser.parse_args()

    if check_filename(args.filename):
        return args.filename
    else:
        sys.exit("Le paramètre dois être un nom de fichier !")


class Pinger:
    """Une classe pour représenter un Ping.

    Args:
       system_now (str): système d'exploitation actuel.
        count (int): nombre de ping (par défaut 4).
        nbr_second (int): nombre de seconde pour chaque ping (par défaut 4).

    Attributes:
        __system_now (str): système d'exploitation actuel.
        __count (int): nombre de ping (par défaut 4).
        __nbr_second (int): nombre de seconde pour chaque ping (par défaut 4).

    Returns:
        str: La commande ping avec la version du système d'exploitation actuel.
    """

    def __init__(self, system_now=system().lower(), count=4, nbr_second=4):
        self.__system_now = system_now

        if isinstance(count, int):
            self.__count = count
        else:
            sys.exit("Pas un entier !")

        if isinstance(count, int):
            self.__nbr_second = nbr_second
        else:
            sys.exit("Pas un entier !")

    def number_of_ping(self) -> str:
        """nombre de seconde pour chaque ping.
            Returns:
                str: Le nombre de ping demandé pour la version du système d'exploitation actuel.
        """
        if self.__system_now == "windows":
            return f"-n {self.__count}"
        else:
            return f"-c {self.__count}"

    def timeout(self) -> str:
        """timeout pour chaque ping.
            Returns:
                str: Le nombre de timeout pour chaque ping avec la version du système d'exploitation actuel.
        """
        if self.__system_now == "windows":
            return f"-w {(self.__nbr_second * 1000)}"
        else:
            return f"-w {self.__nbr_second}"

    def __str__(self):
        return f"ping {self.number_of_ping()} {self.timeout()}"


def ping(hostname: str) -> bool:
    """Effectuer la commande ping sur les sites.

    Instancier un objet Pinger(), le concatener avec le hostname qu'on souhaite faire le ping()
    dessus. Passer la commande à subprocess.check_output() et on test si la valeur de retour contient la sous-chaine
    "0%" (aucune pertes de paquets)


    Parameters:
            hostname (str): un nom de fichier

    Returns:
            boolean (bool): Booléen si la commande ping() n'a subi aucune pertes.
    """
    test1 = Pinger()
    commande = f"{test1} {hostname}"
    try:
        output = subprocess.check_output(commande, shell=False, universal_newlines=True)

        if "0%" in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False


def exec_script(filename: str):
    """Exécuter le script.

    Ouvrir le fichier, boucler tant qu'il y a des lignes, faire un ping() de chaque ligne grâce à la fonction ping() et
    afficher le résultat. Si ok -> UP, sinon DOWN.

    Parameters:
            filename (str): un nom de fichier

    Returns:
        none: Affiche le résultat du ping.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            for line in file:
                if ping(f"{line.rstrip()}"):
                    print(f"{line.rstrip()} UP")
                else:
                    print(f"{line.rstrip()} DOWN")

    except FileNotFoundError:
        sys.exit("Fichier introuvable !")
    except IOError:
        sys.exit("Erreur IO !")


if __name__ == '__main__':
    exec_script(check_args())
