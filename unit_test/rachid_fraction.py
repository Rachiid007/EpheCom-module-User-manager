from math import gcd


def convertir_en_fraction(objet):
    """Convertit "int" en Fractions"""
    if isinstance(objet, int):
        return Fraction(objet)
    else:
        raise TypeError("l'Objet doit être de type int.")


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : November 2020
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num et den sont des entiers
        POST : sauvegarde num et den dans les proriétés numerator et denominator et
                crée la propriété pgcd qui est le plus grand commun diviseur
        RAISES : ZeroDivisionError si den == 0 et aussi si num et den != int
        """

        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("The numerator and denominator must be integers.")

        if den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être 0 !")

        self.__pgcd = gcd(num, den)

        self.__numerator = int(num / self.__pgcd)
        self.__denominator = int(den / self.__pgcd)

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @property
    def pgcd(self):
        return self.__pgcd

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : un objet fraction
        POST : Renvoit une chaine de caractères qui est la forme la plus réduite de la fraction
        """

        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return '%s/%s' % (round(self.__numerator / self.__pgcd), round(self.__denominator / self.__pgcd))

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : un objet fraction
        POST : Renvoit une chaine de caractères qui est la forme mixte de la fraction
        """
        reste = self.__numerator % self.__denominator
        nombre_entier = round((self.__numerator - reste) / self.__denominator)
        return f"""{nombre_entier} {reste}/{self.__denominator}"""

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : 2 objets fractions
         POST : renvoit un objet Fraction contenant le résultat de la somme des 2 fractions en forme réduite
         """
        if not isinstance(other, Fraction):
            other = convertir_en_fraction(other)

        if not self.__denominator == other.denominator:
            num = self.__numerator * other.denominator + other.numerator * self.__denominator
            den = self.denominator * other.denominator
            div = gcd(num, den)
            return Fraction(round(num / div), round(den / div))

        num = self.numerator + other.numerator
        div = gcd(num, self.__denominator)
        return Fraction(round(num / div), round(self.__denominator / div))

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : 2 objets fractions
        POST : renvoit un objet Fraction contenant le résultat de la différence des 2 fractions en forme réduite
        """
        if not isinstance(other, Fraction):
            other = convertir_en_fraction(other)

        if not self.__denominator == other.denominator:
            num = self.__numerator * other.denominator - other.numerator * self.__denominator
            den = self.denominator * other.denominator
            div = gcd(num, den)
            return Fraction(round(num / div), round(den / div))

        num = self.numerator - other.numerator
        div = gcd(num, self.__denominator)
        return Fraction(round(num / div), round(self.__denominator / div))

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : 2 objets fractions
        POST : renvoit un objet Fraction contenant le résultat du produit des 2 fractions en forme réduite
        """
        if not isinstance(other, Fraction):
            other = convertir_en_fraction(other)

        num = self.__numerator * other.numerator
        den = self.denominator * other.denominator
        div = gcd(num, den)
        return Fraction(round(num / div), round(den / div))

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : 2 objets fractions
        POST : renvoit un objet Fraction contenant le résultat du quotient des 2 fractions en forme réduite
        RAISES : ZeroDivisionError si other est une fraction nulle
        """
        if not isinstance(other, Fraction):
            other = convertir_en_fraction(other)

        if other.numerator == 0:
            raise ZeroDivisionError("Can't divide by 0")

        num = self.__numerator * other.denominator
        den = self.denominator * other.numerator
        div = gcd(num, den)
        return Fraction(round(num / div), round(den / div))

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : 2 objets fractions
        POST : renvoit un objet Fraction contenant le résultat de la fraction 1 puissance fraction 2 en forme réduite
        """
        if other.denominator == 1:
            power = other.numerator
            if power >= 0:
                return Fraction(self.numerator ** power,
                                self.denominator ** power)
            elif self.numerator >= 0:
                return Fraction(self.denominator ** -power,
                                self.numerator ** -power)
            else:
                return Fraction((-self.denominator) ** -power,
                                (-self.numerator) ** -power)
        else:
            # A fractional power will generally produce an
            # irrational number.
            return float(self) ** float(other)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : 2 objets fractions
        POST : renvoit true si les 2 fractions sont équivalentes et false dans le cas contraire
        """
        if not isinstance(other, Fraction):
            other = convertir_en_fraction(other)

        return self.__numerator == other.numerator and self.__denominator == other.denominator

    def __float__(self):
        """Returns the decimal value of the fractions

        PRE : un objet fraction
        POST : renvoit la fraction sous forme décimal
        """
        return self.__numerator / self.__denominator

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : un objet fraction
        POST : renvoit true si la fraction vaut 0 et false dans le cas contraire
        """
        return self.__numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : un objet fraction
        POST : renvoit true si la simplification de la fraction est un integer et false dans le cas contraire
        """
        var = self.__numerator / self.__denominator

        return var - int(var) == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : un objet fraction
        POST : renvoit true si la valeur absolue de la fraction < 1 et false dans le cas contraire
        """
        return abs(self.__numerator / self.__denominator) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : un objet fraction
        POST : renvoit true si le numérateur de la simplification de la fraction ==  1 et false dans le cas contraire
        """
        return round(self.__numerator / self.__pgcd) == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : other est un objets Fraction
        POST : renvoit True si la différence entre la Fraction courante et l'autre Fraction est une Fraction unitaire.
        """
        if not isinstance(other, Fraction):
            other = convertir_en_fraction(other)

        common_num = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        common_denom = self.denominator * other.denominator
        div = gcd(common_num, common_denom)
        return common_num / div == 1

        # return (self - other).numerator == 1 and not (self - other).denominator == 1
