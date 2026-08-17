from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create reverse of what prerequisities unlock a course
        # for each course count how many prerequisities it has
        # if a course has zero prereq, add it to queue
        # start popping elements from the queue, check indegrees, decrement count for all dependant courses
        # if a course count becomes zero, add to queue
        indegrees = [[] for _ in range(numCourses)]
        hashmap = defaultdict()
        for i in range(numCourses):
            hashmap[i] = 0
        for course, pre in prerequisites: 
            indegrees[pre].append(course)
            hashmap[course] += 1
        q = deque()
        for course in hashmap: 
            if hashmap[course] == 0:
                q.append(course)
        res = []
        while q: 
            # pop the top of the queue
            prereq = q.popleft()
            res.append(prereq)
            # for all dependant courses
            for course in indegrees[prereq]:
                # decremenet count
                hashmap[course] -= 1
                if hashmap[course] <= 0:
                    q.append(course)
        
        return res if len(res) == numCourses else []



