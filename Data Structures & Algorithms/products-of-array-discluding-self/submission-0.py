class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 2, 4, 6
        # 1, 1, 2, 8 -> prefix
        # 48,24, 6, 1 -> postfix
        # 48, 24, 12, 8
        prefix, postfix = [1 for i in range(len(nums))], [1 for i in range(len(nums))]
        last_index = len(nums) - 1
        prev = 1
        # calcualte prefix 
        for i in range(1, last_index + 1):
            prev = prev * nums[i-1]
            prefix[i] = prev
        # calculate postfix
        prev = 1 
        for i in range(last_index - 1, -1, -1):
            prev *= nums[i + 1]
            postfix[i] = prev
        for i in range(len(nums)):
            prefix[i] = prefix[i] * postfix[i]
        return prefix
        
            
