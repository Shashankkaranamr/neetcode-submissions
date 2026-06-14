class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        catchup_time=0
        time=0
        stack=[]
        fleet_count=0
        pair=[[p,s] for p,s in zip(position,speed)]
        pair.sort()
        print(pair)
        for i in range(len(pair)-1,-1,-1):
            if not stack:
                stack.append(i)
            else:
                time=(target-pair[stack[-1]][0])/pair[stack[-1]][1]
                catchup_time=(target-pair[i][0])/pair[i][1]
                
                if time>=catchup_time:
                    pass
                else:
                    while stack:
                        stack.pop()
                    fleet_count+=1
                    stack.append(i)
      
        if stack:
            return fleet_count+1 
        else:
            return fleet_count
        

