class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        def valid(diff: int) -> bool:
            count = 0
            ind = 0
            while ind < len(nums)-1 and count < p:
                if nums[ind+1] - nums[ind] <= diff:
                    count += 1
                    ind += 2
                else:
                    ind += 1
            return count == p

        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if valid(mid):
                high = mid
            else:
                low = mid + 1
        return low
