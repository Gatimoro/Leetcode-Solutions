class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        daddys = list(range(len(edges)+1))
        rank = [0] * (len(edges)+1)
        def wheresPapa(baby):
            if daddys[baby] != baby:
                baby=wheresPapa(daddys[baby])
            return baby
        last=None
        def same(x, y):
            daddy_x = wheresPapa(x)
            daddy_y = wheresPapa(y)
            if daddy_x == daddy_y:
                return True
            if rank[daddy_x]<rank[daddy_y]:
                daddys[daddy_x]=daddy_y
                rank[daddy_y]+=1
            else:
                daddys[daddy_y]=daddy_x
                rank[daddy_x]+=1
            return False
        for x,y in edges:
            if same(x,y):return [x,y]
"""find first edge that creates a cycle"""
