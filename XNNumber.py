def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        answer.append(x * i)
    return answer

print(solution(2, 5))




def number_generator(x, n):
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))