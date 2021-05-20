# 이진 탐색(재귀구조)
def binary_search(array,target,start,end):
    if start > end :
        return None
    mid = (start + end)//2
    if array[mid] == target:
        return mid+1
    elif array[mid] > target:
        return binary_search(array,target,start,end = mid-1)
    else :
        return binary_search(array,target,mid+1,end)
n_find = input().split()
find = int(n_find[1])
array = list(map(int,input().split()))
if binary_search(array,find,0,int(n_find[0])-1) != None:
    print(binary_search(array,find,0,int(n_find[0])-1) )
else :
    print("None")


# 이진 탐색(반복문)
def binary_search(array,target,start,end):
    while start <=end:
        mid = (start + end ) // 2
        if array[mid]==target:
            return mid+1
        elif array[mid]>target:
            end = mid-1
        else :
            start = mid + 1
    return None
n_find = input().split()
find = int(n_find[1])
array = list(map(int,input().split()))
if binary_search(array,find,0,int(n_find[0])-1) != None:
    print(binary_search(array,find,0,int(n_find[0])-1) )
else :
    print("None")