class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        wigga=True
        ans=[]
        for num in nums:
            if wigga:
                times = num
            else:
                ans+=times*[num]
            wigga=not wigga
        return ans
"""remove duplicates from linked list""
