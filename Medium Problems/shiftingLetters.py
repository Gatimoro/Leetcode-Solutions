class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = []
        shifts=reversed(list(accumulate(reversed(shifts))))
        for letter, shift in zip(s, shifts):
            ans.append(ascii_lowercase[(ord(letter)+7+shift)%26])
        return ''.join(ans)
"""You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.""" 
