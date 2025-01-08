class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        length=len(moves);
        p2wins=(length+1)%2;
        winlines=[0]*8;
        
        if length>=5:
            for i in range(p2wins,length,2):
                if moves[i][0]==moves[i][1]:
                    winlines[7]+=1
                if moves[i][0]==2-moves[i][1]:
                    winlines[6]+=1
                winlines[moves[i][0]]+=1
                winlines[moves[i][1]+3]+=1
            if 3 in winlines:
                return "B" if p2wins else "A"
        return "Draw" if length==9 else "Pending"

  #Returns who won at tictactoe
