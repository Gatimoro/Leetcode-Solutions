# You are given an integer array nums and an integer goal.

# You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

# Return the minimum possible value of abs(sum - goal).

# Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        nums.sort()
        best = abs(goal)
        sums = set([0])
        sums2 = set([0])
        for n in nums[:len(nums) // 2]:
            sums.update([n + s for s in sums])
            # print(sums)
        for n in nums[len(nums) // 2:]:
            sums2.update([n + s for s in sums2])
            # print(sums2)
        right = sorted(sums2)
        def find_closest(n, right):
            l, r = 0, len(right) - 1
            while l < r:
                m = (l+r+1)//2
                val = right[m]
                if val == n:
                    return 0
                elif val < n:
                    l = m
                else:
                    r = m - 1 
            # print(right)
            # print(n, right[l])

            # print(abs(n - right[l]), abs(n - right[min(l+1, len(right) - 1)]))
            return min(abs(n - right[l]), abs(n - right[min(l+1, len(right) - 1)]))          
        
        #now weh ave 2 sorted lists with the possible sums of the right and the left sides, now i'll just check every combination
        for gul in sums:
            best = min(best, find_closest(goal - gul, right))
            # print(best)
        return best
