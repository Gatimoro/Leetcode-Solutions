class Solution:
    def climbStairs(self, n: int) -> int:#The first step is either a 1 or a 2 so the combinations with n steps is the same as combinations with n-1 steps + combinations with n-2 steps. Fibonacci sequence arises.
        return int(((5**0.5/2+0.5)**(n+1))/(5**0.5)+0.5)
