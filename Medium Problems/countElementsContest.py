# You are given an integer array nums of length n and an integer k.

# An element in nums is said to be qualified if there exist at least k elements in the array that are strictly greater than it.

# Return an integer denoting the total number of qualified elements in nums.
class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        remaining = len(nums)
        total = 0
        for n, val in sorted(list(c.items())):
            # print(n,val)
            remaining -= val
            if remaining >= k:
                total += val
        return total
