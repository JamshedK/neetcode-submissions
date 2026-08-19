class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            # get the right most bit
            right_most = n & 1
            if right_most == 1:
                count += 1
            n = n >> 1
        return count
