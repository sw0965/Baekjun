"""
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.

입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
입력으로 주어지는 간선은 양방향이다.
"""


"""
런타임 에러 (시간초과 예상)


import sys
import copy

input = sys.stdin.readline

n, m, v = map(int, input().split())
num = [list(map(int, input().strip().split())) for _ in range(m)]


dfs1 = []
bfs1 = []

def dfs(v2):
    dfs1.append(v2)
    if num_rep == []:
        return
    i = 0
    dfs2 = []
    while i < len(num_rep):
        que = num_rep[i]
        if v2 in que:
            
            if que[0] == v2:
                dfs2.append(que[1])
            elif que[1] == v2:
                dfs2.append(que[0])

            dfs2.sort()
            num_rep.remove(que)

            i = 0
        else:
            i += 1
    
    v2 = dfs2[0]
    dfs(v2)


def bfs(v2):
    bfs1.append(v2)

    if num_rep == []:
        return
    i = 0
    bfs2 = []
    while i < len(num_rep):
        que = num_rep[i]
        if v2 in que:
            
            if que[0] == v2:
                bfs2.append(que[1])
            elif que[1] == v2:
                bfs2.append(que[0])

            bfs2.sort()
            num_rep.remove(que)

            i = 0
        else:
            i += 1
    bfs1.extend(bfs2)
    
    v2 = bfs2[0]
    bfs(v2)

num_rep = copy.deepcopy(num)

bfs(v)
num_rep = copy.deepcopy(num)

dfs(v)



print(" ".join(map(str, dfs1)))

result = []
seen = set()  

for item in bfs1:
    if item not in seen: 
        result.append(item)
        seen.add(item)  
print(" ".join(map(str, result)))

"""

"""
https://kill-xxx.tistory.com/20
참고..

4 5 1 (n: 노드의 수, m: 간선의 수, v: 시작지점) 
1 2
1 3
1 4
2 4
3 4

이 입력값을 어떻게 그래프화 시켜야 하나 생각
그래프를 표로 표현하여 대부분 문제를 푼다.
ex) 1과 2가 연결되어 있으므로 그래프 상
이렇게 되어있고 [1,2]와 [2,1]은 연결되어 있으므로 아래처럼 채크
     0 1 2 3 4
   0 ■ ■ ■ ■ ■
   1 ■ □ 1 □ □
   2 ■ 1 □ □ □
   3 ■ □ □ □ □
   4 ■ □ □ □ □

다 체크 후 결과는
     0 1 2 3 4
   0 ■ ■ ■ ■ ■
   1 ■ □ 1 1 1
   2 ■ 1 □ □ 1
   3 ■ 1 □ □ 1
   4 ■ 1 1 1 □

bfs, dfs 함수를 만들어 둔 뒤 visit 체크
"""


from collections import deque

# 노드의 수, 간선, 시작지점 입력
n, m, v = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)]

# visited = [0] * n+1
# print("visited : ", visited)
dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)

answer = []

def dfs(v):
    # v = 시작
    dfs_visited[v] = 1
    # print("v: ", v)
    answer.append(v)

    for i in range(1, n+1):
        if graph[v][i] == 1 and dfs_visited[i] != 1:
            dfs(i)
    return answer

def bfs(v):
    bfs_answer = []

    que = deque()
    que.append(v)
    bfs_answer.append(v)
    bfs_visited[v] = 1

    while que:
        nv = que.popleft()

        for i in range(1, len(graph[nv])):
            if graph[nv][i] == 1 and bfs_visited[i] == 0:
                bfs_visited[i] = 1
                que.append(i)
                bfs_answer.append(i)
    return bfs_answer


for i in range(m):
    x, y = map(int, input().split())
    # print(x, y)
    graph[x][y] = 1
    graph[y][x] = 1
    

print(*dfs(v))
print(*bfs(v))


    