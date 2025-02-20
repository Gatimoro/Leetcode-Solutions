class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(map(lambda x: int(x,2), nums))
        curr = 0
        while curr in seen:
            curr+=1
        return bin(curr)[2:].zfill(len(nums))
"""Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them."""
