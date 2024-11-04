class Solution:
    def compressedString(self, word: str) -> str:
        last=word[0]
        comp=[];
        n=1;
        for a in word[1:]:
            if a !=last:
                comp.append(str(n)+last)
                n=1
                last=a
            else:
                if n!=9:
                    n+=1
                else:
                    n=1
                    comp.append('9'+last)
        comp.append(str(n)+last)
        return ''.join(comp)
