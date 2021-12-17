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
        with self.assertRaises(PseudoNotValid):
            update_verify("aaaaa","aaaaa","aa","","","","","","","")
        with self.assertRaises(PseudoNotValid):
            update_verify("aaaaa","aaaaa","tototo","","","","","","","")
        with self.assertRaises(EmailNotValid):
            update_verify("aaaaa","aaaaa","",2,"","","","","","")
        with self.assertRaises(EmailNotValid):
            update_verify("aaaaa","aaaaa","","tototo@students.ephec.be","","","","","","")
        with self.assertRaises(NameNotValid):
            update_verify("aaaaa","aaaaa","","","aa","","","","","")
        with self.assertRaises(PseudoNotValid):
            update_verify("aaaaa","aaaaa","","",2,"","","","","")
        with self.assertRaises(NameNotValid):
            update_verify("aaaaa","aaaaa","","","","aa","","","","")
        with self.assertRaises(PseudoNotValid):
            update_verify("aaaaa","aaaaa","","","",2,"","","","")
        with self.assertRaises(PasswordNotValid):
            update_verify("aaaaa","aaaaa","","","","","aa","","","")
        with self.assertRaises(PasswordsNotSame):
            update_verify("aaaaa","aaaaa","","","","","aaaaaaaa","aaaaaaaaaaaaa","","")
        with self.assertRaises(SecurityQuestionNotCorrect):
            update_verify("aaaaa","aaaaa","","","","","","",2,"")
        with self.assertRaises(SecurityQuestionNotCorrect):
            update_verify("aaaaa","aaaaa","","","","","","","aa","")
        with self.assertRaises(SecurityAnswerNotCorrect):
            update_verify("aaaaa","aaaaa","","","","","","","",2)
        with self.assertRaises(SecurityAnswerNotCorrect):
            update_verify("aaaaa","aaaaa","","","","","","","","aa")
        self.assertEqual(update_verify("aaaaa","aaaaaaaaaa","","","","","","","",""), "current Password not correct !")
        self.assertTrue(update_verify("aaaaa","aaaaa","","","","","","","",""))

if __name__ == '__main__':
    unittest.main()
