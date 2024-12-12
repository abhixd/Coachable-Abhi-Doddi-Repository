class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_list = {}
        res = 0
        visited = [0] * n

        for i in range(n):
            adj_list[i] = []

        for edge in edges:
            first = edge[0]
            second = edge[1]

            if first in adj_list:
                adj_list[first].append(second)
            else:
                adj_list[first] = [second]

            if second in adj_list:
                adj_list[second].append(first)
            
            else:
                adj_list[second] = [first]

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





            







        
