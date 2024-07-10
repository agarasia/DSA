from collections import defaultdict
from typing import List

class TwitterBruteForce:

    def __init__(self):
        self.tweets = []
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        followees = self.following[userId] | {userId}  # Include the user's own tweets
        for user, tweet in reversed(self.tweets):  # Reverse to get the most recent tweets first
            if user in followees:
                feed.append(tweet)
            if len(feed) == 10:
                break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
# T(n) = O(1)ForPosttweet ,O(N)ForGetnewsfeed, O(1)ForFollow, O(1)ForUnfollow
# S(n) = O(n)

t = TwitterBruteForce()
t.postTweet(1, 5)
print(t.getNewsFeed(1))
t.follow(1, 2)
t.postTweet(2, 6)
print(t.getNewsFeed(1))
t.unfollow(1, 2)
print(t.getNewsFeed(1))
