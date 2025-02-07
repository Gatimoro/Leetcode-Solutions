class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorcount={}
        ball_col={}
        ans=[]
        cols=0
        for a,b in queries:
            if b in colorcount and colorcount[b]!=0: colorcount[b]+=1
            else: 
                colorcount[b]=1
                cols+=1
            if a in ball_col: 
                colorcount[ball_col[a]]-=1
                if colorcount[ball_col[a]] == 0: cols-=1
            ball_col[a]=b
            ans.append(cols)
        return ans
"""You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.

Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color."""
