class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        courses=prerequisites
        for a,b in courses:
            graph[a].append(b)
        if self.is_cyclic(graph,numCourses):
            return []
        return self.topological_sort(graph,numCourses)
    def is_cyclic(self,graph,numCourses):
        UNVISITED=0
        VISITING=1
        VISITED=2
        seen_arr=[UNVISITED]*numCourses

        def dfs(n):
            if seen_arr[n]==VISITING:return False
            elif seen_arr[n]==VISITED:return True
            seen_arr[n]=VISITING
            for nei in graph[n]:
                if not dfs(nei):
                    return False
            seen_arr[n]=VISITED
            return True


        for n in range(numCourses):

            if not dfs(n):
                return True
        return False
    def topological_sort(self,graph,numCourses:int):
        n=numCourses
        V=[False]*n
        order=[None]*n
        i=n-1
        def dfs(i,at,order,V,graph):
            V[at]=True
            for nei in graph[at]:
                if V[nei]==False:
                    i=dfs(i,nei,order,V,graph)
            print(i)
            order[i]=at
            return i-1
        for at in range(n):
            if V[at]==False:
                i=dfs(i,at,order,V,graph)
        return order[::-1]
    


        