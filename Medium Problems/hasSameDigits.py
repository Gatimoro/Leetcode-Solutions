# You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:

# For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
# Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
# Return true if the final two digits in s are the same; otherwise, return false.
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        if n == 2:
            return s[0] == s[1]
        
        row = [1]
        for _ in range(n - 2):
            new_row = [1]
            for i in range(len(row) - 1):
                new_row.append((row[i] + row[i + 1]) % 10)
            new_row.append(1)
            row = new_row
        
        digits = [int(c) for c in s]
        
        left_sum = sum(digits[i] * row[i] for i in range(n - 1)) % 10
        right_sum = sum(digits[i + 1] * row[i] for i in range(n - 1)) % 10
        
        return left_sum == right_sum


