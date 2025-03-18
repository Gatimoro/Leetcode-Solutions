class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return "".join(a[1] for a in sorted((index, letter) for index, letter in zip(indices,s)))
"put the corresponding letter at the corresponding index"
            
