class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gain=[g-c for g,c in zip(gas,cost)]
        if sum(gain)<0:
            return -1
        tot,ans=0,0
        for i in range(len(gain)):
            tot+=gain[i]
            if tot<0:
                ans=i+1
                tot=0
        return ans
"""Desciption:
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique."""
