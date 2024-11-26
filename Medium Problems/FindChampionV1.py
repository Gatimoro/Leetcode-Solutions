class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        losers=[]
        winners=[]
        count=0
        for x in edges:
            if x[1] not in losers:
                losers.append(x[1])
                count+=1
        for x in edges:   
            if x[0] not in winners and x[0] not in losers:
                winners.append(x[0])
                count+=1
        if count>=n and len(winners)==1:
            return winners[0]
        elif not edges and n==1:
            return 0
        else:
            return -1
