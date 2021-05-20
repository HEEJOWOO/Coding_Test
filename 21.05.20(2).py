def binary_search(array,find,start,end):

    while start<=end:
        mid = (start + end) // 2
        if array[mid]==find:
            return mid
        elif array[mid]>find:
            end = mid - 1
        else :
            start = mid +1
    return False


n = int(input())
array = list(map(int,input().split()))
array.sort()
k = int(input())
find_box = list(map(int,input().split()))

for i in find_box:
    result = binary_search(array,i,0,n-1)
    if result != False:
        print("Yes",end=' ')
    else :
        print("No", end=' ')


n,k = input().split()
array = list(map(int,input().split()))

start = 0
end = max(array)
result=0
while(start<=end):
    mid = (start+end)//2

    total = 0
    for i in array:
        if i > mid:
            total+=i-mid
    if total<int(k):
        end = mid - 1

    else:
        result = mid
        start = mid + 1
print(result)
