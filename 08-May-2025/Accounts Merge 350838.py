# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        email_to_ids = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_ids[email].append(i)

        for ids in email_to_ids.values():
            for i in range(1, len(ids)):
                union(ids[0], ids[i])

        root_to_emails = defaultdict(set)
        for email, ids in email_to_ids.items():
            root = find(ids[0])
            root_to_emails[root].add(email)

        result = []
        for root, email_set in root_to_emails.items():
            name = accounts[root][0]
            result.append([name] + sorted(email_set))

        return result
