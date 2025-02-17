class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        target = (2<<(len(tiles)-1)) - 1
        ans=0
        def check(rem):
            used=set()
            nonlocal ans
            for d, let in enumerate(tiles):
                if not (let in used or rem & (1<<d)):
                    ans+=1
                    used.add(let)
                    nrem = rem | (1<<d)
                    check(nrem)
        check(0)
        return ans
"""You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles."""
