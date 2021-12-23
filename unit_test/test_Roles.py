from Classes.Roles import *
from unittest import TestCase


class TestRoles(TestCase):
    def test_insert_role_in_db(self):
        # création d'un objet RolesDBManagement
        roles_db = RolesDBManagement()

        #   delete du role admin2 de la DB
        roles_db.delete_role_from_db("admin2", "10001")

        # création d'un objet role
        role = Role(0, "admin2", "administrateur2", "10001", [1, 5, 22])

        # test insertion un role qui n'existe pas dans la DB
        self.assertEqual(roles_db.insert_role_in_db(role), "Role inserted in the DB",
                         "Test insertion role qui n'existe "
                         "pas dans la DB")
        # test insertion du même role: raises AlreadyExistException existe déjà dans la DB
        self.assertRaises(AlreadyExistException, roles_db.insert_role_in_db, role)

    def test_delete_role_from_db(self):
        roles_db = RolesDBManagement()
        # test delete un role qui existe dans la DB
        self.assertEqual(roles_db.delete_role_from_db("admin2", "10001"), "Role deleted from the DB", "un role qui "
                                                                                                      "existe ds la DB")
        # test delete un role qui n'existe pas dans la DB: Raises DoesNotExistException
        self.assertRaises(DoesNotExistException, roles_db.delete_role_from_db, "admin2", "10001")

    def test_update_role_in_db(self):
        roles_db = RolesDBManagement()
        role = Role(0, "admin2", "new administrateur2", "10001", [4, 4, 22])
        # test update un role qui n'existe pas dans la DB: Raises DoesNotExistException
        self.assertRaises(DoesNotExistException, roles_db.update_role_in_db, role)
        roles_db.insert_role_in_db(role)
        # test update un role qui existe dans la DB
        self.assertEqual(roles_db.update_role_in_db(role), "Role updated in the DB", "Test update role qui existe ")
