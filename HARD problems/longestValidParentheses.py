class Solution:
    def longestValidParentheses(self, s: str) -> int:#this solution has 75%+ runtime but i'm pretty sure isn't the right way to solve this problem. There must be something simpler.
        opens=closes=length=length2=top=hold=hold2=0
        for par,rev in zip(s,reversed(s)):
            if par=='(':
                opens+=1
            else:
                opens -= 1
                hold+=2
            if rev ==')':
                closes+=1
            else:
                closes -= 1
                hold2+=2
            if opens<0:
                opens=length=hold=0
            elif opens==0:
                length+=hold
                hold=0
                top=max(length,top)
            if closes<0:
                closes=length2=hold2=0
            elif closes==0:
                length2+=hold2
                hold2=0
                top=max(length2,top)
        return top
"""Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring."""
