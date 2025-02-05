class Solution:
    def partition(self, s: str) -> List[List[str]]:
        bitmask=0
        mem={}
        betweens=len(s)-1
        arr = list(s)
        ans=[]
        for bitmask in range(1<<betweens):
            #get split indices
            splits=[i+1 for i in range(betweens) if bitmask&(1<<(i))]
            candidate=[]
            last=0
            for split_index in splits+[len(s)]:
                temp = "".join(arr[last:split_index])

                #memoization check
                if temp not in mem:
                    #palindromic check
                    rev=temp[::-1]
                    if temp==rev:
                        mem[temp] = True #yay
                        mem[rev]=True
                        candidate.append(temp)
                    else: 
                        mem[temp] = False
                        mem[rev] = False
                        break
                
                #if we already computed the string
                else:
                    if mem[temp]: candidate.append(temp)
                    else: break
                last=split_index
            if mem[temp]: ans.append(candidate)
        return ans
"""Finds all palindrome partitions through brute force and memoization."""
