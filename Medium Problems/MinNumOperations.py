class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxs=[int(b) for b in boxes]
        toleft=list(accumulate(boxs))
        tot=toleft[-1]
        ans=[sum([i for i,j in enumerate(boxes) if j=='1'])]
        for i in range(len(boxes)-1):
            ans.append(ans[-1]+2*toleft[i]-tot)
        return ans
"""You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.

 """
