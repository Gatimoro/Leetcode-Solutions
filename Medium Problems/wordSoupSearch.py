class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        target=len(word)
        def search(x , y , i, seen):
            if i==target:return True
            seen.add((x,y))
            for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if (nx,ny) in seen or nx==-1 or ny==-1 or ny==len(board[0]) or nx==len(board):continue
                if board[nx][ny] == word[i] and search(nx,ny,i+1,seen.copy()):return True
            return False
        for i,row in enumerate(board):
            for j, element in enumerate(row):
                if element==word[0] and search(i,j,1,set()):return True
        return False
"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once."""
