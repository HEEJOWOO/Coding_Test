##################################################################################################
## 조건 1: 상, 하 , 좌, 우 붙어 있는 경우 서로 연결되어 있는 것으로 간주
## 입력 : N, M 두 정수가 주어짐, N개의 줄에는 각각 M개의 정수로 미로의 정보가 주어짐
## 출력 : 0으로 구성되어 있는 묶음 갯수 출력
##################################################################################################
# 깊이 우선 탐색(DFS)
n,m = map(int,input().split()) #가로 세로 입력
array = []
for _ in range(n):
    array.append(list(map(int,input()))) #주어진 행 갯수만큼 2차원 배열, 미로 생성

def dfs(x,y):
    if x < 0 or y<0 or x >=n or y>=m: #예외 처리 
        return False
    if array[x][y]==0: # 미로 칸 중 0인것에 대해서 방문처리 진행
        array[x][y]=1

        dfs(x-1, y) #재귀 함수 호출로 주변 칸 탐색
        dfs(x, y - 1)
        dfs(x+1, y)
        dfs(x, y + 1)

        return True
    return False

result =0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result += 1
print(result)




