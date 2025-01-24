class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        strudel = [[] for _ in range(len(graph))]
        for i, val in enumerate(graph):
            for link in val:
                strudel[link].append(i)
        remaining = [len(cons) for cons in graph]
        remove=[i for i in range(len(remaining)) if not remaining[i]]
        while remove:
            hold=[]
            for node in remove:
                for pos in strudel[node]:
                    remaining[pos]-=1
                    if not remaining[pos]:
                        hold.append(pos)
            remove=hold[:]
        return [i for i, nod in enumerate(remaining) if not nod]
