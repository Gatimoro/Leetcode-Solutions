import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        l=[x*-1 for x in gifts]
        heapq.heapify(l)
        while k>0:
            a=-heapq.heappop(l)
            a=-isqrt(a)
            heapq.heappush(l,a)
            k-=1
        return -1*sum(l)
