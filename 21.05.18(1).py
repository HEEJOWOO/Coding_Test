#선택 정렬

n=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(n)):
    min_index = i
    for j in range(i+1,len(n)):
        if n[min_index] > n[j]:
            min_index = j
    n[i],n[min_index] = n[min_index],n[i]

print(n)