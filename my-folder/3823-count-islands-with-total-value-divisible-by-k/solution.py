class Solution:

    def findSum(self, grid, i, j, m, n):
        # print(grid)
        if i < 0:
            temp = grid[i+1][j] 
            grid[i+1][j] = 0
            return temp
        if i >= m:
            # return grid[i-1][j]
            temp = grid[i-1][j] 
            grid[i-1][j] = 0
            return temp
        if j < 0:
            # return grid[i][j+1]
            temp = grid[i][j+1]
            grid[i][j+1] = 0
            return temp
            
        if j >= n:
            temp = grid[i][j-1]
            grid[i][j-1] = 0
            return temp
        if grid[i][j] == 0:
            return 0
        temp = grid[i][j]
        grid[i][j] = 0
        
        
        return temp + self.findSum(grid, i+1, j, m, n) + self.findSum(grid, i-1, j, m, n) + self.findSum(grid, i, j+1 , m, n) + self.findSum(grid, i, j-1, m, n)
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        # print(m)
        n = 0
        for num in grid[0]:
            n+=1
        # print(m,n) 
        count = 0
        i = 0
        j= 0
        while i < m:
            j=0
            while j < n:
                print(i,j)
                if grid[i][j]!=0:
                    su = self.findSum(grid, i, j , m, n)
                    # print(su)
                    # print(grid)
                    if su % k ==0:
                        count +=1
                j+=1
            i+=1
            # print(i,m)
        
        
        return count

        
