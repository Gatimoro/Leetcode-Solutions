class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cur_row = [0,poured,0]
        for row in range(query_row ):
            cur_row = [0] + [ max((tl-1)/2, 0) + max((tr-1)/2, 0) for tl, tr in pairwise(cur_row)] + [0]
        return min(1, cur_row[query_glass + 1])
