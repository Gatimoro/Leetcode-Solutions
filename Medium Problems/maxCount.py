class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned,length=sorted(banned)+[0],len(banned)
        tot=ans=b=0
        for x in range(1,n+1):
            if x!=banned[b]:
                tot+=x
                ans+=1
            else:
                while b<length and banned[b]==x:
                    b+=1
            if tot+1+x>maxSum:
                break
        return ans
            
        
                
