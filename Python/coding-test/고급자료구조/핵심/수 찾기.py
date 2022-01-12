n = int(input())
nl = set(map(int, input().split(' '))) # set으로 진행하면 해시 자료구조로 풀 수 있음
m = int(input())
ml = list(map(int, input().split(' ')))

for i in ml:
    if i in nl:
        print(1)
    else:
        print(0)