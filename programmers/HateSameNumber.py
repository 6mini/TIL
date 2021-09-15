arr1 = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]

def solution(arr):
    ans = []
    for i in range(len(arr)):
        if i == 0:
            ans.append(arr[i])
        elif arr[i] != arr[i-1]:
            ans.append(arr[i])
    return ans

print(solution(arr1))
print(solution(arr2))