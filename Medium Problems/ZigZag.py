class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
            return s
        ansa=['']*(numRows+1)
        row=0
        next=1
        for element in s:
            ansa[row]+=element
            row+=next
            if not 0<row<numRows-1:
                next=-next    
        for x in ansa[:-1]:
            ansa[numRows]+=x
        return ansa[numRows]
            
