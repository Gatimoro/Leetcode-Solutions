# You are given an integer num.

# A number num is called a Complete Prime Number if every prefix and every suffix of num is prime.

# Return true if num is a Complete Prime Number, otherwise return false.

# Note:

# A prefix of a number is formed by the first k digits of the number.
# A suffix of a number is formed by the last k digits of the number.
# Single-digit numbers are considered Complete Prime Numbers only if they are prime.
from functools import lru_cache
class Solution:
    def completePrime(self, num: int) -> bool:
        @lru_cache()
        def is_prime(num):
            if num == 1: return False
            for n in range(2, int(num**0.5 + 1)):
                if num % n == 0:
                    return False
            return True
        s = str(num)
        for i in range(len(s)):
            if not is_prime(int(s[:i+1])) or not is_prime(int(s[i:])):
                return False
        return True
