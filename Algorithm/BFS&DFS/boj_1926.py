
'''
문제 

어떤 큰 도화지에 그림이 그려져 있을 때, 
그 그림의 개수와, 
그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 
그림의 넓이란 그림에 포함된 1의 개수이다.

입력

첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 
두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)
'''


"""
1. 아이디어

- 1을 찾아나가는 문제 = BFS
- 2중 For문을 돌리며 값은 1이여야 하고 방문이 안되어 있는 곳
- BFS 돌면서 그림 개수 +1, 최대값을 갱신

2. 시간복잡도
 - BFS : O(V+E)
    - V : 가로개수 * 세로개수 = m * n
    - E : 한개에 Vertex에서 4개까지 나오니 넉넉잡아 = V * 4
    = V + E -> V + 4V = 5V
    = 5 * m * n
    V = 500 * 500
    E = 4 * 500 * 500
    V+E = 5 * 250000 = 100만 < (1초 연산 2억개) >>>가능
    
3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

print(n, m, "\n")
print(map)

# 0,1 오른쪽 1,0 아래 0,-1 왼쪽 -1,0 위쪽
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    rs = 1 # 사이즈 
    q = [(y, x)] # queue 에 넣어주기
    while q: # queue에 더 안들어올때 까지
        ey, ex = q.pop()
        # 동서남북 4 방향으로 움직이며 1이 있는지 확인
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            # map 사이즈가 초과되지 않게 끝쪽은 아래 혹은 왼쪽 오른쪽이 없을 수도 있으니
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1 # 그림(1)이 발견되면 +1 
                    chk[ny][nx] = True
                    q.append((ny,nx))

    return rs

cnt = 0 
maxv = 0

# 2중 for문 y를 먼저 그 뒤 x
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True # 방문을 True로 변경
            # 전체 그림 갯수를 +1
            cnt += 1
            # BFS 를 통해 그림 크기를 구해주기
            # 최대값 갱신
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)