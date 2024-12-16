class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if color == image[sr][sc]:
            return image

        og_color = image[sr][sc]
        queue = deque()
        queue.append((sr,sc))

        while queue:
            curr = queue.popleft()
            image[curr[0]][curr[1]] = color

            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            for x,y in directions:
                new_x = curr[0] + x
                new_y = curr[1] + y

                if 0 <= new_x < len(image) and 0 <= new_y < len(image[0]) and image[new_x][new_y] == og_color:
                    queue.append((new_x,new_y))

        return image
                    
