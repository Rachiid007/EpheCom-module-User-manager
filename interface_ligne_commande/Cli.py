import sys
# adding Classes to the system path
sys.path.insert(0, '../Classes')

from Roles import *
from Users import *
from Permission import *
import argparse


"""
from Classes.Roles import *
from Classes.Users import *
from Classes.Permission import *
import argparse
"""


class Cli:
    """ Used to process CLI commands
    usage:
    get all roles
    python Cli.py --action roles --roles get_all

    add a new role
    python Cli.py --action roles --roles add --id_role [role id]  --name [role name] --description [role description]
        --id_user [user ID] --perm_list [permission list]

    delete a role
    python Cli.py --action roles --roles delete --name [role name] --id_user [id user]

    login
    python Cli.py --action login --pseudo [Pseudo] --password [password]

    register:
    python Cli.py --action register --pseudo [Pseudo] --password [Password] --birthdate [birthdate]
            --email [Email address] --sec_question [Question] --sec_answer [Response]

    """

    @staticmethod
    def roles(arguments):
        """ Used to process roles CLI commands: display all roles add a new roles, delete a role
        Post: Display the result of the command or/and add or delete a role
        """

        rolesdb = RolesDBManagement()
        if arguments.role == "get_all":
            for x in rolesdb.get_all_roles_from_db():
                print(x)
        elif args.role == "add":
            role = Role(0, arguments.name, arguments.description, arguments.id_user,
                        arguments.perm_list)
            print(rolesdb.insert_role_in_db(role))
        elif args.role == "delete":
            print(rolesdb.delete_role_from_db(arguments.name, arguments.id_user))

    @staticmethod
    def users(arguments):
        """ Used to process users CLI commands: display all users, add a new user, delete a user
        Post: Display the result of the command or/and add or delete a user
        """
        user_managt = UsersOperations()
        if args.user == "get_all":
            for x in user_managt.get_all_users():
                print(f"id user : {x['_id']} | Pseudo : {x['pseudo']} | email : {x['email']} " 
                      f"| First name : {x['first_name']} | Last name : {x['last_name']}")
        elif args.user == "delete":
            user_managt.delete_specific_user(arguments.pseudo)
        elif args.user == "login":
            is_user_db = login_verify(arguments.pseudo, arguments.password)
            if not is_user_db:
                print("Pseudo or password incorrect !")
            else:
                print("Login Ok")
                print(is_user_db)
        elif args.user == "register":
            try:
                register_verify(arguments.pseudo, arguments.email, arguments.birthdate, arguments.password,
                                arguments.password, arguments.sec_question, arguments.sec_answer)

            except PseudoNotValid or EmailNotValid or PasswordNotValid or PasswordsNotSame or \
                   AgeNotValid or SecurityQuestionNotCorrect or SecurityAnswerNotCorrect as error:
                print(error)

    @staticmethod
    def permission(arguments):
        """ Used to process permissions CLI commands: display all permissions, add a new permission, delete a permission
        Post: Display the result of the command or/and add or delete a permission
        """

        permission_managt = Permissions()
        if args.permission == "get_all":
            for x in permission_managt.list_perm():
                print(f"Name : {x}")
        elif args.permission == "add":
            obj_perm = Permissions(arguments.name, arguments.description)
            obj_perm.add_db_perm()
        elif args.permission == "delete":
            obj_perm = Permissions(arguments.name)
            obj_perm.remove_perm()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Ce script offre la CLI du projet
    get all roles
    python Cli.py --role get_all

    add a new role
    python Cli.py --role add --name [role name] --description [role description]
        --id_user [user ID] --perm_list [permission list]

    delete a role
    python Cli.py --role delete --name [role name] --id_user [id user]
    
    delete a user
    python Cli.py --user delete --pseudo [the pseudo of the user]
    
    get all users
    python Cli.py --user get_all
    
    login
    python Cli.py --user login --pseudo [Pseudo] --password [password]

    register:
    python Cli.py --user register --pseudo [Pseudo] --password [Password] --birthdate [birthdate] 
            --email [Email address] --sec_question [Question] --sec_answer [Response]
    
    get all permissions
    python Cli.py --permission get_all

    add a new permission
    python Cli.py --permission add --name [permission name] --description [description]
    
    delete a permission
    python Cli.py --permission delete --name [permission name]
    
    """, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-r", "--role", help="roles actions")
    parser.add_argument("-us", "--user", help="roles actions")
    parser.add_argument("-u", "--pseudo", help="The pseudo of the user.")
    parser.add_argument("-p", "--password", help="the password")
    parser.add_argument("-b", "--birthdate", help="the birthdate")
    parser.add_argument("-n", "--name", help="The name")
    parser.add_argument("-e", "--email", help="email address")
    parser.add_argument("-sq", "--sec_question", help="the second question")
    parser.add_argument("-sa", "--sec_answer", help="the second answer")
    parser.add_argument("-iu", "--id_user", help="the id of a user")
    parser.add_argument("-perm", "--perm_list", help="the id of a user")
    parser.add_argument("-d", "--description", help="the description")
    parser.add_argument("-P", "--permission", help="permissions actions")

    args = parser.parse_args()

    cli = Cli()
    try:
        if args.role:
            cli.roles(args)
        elif args.user:
            cli.users(args)
        elif args.permission:
            cli.permission(args)
    except Exception as e:
        print(e)



