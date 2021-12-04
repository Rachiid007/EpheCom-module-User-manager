def register():
    email = input("What's your email ?")
    pseudo = input("What's your pseudo ?")
    password = input("What's your password ?")
    confirm_password = input("Confirm password ?")

    # Function for register


def login():
    pseudo = input("What's your pseudo ?")
    password = input("What's your password ?")

    # Function for login


def log_or_register():
    if input("Do you want to login or register ?") == "register":
        register()
    login()


if __name__ == " __main__":
    log_or_register()
