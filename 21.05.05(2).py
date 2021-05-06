#######################################################################################
## 조건 1: 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한개의 모음과 최소 두 개의 자음으로 구성
## 조건 2: 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되어 있음 (ex : abc(o), bac(x)
## 입력 : 첫째 줄에 두 정수 n, m이 주어짐(3<=L<=C<=15)
## 다음 줄에는 C개의 문자들이 주어지며 공백으로 구분
## 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없음
## 출력 : 각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력
#######################################################################################
# 조합 알고리즘 사용

import itertools

n, m = map(int, input().split()) #m 개의 문자들중 n개의 조합
vol = ('a','e','i','o','u') #모음
array = list(map(str, input().split()))
array.sort()

for i in itertools.combinations(array,n): #itertools의 조합 combinations 사용 
    count=0
    for j in i: #출력된 조합중 하나인 i문자들에서 모음이 있는지 판별
        if j in vol:
            count+=1
    if count>=1 and 2<=m-count:
        print("".join(i))