class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        #dp array
        dp = [[0]*len(s1) for _ in range(len(s2))]

        #first pos of the first letter in each other word
        incol = s1.find(s2[0])
        inrow = s2.find(s1[0])

        #suma keeps track of the deletions needed to make s1[:i+1] equal to s2[:j+1].
        suma = ord(s2[0])
        for i in range(len(s1)):#work out the first row
            suma += ord(s1[i])
            if i == incol:
                suma -= 2 * ord(s2[0])
            dp[0][i] = suma

        suma = ord(s1[0])
        for i in range(len(s2)):#work out the first column
            suma += ord(s2[i])
            if i == inrow:
                suma -= 2 * ord(s1[0])
            dp[i][0] = suma
        
        #go through the dp array
        for i in range(1,len(s2)):
            for j in range(1,len(s1)):
                
                #in the case the letters are equal, just take the answer for both words[:-1]
                if s2[i]==s1[j]:
                    dp[i][j] = dp[i-1][j-1]
                #else take the minimum between ans for word1[:-1] & word2 plus the cost of deleting the last character for word1 and the same but with word2.
                else: 
                    dp[i][j] = min(dp[i-1][j] + ord(s2[i]),dp[i][j-1] + ord(s1[j]))
        return dp[-1][-1]
