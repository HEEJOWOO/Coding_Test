n,k = input().split()
array = list(map(int,input().split()))
def binary_search(array,find,start,end):
    while(start<end):
        mid = (start+end)//2
        if array[mid]>=find:
            end-=1
        else :
            start+=1
    return start

result = binary_search(array,int(k),0,int(n))
print(result+1)