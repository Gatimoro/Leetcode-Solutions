"""I actually wrote a solution for this one: 
Intuition
The numbers are guaranteed to appear. We will keep count of how many matches we have and which numbers have we found.

Notice that there are 3 scenarios when checking the next index:

0 found: That means that both the new number from A doesn't appear in B, and viceversa. Since there are no repeats, this must mean that we have not seen the 2 numbers so far.

1 found: The new number from A == new from B or we have previously seen only one of the new numbers. In the case of newA=newB we will need to update our set of seen numbers after checking newA so that the second check counts it.

2 found: Both numbers were seen.

Approach
The second array is a permutation of the first one and the values are not repeated so in total we have len(A) pairs of numbers. When we see the first one, we add it to the list and when we eventually find it's counterpart, we count it.

Complexity
Time complexity: O(n)
Space complexity: O(n)
Both O(n) because we iterate through the whole array and we end up with a set of len(input)"""
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen=set()
        count=0
        ans=[]
        for new1, new2 in zip(A,B):
            if new1 in seen:#check if we found a pair
                count+=1
            seen.add(new1) #for the case new1==new2.
            if new2 in seen:#again check if we found a pair 
                count+=1
            seen.add(new2)
            ans.append(count) #add num of pairs found
        return ans
"""You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once."""
