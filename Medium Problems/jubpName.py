class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        leng = len(arr)
        visited = set()
        dq = deque([start])
        while dq:
            cur = dq.popleft()
            jump = arr[cur]
            if cur + jump < leng and cur + jump not in visited:
                if arr[cur+jump] == 0: return True
                visited.add(cur+jump)
                dq.append(cur+jump)

                
            if cur - jump >= 0 and cur - jump not in visited:
                if arr[cur-jump] == 0: return True
                visited.add(cur-jump)
                dq.append(cur-jump)
        
        return False
"""Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time."""
