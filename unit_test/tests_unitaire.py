from Classes.Users import *
import unittest


class testUnitaire(unittest.TestCase):

    def test_is_valid_email(self):
        with self.assertRaises(EmailNotValid):
            ValidationsInfosUsers.is_valid_email(int(3))
        with self.assertRaises(EmailNotValid):
            ValidationsInfosUsers.is_valid_email("ggggg")
        with self.assertRaises(EmailNotValid):
            ValidationsInfosUsers.is_valid_email("gggg@.be")
        with self.assertRaises(EmailNotValid):
            ValidationsInfosUsers.is_valid_email("gggg@ee.b")
        self.assertTrue(ValidationsInfosUsers.is_valid_email("gggg@e.be"))
        self.assertTrue(ValidationsInfosUsers.is_valid_email("aaaa@aaaa.aa"))

    def test_is_valid_password(self):
        with self.assertRaises(PasswordNotValid):
            ValidationsInfosUsers.is_valid_password("aa")
        with self.assertRaises(PasswordNotValid):
            ValidationsInfosUsers.is_valid_password("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.assertTrue(ValidationsInfosUsers.is_valid_password("aaaA_aa.a+a@a22a"))
        self.assertTrue(ValidationsInfosUsers.is_valid_password("aaaaaaaaa"))

"""
    def test_update_verify(self):
        with self.assertRaises(PseudoNotValid):
            update_verify("totototo", "totototo", "aa", "", "", "", "", "", "", "")
        with self.assertRaises(PseudoNotValid):
            update_verify("totototo", "totototo", "rachid007", "", "", "", "", "", "", "")
        with self.assertRaises(EmailNotValid):
            update_verify("totototo", "totototo", "", 2, "", "", "", "", "", "")
        with self.assertRaises(EmailNotValid):
            update_verify("totototo", "totototo", "", "tototo@student.ah", "", "", "", "", "", "")
        with self.assertRaises(NameNotValid):
            update_verify("totototo", "totototo", "", "", "aa", "", "", "", "", "")
        with self.assertRaises(NameNotValid):
            update_verify("totototo", "totototo", "", "", 2, "", "", "", "", "")
        with self.assertRaises(NameNotValid):
            update_verify("totototo", "totototo", "", "", "", "aa", "", "", "", "")
        with self.assertRaises(NameNotValid):
            update_verify("totototo", "totototo", "", "", "", 2, "", "", "", "")
        with self.assertRaises(PasswordNotValid):
            update_verify("totototo", "totototo", "", "", "", "", "aa", "", "", "")
        with self.assertRaises(PasswordsNotSame):
            update_verify("totototo", "totototo", "", "", "", "", "aaaaaaaa", "aaaaaaaaaaaaa", "", "")
        with self.assertRaises(SecurityQuestionNotCorrect):
            update_verify("totototo", "totototo", "", "", "", "", "", "", 2, "")
        with self.assertRaises(SecurityQuestionNotCorrect):
            update_verify("totototo", "totototo", "", "", "", "", "", "", "aa", "")
        with self.assertRaises(SecurityAnswerNotCorrect):
            update_verify("totototo", "totototo", "", "", "", "", "", "", "", 2)
        with self.assertRaises(SecurityAnswerNotCorrect):
            update_verify("totototo", "totototo", "", "", "", "", "", "", "", "aa")
        self.assertEqual(update_verify("totototo", "aaaaaaaaaa", "", "", "", "", "", "", "", ""),
                         "current Password not correct !")
        self.assertTrue(update_verify("totototo", "totototo", "", "", "", "", "", "", "zzzzzz", "qqqqqq"))
        self.assertTrue(
            update_verify("totototo", "totototo", "tototototo", "toto@gmail.com", "bbbbb", "ccccc", "dddddddd",
                          "dddddddd", "zzzzzz", "qqqqqq"))
"""

if __name__ == '__main__':
    unittest.main()
