class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s)==len(goal) and goal in s+s
#this program returns whether you can rotate a string into a goal string
