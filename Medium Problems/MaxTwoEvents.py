# You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

# Return this maximum sum.

# Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        #       events[start, end, value] -> deltas [time, isEnd, value]
        deltas = sorted([(event[1], True, event[2]) for event in events] + [(event[0], False, event[2]) for event in events])
        bestLeft, ans = 0, 0
        for time, isEnd, value in deltas:
            if isEnd:
                bestLeft = max(value, bestLeft)
            else:
                ans = max(bestLeft + value, ans)
        return ans
        
