from Users import ValidationsInfosUsers, EmailNotValid, PasswordNotValid
import unittest

class testUnitaire(unittest.TestCase):

    def test_is_valid_email(self):
        with self.assertRaises(EmailNotValid):
            ValidationsInfosUsers.is_valide_email(int(3))
        with self.assertRaises(EmailNotValid):
            ValidationsInfosUsers.is_valide_email("ggggg")
        with self.assertRaises(EmailNotValid):
            ValidationsInfosUsers.is_valide_email("gggg@.be")
        with self.assertRaises(EmailNotValid):
            ValidationsInfosUsers.is_valide_email("gggg@ee.bee")
        self.assertTrue(ValidationsInfosUsers.is_valide_email("aaaa@aaaa.aa"))

    def test_is_valid_password(self):
        with self.assertRaises(PasswordNotValid):
            ValidationsInfosUsers.is_valid_password("aa")
        with self.assertRaises(PasswordNotValid):
            ValidationsInfosUsers.is_valid_password("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.assertTrue(ValidationsInfosUsers.is_valid_password("aaaA_aa.a+a@a22a"))
        self.assertTrue(ValidationsInfosUsers.is_valid_password("aaaaaaaaa"))

    def test_update_verify(self):
        print("a faire")

if __name__ == '__main__':
    unittest.main()
