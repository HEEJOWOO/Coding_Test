#삽입 정렬
n=[0,1,2,3,4,5,6,7,9,8]
for i in range(1,len(n)):
    for j in range(i,0,-1):
        if n[j]<n[j-1]:
            n[j],n[j-1]=n[j-1],n[j]
        else:
            break
print(n)