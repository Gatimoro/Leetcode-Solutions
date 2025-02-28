class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1 = len(str1) + 1
        l2 = len(str2) + 1
        indices = [[None] * l2 for _ in range(l1)]
        lengths = [[0] * l2 for _ in range(l1)]
        # for row in dp: print(row)

        for i in range(1, l1):
            for j in range(1, l2):
                if str1[i-1] == str2[j-1]:
                    lengths[i][j], indices[i][j] = lengths[i-1][j-1] + 1, (i-1, j-1)
                elif lengths[i-1][j] > lengths[i][j-1]:
                    lengths[i][j], indices[i][j] = lengths[i-1][j], indices[i-1][j]
                else:
                    lengths[i][j], indices[i][j] = lengths[i][j-1], indices[i][j-1]
        
        ans=[]
   
        i, j = 0, 0
        curr_i, curr_j = l1-1, l2-1
        dalist=[(l1-1,l2-1)]
        while indices[curr_i][curr_j]:
            dalist.append(indices[curr_i][curr_j])
            curr_i, curr_j = indices[curr_i][curr_j]
        for ti, tj in reversed(dalist):
            while j<tj:
                ans.append(str2[j])
                j+=1
            while i<ti:
                ans.append(str1[i])
                i+=1
            i+=1
        return ''.join(ans)
"""Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s."""
