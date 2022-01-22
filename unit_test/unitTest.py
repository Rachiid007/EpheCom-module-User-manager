from rachid_fraction import Fraction
import unittest


class FractiontTest(unittest.TestCase):

    def test_Fraction_is_instance_of_Fraction(self):
        self.assertIsInstance(Fraction(1, 2), Fraction, "pas une class Fraction")

    def test_init(self):
        """ Test the __init__ """
        fractionTest = Fraction(1, 2)
        self.assertEqual(fractionTest.numerator, 1)
        self.assertEqual(fractionTest.denominator, 2)

    def test_init_error(self):
        """ Test __init__ when denominator is zero """
        with self.assertRaises(ZeroDivisionError):
            Fraction(9, 0)

    def test_str(self):
        """ Test __str__ """
        fraction = Fraction(5, 9)
        self.assertEqual(str(fraction), '5/9')

    # *** *** *** Testing overload operators *** *** ***

    def test_add(self):
        """ test the + operation """
        self.assertEqual(Fraction(1, 2) + Fraction(4, 4), Fraction(3, 2), "1/2 + 4/4 = 3/2")
        self.assertEqual(Fraction(1, 2) + Fraction(-4, 4), Fraction(-1, 2), "1/2 + -4/4 = -1/2")
        self.assertEqual(Fraction(1, 2) + Fraction(4, 1), Fraction(9, 2), "1/2 + 4/1 = 9/2")
        self.assertEqual(Fraction(1, 2) + Fraction(0, 1), Fraction(1, 2), "1/2 + 0 = 1/2")
        self.assertEqual(Fraction(1, 2) + Fraction(1, 1), Fraction(3, 2), "1/2 + 1 = 3/2")

        # self.assertEqual(Fraction(1, 2) + Fraction(4, 0), ZeroDivisionError, "1/2 + 4/0 = ERROR: division by 0 !")

    def test_minus(self):
        """ test the - operation """
        self.assertEqual(Fraction(4, 5) - Fraction(1, 2), Fraction(3, 10), "4/5 - 1/2 = 3/10")
        self.assertEqual(Fraction(1, 2) - Fraction(1, 2), Fraction(0, 1), "1/2 - 1/2 = 0")
        self.assertEqual(Fraction(1, 2) - Fraction(3, 2), Fraction(-1, 1), "1/2 - 3/2 = -1")
        self.assertEqual(Fraction(3, 2) - Fraction(1, 1), Fraction(1, 2), "3/2 - 1 = 1/2")

        # self.assertEqual(Fraction(1, 2) - Fraction(4, 0), ZeroDivisionError, "1/2 - 4/0 = ERROR: division by 0 !")

    def test_times(self):
        """ test the * operation """
        self.assertEqual(Fraction(1, 2) * Fraction(1, 2), Fraction(1, 4), "1/2 * 1/2 = 1/4")
        self.assertEqual(Fraction(1, 2) * Fraction(-1, 2), Fraction(-1, 4), "1/2 * 1/2 = -1/4")
        self.assertEqual(Fraction(1, 2) * Fraction(0, 1), Fraction(0, 1), "1/2 * 0 = 0")
        self.assertEqual(Fraction(1, 2) * Fraction(1, 1), Fraction(1, 2), "1/2 * 1 = 1/2")
        # self.assertEqual(Fraction(1, 2) * Fraction(4, 0), ZeroDivisionError, "1/2 * 4/0 = ERROR: division by 0 !")

    def test_divide(self):
        """ test the / operation """
        self.assertEqual(Fraction(3, 2) / Fraction(1, 2), Fraction(3, 1), "3/2 / 1/2 = 3")
        self.assertEqual(Fraction(1, 2) / Fraction(1, 2), Fraction(1, 1), "1/2 / 1/2 = 1")
        self.assertEqual(Fraction(1, 2) / Fraction(-1, 2), Fraction(1, -1), "1/2 / -1/2 = -1")
        self.assertEqual(Fraction(-1, 2) / Fraction(-1, 2), Fraction(-1, -1), "1/2 / -1/2 = 1")
        self.assertEqual(Fraction(-3, 2) / Fraction(-1, 2), Fraction(-3, -1), "-3/2 / -1/2 = 3")
        self.assertEqual(Fraction(1, 2) / Fraction(1, 1), Fraction(1, 2), "1/2 / 1 = 1/2")

        # self.assertEqual(Fraction(1, 2) / Fraction(4, 0), ZeroDivisionError, "1/2 / 4/0 = ERROR: division by 0 !")

    def test_power(self):
        """ test the ** operation """
        self.assertEqual(Fraction(1, 2) ** Fraction(1, 2), 0.7071067811865476, "1/2 ** 1/2 = 0.71")
        self.assertEqual(Fraction(1, 2) ** Fraction(-1, 2), 1.4142135623730951, "1/2 ** -1/2 = 1.41")
        self.assertEqual(Fraction(1, 2) ** Fraction(0, 1), 1, "1/2 ** 0 = 1")
        self.assertEqual(Fraction(1, 2) ** Fraction(1, 1), Fraction(1, 2), "1/2 ** 1 = 1/2")

    def test_eq(self):
        """ test the == operation """
        self.assertEqual(Fraction(1, 2) == Fraction(3, 4), True, "1/2 == 1/2 => True")
        self.assertEqual(Fraction(1, 2) == Fraction(-1, 2), False, "1/2 == -1/2 => False")
        self.assertEqual(Fraction(1, 2) == Fraction(3, 2), False, "1/2 == 3/2 => False")
        self.assertEqual(Fraction(4, 3) == Fraction(1, 2), False, "4/3 == 1/2 => False")

    def test_floot(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5, "1/2 = 0.5")
        self.assertEqual(float(Fraction(1, 4)), 0.25, "1/4 = 0.25")
        self.assertEqual(float(Fraction(1, 3)), 0.3333333333333333, "1/2 = 0.5")
        self.assertEqual(float(Fraction(0, 1)), 0.0, "0 = 0.0")
        self.assertEqual(float(Fraction(1, 1)), 1.0, "1 = 1.0")
        self.assertEqual(float(Fraction(-2, 3)), -0.6666666666666666, "-2/3 = -0.6")

    # *** *** *** Checking the test property *** *** ***

    def test_is_zero(self):
        self.assertEqual(Fraction(1, 2).is_zero(), False, "1/2 != 0")
        self.assertEqual(Fraction(-1, 2).is_zero(), False, "-1/2 != 0")
        self.assertEqual(Fraction(0, 2).is_zero(), True, "0/2 == 0")
        self.assertEqual(Fraction(0, 100).is_zero(), True, "0/100 == 0")

    def test_is_integer(self):
        self.assertEqual(Fraction(1, 2).is_integer(), False, "1/2 = 0.5")
        self.assertEqual(Fraction(10, 5).is_integer(), True, "10/5 = 2")
        self.assertEqual(Fraction(-6, 2).is_integer(), True, "-6/2 = -3")
        self.assertEqual(Fraction(3, 1).is_integer(), True, "3 = 3 -> int")
        self.assertEqual(Fraction(1, 1).is_integer(), True, "1 = 1")
        self.assertEqual(Fraction(0, 1).is_integer(), True, "0 = int")

    def test_is_proper(self):
        self.assertEqual(Fraction(1, 2).is_proper(), True, "1/2 < 1")
        self.assertEqual(Fraction(1, 4).is_proper(), True, "1/4 < 1")
        self.assertEqual(Fraction(-2, 3).is_proper(), True, "-2/3 < 1")
        self.assertEqual(Fraction(1, 1).is_proper(), False, "1 == 1")
        self.assertEqual(Fraction(0, 1).is_proper(), True, "0 < 1")

    def test_is_unit(self):
        self.assertEqual(Fraction(1, 2).is_unit(), True, "1/2 unit")
        self.assertEqual(Fraction(2, 3).is_unit(), False, "2/3 no unit")
        self.assertEqual(Fraction(-1, 2).is_unit(), False, "-1/2 no unit")
        self.assertEqual(Fraction(1, 42).is_unit(), True, "1/42 unit")
        self.assertEqual(Fraction(1, 1).is_unit(), True, "1 unit")
        self.assertEqual(Fraction(0, 1).is_unit(), False, "0 no unit")

    def test_is_adjacent_to(self):
        self.assertEqual(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)), True, "1/3 et 1/2 = adjacent")
        self.assertEqual(Fraction(1, 3).is_adjacent_to(Fraction(1, 4)), True, "1/3 et 1/4 = 1/12 adjacent")
        self.assertEqual(Fraction(1, 2).is_adjacent_to(Fraction(1, 5)), False, "1/2 et 1/5 = 3/10 no adjacent")


if __name__ == '__main__':
    unittest.main()
