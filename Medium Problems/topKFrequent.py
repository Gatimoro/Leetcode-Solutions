import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=defaultdict(int)
        z=defaultdict(list)
        for num in nums:
            c[num]+=1
            z[c[num]].append(num)
        x=random.choice(list(z.values()))
        while len(x)!=k:x=random.choice(list(z.values()))
        return x
"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order."""
