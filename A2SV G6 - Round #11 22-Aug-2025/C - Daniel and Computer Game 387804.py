# Problem: C - Daniel and Computer Game - https://codeforces.com/gym/604781/problem/C

# from collections import deque
# import sys
# n, k = map(int, sys.stdin.readline().split())
# left_wall = input()
# right_wall = input()

# walls = [left_wall, right_wall]
#             #[left, right] walls
# visited = [[False, False] for _ in range(n)]

#             #position, wall, time
# que = deque()
# que.append((0,0,0))

# visited[0][0] = True
# res = False
# while que:
#     pos, wall, time = que.popleft()
#     # print(pos, wall, time)
#     if pos + k >= n:
#         res = True
#         break

#     if (not visited[pos + k][1 - wall]) and walls[1-wall][pos+k] == '-' and pos >= time:
#         visited[pos+k][1-wall] = True
#         que.append((pos+k, 1-wall, time + 1))
#     if (not visited[pos + 1][wall]) and walls[wall][pos+1] == '-' and pos >= time:
#         # print("afafa", pos+move, wall, time+1, move)
#         visited[pos+1][wall] = True
#         que.append((pos+1, wall, time + 1))
#     if (not visited[pos - 1][wall]) and walls[wall][pos-1] == '-' and pos >= time:
#         # print("afafa", pos+move, wall, time+1, move)
#         visited[pos-1][wall] = True
#         que.append((pos-1, wall, time + 1))

# if res:
#     print("YES")
# else:
#     print("NO")










from collections import deque


n,m = map(int,input().split())
temp = []
temp.append(list(input()))
temp.append(list(input()))

st = deque([(0,0,0)])
seen = set((0,0))
ans = "NO"
while st:
    node,pos,level = st.popleft()
    # print(node, pos, level)
    if node >= n-m:
        ans = "YES"
        break

    if (node - 1,pos) not in seen and temp[pos][node - 1] == '-' and level <= node:
        seen.add((node - 1,pos))
        st.append((node - 1,pos,level + 1))

    if (node + 1,pos) not in seen and temp[pos][node + 1] == '-' and level <= node:
        seen.add((node + 1,pos))
        st.append((node + 1,pos,level + 1))

    if (node + m,1- pos) not in seen and temp[1 - pos][node + m] == '-' and level <= node:
        seen.add((node + m,1 - pos))
        st.append((node + m,1 - pos,level + 1))


print(ans)
