class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters=[]
        for letter in set(s):
            letters.append([s.find(letter),s.rfind(letter)])
        letters.sort()
        lin=0
        ans=[]
        curend=0
        for [strt1, end1],[strt2,end2] in pairwise(letters):
            curend=max(curend,end1)
            if strt2>=curend:
                ans.append(curend-lin+1)
                lin=strt2
        return ans+[len(s)-lin]
"""You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts."""
