# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

class Players:
    def __init__(self, size):
        self.parents = list(range(size))
        self.sizes = [1] * size
        self.points = [0] * size
        self.extra_points = [0] * size

    def get_ultimate(self, n):
        if self.parents[n] != n:
            return self.get_ultimate(self.parents[n])
        return n

    def get_points(self, n):
        amt = self.points[n]
        if self.parents[n] == n:
            return amt
        amt += self.get_points(self.parents[n]) - self.extra_points[n]
        return amt

    def add_points(self, n, p):
        top = self.get_ultimate(n)
        self.points[top] += p

    def link(self, n1, n2):
        n1 = self.get_ultimate(n1)
        n2 = self.get_ultimate(n2)
        if n1 == n2:
            return False
        if self.sizes[n1] < self.sizes[n2]:
            n1, n2 = n2, n1
        self.sizes[n1] += self.sizes[n2]
        self.parents[n2] = n1
        self.extra_points[n2] = self.points[n1]
        return True


def main():
    node_num, query_num = map(int, input().split())
    players = Players(node_num + 1)
    for _ in range(query_num):
        parts = input().split()
        if parts[0] == "get":
            n = int(parts[1])
            print(players.get_points(n))
        elif parts[0] == "add":
            n, p = int(parts[1]), int(parts[2])
            players.add_points(n, p)
        elif parts[0] == "join":
            a, b = int(parts[1]), int(parts[2])
            players.link(a, b)


if __name__ == "__main__":
    main()