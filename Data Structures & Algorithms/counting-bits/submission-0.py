class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(n):
            count = 0
            for i in range(32):
                # get the right most bit
                right_most = n & 1
                if right_most == 1:
                    count += 1
                n = n >> 1
            return count
        res = []
        for i in range(n + 1):
            res.append(count_ones(i))
        return res

            