class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from functools import lru_cache
        import sys
        sys.set_int_max_str_digits(0)
        @lru_cache(maxsize=None)
        def size(n):
            if n>1:
                return (size(n-1)<<1) + 1
            else:
                return 1
        @lru_cache(maxsize=None)
        def bloberfish(sub):
            if sub>2:
                pufferfish=swordfish=bloberfish(sub-1)
                blowfish=0
                while swordfish:
                    blowfish=blowfish<<1
                    if not swordfish%2:
                        blowfish+=1
                    swordfish=swordfish>>1
                blowfish=(blowfish<<1)+1
                Marine=((pufferfish<<1)+1)<<(int(pufferfish).bit_length()+1)
                Marine+=blowfish
            elif sub==1:
                Marine=1
            else:
                Marine=3
            return Marine
        while size(n)>k:
            n-=1
        print(bin(bloberfish(n)))
        print(bin(bloberfish(n-1)))
        print(bin(bloberfish(n-2)))
        print(k,size(n),size(n-1),size(n-2),'\nn ',n)
        for x in range (5,16):
            print('\n'+str(bin(bloberfish(x)))+'\n')
            print(size(x))
        if (bloberfish(n+1)>>(k-size(n)))%2:
            return '1'
        else:
            return '0'
