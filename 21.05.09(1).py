##################################################################################################
## 조건 1: L : 왼쪽으로 한 칸 이동 , R : 오른쪽으로 한 칸 인동 , U : 위로 한 칸 이동, D : 아애로 한 칸 이동
## 조건 2: 정사각형 공간을 벗어나는 움직임은 무시 
## 입력 : 첫째 줄에 공간의 크기를 나타내는 N이 주어짐(1<=N<=100)
## 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어짐 (1<=이동횟수<=100)
## 출력 : 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백으로 구분하여 출력 
##################################################################################################
# 구현

n = int(input()) # 이동할 횟수 입력
array = input().split() #이동할 방향 입력

dx = [0,0,-1,1] #이동할 수 있는 각 방향에 대한 x,y 좌표 저장
dy = [-1,1,0,0]
vol = ['l','r','u','d']
x = 1
y = 1
for i in array: #입력된 방향 과 저장되어있는 방향을 비교하여 맞으면 동일한 index의 dx, dy 값을 가져와 방향 이동 
    for j in range(len(vol)):
        if i==vol[j]:
            nx=x+dx[j]
            ny=y+dy[j]
    if nx<1 or ny<1 or nx>n or ny>n: #정사각형 범위 넘으면 무시
        continue
    x,y=nx,ny
print(x,y)

