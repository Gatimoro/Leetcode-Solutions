class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        col=image[sr][sc]
        if col!=color:
            stacc=deque([(sr,sc)])
            while stacc:
                i, j = stacc.popleft()
                image[i][j]=color
                if i!=0 and image[i-1][j] == col:
                    stacc.append((i-1,j))
                if j!=0 and image[i][j-1] == col:
                    stacc.append((i,j-1))
                if j!=len(image[0])-1 and image[i][j+1] == col:
                    stacc.append((i,j+1))
                if i!=len(image)-1 and image[i+1][j] == col:
                    stacc.append((i+1,j))
        return image
"""Performs a flood fill on an image"""
