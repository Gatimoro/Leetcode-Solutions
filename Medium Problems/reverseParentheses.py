# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.
class Solution:
    def reverseParentheses(self, s: str) -> str:
        arr = [l for l in s if l not in ')(']
        stack = []
        # arr[0:len(arr)] = arr[0:len(arr)][::-1]
        i = 0
        for letter in s:
            # print(arr, letter)
            if letter == '(':
                stack.append(i)
            elif letter== ')':
                j = stack.pop()
                arr[j:i] = arr[j:i][::-1]
            else:
                i+=1
        return "".join(arr)
