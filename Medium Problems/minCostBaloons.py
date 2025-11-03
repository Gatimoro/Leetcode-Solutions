# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

# Return the minimum time Bob needs to make the rope colorful.
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        last = ''
        max_cost = float('inf')
        total = 0
        #go through baloons
        for (i, baloon) in enumerate(colors):
            if baloon == last:
                #we need to remove baloons
                if max_cost > neededTime[i]:
                    #we have a baloon in the current row 
                    #that takes longer to remove
                    total += neededTime[i]
                else:
                    #this baloon takes so long to remove that
                    #we just remove tha last slowest
                    total += max_cost
                    max_cost = neededTime[i]
            else:
                #this is the start of a new row
                max_cost = neededTime[i] #is the cost of the baloon we don't want to remove because it takes very long
                last = baloon #the color of the row
        return total
