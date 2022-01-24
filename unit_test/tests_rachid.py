import unittest
from Classes.Users import *


class RachidTest(unittest.TestCase):

    def setUp(self):
        self.Uop = UsersOperations()
        self.viU = ValidationsInfosUsers()

    def test_is_not_exist_pseudo(self):
        with self.assertRaises(PseudoNotValid):
            # existe dans la DB
            self.Uop.is_not_exist_pseudo("")

        with self.assertRaises(PseudoNotValid):
            # existe dans la DB
            self.Uop.is_not_exist_pseudo("rachiiiid007")

        with self.assertRaises(PseudoNotValid):
            # existe dans la DB
            self.Uop.is_not_exist_pseudo("totototo")

        self.assertEqual(self.Uop.is_not_exist_pseudo("chaos"), True, " 'chaos' -> n'existe pas dans la DB")

    def test_is_age_min_13_yeas(self):
        with self.assertRaises(AgeNotValid):
            # vide !
            self.viU.is_age_min_13_years("")

        with self.assertRaises(AgeNotValid):
            # pas bon min 13 ans
            self.viU.is_age_min_13_years("2009-11-5")

        self.assertEqual(self.viU.is_age_min_13_years("2008-11-5"), True, "age > 13 ok !")

        self.assertEqual(self.viU.is_age_min_13_years("1986-11-5"), True, "age > 13 ok !")

        with self.assertRaises(AgeNotValid):
            # no OK
            self.viU.is_age_min_13_years("2025-11-5")


"""
    def test_register_verify(self):
        with self.assertRaises(PseudoNotValid):
            # les champs sont vide
            register_verify("", "", "", "", "", "", "")

        with self.assertRaises(PseudoNotValid):
            # l'utilisateur existe déjà
            register_verify("totototo", "totototo@ephec.com", "2002-04-21", "abdel1234", "abdel1234",
                            "C'est qui toto ?", "c'est toto")

        with self.assertRaises(EmailNotValid):
            # L'email existe déjà
            register_verify("userno007", "toto@ephec.be", "1998-04-21", "abdel1234", "abdel1234", "c'est qui Toto",
                            "c'est Toto")

        with self.assertRaises(PasswordNotValid):
            # Le MDP ne respect pas la norme
            register_verify("userno007", "hdbyhdb@ephec.com", "1998-04-21", "aaa", "aaa", "c'est qui Toto",
                            "c'est Toto")

        with self.assertRaises(PasswordsNotSame):
            # Les 2 MDP sont pas identique
            register_verify("userno007", "hdbyhdb@ephec.com", "1998-04-21", "abdel123", "rachid123", "c'est qui Toto",
                            "c'est Toto")

        self.assertTrue(register_verify("rachid007", "rachid@ephec.com", "1998-04-21", "abdel1234", "abdel1234",
                                        "C quoi mon meilleur langage de progra ?", "Python "), "Tu t'es inscrit")
"""

if __name__ == '__main__':
    unittest.main()
