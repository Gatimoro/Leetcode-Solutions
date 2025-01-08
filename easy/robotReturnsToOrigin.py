class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=moves.count('R')-moves.count('L')
        if x:
            return False
        x=moves.count('U')-moves.count('D')
        return x==0
