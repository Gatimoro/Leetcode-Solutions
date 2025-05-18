# You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.

# Return the minimum number of swaps required to rearrange nums into this sorted order.

# A swap is defined as exchanging the values at two distinct positions in the array.


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def s(n):
            tot = 0 #Bruh moment
            while n:
                tot += n % 10
                n //= 10
            return tot

        indexed = list(enumerate(nums))
        indexed.sort(key=lambda x: (s(x[1]), x[1]))
    
        pos = [0] * len(nums)
        for new_index, (old_index, _) in enumerate(indexed):
            pos[old_index] = new_index

        visited = [False] * len(nums)
        tot = 0

        for i in range(len(nums)):
            if visited[i] or pos[i] == i:
                continue

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[j]
                cycle_size += 1

            if cycle_size > 1:
                tot += cycle_size - 1

        return tot  
