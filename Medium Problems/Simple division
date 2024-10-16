class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans=''
        carry=''
        #determine the sign of the result
        neg=False
        if divisor<0:
            neg=not neg
        if dividend<0:
            neg=not neg

        #If the divisor is greater than the dividend, directly return 0
        sor=abs(divisor)
        end=abs(dividend)
        if sor>end:
            return 0
        
        #algorithm for simple division that we all learn in middle school.
        for stringlet in str(end):
            subquotient=0
            last=int(carry+stringlet)
            while last>=sor:
                last-=sor
                subquotient+=1
            carry=str(last)
            ans+=str(subquotient)

        #if the quotient is out of range, return approximation
        if not -2147483649<int (ans)<2147483648:
            if neg:
                return -2147483648      
            return 2147483647
        
        #if the answer is in range and nonzero, return it with it's sign.
        if neg:
            return -int(ans)
        return int(ans)
