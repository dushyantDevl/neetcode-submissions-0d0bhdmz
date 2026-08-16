class Twitter:
    def __init__(self):
        self.time = 0
        self.posts = []                 # (time, tweetId, userId)
        self.following = {}             # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append((self.time, tweetId, userId))
        self.time += 1
        
        ## make sure userId maps to something; if it's brand new, 
        ## start it as an empty set
        self.following.setdefault(userId, set())

    def getNewsFeed(self, userId: int) -> List[int]:
        # oter than followees list include user itself (using union symbol '|')
        followees = self.following.get(userId, set()) | {userId}
        
        relevant = [(t, tid) for t, tid, u in self.posts if u in followees]
        relevant.sort(reverse=True) # newest first
        
        return [tid for _, tid in relevant[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)   # discard: no KeyError