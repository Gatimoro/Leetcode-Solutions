class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=deque([asteroids[0]])
        for asteroid in asteroids[1:]:
            explode=False
            while stack and 0<stack[-1]<=-asteroid:
                if stack.pop()==-asteroid:
                    explode=True
                    break
            if not explode:
                if stack and stack[-1]>0 and asteroid<0:
                    continue
                stack.append(asteroid)
        return list(stack)
