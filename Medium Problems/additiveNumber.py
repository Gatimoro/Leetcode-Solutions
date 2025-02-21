class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def check(p1, p2, i):
            ls = str(p1 + p2)
            if len(ls)+i>len(num) or ls != num[i:i+len(ls)]:
                return False
            elif len(ls)+i == len(num): return True
            return check(p2, int(ls), i+len(ls))
        if num[0]=='0':
            for bracket in range(2,len(num)):
                b = int(num[1:bracket])
                if check(0,b,bracket): return True
        else:
            for split in range(1,len(num)):
                a=int(num[:split])
                if num[split] == '0':
                    if check(a,0,split+1):return True
                    continue
                for bracket in range(split+1,len(num)):
                    b = int(num[split:bracket])
                    if check(a,b,bracket): return True
        return False
"""An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid."""
