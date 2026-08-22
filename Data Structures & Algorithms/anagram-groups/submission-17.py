class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_hash=defaultdict(list)
        for s in strs:
            char_arr=[0]*26
            for c in s:
                char_arr[ord(c)-ord('a')]+=1
            ana_hash[tuple(char_arr)].append(s)
        return list(ana_hash.values())