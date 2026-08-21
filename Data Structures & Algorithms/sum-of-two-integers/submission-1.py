class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry_in = 0
        res = 0
        for i in range(32):
            # find the i'th bit for a and b
            a_bit = 1 & (a >> i)
            b_bit = 1 & (b >> i)
            # calculate the sum without carry
            sum_bit = a_bit ^ b_bit ^ carry_in
            carry_out = (a_bit & b_bit) | (carry_in & (a_bit ^ b_bit))
            carry_in = carry_out
            # add i to the result in the given position
            if sum_bit == 1:
                res = res | (1 << i)
        # and to isolate bit 31
        if res & (1 << 31):
            res -= (1 << 32)
        return res