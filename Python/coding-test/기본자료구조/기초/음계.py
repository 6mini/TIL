def main():
    a = list(map(int, input().split(' ')))
    
    asc = True
    desc = True

    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            desc = False
        elif a[i] < a[i - 1]:
            asc = False

    if asc:
        print('ascending')
    elif desc:
        print('descending')
    else:
        print('mixed')


if __name__ == '__main__':
    main()