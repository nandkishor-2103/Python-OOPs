# ! ===========================================
# !         CUSTOM DATATYPE CREATION
# ! ===========================================

# * Custom Datatype: Fraction
class Fraction:
    # parametrized constructor
    def __init__(self, numerator, denominator):
        """Required two parameter to initalize the object that is numerator and denominator"""
        self.numerator = numerator
        self.denominator = denominator

    # method to return the string representation of the object
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Method to add two fraction objects"""
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Method to subtract two fraction objects"""
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """Method to multiply two fraction objects"""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """Method to divide two fraction objects"""
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def convert_to_decimal(self):
        """Method to convert fraction to decimal"""
        return self.numerator / self.denominator


fr1 = Fraction(3, 4)
fr2 = Fraction(1, 2)
print(fr1.convert_to_decimal())
print(f"Addition of two fractions ({fr1} + {fr2}) = {fr1 + fr2}")
print(f"Subtraction of two fractions ({fr1} - {fr2}) = {fr1 - fr2}")
print(f"Multiplication of two fractions ({fr1} * {fr2}) = {fr1 * fr2}")
print(f"Division of two fractions ({fr1} / {fr2}) = {fr1 / fr2}")
