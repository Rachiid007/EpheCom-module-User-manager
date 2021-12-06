from connection import *
from interface_ligne_commande.connection import *

if __name__ == "__main__":
    ilc = input("Launching command line interface ? [y/n])")
    if ilc == "y":
        ilc_launcher()
    else:
        Connection().run()
