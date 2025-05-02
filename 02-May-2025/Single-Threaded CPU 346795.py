# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        tasks.sort()
        available_tasks = []
        #proccessingtime, enquetime, id
        ans = []
        total_time = tasks[0][0]
        j = 0
        while j < n or available_tasks:
            while j < n and tasks[j][0] <= total_time:
                heappush(available_tasks, (tasks[j][1],tasks[j][2],tasks[j][0]))
                j += 1
            if available_tasks:
                process_time, id_, enque_time = heappop(available_tasks)
                total_time += process_time
                ans.append(id_)
            else:
                total_time = tasks[j][0]
        return ans