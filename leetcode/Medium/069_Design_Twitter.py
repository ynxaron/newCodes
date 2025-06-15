TweetFeedStackLen = 10
class Tweet:
    def __init__(self):
        self.tweets = []

    def addTweet(self, tweetId: int):
        if len(self.tweets) == TweetFeedStackLen:
            self.tweets.remove(0)
        self.tweets.append(tweetId)

class Twitter:
    def __init__(self):
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int):
        if userId not in self.tweets:
            self.tweets[userId] = Tweet()
        self.tweets[userId].addTweet(tweetId)
