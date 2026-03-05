# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.
class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i, n in enumerate(s):
            count += i & 1 ^ int(n)
        return min(count, len(s) - count)
