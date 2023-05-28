

class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            raise ValueError("Invalid number")
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot add two elements of different field orders")
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot multiply two elements of different field orders")
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        # Perform exponentiation using Fermat's Little Theorem
        # Note: Assumes prime is a prime number
        exponent = exponent % (self.prime - 1)
        num = pow(self.num, exponent, self.prime)
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        num = (self.num - other.num) % self.prime
        # we return an element of the same class
        return self.__class__(num, self.prime)
