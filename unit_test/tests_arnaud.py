import unittest
from unit_test.Users import *


class ArnaudTests(unittest.TestCase):
    def test_is_valid_pseudo(self):
        #   TYPE
        with self.assertRaises(PseudoNotValid):
            ValidationsInfosUsers().is_valid_pseudo(12345)
        with self.assertRaises(PseudoNotValid):
            ValidationsInfosUsers().is_valid_pseudo([12])
        with self.assertRaises(PseudoNotValid):
            ValidationsInfosUsers().is_valid_pseudo(
                {"hello": "yo", "hell": "yo", "ello": "yo", "helo": "yo", "hllo": "yo"})
        self.assertTrue(ValidationsInfosUsers().is_valid_pseudo("ChaosArnhug"))

        #   Length
        with self.assertRaises(PseudoNotValid):
            ValidationsInfosUsers().is_valid_pseudo("Aaa")

        #   Empty str
        with self.assertRaises(PseudoNotValid):
            ValidationsInfosUsers().is_valid_pseudo("")

    def test_is_valid_security_question(self):
        #   TYPE
        with self.assertRaises(SecurityQuestionNotCorrect):
            ValidationsInfosUsers().is_valid_security_question(123)
        with self.assertRaises(SecurityQuestionNotCorrect):
            ValidationsInfosUsers().is_valid_security_question([12])
        with self.assertRaises(SecurityQuestionNotCorrect):
            ValidationsInfosUsers().is_valid_security_question(
                {"hello": "yo", "hell": "yo", "heo": "yo", "helo": "yo", "hllo": "yo"})
        self.assertTrue(ValidationsInfosUsers().is_valid_security_question("Couleur chat"))

        #   Length
        with self.assertRaises(SecurityQuestionNotCorrect):
            ValidationsInfosUsers().is_valid_security_question("test")
        with self.assertRaises(SecurityQuestionNotCorrect):
            ValidationsInfosUsers().is_valid_security_question(
                "testtesttesttesttesttesttesttesttesttesttesttesttesttest")

        #   Empty str
        with self.assertRaises(SecurityQuestionNotCorrect):
            ValidationsInfosUsers().is_valid_security_question("")

    def test_is_valid_security_answer(self):
        #   TYPE
        with self.assertRaises(SecurityAnswerNotCorrect):
            ValidationsInfosUsers().is_valid_security_answer(123)
        with self.assertRaises(SecurityAnswerNotCorrect):
            ValidationsInfosUsers().is_valid_security_answer([12])
        with self.assertRaises(SecurityAnswerNotCorrect):
            ValidationsInfosUsers().is_valid_security_answer(
                {"hello": "yo", "hell": "yo", "heo": "yo", "helo": "yo", "hllo": "yo"})
        self.assertTrue(ValidationsInfosUsers().is_valid_security_answer("Il est noir"))

        #   Length
        with self.assertRaises(SecurityAnswerNotCorrect):
            ValidationsInfosUsers().is_valid_security_answer("test")
        with self.assertRaises(SecurityAnswerNotCorrect):
            ValidationsInfosUsers().is_valid_security_answer(
                "testtesttesttesttesttesttesttesttesttesttesttesttesttest")

        #   Empty str
        with self.assertRaises(SecurityAnswerNotCorrect):
            ValidationsInfosUsers().is_valid_security_answer("")

    def test_password_encryption(self):
        self.assertEqual(ValidationsInfosUsers().password_encryption("bonjour"),
                         "3041edbcdd46190c0acc504ed195f8a90129efcab173a7b9ac4646b92d04cc80005"
                         "acaa3554f4b1df839eacadc2491cb623bf3aa6f9eb44f6ea8ca005821d25d")

        self.assertNotEqual(ValidationsInfosUsers().password_encryption("bonjour"), "bonjour")
