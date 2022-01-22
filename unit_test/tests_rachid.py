import unittest
from Classes.Users import *


class RachidTest(unittest.TestCase):

    def setUp(self):
        self.Uop = UsersOperations()
        self.viU = ValidationsInfosUsers()

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


if __name__ == '__main__':
    unittest.main()
