# OPTIMAL Solution
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        # Keeping track of the number of tweets
        self.count = 0
        # It is a list of tweets for each user where
        # it is stored as a pair like 
        # userId -> list of [count,tweetIds] inside a hashmap
        self.tweetMap = defaultdict(list)
        # It is a hashmap of list of followers for each userId
        # for the people they follow like
        # userId -> set of followeeId
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Finding the userId from our hashmap for tweet then we
        # are appending the pair aka count of tweet and the actual
        # tweet id aka [count,tweetId]
        self.tweetMap[userId].append([self.count, tweetId])
        # Decreasing the count as we are using a maxHeap
        # to keep track of the number of tweets
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Appending the 10 recent feeds where the most
        # recent is in the beginning of the list
        res = []
        # We need a minHeap to figuring out the most recent tweet
        # of that userId
        minHeap = []
        # We also want the 10 most recent followeeId's and 
        # following themselves thus we add themselves into the list
        self.followMap[userId].add(userId)
        # Iterating through every person that the userId follows
        for followeeId in self.followMap[userId]:
            # Checking if there is any tweets between followeeId
            # and the userId in the tweet hashmap aka if it is empty
            if followeeId in self.tweetMap:
                # Obtaining the index aka last value of the list
                index = len(self.tweetMap[followeeId]) - 1
                # Getting the last tweet and the count of that followee person that
                # the userId follows
                count, tweetId = self.tweetMap[followeeId][index]
                # Append tweet metadata to the minHeap:
                # - `count`: timestamp for sorting by recency
                # - `tweetId`: the tweet's ID
                # - `followeeId`: who posted the tweet
                # - `index - 1`: to track the previous tweet by this followee
                # We'll use this data to build a sorted news feed and fetch earlier tweets.
                # where our minHeap will be sorted based on count aka recency
                minHeap.append([count, tweetId, followeeId, index - 1])
        # Turning it into a minHeap
        heapq.heapify(minHeap)

        # Iterating until our minHeap is non empty and our
        # result array is less 10 tweets returned
        while minHeap and len(res) < 10:
            # Popping the most recent tweet that happened
            count, tweetId, followeeId, index =  heapq.heappop(minHeap)
            # Appending our tweetId into our result array
            res.append(tweetId)
            # Checking if the amount of tweets with that
            # followeeId and userId is not empty
            if index >= 0:
                # Getting more tweets if that followeeId had
                # tweets with that user that is the next tweet
                # that is being added to the minHeap
                count, tweetId = self.tweetMap[followeeId][index]
                # Pushing the new tweets that we got back into the minHeap
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res     

    def follow(self, followerId: int, followeeId: int) -> None:
        # We are basically finding the key aka the followerId from
        # our hashmap and then adding the new followeeId into the values
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # First checking if followeeId is even in our hashmap
        if followeeId in self.followMap[followerId]:
            # We are basically finding the key aka the followerId from
            # our hashmap and then removing the new followeeId into the values
            self.followMap[followerId].remove(followeeId)    
'''Explained: Time Complexity: O(n) (for each getNewsFeed 
all and O(1) for remaning methods) Space Complexity: O(N∗m+N∗M+n) 
(where n is the total number of followeeIds associated 
with the userId, m is the maximum number of tweets 
by any user (m can be at most 10), N is the 
total number of userIds, and M is the 
maximum number of followees for any user)

We are going to explain more here TODO
'''
