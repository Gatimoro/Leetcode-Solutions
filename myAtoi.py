class Solution(object):
    def myAtoi(self, s):
        answer=''
        i=0
        neg=0
        for blurp in s:
            if i==0 and blurp!=' ':
                if blurp not in '+-0987654321':
                    return 0
                elif blurp in'-+':
                    neg=(int(blurp+'1')+2)%3
                elif blurp !='0':
                    answer+=blurp
                    i+=1
                i+=1
            elif 0<i<3:
                if '0'>blurp or blurp>'9':
                    if answer =='':
                        return 0
                    return int(answer)
                elif blurp!='0' and answer=='' or answer!="":
                    answer+=blurp
                    i+=2
            elif i>2:
                if '0'<=blurp<='9':
                    answer+=blurp
                    i+=2
                    if i//2>10:
                        return (int(neg*'-'+'2147483647')-neg)
                else:
                    break
        if i//2>9:
            for c in range(0,i//2):
                if answer[c]>'214748364700'[c]:
                    return int(neg*'-'+'2147483647')-neg
                elif answer[c]<'214748364700'[c]:
                    break;
        if answer == '':
            return 0
        return int(neg*'-'+answer)
