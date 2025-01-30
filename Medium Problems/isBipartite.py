class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [None] * len(graph)
        for start in range(len(graph)):
            if color[start]==None:
                color[start] = True
                toCheck = deque([start])
                while toCheck:
                    node = toCheck.pop()
                    shade = color[node]
                    for neighbor in graph[node]:
                        if color[neighbor]==None:
                            color[neighbor] = not shade
                            toCheck.append(neighbor)
                        elif color[neighbor]==shade:
                            return False
        return True
