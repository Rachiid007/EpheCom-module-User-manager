import unittest

import User_Verification as u_v


class RachidTest(unittest.TestCase):

    def setUp(self) -> None:
        self.user_test = u_v.UsersOperations()

    def test_is_exist_user_name(self):
        self.assertEqual(self.user_test.is_exist_user_name(""), False, "'' -> n'existe pas dans la DB (vide)")
        self.assertEqual(self.user_test.is_exist_user_name("rachid007"), True,
                         "'rachid007' -> existe dans la DB")  # l'ajouter
        self.assertEqual(self.user_test.is_exist_user_name("chaos"), False, " 'chaos' -> n'existe pas dans la DB")

    def test_is_age_min_13_yeas(self):
        self.assertEqual(u_v.is_age_min_13_yeas("")[0], False, "'' -> n'age pas bon (vide)")
        self.assertEqual(u_v.is_age_min_13_yeas(12)[0], False, "'12' -> pas bon min 13 ans")
        self.assertEqual(u_v.is_age_min_13_yeas(13)[0], True, "'13' -> age ok")
        self.assertEqual(u_v.is_age_min_13_yeas(36)[0], True, "'36' -> age ok")
        self.assertEqual(u_v.is_age_min_13_yeas(-7)[0], False, "'-7' -> age no ok")

    def test_register_verify(self):
        self.assertEqual(u_v.register_verify("", "", "", "", ""),
                         (False, 'Un ou plusieur champ ne sont pas complété !'),
                         "les champs sont vide")

        self.assertEqual(u_v.register_verify("rachid007", "bellaalirachid@gmail.com", 50, "abdel1234", "abdel1234"),
                         (False, "Le nom d'utilisateur existe déjà !"), "l'utilisateur existe déjà")

        self.assertEqual(u_v.register_verify("userno007", "bellaalirachid@gmail.com", 42, "abdel1234", "abdel1234"),
                         (False, "L'adresse email existe déjà !"), "l'email existe déjà")

        self.assertEqual(u_v.register_verify("userno007", "hdbyhdb@glpx.com", 25, "aaa", "aaa"),
                         (False, 'Le MDP ne respect pas la norme !'), "Le MDP ne respect pas la norme !")

        self.assertEqual(u_v.register_verify("userno007", "hdbyhdb@glpx.com", 23, "abdel123", "rachid123"),
                         (False, 'Les 2 MDP ne correspondent pas !'), "Les 2 MDP sont pas identique !")

        self.assertEqual(u_v.register_verify("Abderrachid", "usertest@gmail.com", 25, "abdel1234", "abdel1234"),
                         (True, "L'utilisateur a été créée"), "Tu t'es inscrit")


if __name__ == '__main__':
    unittest.main()
