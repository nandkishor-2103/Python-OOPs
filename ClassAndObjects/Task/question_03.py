class Computation:

    def __init__(self):
        pass

    def Factorial(self, n):
        def factorial(n):
            if n == 1:
                return 1

            return n * factorial(n-1)

        return factorial(n)

    # 2. Sum of first n natural numbers
    def naturalSum(self, n):
        return (n *(n + 1))/2

    # 3. Check whether n is prime
    def testPrime(self, n):
        if n < 2 or n % 2 == 0:
            return False

        # Check odd factors up to the square root of n
        for i in range(3, (n**0.5)+1, 2):
            if n % i == 0:
                return False

        return True

    # 4. Check whether two numbers are prime to each other
    #    (Coprime)
    def testPrims(self, a, b) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return gcd(a, b) == 1

    # 5. Display multiplication table of a number
    def tableMult(self, n):
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)

    # 6. Display multiplication tables from 1 to 9
    def allTablesMult(self):

        for n in range(1, 10):
            print("\nTable of", n)

            self.tableMult(n)
