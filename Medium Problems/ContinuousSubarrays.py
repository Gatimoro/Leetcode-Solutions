class Solution:"""THIS SOLUTION IS NOT MY BEST WORK. IM CURRENTLY WORKING ON MY V2"""
    def continuousSubarrays(self, nums: List[int]) -> int:
        counter=Counter()
        counter[nums[0]]=1
        ans,cur,count=1,0,1
        for x in range(1,len(nums)):
            if nums[x]<min(counter)-2 or nums[x]>max(counter)+2:
                counter.clear()
                counter[nums[x]]=1
                count=1
                cur=x
            else:
                while count and (max(counter)>nums[x]+2 or min(counter)<nums[x]-2):
                    counter[nums[cur]]-=1
                    if not counter[nums[cur]]:
                        counter.pop(nums[cur])
                    cur+=1
                    count-=1
                count+=1
                counter[nums[x]]+=1
            ans+=count
        return ans
    """DESCRIPTION: You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array."""
                        
