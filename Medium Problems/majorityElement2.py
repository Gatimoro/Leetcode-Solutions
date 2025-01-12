class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        minimum = len(nums)//3 +1;
        ans=[];
        for num in set(nums):
            if nums.count(num)>=minimum:
                ans.append(num);
        return ans;
"""find the elements that appear more than a third of the array length"""
