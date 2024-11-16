class Solution:
    def numWays(self, s: str) -> int:
        #count 1's
        monty=s.count('1');
#if there are no 1's, we have have to place 2 'walls' between the zeros, from left to right and assuming wall1 is the one to the left, we place wall1 in the first gap, leaving n-2 gaps ie combinations with the wall1 on first, then we have n-3 combinations with wall1 on second and so on. So we end up with a consecutive sum from n-2 to 1. this sum simplifies to (n-1)(n-2)/2.
        if not monty:
            n=len(s)
            return ((n-1)*(n-2)//2)%1000000007
#if there is no way to split in 3... blah blah blah
        if monty%3:
            return 0
#cut is the # of 1's per split section
        cut=monty//3
#define 4 vars in 1 line for confusion
        left=right=split1=split2 = 0
        #from left and right, we count until we reach cut # of '1', after which we count the gaps in between the last '1' from the partition and the next '1', which will mark the mandatory begining of the middle partition. We count these gaps because if we have to split in one of the right gaps and in one of the left gaps, the amount of combinations will be the left gaps times the right gaps.
        for x in s:
            if left<cut:
                if x=='1':
                    left+=1
            else:
                split1+=1
                if x=='1':
                    break
#second iteration of the code on top, this time executed from the right
        for x in s[::-1]:
            if right<cut:
                if x=='1':
                    right+=1
            else:
                split2+=1
#as soon as we are over the cut and find the next 1, we have enough info to return answer.
                if x=='1':
                    return (split1 * split2)%(1000000007)
