# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for a in nums:
            divs = set()
            for i in range(1, int(a**0.5 + 1)):
                d, remainder = divmod(a, i)
                if not remainder:
                    divs.add(d)
                    divs.add(i)
                    if len(divs) > 4:
                        break
            if len(divs) == 4: total += sum(divs)
        return total
