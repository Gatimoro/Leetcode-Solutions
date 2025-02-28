class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def valid(a,b):
            flag = False
            for i in range(len(a)):
                if a[i] != b[i]:
                    if flag: 
                        return False
                    flag = True
            return flag
        deq = deque([startGene])
        bank = set(bank)
        curdepth=1
        while deq:
            for _ in range(len(deq)):
                cur = deq.popleft()
                found = []
                for word in bank:
                    if valid(word, cur):
                        deq.append(word)
                        found.append(word)
                        if word == endGene:
                            return curdepth
                if found: bank-=set(found)
            curdepth+=1
        return -1
"""A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank."""
