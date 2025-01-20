class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = [0] * len(isConnected)
        res = 0

        def dfs(node):
 
            visited[node] = 1
            for j in range(len(isConnected[node])):
                if isConnected[node][j] == 1 and visited[j] == 0:
                    dfs(j)
            return

        for i in range(len(isConnected)):
            if visited[i] == 0:
                dfs(i)
                res += 1
                print(visited)

        return res

