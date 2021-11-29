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
            Snackbar(text="Invalid pseudo or password").open()
            return
        print(pseudo, password)
        # Reset field
        self.root.ids.pseudo.text = ""
        self.root.ids.password.text = ""


Login().run()
