##################################################################################################
## 조건 1: 0은 갈 수 없는 곳 
## 조건 2: 1은 갈 수 있는 곳
## 입력 : N, M 두 정수가 주어짐, N개의 줄에는 각각 M개의 정수로 미로의 정보가 주어짐
## 출력 : 첫째 줄에 최소 이동 칸의 개수를 출력
##################################################################################################
# 너비 우선 탐색(BFS)
from collections import deque

n,m =map(int,input().split()) #행, 열 입력

array = []
for _ in range(n):
    array.append(list(map(int,input()))) #미로 입력, 2차원 배열
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0  or ny < 0 or nx >= n or ny >= m: #예외 처리 범위 초가
                continue
            if array[nx][ny]==0: #예외 처리 갈수 없는 곳
                continue
            if array[nx][ny]==1:
                array[nx][ny] = array[x][y]+1 #최단 경로 입력  
                queue.append((nx,ny))
    return array[n-1][m-1] #미로의 오른쪽 맨 아래 까지 가는 최소 칸 갯수 출력

print(bfs(0,0))


