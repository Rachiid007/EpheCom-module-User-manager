from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.snackbar import Snackbar


class Register(MDApp):
    def build(self):
        return Builder.load_file("register.kv")

    def register(self):
        pseudo = self.root.ids.pseudo.text
        password = self.root.ids.password.text
        password_confirm = self.root.ids.password_confirm.text
        email = self.root.ids.email.text

        if pseudo == "" or password == "" or password_confirm == "" or email == "":
            Snackbar(
                text="[color=#ffffff]All field must be completed ! [/color]",
                font_size="20dp",
                bg_color=[118/255, 106/255, 221/255, 1],
                snackbar_animation_dir="Top"

            ).open()
            return
        print(pseudo, password, password_confirm, email)
        self.root.ids.pseudo.text = ""
        self.root.ids.password.text = ""
        self.root.ids.password_confirm.text = ""
        self.root.ids.email.text = ""

        # Appel de la fonction de traitement ici


Register().run()
