###################################################
##입력 조건 : 첫째 줄에 수열에 속해 잇는 수의 개수 N이 주어짐,둘째 줄부터 N개의 수를 줄마다 입력 받음 
##출력 조건 : 입력 받은 N개의 수에 대해 내림 차순 정리 
###################################################

n=int(input())
array =[]
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)
for i in array:
    print(i,end=' ')
 
###################################################
##입력 조건 : N명 입력, 둘째 줄부터 사람 점수 형식으로 줄마다 입력(N개)
##출력 조건 : 점수가 낮은 순서대로 사람 이름 출력 
###################################################

n = int(input())

array = []
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))

array=sorted(array,key=lambda x : x[1])
for student in array:
    print(student[0], end = ' ')

###################################################
##입력 조건 : n은 자연수 갯수, k는 교차 가능한 횟수 / array_a, array_b n개의 자연수를 갖고 있는 두개의 배열 입력
##출력 조건 : k번 array_b에서 array_a로 교차하여 만들 수 있는 배열의 모든 원소의 합의 최댓값 출력 
###################################################

n,k=map(int,input().split())
array_a = list(map(int,input().split()))
array_b = list(map(int,input().split()))
array_a.sort()
array_b.sort()
for i in range(k):
    if array_a[i]<array_b[(len(array_b)-1)-i]:
        array_a[i],array_b[(len(array_b)-1)-i]=array_b[(len(array_b)-1)-i],array_a[i]
    else :
        break
print(sum(array_a))