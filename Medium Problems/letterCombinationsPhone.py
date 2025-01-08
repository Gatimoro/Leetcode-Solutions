class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters=[('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i'), ('j', 'k', 'l'), ('m', 'n', 'o'), ('p', 'q', 'r','s'),('t','u','v'), ('w', 'x', 'y', 'z')]
        if not digits:
            return []
        ans=[list(letters[int(digits[0])-2])]
        for dig in digits[1:]:
            ans.append([])
            for letter in letters[int(dig)-2]:
                for string in ans[-2]:
                    ans[-1].append(string+letter)
        return ans[-1]
"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters."""
