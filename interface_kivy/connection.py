from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

from Users import *


class Connection(MDApp):
    def build(self):
        """
        Construit l'application sur base du modèle codé sur connection.kv
        """
        return Builder.load_file("connection.kv")

    def login(self):
        """
        Traitement du login sur l'application
        """
        pseudo = self.root.ids.l_pseudo.text
        password = self.root.ids.l_password.text

        # Gestion champs vide
        if pseudo == "" or password == "":
            Snackbar(
                text="[color=#ffffff]All field must be completed ! [/color]",
                font_size="20dp",
                bg_color=[118 / 255, 106 / 255, 221 / 255, 1],
                snackbar_animation_dir="Top"

            ).open()
            return
        # Reset field
        self.root.ids.l_pseudo.text = ""
        self.root.ids.l_password.text = ""

        # Lancement du login avec db
        users_test = Users(user_name=pseudo, email="", password=password)
        users_test.is_user_in_bdd()

        # si il est en BDD -> True, {dict avec info de l'User}

            Snackbar(
                text="[color=#ffffff]Pseudo or password incorrect ! [/color]",
                font_size="20dp",
                bg_color=[118 / 255, 106 / 255, 221 / 255, 1],
                snackbar_animation_dir="Top"

            ).open()
            return
        print("OK launch main app")
        # Stop connection app and launch main app

    def register(self):
        """
        Traitement du register sur l'application
        """
        pseudo = self.root.ids.r_pseudo.text
        password = self.root.ids.r_password.text
        password_confirm = self.root.ids.r_password_confirm.text
        email = self.root.ids.r_email.text
        age = 22

        # Gestion champs vide
        if pseudo == "" or password == "" or password_confirm == "" or email == "":
            Snackbar(
                text="[color=#ffffff]All field must be completed ! [/color]",
                font_size="20dp",
                bg_color=[118 / 255, 106 / 255, 221 / 255, 1],
                snackbar_animation_dir="Top"

            ).open()
            return
        print(pseudo, password, password_confirm, email)
        #   Reset field
        self.root.ids.r_pseudo.text = ""
        self.root.ids.r_password.text = ""
        self.root.ids.r_password_confirm.text = ""
        self.root.ids.r_email.text = ""

        # Appel de la fonction de traitement ici
        register_verify(pseudo, email, password, password_confirm, age)  # RAJOUTER le champ AGE !!!!
