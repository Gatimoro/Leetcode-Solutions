# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ansa = []
        seen = set()
        added = 0
        for i, n in enumerate(nums):
            for seq in ansa.copy():
                if seq[-1] <= n and str(seq +[n]) not in seen:
                    seen.add(str(seq+[n]))
                    added += 1
                    ansa.append(seq + [n])
            if str(n) not in seen:
                added += 1
                ansa.append([n])
                seen.add(n)
            # print(ansa)
            # print(added)
        return [x for x in ansa if len(x) >= 2]
