class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ['1']
        next_ans = []
        for cycle in range(n-1):
            last=ans[0]
            count=0
            for n in ans:
                if last==n:
                    count+=1
                else:
                    next_ans.append(str(count))
                    next_ans.append(last)
                    count=1
                last = n
            ans=next_ans[:]
            ans.append(str(count))
            ans.append(last)
            next_ans=[]
        return "".join(ans)

"""The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence."""
