class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]                 PRETTY BAD IF YOU ASK ME
        :type k: int
        :rtype: List[int]
        """
        n=len(code)
        ansa=[]
        if k==0:
            return [0,]*n
        elif k<0:
            ansa.append(sum(code[n+k:]))
            for i in range(n-1):

                ansa.append(ansa[i]-code[k+i]+code[i])
        else:
            ansa.append(sum(code[1:k+1]))
            for i in range(1,n):
                ansa.append(ansa[i-1]-code[i]+code[(i+k)%n])
        return ansa
                
