class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def valid(h):
            count = 0
            for cit in citations:
                if cit>=h:
                    count += 1
            return count >= h
        l=0
        r = 1000
        while l<r:
            m = (l+r+1)>>1
            if valid(m):
                l = m
            else:
                r = m - 1
        return r
"""Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

"""
