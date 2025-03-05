class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))
        def nord(letter):
            return ord(letter)-97

        def minlex(symbol):
            if parent[symbol] != parent[parent[symbol]]:
                parent[symbol] = minlex(parent[symbol])
            return parent[symbol]

        def join(symbol_a, symbol_b):
            firpar, secpar = minlex(nord(symbol_a)), minlex(nord(symbol_b))
            if firpar == secpar:
                return
            if firpar < secpar:
                parent[secpar] = firpar
            else:
                parent[firpar] = secpar

        for a, b in zip(s1,s2):
            join(a, b)
        return ''.join([chr(97+minlex(nord(letter))) for letter in baseStr])
"""You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

 """
