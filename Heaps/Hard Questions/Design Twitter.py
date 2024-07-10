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

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.user_tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        if userId in self.user_tweets:
            tweets.extend(self.user_tweets[userId])
        if userId in self.following:
            for followee in self.following[userId]:
                if followee in self.user_tweets:
                    tweets.extend(self.user_tweets[followee])
        
        # Sort the tweets by timestamp in descending order and get the top 10
        tweets.sort(key=lambda x: x[0], reverse=True)
        return [tweetId for _, tweetId in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

# Posting a tweet is O(1) with respect to the number of tweets per user.
# Retrieving the news feed is O(N log k), where N is the number of followees (including the user themselves) and k is the number of tweets to retrieve (in this case, 10).
# Following and unfollowing are O(1) operations.


t = TwitterBruteForce()
t.postTweet(1, 5)
print(t.getNewsFeed(1))
t.follow(1, 2)
t.postTweet(2, 6)
print(t.getNewsFeed(1))
t.unfollow(1, 2)
print(t.getNewsFeed(1))

t = Twitter()
t.postTweet(1, 5)
print(t.getNewsFeed(1))
t.follow(1, 2)
t.postTweet(2, 6)
print(t.getNewsFeed(1))
t.unfollow(1, 2)
print(t.getNewsFeed(1))
