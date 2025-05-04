class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        min = nums[1] - nums[0]
        for i in range(2, len(nums)):
            val = nums[i] - nums[i-1]
            if val < min:
                min = val
        return min
