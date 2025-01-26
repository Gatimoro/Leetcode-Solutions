"""Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes."""
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        priority=[]
        full=set()
        floods={}
        for day in range(len(rains)):
            if rains[day]:
                if rains[day] in full:
                    # if not floods[rains[day]]:
                    #     floods[rains[day]]=[day]
                    # else:
                    #     floods[rains[day]].append(day)
                    priority.append(rains[day])
                else:
                    full.add(rains[day])

        full=set()
        i=0
        for rain in range(len(rains)):
            if rains[rain]:
                if rains[rain] in full:
                    return []
                full.add(rains[rain])
                rains[rain]=-1
            else:
                if i<len(priority):

                    if priority[i] in full:
                        rains[rain]=priority[i]
                        full.remove(priority[i])
                        i+=1
                    else:
                        b=i
                        while b<len(priority) and priority[b] not in full:
                            b+=1
                        if b<len(priority):
                            p=priority.pop(b)

                            rains[rain]=p
                            full.remove(p)
                        else:
                            rains[rain]=1
                else:
                    rains[rain]=1
            
        return rains if i==len(priority) else []
