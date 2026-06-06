class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_strs=defaultdict(list)
        
        for str in strs:
            arr=[0]*26
            for i in str:
                arr[ord(i)-97]+=1
            tuple_arr=tuple(arr)
            hash_strs[tuple_arr].append(str)
            
        return list(hash_strs.values())
            