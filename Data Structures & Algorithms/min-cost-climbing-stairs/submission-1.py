class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n=len(cost)-1
        for i in range(n-1,-1,-1):
            dist1,dist2=0,0
            
            if i+2<=n:
                dist1=cost[i]+cost[i+1]
                dist2=cost[i]+cost[i+2]
                cost[i]=min(dist1,dist2)
            else:
                cost[i]=cost[i]+cost[i+1]

        return min(cost[0],cost[1])
        



