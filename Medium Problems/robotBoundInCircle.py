class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        twist=instructions.count('R')-instructions.count('L')
        coords=[0,0]
        dir=0
        where=[(1,0),(0,1),(-1,0),(0,-1)]
        for ins in instructions:
            match ins:
                case 'R':
                    dir=(dir-1)%4
                case 'L':
                    dir=(dir+1)%4
                case _:
                    coords[0]+=where[dir][0]
                    coords[1]+=where[dir][1]
        return coords==[0,0] or dir>0
#if the robot changes direction, it will eventually after every 4 iterations if it moved x and y tiles, it will end up at position (x+y-x-y), (y+x-y-x). Meaning it returns to the origin. 
"""DESC:
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle."""
