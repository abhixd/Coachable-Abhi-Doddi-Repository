class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        res = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append(((i,j),0))


        while queue:
            curr = queue.popleft()
            pos = curr[0]
            time = curr[1]
            res = max(res,time)
            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            for x,y in directions:
                new_x = pos[0] + x
                new_y = pos[1] + y

                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 0
                    queue.append(((new_x,new_y),time + 1))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1


        return res
