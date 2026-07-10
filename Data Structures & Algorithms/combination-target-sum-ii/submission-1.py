class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        def backtrack(start_index,curr_comb,rem):
            if rem==0:
                result.append(curr_comb[:])
                result

            for i in range(start_index,len(candidates)):
                if i>start_index and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>rem:
                    break
                curr_comb.append(candidates[i])
                backtrack(i+1,curr_comb,rem-candidates[i])
                curr_comb.pop()
        backtrack(0,[],target)
        return result            