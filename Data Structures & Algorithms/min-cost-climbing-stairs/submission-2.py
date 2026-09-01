class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1,step2=0,0
        for c in reversed(cost):
            step1,step2=c+min(step1,step2),step1
        return min(step1,step2)
