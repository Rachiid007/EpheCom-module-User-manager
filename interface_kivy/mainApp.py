from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.picker import MDDatePicker
from Classes.Users import *
from kivy.core.window import Window

Window.fullscreen = 'auto'


def snackbar_message(text) -> None:
    """
    Open a snackbar with a message text
    PRE: text is a string
    POST: Display a snackbar on the application
    """
    Snackbar(
        text=f"[color=#ffffff]{text} [/color]",
        font_size="20dp",
        bg_color=[118 / 255, 106 / 255, 221 / 255, 1],
        snackbar_animation_dir="Top"
    ).open()


class Connection(MDApp):
    dialog = None

    def build(self):
        """The app is build by following the model in mainApp.kv"""
        return Builder.load_file("mainApp.kv")

    def login(self):
        """Manage the login on the app"""
        pseudo = self.root.ids.l_pseudo.text
        password = self.root.ids.l_password.text

        # Empty field
        if pseudo == "" or password == "":
            return snackbar_message("All field must be completed !")

        # Connection and login with the DB
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
        """Manage the register on the app"""
        pseudo = self.root.ids.r_pseudo.text
        password = self.root.ids.r_password.text
        password_confirm = self.root.ids.r_password_confirm.text
        email = self.root.ids.r_email.text
        birthday = self.root.ids.r_age.text
        sec_question = self.root.ids.r_security_question
        sec_answer = self.root.ids.r_security_answer

        # Empty field
        if pseudo == "" or password == "" or password_confirm == "" or email == "" or sec_question == "" \
                or sec_answer == "":
            return snackbar_message("All field must be completed !")

        try:
            register_verify(pseudo, email, birthday, password, password_confirm, sec_question, sec_answer)

        except PseudoNotValid or EmailNotValid or PasswordNotValid or PasswordsNotSame or \
               AgeNotValid or SecurityQuestionNotCorrect or SecurityAnswerNotCorrect as error:
            snackbar_message(error)

        finally:
            # Reset field
            self.root.ids.r_pseudo.text = ""
            self.root.ids.r_password.text = ""
            self.root.ids.r_password_confirm.text = ""
            self.root.ids.r_email.text = ""
            self.root.ids.r_age.text = ""
            self.root.ids.r_security_question = ""
            self.root.ids.r_security_answer = ""

        snackbar_message("Profile created")

    def display_date_picker(self):
        """Manage the birthday date for the register"""
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.save_age)
        date_dialog.open()

    def save_age(self, instance, value, date_range):
        """Show the chosen date for the birthdate"""
        self.root.ids.r_age.text = str(value)

    def display_profile_data(self, data: dict):
        """Display the user's data on the dedicated page"""

        # Construction
        data_keys = data.keys()
        data_string = f""
        for keys in data_keys:
            if keys == "_id" or keys == "password" or keys == "pseudo":
                continue
            data_string += f"\n\n{keys} : {data[keys] if not data[keys] == '' else 'Unknown'}"

        # Display
        self.root.ids.p_display_pseudo.text = data["pseudo"]
        self.root.ids.p_display_data.text = data_string

        # Prefill the update fields
        self.root.ids.ed_pseudo.text = data["pseudo"]
        self.root.ids.ed_email.text = data["email"]
        self.root.ids.ed_first_name.text = data["first_name"]
        self.root.ids.ed_last_name.text = data["last_name"]
        self.root.ids.ed_security_question.text = data["security_question"]
        self.root.ids.ed_security_answer.text = data["security_answer"]

    def update_profile(self):
        """Manage the update of the user's data"""
        current_pseudo = self.root.ids.p_display_pseudo.text
        current_password = self.root.ids.ed_current_password.text
        new_pseudo = self.root.ids.ed_pseudo.text
        email = self.root.ids.ed_email.text
        password = self.root.ids.ed_password.text
        confirm_password = self.root.ids.ed_password_confirm.text
        first_name = self.root.ids.ed_first_name.text
        last_name = self.root.ids.ed_last_name.text
        security_question = self.root.ids.ed_security_question.text
        security_answer = self.root.ids.ed_security_answer.text

        # Update the data
        try:
            update_verify(current_pseudo, current_password, new_pseudo, email, first_name, last_name, password,
                          confirm_password, security_question, security_answer)

        except PseudoNotValid or EmailNotValid or PasswordNotValid or PasswordsNotSame or \
               AgeNotValid or SecurityQuestionNotCorrect or SecurityAnswerNotCorrect as error:
            snackbar_message(error)

    def delete_profile(self):
        """Delete the user from the DB"""
        delete_user(self.root.ids.p_display_pseudo.text)
        self.log_out()

    def display_list_user(self):
        """Display the list which contain all the users and their public data"""
        list_user = UsersOperations().get_all_users()
        for user in list_user:
            self.root.ids.display_all_user.add_widget(
                ThreeLineListItem(text=user["pseudo"],
                                  secondary_text=f"      Firstname : "
                                                 f"{user['first_name'] if not user['first_name'] == '' else 'Unknown'}, "
                                                 f"Lastname : "
                                                 f"{user['last_name'] if not user['last_name'] == '' else 'Unknown'}, "
                                                 f"age : {user['age']} year",

                                  tertiary_text=f"      Email : {user['email']}"
                                  )
            )

    def log_out(self):
        """Disconnect the user from the app"""
        self.root.current = "connection"
        print("Success login out")

    def go_to_forgot_psw(self):
        """Change the screen to the forgot psw one"""
        pseudo = self.root.ids.l_pseudo.text
        if pseudo == "":
            return snackbar_message("The pseudo field must be filled !")
        try:
            self.root.ids.fp_question.text = recup_password(pseudo)
            self.root.current = "forgot_psw"

        except PseudoNotValid as error:
            snackbar_message(error)

    def forgot_psw(self):
        """Manage the forgot password actions"""
        answer = self.root.ids.fp_answer.text
        password = self.root.ids.fp_new_psw.text
        confirm_password = self.root.ids.fp_confirm_psw.text

        if answer == '' or password == '' or confirm_password == '':
            snackbar_message("All field must be completed")

        #   Management


Connection().run()
