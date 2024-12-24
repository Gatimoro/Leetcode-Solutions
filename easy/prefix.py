class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        guess=strs[0][:len(min(strs,key=lambda x:len(x)))]
        while guess:
            found=True
            for string in strs[1:]:
                for ind, (i, j) in enumerate(zip(string,guess)):
                    if i!=j:
                        guess=guess[:ind]
                        found=False
                        break
                if not found:
                    break
            if found:
                break
        return guess
"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""
