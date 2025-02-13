"""I realized that after the transformation, if you started with an array of length N: x1, x2, x3 ... xN; you will end up with: xN XOR x1, x1 XOR x2, x3 XOR x4 ... xN-1 XOR xN. 
Where every element appears twice in between XORs. If our array looks like this, it must be able to be generated by the transformation. And if you XOR the whole array, you end up with
xN XOR x1 XOR x1 XOR x2 XOR x2 XOR x3 ... XOR xN-1 XOR xN. Since a XOR a = 0 and each element appears twice, the XOR must be 0 or else it can not be generated by our transformation."""
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0
"""A 0-indexed array derived with length n is derived by computing the bitwise XOR (⊕) of adjacent values in a binary array original of length n.

Specifically, for each index i in the range [0, n - 1]:

If i = n - 1, then derived[i] = original[i] ⊕ original[0].
Otherwise, derived[i] = original[i] ⊕ original[i + 1].
Given an array derived, your task is to determine whether there exists a valid binary array original that could have formed derived.

Return true if such an array exists or false otherwise.

A binary array is an array containing only 0's and 1's
 """
