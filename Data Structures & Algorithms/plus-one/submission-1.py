class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            carry = total // 10
            total = total % 10
            digits[i] = total
        if carry: 
            digits.insert(0, carry)
        return digits