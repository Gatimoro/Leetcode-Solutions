class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add(a, s):
            return ''.join([str((int(letter) + a * (i % 2))%10)  for (i, letter) in enumerate(s)])
        # print (add(a, s))
        def rotate(b, s):
            return s[-b:] + s[:-b]
        # print(rotate(b, s))
        seen = set()
        best = s
        def dfs(state):
            nonlocal best
            if state not in seen:
                seen.add(state)
                best = min(best, state)
                dfs(rotate(b,state))
                dfs(add(a,state))
        dfs(s)
        return best
