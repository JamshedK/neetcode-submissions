class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        leftOver = 1
        for i in range(len(digits)-1, -1, -1):
            total = leftOver + digits[i]
            # if the sum exceed 10, total becomes total - 10 with leftOver 1
            if total >= 10:
                total = total - 10
                leftOver = 1
            # else, leftover is zero and total is what it is
            else:
                leftOver = 0
            digits[i] = total
        if leftOver == 1:
            digits.insert(0, 1)
        return digits
