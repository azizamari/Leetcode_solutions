class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.m=len(grid)
        self.n=len(grid[0])
        fresh=set()
        rotten=set()
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]==1:
                    fresh.add((i,j))
                elif grid[i][j]==2:
                    rotten.add((i,j))
        c=0
        while len(fresh)!=0:
            changed=0
            for i,j in list(rotten):
                for x in [(i-1,j), (i,j-1),(i,j+1),(i+1,j)]:
                    if x in fresh:
                        changed+=1
                        fresh.remove(x)
                        rotten.add(x)
            if changed==0:
                return -1
            c+=1
        return c
