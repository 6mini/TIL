def main():
    n, m = list(map(int, input().split(' ')))
    l = list(map(int, input().split(' ')))
    a = 0
    
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                sum = l[i] + l[j] + l[k]
                if sum <= m and sum > a:
                    a = sum
    print(a)
                    

    



if __name__ == '__main__':
    main()