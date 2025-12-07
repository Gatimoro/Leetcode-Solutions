# You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

# 0 means the cell cannot be walked through.
# 1 represents an empty cell that can be walked through.
# A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
# In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

# You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

# Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

# Note: The input is generated such that no two trees have the same height, and there is at least one tree needs to be cut off.

 
class Point:
    x = 0
    y = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def hax(self):
        return (self.x, self.y)
    def unavailable(self, f):
        if f[self.x][self.y] == 0:
            return True

dirs = [(0, 1), (1, 0), (-1, 0),(0,-1)]
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(forest), len(forest[0])
        ordered = sorted(set([item for line in forest for item in line]))
        points = [Point()]

        if ordered[0] == 0:
            ordered = ordered[1:]
        if ordered[0] == 1:
            ordered = ordered[1:]
        visited = set()
        for goal in ordered:
            visited = set()
            while True:
                if not points:
                    return -1
                nextQ = Deque()
                found = False
                for point in points:
                    # print("steps", ans, point.x, point.y)
                    if point.hax() in visited or point.unavailable(forest):
                        continue
                    visited.add(point.hax())
                    if forest[point.x][point.y] == goal:
                        points = [point]
                        found = True
                        break
                    for dx, dy in dirs:
                        nx, ny = point.x + dx, point.y + dy
                        if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                            continue
                        next_point = Point(nx,ny)
                        nextQ.append(next_point)
                if not found:
                    points = nextQ
                    ans += 1
                else:
                    break
        return ans
