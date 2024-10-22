class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]      this is one of those that took too long,
        :rtype: List[List[int]]        I kept having problems so i ended up using eval.
        """
        numa=[]
        def add(num,arr):
            if len(arr)==1:
                numa.append(eval('['+str(arr[0])+num+']'))
                return
            else:
                for n in range(len(arr)):
                    add(num+','+str(arr[n]),arr[:n]+arr[n+1:])
        add('',nums)
        return numa
