class Solution:
    def reverseBits(self, n: int) -> int:
        bino=bin(n)[-1:1:-1]
        return int(''.join([bino,(32-len(bino))*'0']),2)
