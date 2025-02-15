class Solution:#certainly one of my worst solutions so far. I definetly missed something. There is no way that the acceptance is actually 81%.
    def punishmentNumber(self, n: int) -> int:
        ans=0
        def check(num):
            s= str(num*num)
            bong = deque([(0,0)])
            power=len(str(num))
            while bong:
                cur, last_ind = bong.pop()
                for jump in range(1,power+1):
                    if last_ind>=len(s):break
                    new = cur + int(s[last_ind:last_ind + jump])
                    if new <= num:
                        bong.append((new, last_ind + jump))
                    if new==num and last_ind+jump == len(s):
                        return num*num
            return 0
        for num in range(9,n+1):
            ans+=check(num)
        return ans+1
"""Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

1 <= i <= n
The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i."""
