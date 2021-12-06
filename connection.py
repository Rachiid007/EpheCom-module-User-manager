from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from Users import *


def snackbar_message(text: str) -> None:
    Snackbar(
        text=f"[color=#ffffff]{text} [/color]",
        font_size="20dp",
        bg_color=[118 / 255, 106 / 255, 221 / 255, 1],
        snackbar_animation_dir="Top"
    ).open()


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
            return snackbar_message("All field must be completed !")

        # Reset field
        self.root.ids.l_pseudo.text = ""
        self.root.ids.l_password.text = ""

        # Lancement du login avec db
        users_test = Users(user_name=pseudo, email="", password=password, age=13)
        is_user_db = users_test.is_user_in_bdd()

        # Gestion données incorrecte
        if not is_user_db[0]:
            return snackbar_message("Pseudo or password incorrect !")

        print(is_user_db[1])
        self.root.current = "profile"

    def register(self):
        """
        Traitement du register sur l'application
        """
        pseudo = self.root.ids.r_pseudo.text
        password = self.root.ids.r_password.text
        password_confirm = self.root.ids.r_password_confirm.text
        email = self.root.ids.r_email.text
        age = self.root.ids.r_age.text

        # Gestion champs vide
        if pseudo == "" or password == "" or password_confirm == "" or email == "":
            return snackbar_message("All field must be completed !")

        print(pseudo, password, password_confirm, email)
        #   Reset field
        self.root.ids.r_pseudo.text = ""
        self.root.ids.r_password.text = ""
        self.root.ids.r_password_confirm.text = ""
        self.root.ids.r_email.text = ""
        self.root.ids.r_age.text = ""

        # Appel de la fonction de traitement ici
        verification = register_verify(pseudo, email, password, password_confirm, age)
        if not verification[0]:
            return snackbar_message(verification[1])

        print("Register done")

    def log_out(self):
        self.root.current = "connection"
        print("Success login out")


Connection().run()
