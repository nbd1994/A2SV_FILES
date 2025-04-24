# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # indegree_count = [0]*numCourses
        # adj_list = [[] for _ in range(numCourses)]
        # for a,b in prerequisites:
        #     adj_list[b].append(a)
        #     indegree_count[a] += 1
        # que = deque()
        # ans = []
        # for i in range(numCourses):
        #     if indegree_count[i] == 0:
        #         que.append(i)
        # # print(adj_list)
        # # print(indegree_count)
        # while que:
        #     node = que.popleft()
        #     ans.append(node)
        #     for neig in adj_list[node]:
        #         indegree_count[neig] -= 1
        #         if indegree_count[neig] == 0:
        #             que.append(neig)
        # return ans if len(ans) == numCourses else []

        adj_list = [[] for _ in range(numCourses)]
        WHITE = 0
        BLACK = 1
        GRAY = 2
        colors = [WHITE]*numCourses
        is_possible = True
        for a,b in prerequisites:
            adj_list[a].append(b)
        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return
            colors[node] = GRAY
            for neig in adj_list[node]:
                if colors[neig] == WHITE:
                    dfs(neig)
                elif colors[neig] == GRAY:
                    is_possible = False
            colors[node] = BLACK
            ans.append(node)
        ans = []
        for n in range(numCourses):
            if colors[n] == WHITE:
                dfs(n)
        return ans if is_possible else []