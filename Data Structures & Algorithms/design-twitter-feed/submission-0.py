class Twitter:

    def __init__(self):
        self.count=0
        self.TweetMap=collections.defaultdict(list)
        self.FollowerMap=collections.defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.TweetMap[userId].append((self.count,tweetId))
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        result=[]
        maxHeap=[]
        self.FollowerMap[userId].add(userId)
        for followee in self.FollowerMap[userId]:
            if self.TweetMap[followee]:
                index=len(self.TweetMap[followee])-1
                count,tweetId=self.TweetMap[followee][index]
                maxHeap.append((count,tweetId,followee,index-1))
        heapq.heapify(maxHeap)
        while maxHeap and len(result)<10:
            count,tweetId,followee,index=heapq.heappop(maxHeap)
            result.append(tweetId)
            if index>=0:
                count,tweetId=self.TweetMap[followee][index]
                heapq.heappush(maxHeap,(count,tweetId,followee,index-1))
        return result


   
    def follow(self, followerId: int, followeeId: int) -> None:
        self.FollowerMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.FollowerMap[followerId]:
            self.FollowerMap[followerId].remove(followeeId)

        
        
