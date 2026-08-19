class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited=set()
        def dfs(n):
            visited.add(n)
            for nei in graph[n]:
                if nei not in visited:
                    dfs(nei)
        dfs(0)
        return len(visited)==n
        
        