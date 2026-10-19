class Solution:


    def nextCell(self, value, tup):
        if value == "R":
            return (tup[0],tup[1]+1)
        elif value == "D":
            return (tup[0]+1,tup[1])
        elif value == "L":
            return (tup[0],tup[1]-1)
        else:
            return (tup[0]-1,tup[1])
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m = len(grid)

        i = 0
        j = 0
        while True:
            val = grid[i][j]
            grid[i][j]="X"
            prev = (i,j)
            next_val = self.nextCell(val, [i,j])
            i = next_val[0]
            j = next_val[1]
            if i >= m or j>= len(grid[i]) or i<0 or j<0 or grid[i][j]=="X":
                # print(i,j)
                return [prev[0],prev[1]]
        
