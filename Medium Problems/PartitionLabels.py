class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        n = len(s)
        forward, backward = set([s[0]]), set([s[-1]])
        infront = [0] * n
        infront[-1] = 1
        bsiz = 1
        for l in range(n-2, -1, -1):
            if s[l] not in backward:
                backward.add(s[l])
                infront[l] = infront[l + 1] + 1
            else:
                infront[l] = infront[l+1]
        total = infront[0]
        last = 0
        ans = []
        for l in range(1,n):
            #if the number in front at l is greater than at l +1
            #it means that we just witnnesed the last instance of a letter
            #but when do we know that the current letters don't appear any more?
            #proposition: when the # of dif. letters in front == the # of dif. letters
            #at the back, we can make a cut.
            
            if bsiz + infront[l] == total:
                #make cut
                ans.append(l-last)
                last = l
            print(bsiz, infront[l])
            if s[l] not in forward:
                forward.add(s[l])
                bsiz += 1
        return ans + [total-last]
"""You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts."""
