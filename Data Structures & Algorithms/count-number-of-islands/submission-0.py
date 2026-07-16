class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.islandSearch(grid,[i,j])
                    count += 1
        return count



    def islandSearch(self, grid, position):
        stack = []
        stack.append(position)
        while stack:
            curr = stack.pop()
            row, col = curr[0], curr[1]
            
            # Skip if out of bounds or already visited/water
            if (row < 0 or row >= len(grid) or 
                col < 0 or col >= len(grid[0]) or 
                grid[row][col] == "0"):
                continue
            
            # Mark as visited
            grid[row][col] = "0"
            
            # Add all four neighbors to stack
            stack.append([row - 1, col])  # north
            stack.append([row + 1, col])  # south
            stack.append([row, col - 1])  # west
            stack.append([row, col + 1])  # east

    
            