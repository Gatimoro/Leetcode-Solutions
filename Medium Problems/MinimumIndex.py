class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        majo = nums[0]
        xcount = 0
        for num in nums:
            xcount += 1 if num == majo else -1
            if not xcount: 
                majo = num
                xcount= 1

        tcount = nums.count(majo)
        length = len(nums)
        # if tcount == (length >> 1) + 1:
        #     return -1
        lcount = 0
        for i, num in enumerate(nums):
            if num != majo: continue
            lcount += 1
            left_size, right_size = i + 1, length - i - 1
            if (left_size>> 1) < lcount and (right_size>> 1) < tcount - lcount:
                return i
        return -1
"""An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.

You are given a 0-indexed integer array nums of length n with one dominant element.

You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:

0 <= i < n - 1
nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.
Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, both ends being inclusive. Particularly, if j < i then nums[i, ..., j] denotes an empty subarray.

Return the minimum index of a valid split. If no valid split exists, return -1."""
