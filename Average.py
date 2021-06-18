def solution(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)

a = [1,2,3,4]
print(solution(a))