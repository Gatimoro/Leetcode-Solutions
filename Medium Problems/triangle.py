class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cur=deque([0])
        last=deque([triangle[0][0]])
        for layer in range(1,len(triangle)-1):
            cur.appendleft(triangle[layer-1][0]+cur[0])
            for i, [a, b] in enumerate(pairwise(triangle[layer-1]),start=1):
                cur[i]+=min(a, b)
            cur[-1]+=last[-1]
            last=list(cur)
            print(last)

        return min(last)
"""Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row."""
