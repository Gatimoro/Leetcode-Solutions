class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        if len(flowerbed)<3:
            if not 1 in flowerbed:
                return n<2
            return False
        c=0
        count=deque([])
        maximum=0
        maximum+=1 if not(flowerbed[0] or flowerbed[1]) else 0
        maximum+=1 if not(flowerbed[-2] or flowerbed[-1]) else 0
        
        for p in flowerbed[1:-1]:
            if c and p:
                count.append(c)
                c=0
            else:
                c+=1
        count.append(c)
        while maximum<n and count: 
            f=count.pop()
            if f >= 3:
                maximum += (f-1)//2

        return maximum >= n
"""DESCRIPTION:
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating 
the no-adjacent-flowers rule and false otherwise.
