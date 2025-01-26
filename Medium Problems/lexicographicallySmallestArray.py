"""You are given a 0-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10."""
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        with_index = sorted(((x,i) for i,x in enumerate(nums)))
        groups=[]
        i=0
        while i < len(nums):
            groups.append([[with_index[i][1]],with_index[i][0]])
            i+=1
            while i<len(nums) and with_index[i][0]-groups[-1][-1]<=limit:
                groups[-1].append(with_index[i][0])
                groups[-1][0].append(with_index[i][1])
                i+=1
        for group in groups:
            for ingroup, innums in enumerate(sorted(group[0]), start=1):
                nums[innums] = group[ingroup]
        return nums
