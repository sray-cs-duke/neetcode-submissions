from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for course in range(numCourses):
            graph[course] = []
        remaining = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            remaining[course] += 1
        queue = deque()

        for course in range(numCourses):
            if remaining[course] == 0:
                queue.append(course)
        completed = 0
        while queue:
            current = queue.popleft()
            completed += 1

            for next_course in graph[current]:
                remaining[next_course] -= 1

                if remaining[next_course] == 0:
                    queue.append(next_course)
        return completed == numCourses

        