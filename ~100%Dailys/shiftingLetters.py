class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        delta_shift = [0]*(len(s)+1) # add 1 because the interval is inclusive
        for start, end, sign in shifts:
            diff=2*sign-1 #change 0s to -1 and 1s to 1.
            delta_shift[start]+=diff #add how much the total shift varies from that point onward.
            delta_shift[end+1]-=diff
        delta_shift=accumulate(delta_shift) #get how much should we shift at each point
        ans=[]
        for i, [letter, delta] in enumerate(zip(s, delta_shift)):
            if delta==0: #skip redundant shift
                continue
            ans[i]=(chr((ord(letter)-97+delta)%26+97)) #shift by howevermany indices we calculated after accumulating delta_shift. 
        return ''.join(ans) #finally since the answer is a list, join it and return as string.
"""Desc:
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied."""
