
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n # create a list of n elements, all True
        is_prime[0] = is_prime[1] = False # 0 and 1 are not prime numbers

        for i in range(2, int(n ** 0.5) + 1): # iterate from 2 to square root of n
            if is_prime[i]: # if i is a prime number
                for j in range(i * i, n, i): # iterate from i^2 to n with step i
                    is_prime[j] = False # mark all multiples of i as False

        return sum(is_prime)
