class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output_arr=[0]*len(temperatures)
        for temp in range(len(temperatures)):
            if not stack:
                stack.append(temp)
            else:
                if temperatures[temp]<temperatures[stack[-1]]:
                    stack.append(temp)
                else:
                    while stack and temperatures[stack[-1]]<temperatures[temp]:
                        
                        
                        output_arr[stack[-1]]=temp-stack[-1]
                        stack.pop()
                    stack.append(temp)
        while not stack:
            output_arr[stack.pop()]=0
            
        return output_arr



        