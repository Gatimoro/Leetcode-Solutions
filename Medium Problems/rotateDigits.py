class Solution:

    def rotatedDigits(self, n: int) -> int:
        good = set(['7','4','3'])
        changing = set(['2','5','6','9'])
        ans = 0
        for i in range(n+1):
            found=False
            for dig in str(i):
                if dig in changing:
                    found = True
                elif dig in good:
                    found = False
                    break
            if found:
                ans+=1
        return ans
"""An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].

 """
