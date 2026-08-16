from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # need to convert into adjacenry graph
        hashmap = {}
        for i in range(numCourses):
            hashmap[i] = []
        for course, prereq in prerequisites:
            hashmap[course].append(prereq)
        # print(hashmap)
        
        # from this course, check if there is a cycle
        def dfs(course, path):
            if course in path: 
                return True
            if course in visited:
                return False
            path.add(course)
            visited.add(course)
            for pre in hashmap[course]:
                if dfs(pre, path):
                    return True
            path.remove(course)
            return False
        visited = set()
        for i in range(numCourses):
            path = set()
            if i not in visited and dfs(i, path) == True: 
                return False
        
        return True