# Definition for singly-linked list.
# class ListNode(object):      
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]       BY FAR MY WORST PROGRAM, BOTTOM 30
        :rtype: List[int]                AND IT TOOK ME  2 HOURS TO GET IT TO WORK NTAUNTAHARC.RUCXED
        """
        maxis=[head.val]
        vals=[]
        curr=head.val
        ind=0
        self=head
        while self:
            if self.val>curr:
                maxis+= [self.val,]*(vals[ind:].count(self.val)+1)
                ind=len(vals)+1
            curr=self.val
            vals.append(self.val)
            self=self.next
        for x in range(len(vals)-1):
            if maxis: 
                if vals[x] == maxis[0]:
                    maxis=maxis[1:]
                happy=False
                for k in maxis:
                    if k>vals[x]:
                        vals[x]=k
                        happy=True
                        break
                if not happy:
                    vals[x]=0
            else:
                vals[x]=0
        vals[-1]=0
        return vals
