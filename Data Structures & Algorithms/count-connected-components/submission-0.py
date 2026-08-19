class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count=0
        visited=[False]*n
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def dfs(node):
            visited[node]=True
            for nei in graph[node]:
                if visited[nei]==False:
                    dfs(nei)

        for i in range(n):
            if visited[i]==False:
                count+=1
                dfs(i)
        return count