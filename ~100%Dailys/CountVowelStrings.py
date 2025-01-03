class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        valid=[0]*(len(words)+1)
        cur=0
        vowels={'a','e','i','o','u'}
        for i,word in enumerate(words,start=1): #remembah how many words start and end with a vowel before any index in an array (get prefix sum for each index)
            if word[0] in vowels and word[-1] in vowels:
                cur+=1
            valid[i]=cur
        ans=[0]*len(queries)
        for c,[i,j] in enumerate(queries): #now get how many words are between a and b by doing prefix b - prefix a
            ans[c]=(valid[j+1]-valid[i])
        return ans
"""You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 """
