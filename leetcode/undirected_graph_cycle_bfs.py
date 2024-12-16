from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
	    
	    visited = set()
	    res = 0
		
		def bfs(node):
		    queue = deque()
		    queue.append((node, -1))
		    visited.add(node)
		    
		    while queue:
		        curr, parent = queue.popleft()
		        
		        for val in adj[curr]:
		            if val == parent:
		                continue
		            if val in visited:
		                return 1
		            
		            visited.add(val)
		            queue.append((val, curr))
		            
		            
		    return 0
		    
		    
		    
	    for i in range(len(adj)):
	        if i not in visited:
	            if bfs(i) == 1:
	                return 1
	                
	                
	    return 0
