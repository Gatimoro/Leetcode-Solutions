class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=[['e', 'i', 'o', 'p', 'q', 'r', 't', 'u', 'w', 'y'],['a', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 's'],['b', 'c', 'm', 'n', 'v', 'x', 'z']]
        ans=[]
        lens=[len(rows[0])-1,len(rows[1])-1,len(rows[2])-1]
        for word in words:
            cur = sorted(word.lower())
            last=cur[0]
            row = 0 if last in rows[0] else 1 if last in rows[1] else 2
            index=0
            found=True
            for letter in cur:
                if letter==last:
                    continue
                while index < len(rows[row])-1 and rows[row][index]!=letter:
                    index+=1
                if letter!=rows[row][index]:
                    found=False
                    break
                last=letter
            if found:
                ans.append(word)
        return ans
"""RETURNS ALL WORDS THAT CAN BE WRITTEN USING EXCLUSIVELY ONE QUERTY ROW."""
