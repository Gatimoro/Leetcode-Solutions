class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        class fren:
            def __init__(self, data):
                self.data = data
        fren.head=fren(1)
        val=fren.head
        for i in range(2,n+1):
            val.next=fren(i)
            val=val.next
        val.next=fren.head
        ansa=[] 
        val=fren.head
        m=1
        while val.data:
            val.data=0
            for kkk in range(k*m):
                val=val.next
            m+=1
        p=fren.head
        for crumb in range(n):
            if p.data:
                ansa+=[p.data]
            p=p.next
        return ansa
            
            
