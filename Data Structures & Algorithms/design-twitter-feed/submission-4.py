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
        # get this users tweets
        # get all the users this user follows
        # go through this users and all the people he follows tweets, add to minheap of size 10

        # time complexity analysis: 
            # n users, m tweets and k follows
            # number of tweets = O(k * m)
        minheap = []
        follows_list = set()
        # if a user follows someone, get the list
        if userId in self.follows:
            print(f"user follows {self.follows[userId]}")
            follows_list = self.follows[userId]
        follows_list.add(userId)
        for userId in follows_list:
            if userId not in self.tweets: 
                continue
            user_tweets = self.tweets[userId]
            for tweet  in user_tweets[-10:]: 
                tweetId, ts = tweet
                # if less than 10, keep adding
                if len(minheap) < 10: 
                    heapq.heappush(minheap, [ts, tweetId])
                # replace if least recent tweet, it's too old
                elif minheap[0][0] < ts: 
                    heapq.heappop(minheap)
                    # push the new tweet
                    heapq.heappush(minheap, [ts, tweetId])
        
        # pop all the elements in heapq
        res = []
        while minheap: 
            ts, tweetId = heapq.heappop(minheap)
            res.append(tweetId)
        return res[::-1]

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
        
