class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        check = lambda t: sum(t // i for i in time) >= totalTrips
        lo, hi = 0, min(time) * totalTrips
        while lo < hi:
            mid = (lo+hi) // 2
            if(check(mid)):
                hi = mid
            else:
                lo = mid + 1
        return lo
