from typing import List
import itertools

class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:
        """
        Return all possible results from computing all the different possible ways to group numbers and operators in the given expression.

        Parameters:
            exp (str): The expression string consisting of numbers and operators.

        Returns:
            List[int]: A list containing all possible results. The order of the results are not important.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> expression1 = "2-1-1"
            >>> sorted(solution.diffWaysToCompute(expression1))
            [0, 2]

            # Example 2:
            >>> expression2 = "2*3-4*5"
            >>> sorted(solution.diffWaysToCompute(expression2))
            [-34, -14, -10, -10, 10]
        """
        if exp.isdigit():
            return [int(exp)]
        
        res = []

        for i in range(len(exp)):
            if exp[i] in '+-*':
                left = self.diffWaysToCompute(exp[:i])
                right = self.diffWaysToCompute(exp[i+1:])

                for l, r in itertools.product(left, right):
                    res.append(l+r if exp[i] == '+' else
                               l-r if exp[i] == '-' else
                               l*r)
        
        return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)