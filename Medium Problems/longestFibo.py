class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nexus = defaultdict(list)
        ansa = 0 
        for num in arr:
            for last, length in nexus[num]:
                nexus[last + num].append((num, length+1))
                ansa = max(ansa, length)
        return ansa
        
