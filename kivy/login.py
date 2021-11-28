from kivymd.app import MDApp
from kivy.lang import Builder


class Login(MDApp):
    def build(self):
        return Builder.load_file("login.kv")


Login().run()
