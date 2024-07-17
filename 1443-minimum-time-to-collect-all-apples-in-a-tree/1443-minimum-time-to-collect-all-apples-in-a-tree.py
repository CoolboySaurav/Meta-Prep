class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        """
         
        """
        adj = {i:[] for i in range(n)}
        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par)
            
        def dfs(cur, par):
            
            time = 0
            
            for child in adj[cur]:
                if child == par:
                    continue
                childtime = dfs(child, cur)
                if childtime or hasApple[child]:
                    time += 2 + childtime
            return time
        
        return dfs(0,-1)