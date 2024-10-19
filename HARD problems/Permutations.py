class Solution(object):
    def getPermutation(self, n, k):
        """             THIS WAS MY FIRST HARD PROBLEM AND I BEAT 100% OF ATTEMPTS, I'M ECSTATIC!
        :type n: int    
        :type k: int
        :rtype: str
        """
        sett=[] #initialize sett and ans
        k-=1 #remove 1 from k to make calculations cleaner
        ans=''
        for n in range(1,n+1):#add numbers up to n to an array
            sett.append(n)
        #at each step we select the apropriate index, we have n choices for ans[0] and n! total permutations,
        #which means that the bottom 1/n percentile of permutations will start with sett[0], between 1/n and 2/n
        #percentile will all start with sett[1] and so on. After noticing this fact I came up with the following algorithm
        for i in range(n-1): 
            n-=1
            b=k//math.factorial(n)#b calculates how many times we 'go over' 1/n
            k=k%math.factorial(n)#once we 'go over' 1/n b times, we re-evaluate k to be the remainder
            ans+=str(sett.pop(b))#we went over 1/n b times so our index is b, if we had went 0 times, it means we're at the bottom pecentile and we take the lowest value
        return ans+str(sett[0])#lastly we add the remaining element is sett        
