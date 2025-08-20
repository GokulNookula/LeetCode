# OPTIMAL Solution
class Solution:
    # Topological Sorting algorithm
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Builidng an adjacent list of prereqs
        # Total number of nodes which is c aka 4 empty arrays in a dictonary
        prereq = {c:[] for c in range(numCourses)}

        # Filling in the empty arrays with it's prerequsites that
        # we are given from the user
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # A course has 3 possible states:
        # 1. Visited node -> crs has been added to the output
        # 2. Visting node -> crs not been added to output, but is added to the cycle
        # 3. Univisited node -> crs not been added to the output or cycle
        res = []
        
        # To keep track of the visited nodes and cycle is for
        # making sure to check if that node was already added and
        # we visit it again then its a cycle
        visit, cycle = set(), set()

        def dfs(crs):
            # If the node is already in our cycle
            # then it cant be a topological sort hence
            # we return False to return []
            if crs in cycle:
                return False
            # Checking if our course is already in
            # our visited nodes then we still continue
            # as we havent return back to the beginning course
            # aka crs yet and we want to exhaust all the paths
            if crs in visit:
                return True
            # Adding it to the cycle set to keep track
            cycle.add(crs)
            
            # Getting all the prerequisties of that course aka crs
            # by doing DFS
            for pre in prereq[crs]:
                # Means we found a cycle from the prereq path
                # we took from the beginning of crs and comes back to
                # itself thus it is wrong
                if dfs(pre) == False:
                    return False
            # Removing that crs as it is no longer
            # in our path from cycle as we exhausted all it's
            # paths
            cycle.remove(crs)
            # adding it into visited nodes as we went through
            # all its prereqs thus has been visited where 
            # there is no other direction that needs to be visited
            # from that course thus we can add it to our output now
            visit.add(crs)
            # completed the crs so we add it to output
            res.append(crs)

            return True
        # Going through every courses we are doing it in order
        # per the problem
        for c in range(numCourses):
            # We detected a cycle for that course
            # hence it cant be a topological sort path
            if dfs(c) == False:
                return []
        return res

'''Explained: Time Complexity: O(V+E) where V is number of courses
and E is the number of prerequisites Space Complexity: O(V+E)
'''
