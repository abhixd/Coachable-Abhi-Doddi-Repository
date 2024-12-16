class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        adj_list = {}
        res = 0
        visited = [0] * len(isConnected)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                
                if isConnected[i][j] == 1:
                    if i in adj_list:
                        adj_list[i].append(j)
                    else:
                        adj_list[i] = [j]
                        
        def dfs(node):
            visited[node] = 1
            for val in adj_list[node]:
                if visited[val] == 0:
                    dfs(val)

            return

        for key in adj_list.keys():
            if visited[key] == 0:
                dfs(key)
                res += 1

        return res

        
