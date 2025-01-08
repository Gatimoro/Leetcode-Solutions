class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        lens=len(s)
        i=0
        j=lens-1
        vowels=set('aeiouAE')
        while i<j:
            while i<j and s[i] not in vowels:
                i+=1
            while i<j and s[j] not in vowels:
                j-=1
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return ''.join(s)
