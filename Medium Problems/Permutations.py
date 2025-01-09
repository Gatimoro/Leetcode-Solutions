class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numa=[]
        def daperm(perm,unused):
            if unused:
                for _ in range(len(unused)):
                    perm.append(unused.popleft())
                    daperm(perm,unused)
                    unused.append(perm.pop())
            else:
                numa.append(perm[:])
        daperm(list(),deque(nums))
        return numa
"""return all permutations on nums"""
