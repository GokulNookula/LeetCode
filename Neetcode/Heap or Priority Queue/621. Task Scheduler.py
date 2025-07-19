# OPTIMAL Solution
        # We know each task is 1 unit of time
        # Our goal is to minimize the idle time
        
        # Create a dictionary to 
        # count how many times each task appears
        count = Counter(tasks)
        # Creating a maxHeap for each task in our hashmap count
        maxHeap = [-cnt for cnt in count.values()]
        # Converting the above array into a maxHeap
        heapq.heapify(maxHeap)

        # Keep track of what time it is to deal
        # with n
        time = 0
        # Double ended queue which cotains values as
        # paris of [-cnt, idleTime] where idleTime
        # is at what time that task is going to be available at
        queue = deque()

        # Iterate until our maxHeap is not empty
        # or our queue is not empty
        while len(maxHeap) > 0 or len(queue) > 0:
            # Increasing our time we have taken
            # to process aka our output
            time += 1

            # If our maxHeap is not empty
            if len(maxHeap) != 0: 
                # Popping to obtain the most frequent
                # element count from our heap because
                # always do the task which has the highest
                # frequency first (adding 1 due to negative values aka maxheap)
                cnt = 1 + heapq.heappop(maxHeap)

                # Checking if the count of that task 
                if cnt != 0:
                    # We append the count of that task
                    # along with the time when it is going to be
                    # available at by doing current time + idletime
                    # aka time + n
                    queue.append([cnt, time + n])
            # Checking if our queue is not empty and our
            # first value of the queue aka it's idleTime (queue[0][1])
            # has reached our current time
            if len(queue) != 0 and queue[0][1] == time:
                # We're moving a task from the 
                # cooldown queue back into the heap
                # because its cooldown period has ended 
                # (i.e., the current time has reached its ready time).
                # We only push the task info (not the cooldown time) 
                # back into the maxHeap.
                heapq.heappush(maxHeap, queue.popleft()[0])

        # Returning how long aka time it took to do it
        return time

'''Explained: Time Complexity: O(m) where m is number of tasks Space Complexity: O(1) since we only have 26 characters
'''
