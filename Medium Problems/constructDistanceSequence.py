class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = (2*n-1)
        answers = deque([([0]*(2*n-1),0, 0)])
        target= (1<<n) - 1

        while answers:
            seq, used, start= answers.pop()
            while seq[start]!=0:
                start+=1
            if 1 & used == 0:
                new_seq=seq[:]
                new_seq[start]=1
                new_used = used | 1
                if new_used == target:
                    return new_seq
                answers.append((new_seq, new_used,start+1))
            for x in range(1,n):
                if 0 == (1<<x) & used:
                    if start+x+1<length and seq[start+x+1]==0:
                        new_seq=seq[:]
                        new_seq[start]=x+1
                        new_seq[start+x+1]=x+1
                        new_used = used | 1<<x
                        if new_used == target:
                            return new_seq
                        answers.append((new_seq, new_used, start+1))
"""Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, 
sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] 
because the first position they differ is at the third number, and 9 is greater than 5.
