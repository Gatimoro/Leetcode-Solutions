class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def bits(num):
            if num==0:
                return 0,0
            elif num==-1:
                return 1
            leng, bit = bits(num>>1)
            return 1 + leng, (num & 1) + bit
        
        leng1, bit1 = bits(num1)
        leng2, bit2 = bits(num2)
        if bit2==bit1:
            return num1
        elif bit2>bit1:
            start=1
            for _ in range(bit2-bit1):
                while num1 & start!=0:
                    start<<=1
                num1+=start
                start<<1
            return num1
        else:
            start=2**leng1
            ans=0
            for _ in range(bit2):
                while num1&start==0:
                    start>>=1
                ans+=start
                start>>=1
            return ans
"""Given two positive integers num1 and num2, find the positive integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation."""
