
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges=[]
        component=len(points)
        n=len(points)
        for i in range(len(points)):
            for j in range(len(points)):
                if i!=j:
                    distance=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    edges.append([distance,i,j])
        edges.sort()
        parent=[i for i in range(n)]
        rank=[1]*n
        def find(node):
            if parent[node]!=node:
                parent[node]=find(parent[node])
            return parent[node]
            
        def union(x,y):
            par_x,par_y=find(x),find(y)
            if par_x==par_y:
                return False
            if rank[par_x]>rank[par_y]:
                parent[par_y]=par_x
                rank[par_x]+=rank[par_y]
            else:
                parent[par_x]=par_y
                rank[par_y]+=rank[par_x]
            
            return True
        cost=0  
        for w,s,d in edges:
            if union(s,d):
                cost+=w
                component-=1
                if component==1:
                    break
        return cost

