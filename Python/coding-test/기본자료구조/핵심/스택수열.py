def main():
    n = int(input())
    stack = []
    c = 1
    res = []

    for _ in range(n):
        i = int(input())
        while c <= i:
            stack.append(c)
            c += 1
            res.append('+')
        if stack[-1] == i:
            stack.pop()
            res.append('-')
        else:
            print('NO')
            exit()
    print('\n'.join(res))

                    
if __name__ == '__main__':
    main()