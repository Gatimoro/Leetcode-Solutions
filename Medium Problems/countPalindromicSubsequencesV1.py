#The better solution to this problem can be found in the 100% dailys
#This is quite inefficient
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count=Counter()
        checked=set()
        pref=[{}]
        last=[0]*26
        tocheck=[]
        for i,letter in enumerate(s):#Store how many times we have seen each letter at each index
            count[letter]+=1
            pref.append(dict(count))
            last[ord(letter)-97]=i
            if letter not in checked:
                checked.add(letter)
                tocheck.append([ord(letter)-97,i])#add each encountered for the first time letter to the tocheck list
        ans=0
        for ind, start in tocheck:#if a letter appears more than 0 times between the first and last appearence of a given letter, count it.
            left = pref[start+1]
            right = pref[last[ind]]

            for letter in right:
                if not letter in left or right[letter]-left[letter]>0:
                    ans+=1
        return ans
            
