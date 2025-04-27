# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        que = deque()
        n = len(quiet)
        ans = [i for i in range(n)]
        # cur_quitest = float('inf')
        indegree_count = [0]*n
        adj_list = [[] for _ in range(n)]
        for a,b in richer:
            adj_list[a].append(b)
            indegree_count[b] += 1
        for i in range(n):
            if indegree_count[i] == 0:
                que.append(i)
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                for neig in adj_list[node]:
                    indegree_count[neig] -= 1
                    if indegree_count[neig] == 0:
                        que.append(neig)
                    if quiet[ans[node]] < quiet[ans[neig]]:
                        ans[neig] = ans[node]          
        return ans