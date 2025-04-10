# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list= [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                adj_list[manager[i]].append(i)
        def dfs(m):
            if len(adj_list[m]) == 0:
                return 0
            self_inform_time = informTime[m]
            maxx = float('-inf')
            for subordinate in adj_list[m]:
                maxx = max(maxx,dfs(subordinate))
            return self_inform_time + maxx
        return dfs(headID)