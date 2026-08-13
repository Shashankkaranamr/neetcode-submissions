class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        big_hash=defaultdict(list)

        for s in strs:
            arr=[0]*26
            for i in s:
                arr[ord(i)-97]+=1
            arr_tuple=tuple(arr)
            big_hash[arr_tuple].append(s)
        return list(big_hash.values())