import collections
class TimeMap:

    def __init__(self):
        self.hash_map=collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        values=self.hash_map[key]
        low=0
        high=len(values)-1
        res=""
        while low<=high:
            mid=low+(high-low)//2
            if values[mid][1]==timestamp:
                return values[mid][0]
            elif values[mid][1]>timestamp:
                high=mid-1
            else:
                res=values[mid][0]
                low=mid+1
        return res

        
