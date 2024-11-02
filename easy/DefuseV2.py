class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]                 THIS TIME IT WORKED BETTER
        :type k: int
        :rtype: List[int]
        """
        n=len(code)
        acc=code+code
        if k==0:
            return [0,]*n
        elif k<0:
            code[0]=sum(code[n+k:])
            for i in range(n-1):
                code[i+1]=(code[i]+acc[i+n]-acc[n+i+k])
        else:
            code[0]=sum(code[1:k+1])
            for i in range(1,n):
                code[i]=(code[i-1]-code[i]+acc[k+i])
        return code
