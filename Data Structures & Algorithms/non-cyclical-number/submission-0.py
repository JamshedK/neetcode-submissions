import math
class Solution:
    def isHappy(self, n: int) -> bool:
        
        hashset = set()
        stringN = str(n)
        while True:
            total = 0
            for i in stringN:
                total = total + pow(int(i), 2)
            print(total)
            if total == 1:
                return True
            if total in hashset:
                return False
            stringN = str(total)
            hashset.add(total)
        
            