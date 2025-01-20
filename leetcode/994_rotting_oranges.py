class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append(((i,j),0))

        while queue:
            curr = queue.popleft()
            location = curr[0]
            time = curr[1]
            res = max(res,time)

            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            for x,y in directions:
                new_x = x + location[0]
                new_y = y + location[1]


                if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2
                    queue.append(((new_x,new_y),time + 1))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return res
