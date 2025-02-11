class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        pos = defaultdict(set)
        candidates.sort()
        def calc(path, cur, start):
            for i in range(start, len(candidates)):
                npath = path+[candidates[i]]
                if tuple(npath) not in pos[len(path)]:
                    
                    pos[len(path)].add(tuple(npath))

                    tog = cur + candidates[i]
                    if tog < target:
                        calc(npath, tog, i+1)
                    elif tog == target:
                        ans.append((npath))
        calc([], 0, 0)
        return ans
"""Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations."""
