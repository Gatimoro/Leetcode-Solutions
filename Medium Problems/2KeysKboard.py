class Solution:
    def minSteps(self, n: int) -> int:
        i,ans=2,-1
        while n>1:#if we have a starting number Strt and we want to get to Prime*Strt, we need to apply #Prime operations. If we have the prime factorization of the number we can simply add the primes and correct with a -1 to directly get the answer.
            if not n%i:
                n//=i
                ans+=i
                continue
            i+=1
        return ans+n
