def main():
    test_cases = int(input()) # 테스크 케이스 갯수
    for _ in range(test_cases):
        n, m = list(map(int, input().split(' ')))
        queue = list(map(int, input().split(' '))) # 중요도
        queue = [(i, idx) for idx, i in enumerate(queue)] # 인덱스와 값을 튜플로 생성

        count = 0
        while True:
            if queue[0][0] == max(queue, key=lambda x: x[0])[0]: # 만약 큐 제일 앞의 값이 큐에서 제일 크다면
                count += 1 # 카운트를 1 올리고
                if queue[0][1] == m: # 만약 이 인덱스가 알아보려는 인덱스라면
                    print(count) # 카운트 출력
                    break
                else:
                    queue.pop(0) # 첫 번 째 튜플을 빼고 반복
            else:
                queue.append(queue.pop(0)) # 제일 큰 값이 아니라면 맨 앞 튜플을 맨 뒤로

                    
if __name__ == '__main__':
    main()