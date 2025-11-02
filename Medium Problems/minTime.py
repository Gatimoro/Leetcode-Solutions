# You are given two integer arrays of size 2: d = [d1, d2] and r = [r1, r2].

# Two delivery drones are tasked with completing a specific number of deliveries. Drone i must complete di deliveries.

# Each delivery takes exactly one hour and only one drone can make a delivery at any given hour.

# Additionally, both drones require recharging at specific intervals during which they cannot make deliveries. Drone i must recharge every ri hours (i.e. at hours that are multiples of ri).

# Return an integer denoting the minimum total time (in hours) required to complete all deliveries.
class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        if r[0] == r[1]:
            tasks = sum(d)
            charges = tasks // (r[0] - 1)
            rem = tasks % (r[0] - 1)
            return charges * r[0] - 1 if rem == 0 else charges * r[0] + rem
        def work(t):
            dead = t // (r[0] * r[1] // gcd(r[0], r[1])) # both dead
            
            work1, work2 = (t // r[1]) - dead, (t // r[0]) - dead
            total = t - (dead + work1 + work2)
            # print(work1, work2, dead, total, t)
            return total >= max(d[0] - work1, 0) + max(d[1] - work2, 0)
        left = 0
        right = max(max(d)**2,12)
        # print(work(3))
        while left < right:
            mid = (left + right) // 2
            if work(mid):
                right = mid
            else:
                left = mid + 1
        
        return right
        
