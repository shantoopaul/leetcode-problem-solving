class Solution:
    def reverseBits(self, n: int) -> int:
        # res = 0
        # for i in range(32):
        #     res = (res << 1) | (n & 1)
        #     n >>= 1
        # return res
        return int(bin(n)[2:].zfill(32)[::-1], 2)