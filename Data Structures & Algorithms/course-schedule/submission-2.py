class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=defaultdict(list)
        courses=prerequisites
        for a,b in courses:
            g[a].append(b)

        UNVISITED=0
        VISITING=1
        VISITED=2
        seen_arr=[UNVISITED]*numCourses

        def dfs(node):
            if seen_arr[node]==VISITED: return True
            if seen_arr[node]==VISITING:return False
            seen_arr[node]=VISITING
            for nei in g[node]:
                if not dfs(nei):
                    return False
            seen_arr[node]=VISITED
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        