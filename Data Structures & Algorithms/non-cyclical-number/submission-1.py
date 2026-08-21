class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        str_n = str(n)
        while True: 
            res = 0
            for ch in str_n: 
                res += int(ch) ** 2
            #     print(res, int(ch) **2)
            # print(str_n, res)
            if res == 1:
                return True
            # convert res into ch
            str_n = str(res)
            if str_n in hashset: 
                return False
            hashset.add(str_n)
