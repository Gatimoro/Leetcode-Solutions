class Solution:
    def intToRoman(self, num: int) -> str:
        ans=''
        ref=['M',1000,'D',500,'C',100,'L',50,'X',10,'V',5,'I',1]
        for i in range(7):
            n=num//ref[1+i*2]
            if (n==4):
                if ans and ans[-1]==ref[(i-1)*2]:
                    ans=ans[:-1]+ref[i*2]+ref[(i-2)*2]
                else:
                    ans+=(ref[i*2]+ref[(i-1)*2])
            else:
                ans+=ref[i*2]*n
            num=num%ref[1+i*2]
        return ans
