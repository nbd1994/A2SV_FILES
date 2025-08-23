# Problem: D - The Road to King's Landing - https://codeforces.com/gym/599383/problem/D

tests = int(input())
for _ in range(tests):
    n = int(input())
    segments = []
    for _ in range(n):
        segments.append(list(map(int, input().split())))


    def is_possible(k):
        left_side = 0
        right_side = 0
        for left, right in segments:
            left_side = max(left_side - k, left)
            right_side = min(right_side + k, right)
            if left_side > right_side:
                return False
        return True

    
    max_jump = 10**9
    min_jump = 0

    while min_jump <= max_jump:
        mid = min_jump + (max_jump - min_jump)//2
        if is_possible(mid):
            max_jump = mid - 1
        else:
            min_jump = mid + 1
    print(min_jump)