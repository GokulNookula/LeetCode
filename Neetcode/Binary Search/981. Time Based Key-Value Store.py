# OPTIMAL Solution
class TimeMap:

    def __init__(self):
        # To create a hashmap to store all the data in
        # as it is (foo, [bar, 1]) = (key, value = [list of [value, timestamp]])
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Checking if our current key is not in our hashmap then we create
        # an array that stores a list of arrays of [value, timestamp] in it for
        # that key only which is in ascending order
        if key not in self.store:
            self.store[key] = []
        # Always appending on the end of the list thus keeping it in ascending order
        # as the timestamp increase because time goes from small to big
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Initalizing our output as if we don't have anything
        # then we return empty string
        res = ""
        # Obtaining the array that stores a list of arrays of [value,timestamp]
        # to be able to get our result later
        values = self.store.get(key,[])

        # Running binary search as we return the value that is closest to our
        # timestamp number given
        left = 0
        right = len(values) - 1

        # We set left <= right because 
        while (left <= right):
            # Obtaining the midpoint to check how far are we from timestamp
            midpoint = (left + right) // 2

            # Checking if our midpoint timestamp is less than
            # our timestamp we are searching for 
            # we do this first to check if it is even a valid
            # number or not
            if values[midpoint][1] <= timestamp:
                # Setting the result value everytime and updating until
                # we get as close to our actual timestamp
                res = values[midpoint][0]
                # If it is less then we move our left pointer as
                # our goal is to find that exact timestamp or less than
                # that one aka <=
                left = midpoint + 1
            else:
                # We only move the right pointer and do not assign result
                # a value as it is bigger than than value as per our problem
                # we can only have something less than or equal to the timestamp
                # we are searching for
                right = midpoint - 1
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

'''Explained: Time Complexity: O(1) for set() and O(log n) for get() Space Complexity: o(m * n)
'''
