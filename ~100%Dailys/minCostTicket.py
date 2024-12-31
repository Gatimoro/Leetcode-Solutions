class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        g = [0]*366 #days in a year
        x=0#x is the index and corresponds to the day that's being processed.
        for day in days:
            x+=1
            while x != day:#while we are in between days, the cost remains the same as that of the last day
                g[x] = g[x-1]
                x+=1
            g[x]=min([g[x-1] + costs[0], g[x-7] + costs[1], g[x-30] + costs[2]])#when we reach a day, we calculate the minimum between paying for a month, week and single pass that ends on said day. 
        return g[x] #return the last computed day.



"""DESCRIPTION:
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

 """
