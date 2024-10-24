class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while n:
            if not m or nums2[-1]>nums1[m-1]: #if the greatest from nums2 is bigger than greatest from nums1, add it to the end
                nums1[-1+m+n]=nums2.pop()     #after that remove greatest from nums2
                n-=1                          #it can also be the case that we exhaust all nums1, in which case we have m=0
            else:                             #and we repeat the first if statement
                nums1[-1+m+n]=nums1[m-1]
                m-=1


