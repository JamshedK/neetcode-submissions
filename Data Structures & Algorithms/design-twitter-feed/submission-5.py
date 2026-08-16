import heapq
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.follows = {}
        self.tweets = {}
        self.maxheap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # just store them in a dictionary
        # each tweet has tweetId, timestamp 
        # {userId: [list of [tweetId, timestamp]}
        # do we need to store all tweets? don't need, but maybe yeh
        self.timestamp += 1
        if userId in self.tweets: 
            self.tweets[userId].append([tweetId, self.timestamp])
        else: 
            self.tweets[userId] = [[tweetId, self.timestamp]]

    def getNewsFeed(self, userId: int) -> List[int]:
        # merge K sorted list algorith, use maxheap
        maxheap = []
        res = []
        # add user to the list of his own followers
        if userId not in self.follows:
            self.follows[userId] = set()
        self.follows[userId].add(userId)
        # go through the list of all the users followers and put their most recent tweet into maxheap
        for followeeId in self.follows[userId]:
            if followeeId not in self.tweets:
                continue
            tws = self.tweets[followeeId]
            # for each user, get the last tweet, index and followeeId and add to maxheap
            index = len(tws) - 1
            tweetId, ts = tws[index]
            maxheap.append([-ts, tweetId, followeeId, index - 1])
        
        # heapify
        heapq.heapify(maxheap)
        while maxheap and len(res) < 10: 
            # for each user, pop their tweets 
            ts, tweetId, followeeId, index = heapq.heappop(maxheap)
            res.append(tweetId)
            if index >= 0: 
                # add this users more recent tweet
                tweetId, ts = self.tweets[followeeId][index]
                heapq.heappush(maxheap, [-ts, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # could use a hashmap
        # { followerId: ( set people user follows/folloeweeId )}
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else: 
            self.follows[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # use the hashmap, find followerId and remove followee
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
