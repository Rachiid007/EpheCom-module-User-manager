if __name__ == "__main__":

    ilc = input("Launching command line interface ? [y/n])")
    if ilc == "y":
        from interface_ligne_commande.connection import *
        ilc_launcher()

    else:
        from interface_kivy.mainApp import *
        Connection().run()
