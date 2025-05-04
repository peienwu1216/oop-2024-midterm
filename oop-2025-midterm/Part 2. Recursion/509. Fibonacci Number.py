class Solution:
    def fib(self, n: int) -> int:
        arr = [0] * 50
        arr[1] = 1
        for i in range (2, 40):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n]
