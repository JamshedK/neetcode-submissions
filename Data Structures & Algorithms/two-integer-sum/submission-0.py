class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            first = target-num
            if first in dic: 
                return [dic[first], i]
            dic[num] = i