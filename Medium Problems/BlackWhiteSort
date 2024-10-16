class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        moves=count=0
        #this program returns the minimum amount of swaps in order to organize black balls(1s) to the right and white balls(0) to the left.
        if '1' in s:
            count=s[::-1].index('1')
        for i in s[::-1][count:]:
            if i=='0':
                count+=1
            else:
                moves+=count
        return moves
