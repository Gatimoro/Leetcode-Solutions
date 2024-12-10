class Solution:"""This program finds the longest substring consisting of exclusively 1 character and appearing at least thrice in the string"""
    def maximumLength(self, s: str) -> int:
        counter={}
        if s[-1]!=s[-2]:#in the case that the last 2 letters arent equal, we add a 1 to the last letter count in our counter.
            counter[s[-1]]=[1]
        i=1
        ans=-1
        while i<len(s):#go through the whole string
            c=1
            while i<len(s) and s[i]==s[i-1]:#count the length of the special string
                c+=1
                i+=1
            if s[i-1] not in counter:#add the length of the sequence to the counter
                counter[s[i-1]]=[c]
            else:
                counter[s[i-1]].append(c)
            i+=1#after the nestet while breaks, s[i] MUST != s[i-1]
        for leta in counter:#There are 3 logical possibilities for the max value of with the current ans.
            counter[leta].sort()
            if len(counter[leta])>=3 and counter[leta][-1]==counter[leta][-2]==counter[leta][-3]:
                ans=max(counter[leta][-1],ans)
            elif len(counter[leta])>=2 and counter[leta][-2]+1>=counter[leta][-1]>=2:
                ans=max(counter[leta][-1]-1,ans)
            elif counter[leta][-1]>=3:
                ans=max(counter[leta][-1]-2,ans)
        return ans
