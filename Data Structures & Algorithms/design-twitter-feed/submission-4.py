class Twitter:

    def __init__(self):
        self.user_posts = {}
        self.user_follow = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_posts.keys(): 
            self.user_posts[userId] = []
        self.user_posts[userId].append((tweetId,self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        candidates = [userId]
        candidates += (list(self.user_follow.get(userId,[])))
        posts = []
        for c in candidates:
            posts += self.user_posts.get(c,[])
        posts.sort(key=lambda x:x[1])
        i = 0
        while i < 10 and posts:
            feed.append(posts.pop()[0])
            i += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follow.keys():
            self.user_follow[followerId] = set()
        self.user_follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follow.get(followerId,[]):
            self.user_follow[followerId].remove(followeeId)
