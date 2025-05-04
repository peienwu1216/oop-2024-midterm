class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        
    def find(self, x):
        if self.parents[x] == x:
            return x
        
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_par, y_par = self.find(x), self.find(y)
        self.parents[x_par] = y_par

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        dsu = DisjointSetUnion(m)
        for i in range(m):
            for j in range(i+1, m):
                if isConnected[i][j]:
                    dsu.union(i, j)
        return len(set(dsu.find(i) for i in range(m)))
