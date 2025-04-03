from collections import deque

class Solution: 
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        #strategy: add all the unbound items and then the next group

        insidelocks = [0] * n #how many elements from this elements group moust go before it
        outsidelocks = [0] * m #prop of each group, amount of element outside of it that must go before it.
        groups = [[] for _ in range(m)] #each group of elements
        inside_keys = [[] for _ in range(n)] #prop of element, which values it unlocks inside it's group
        outside_keys = [[] for _ in range(n)] #prop of element, which values it unlocks outside it's group
        groupcount = m
        
        

        for item, item_group in enumerate(group):
            
            if item_group == -1:
                group[item] = groupcount
                groupcount += 1
                groups.append([item])
                outsidelocks.append(0)

                continue

            groups[item_group].append(item)
        
        for item, item_group in enumerate(group):

            for prereq in beforeItems[item]:

                if group[prereq] == item_group:
                    insidelocks[item] += 1
                    inside_keys[prereq].append(item)
                else:
                    outsidelocks[item_group] += 1
                    outside_keys[prereq].append(item_group)
                    
        next_groups = deque()
        for g in range(m):
            if not outsidelocks[g]:
                next_groups.append(g)

        for g in range(m,groupcount):
            if not outsidelocks[g]:
                next_groups.appendleft(g)

        ans = []
        next_elem = deque()
        while next_groups:

            cur_group = next_groups.popleft()

            for element in groups[cur_group]:
                if not insidelocks[element]:
                    next_elem.append(element)
            

            while next_elem:
                n-=1
                e = next_elem.popleft()
                ans.append(e)

                for ins in inside_keys[e]:
                    insidelocks[ins] -= 1
                    if not insidelocks[ins]:
                        next_elem.append(ins)

                for out in outside_keys[e]:
                    outsidelocks[out] -= 1
                    if not outsidelocks[out]:
                        if out>=m:
                            next_groups.appendleft(out)
                        else:
                            next_groups.append(out)
        return ans if not n else []
"""There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution."""
