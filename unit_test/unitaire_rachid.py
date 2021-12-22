import unittest

from Classes.Users import *


class RachidTest(unittest.TestCase):

    def setUp(self):
        self.Uop = UsersOperations()
        self.viU = ValidationsInfosUsers()

    def test_is_exist_user_name(self):
        with self.assertRaises(PseudoNotValid):
            # n'existe pas dans la DB (vide)
            self.Uop.is_not_exist_pseudo("")

        with self.assertRaises(PseudoNotValid):
            # existe dans la DB
            self.Uop.is_not_exist_pseudo("rachid007")

        self.assertEqual(self.Uop.is_not_exist_pseudo("chaos"), False, " 'chaos' -> n'existe pas dans la DB")

    def test_is_age_min_13_yeas(self):
        with self.assertRaises(AgeNotValid):
            # vide !
            self.viU.is_age_min_13_years("")

        with self.assertRaises(AgeNotValid):
            # pas bon min 13 ans
            self.viU.is_age_min_13_years("2009-11-5")

        with self.assertRaises(AgeNotValid):
            # ok
            self.viU.is_age_min_13_years("2008-11-5")

        with self.assertRaises(AgeNotValid):
            # OK
            self.viU.is_age_min_13_years("1986-11-5")

        with self.assertRaises(PseudoNotValid):
            # no OK
            self.viU.is_age_min_13_years("2025-11-5")

    def test_register_verify(self):
        with self.assertRaises(PseudoNotValid):
            # les champs sont vide
            register_verify("", "", "", "", "", "", "")

        with self.assertRaises(PseudoNotValid):
            # l'utilisateur existe déjà
            register_verify("totototo", "totototo@gmail.com", "50", "abdel1234", "abdel1234", "", "")

        with self.assertRaises(EmailNotValid):
            # L'email existe déjà
            register_verify("userno007", "totototo@gmail.com", "42", "abdel1234", "abdel1234", "", "")

        with self.assertRaises(PasswordNotValid):
            # Le MDP ne respect pas la norme
            register_verify("userno007", "hdbyhdb@glpx.com", "25", "aaa", "aaa", "", "")

        with self.assertRaises(PasswordNotValid):
            # Les 2 MDP sont pas identique
            register_verify("userno007", "hdbyhdb@glpx.com", "23", "abdel123", "rachid123", "", "")

        self.assertTrue(register_verify("Abderrachid", "usertest@gmail.com", "25", "abdel1234", "abdel1234", "", ""),
                        "Tu t'es inscrit")


if __name__ == '__main__':
    unittest.main()
