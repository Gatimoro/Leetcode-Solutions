import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        tot=sum(gifts)
        l=[-x for x in gifts]
        heapq.heapify(l)
        for rob in range(k):
            a=-heapq.heappop(l)
            tot-=a
            a=math.floor(math.sqrt(a))
            tot+=a
            heapq.heappush(l,-a)
        return tot
