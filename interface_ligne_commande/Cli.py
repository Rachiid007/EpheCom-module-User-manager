import sys
# adding Classes to the system path
sys.path.insert(0, '..\Classes')
# adding interface_kivy to the system path
sys.path.insert(0, '..\interface_kivy')

from Roles import *
from Users import *
import argparse


class Cli:

    """ Used to process CLI commands
    usage:
    get all roles
    python Cli.py --action roles --roles all

    get roles by name
    python Cli.py --action roles --roles name --name [Name of role]

    get roles by pseudo
    python Cli.py --action roles --roles pseudo --pseudo [Pseudo of a role]

    add a new role
    python Cli.py --action roles --roles add --id_role [role id]  --name [role name] --description [role description]
        --id_user [user ID] --perm_list [permission list]

    delete a role
    python Cli.py --action roles --roles delete --name [role name] --id_user [id user]

    login
    python Cli.py --action login --pseudo [Pseudo] --password [password]

    register:
    python Cli.py --action register --pseudo [Pseudo] --password [Password] --age [age] --email [Email address]
            --sec_question [Question] --sec_answer [Response]

    """

    def roles(self, args):
        """ Used to process roles CLI commands: display all roles, display the roles that have the name or pseudo
        given as params, add new roles, delete a role
        Post: Displqy the result of the command or/and add or delete a role
        """

        rolesdb = RolesDBManagement()
        if args.roles == "all":
            for x in rolesdb.get_all_roles_fromdb():
                print(x)
        elif args.roles == "name":
            for x in rolesdb.get_roles_by_name(args.name):
                print(x)
        elif args.roles == "pseudo":
            for x in rolesdb.get_roles_by_pseudo(args.pseudo):
                print(x)
        elif args.roles == "add":
            role = Role(args.id_role, args.name, args.description, args.id_user, args.perm_list)
            print(rolesdb.insert_role_indb(role))
        elif args.roles == "delete":
            print(rolesdb.delete_role_fromdb(args.name, args.id_user))

    def login(self, arguments):
        """ Check if the user name and password exist in the DB
        :pre: args that contain : user name str, password str
        :post: display the result of the login ok or failed
        """

        is_user_db = login_verify(arguments.pseudo, arguments.password)
        if not is_user_db:
            print("Pseudo or password incorrect !")
        else:
            print("Login Ok")
            print(is_user_db)

    def register(self, arguments):
        """ Check if the user name and password exist in the DB
        :pre: args used in the command : pseudo, email, age, password, password, sec_question, sec_answer
        :post: display the result of the register ok or failed
        """
        try:
            register_verify(arguments.pseudo, arguments.email, arguments.birthdate, arguments.password,
                                       arguments.password, arguments.sec_question, arguments.sec_answer)

        except PseudoNotValid or EmailNotValid or PasswordNotValid or PasswordsNotSame or \
               AgeNotValid or SecurityQuestionNotCorrect or SecurityAnswerNotCorrect as error:
            print(error)



    def users(self, arguments):
        pass

    def permission(self, arguments):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ce script offre la CLI du projet')
    parser.add_argument("-a", "--action", help="login ou register or users ou roles or permissions.")
    parser.add_argument("-u", "--pseudo", help="Le pseudo de l'utilisateur.")
    parser.add_argument("-p", "--password", help="le mot de passe")
    parser.add_argument("-b", "--birthdate", help="the birthdate")
    parser.add_argument("-n", "--name", help="The name")
    parser.add_argument("-e", "--email", help="email address")
    parser.add_argument("-sq", "--sec_question", help="the second question")
    parser.add_argument("-sa", "--sec_answer", help="the second answer")
    parser.add_argument("-ir", "--id_role", help="the id of a role")
    parser.add_argument("-iu", "--id_user", help="the id of a user")
    parser.add_argument("-perm", "--perm_list", help="the id of a user")
    parser.add_argument("-d", "--description", help="the description")
    parser.add_argument("-r", "--roles", help="roles actions")

    args = parser.parse_args()

    cli = Cli()
    try:
        if args.action == "roles":
            cli.roles(args)
        elif args.action == "login":
            cli.login(args)
        elif args.action == "register":
            cli.register(args)
        elif args.action == "users":
            cli.users(args)
        elif args.action == "permission":
            cli.permission(args)

    except Exception as e:
        print(e)
