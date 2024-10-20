class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        operator=['&',' and ', '|', ' or ']
        current=[]
        ignore=0
        for x in expression:
            if x==',':
                expression=expression.replace(',',current[-1],1)
            elif x in operator:
                expression=expression.replace(x,'',1)
                current.append(operator[operator.index(x)+1])
            elif x=='!':
                ignore+=1
            elif x==')':
                if not ignore:
                    current.pop()
                else:
                    ignore-=1
        expression=expression.replace('f','False')
        expression=expression.replace('t','True')
        expression=expression.replace('!','not')
        return eval(expression)
