from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.snackbar import Snackbar


class Login(MDApp):
    def build(self):
        return Builder.load_file("login.kv")

    def login(self):
        pseudo = self.root.ids.pseudo.text
        password = self.root.ids.password.text
        if pseudo == "" or password == "":
            Snackbar(
                text="[color=#ffffff]Invalid pseudo or password ! [/color]",
                font_size="20dp",
                bg_color=[118/255, 106/255, 221/255, 1],
                snackbar_animation_dir="Top"

            ).open()
            return
        print(pseudo, password)
        # Reset field
        self.root.ids.pseudo.text = ""
        self.root.ids.password.text = ""

        # Appel de la fonction de traitement ici


Login().run()
