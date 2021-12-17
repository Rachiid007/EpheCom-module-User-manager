from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.list import OneLineListItem
from kivymd.uix.picker import MDDatePicker
from Classes.Users import *
from kivy.core.window import Window


def snackbar_message(text) -> None:
    """
    ouvre une fenètre avec le texte passé en argument
    PRE: prend en argument un texte(str)
    POST: ouvre en kivy une fenètre avec le texte passé en argument
    """
    Snackbar(
        text=f"[color=#ffffff]{text} [/color]",
        font_size="20dp",
        bg_color=[118 / 255, 106 / 255, 221 / 255, 1],
        snackbar_animation_dir="Top"
    ).open()


def generate_display_user_data(data: dict) -> tuple:
    data_keys = data.keys()
    data_string = f""
    for keys in data_keys:
        if keys == "_id" or keys == "password" or keys == "pseudo":
            continue
        data_string += f"\n\n{keys} : {data[keys] if not data[keys] == '' else None}"
    return data["pseudo"], data_string


Window.fullscreen = 'auto'


class Connection(MDApp):
    dialog = None

    def build(self):
        """
        Construit l'application sur base du modèle codé sur mainApp.kv
        """
        return Builder.load_file("mainApp.kv")

    def login(self):
        """
        Traitement du login sur l'application
        """
        pseudo = self.root.ids.l_pseudo.text
        password = self.root.ids.l_password.text

        # Gestion champs vide
        if pseudo == "" or password == "":
            return snackbar_message("All field must be completed !")

        # Lancement du login avec db
        try:
            is_user_db = login_verify(pseudo, password)
            self.root.current = "profile"
            self.display_profile_data(is_user_db)
            self.display_list_user()

        except PasswordOrUsernameNotCorrect or Exception as error:
            snackbar_message(error)
            self.root.ids.l_pseudo.text = ""
            self.root.ids.l_password.text = ""

    def register(self):
        """
        Traitement du register sur l'application
        """
        pseudo = self.root.ids.r_pseudo.text
        password = self.root.ids.r_password.text
        password_confirm = self.root.ids.r_password_confirm.text
        email = self.root.ids.r_email.text
        age = self.root.ids.r_age.text
        sec_question = self.root.ids.r_security_question
        sec_answer = self.root.ids.r_security_answer

        # Gestion champs vide
        if pseudo == "" or password == "" or password_confirm == "" or email == "" or sec_question == "" \
                or sec_answer == "":
            return snackbar_message("All field must be completed !")

        #   Reset field
        self.root.ids.r_pseudo.text = ""
        self.root.ids.r_password.text = ""
        self.root.ids.r_password_confirm.text = ""
        self.root.ids.r_email.text = ""
        self.root.ids.r_age.text = ""
        self.root.ids.r_security_question = ""
        self.root.ids.r_security_answer = ""

        # Appel de la fonction de traitement ici
        try:
            register_verify(pseudo, email, age, password, password_confirm, sec_question, sec_answer)

        except PseudoNotValid or EmailNotValid or PasswordNotValid or PasswordsNotSame or \
               AgeNotValid or SecurityQuestionNotCorrect or SecurityAnswerNotCorrect as error:
            snackbar_message(error)

        snackbar_message("Profile created")

    def display_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.save_age)
        date_dialog.open()

    def save_age(self, instance, value, date_range):
        self.root.ids.r_age.text = str(value)

    def display_profile_data(self, data: dict):
        """
        Affiche les informations de l'utilisateurs courant sur la page dédiée
        """
        # affichage des infos de l'utilisateur
        display = generate_display_user_data(data)
        self.root.ids.p_display_pseudo.text = display[0]
        self.root.ids.p_display_data.text = display[1]

        # Pré remplissage des champs de modifications
        self.root.ids.ed_pseudo.text = data["pseudo"]
        self.root.ids.ed_email.text = data["email"]
        self.root.ids.ed_first_name.text = data["first_name"]
        self.root.ids.ed_last_name.text = data["last_name"]
        self.root.ids.ed_security_question.text = data["security_question"]
        self.root.ids.ed_security_answer.text = data["security_answer"]

    def display_other_user_data(self, data: dict):
        """
        Affiche les informations d'un autre utilisateur sur la page dédiée
        """
        display = generate_display_user_data(data)
        self.root.ids.ou_display_pseudo.text = display[0]
        self.root.ids.ou_display_data.text = display[1]

    def update_profile(self):
        """
        Traite la mise à jour des informations de l'utilisateur courant
        """
        current_pseudo = self.root.ids.p_display_pseudo.text
        current_password = ""
        new_pseudo = self.root.ids.ed_pseudo.text
        email = self.root.ids.ed_email.text
        password = self.root.ids.ed_password.text
        confirm_password = self.root.ids.ed_password_confirm.text
        first_name = self.root.ids.ed_first_name.text
        last_name = self.root.ids.ed_last_name.text
        security_question = self.root.ids.ed_security_question.text
        security_answer = self.root.ids.ed_security_answer.text

        # Fonction traitement ici
        try:
            update_verify(current_pseudo, current_password, new_pseudo, email, first_name, last_name, password,
                          confirm_password, security_question, security_answer)

        except Exception or PseudoNotValid or EmailNotValid or PasswordNotValid or PasswordsNotSame or \
               AgeNotValid or SecurityQuestionNotCorrect or SecurityAnswerNotCorrect as error:
            snackbar_message(error)

    def delete_profile(self):
        """
        Supprime l'utilisateur courant de la BDD
        """
        delete_user(self.root.ids.p_display_pseudo.text)
        self.log_out()

    def display_list_user(self):
        """
        S'occupe de génèrer l'affichage de la list de tout les utilisateurs de l'application
        """
        list_user = UsersOperations().get_all_users()
        for user in list_user:
            self.root.ids.display_all_user.add_widget(
                OneLineListItem(text=user["pseudo"])  # on_release=self.display_other_user_data(user)
            )

    def log_out(self):
        """
        Déconnecte l'utilisateur courant de l'application
        """
        self.root.current = "connection"
        print("Success login out")


Connection().run()
