class Solution:
    def numSimilarGroups(self, strs):
        length = len(strs[0])
        group = {s:s for s in strs}
        rank = defaultdict(int)
        def findgroup(string):
            if group[string] != group[group[string]]:
                group[string] = findgroup(group[string])
            return group[string]


        def check(fucky, wucky):
            diff = False
            satisfied = False
            for i in range(length):
                if fucky[i] != wucky[i]:
                    if satisfied: 
                        return False
                    if not diff:
                        diff = True
                    else:
                        satisfied = True

            the_one, the_other = findgroup(fucky), findgroup(wucky)
            if the_one == the_other:
                return
            if rank[the_one] > rank[the_other]:
                group[the_other] = the_one
            elif rank[the_one] < rank[the_other]:
                group[the_one] = the_other
            else:
                group[the_one] = the_other
                rank[the_other] += 1
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                check(strs[i],strs[j])
        return len(set(findgroup(s) for s in strs))
"""Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping at most two letters (in distinct positions) within the string X.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?"""
