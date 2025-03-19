import bisect
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        ans = 0
        last = -1001
        for a,b in sorted(pairs, key = lambda x: x[1]):
            if last < a:
                ans += 1
                last = b
        return ans
      """
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order."""

                

        
