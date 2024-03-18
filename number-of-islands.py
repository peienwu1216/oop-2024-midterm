from typing import List
import itertools

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Return the number of islands in a 2D binary grid.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        All four edges of the grid are surrounded by water.

        Parameters:
            grid (List[List[str]]): A 2D binary grid representing a map of '1's (land) and '0's (water).

        Returns:
            int: The number of islands in the grid.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> grid1 = [
            ...     ["1","1","1","1","0"],
            ...     ["1","1","0","1","0"],
            ...     ["1","1","0","0","0"],
            ...     ["0","0","0","0","0"]
            ... ]
            >>> solution.numIslands(grid1)
            1

            # Example 2:
            >>> grid2 = [
            ...     ["1","1","0","0","0"],
            ...     ["1","1","0","0","0"],
            ...     ["0","0","1","0","0"],
            ...     ["0","0","0","1","1"]
            ... ]
            >>> solution.numIslands(grid2)
            3
        """
        m, n = len(grid), len(grid[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        def dfs(i, j):
            nonlocal m, n, dirs, grid
            if grid[i][j] == '0':
                return 

            grid[i][j] = '0'
            for di, dj in dirs:
                0 <= i+di < m and 0 <= j+dj < n and dfs(i + di, j + dj)

        n_islands = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1':
        #             n_islands += 1
        #             dfs(i, j)

        for i, j in itertools.product(range(m), range(n)):
            if grid[i][j] == '1':
                n_islands += 1
                dfs(i, j)

        return n_islands
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    
