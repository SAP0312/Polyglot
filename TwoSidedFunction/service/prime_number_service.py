import math


class PrimeNumberCheck:

    # function to check if a number is prime number
    def is_prime(self,number):
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False;
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i = i + 6

        return True

    # function to check if a number is two sided prime number
    def is_two_sided_prime(self, number):
        num = number
        n = 0
        while num > 0:
            if not self.is_prime(num):
                return False
            n = n + 1
            num = num // 10
        num = number
        n -= 1
        while n > 0:
            num = num % math.pow(10, n)
            if not self.is_prime(num):
                return False
            n -= 1
        return True
