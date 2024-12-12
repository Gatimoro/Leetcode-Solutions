class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        s=0
        if len(gifts)==1:
            for n in range(k):
                gifts[0]=int(gifts[0]**0.5)
                if gifts[0]==1:
                    return 1
        while s<k:
            gifts.sort(reverse=True)
            i=0
            while s<k and i<len(gifts)-1 and gifts[i]>=gifts[i+1]and gifts[i]>=gifts[0]:
                while s<k and gifts[i]>=gifts[i+1]and gifts[i] >= gifts[0]:
                    gifts[i]=int(gifts[i]**0.5)
                    s+=1
                i+=1
        return sum(gifts)
