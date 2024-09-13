"""
문제 

N×M 크기의 배열로 표현되는 미로가 있다.

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력

첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
"""

import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(n)]   # strip = 줄 바꿈포함된 문자열 나눔
chk = [[False] * m for _ in range(n)]

# 0,1 오른쪽 1,0 아래 0,-1 왼쪽 -1,0 위쪽
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
distance = 0


def bfs(y, x):
    global distance
    queue = deque()
    queue.append((y, x))
    # distance = 1
    map[y][x] = 1

    while queue:
        y, x = queue.popleft()

        for k in range(4):
            
            ny = y + dy[k]
            nx = x + dx[k]


            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    # distance += 1
                    map[ny][nx] = map[y][x] + 1
                    queue.append((ny, nx))
                

    return map[n-1][m-1]
        


for j in range(n): 
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            # DFS 로 크기 구하기
            # 방문 체크 표시
            chk[j][i] = True
            distance = bfs(j, i)

        
print(distance)