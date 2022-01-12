def main():
    tc = int(input())
    for _ in range(tc):
        fc = [] # 커서 앞 스택
        bc = [] # 커서 뒤 스택
        keys = input()
        for key in keys:
            if key == '-': # 지우기
                if fc:
                    fc.pop()
            elif key == '<': # 커서 앞 글자 뒤로
                if fc:
                    bc.append(fc.pop())
            elif key == '>': # 커서 뒤 글자 앞으로
                if bc:
                    fc.append(bc.pop())
            else:
                fc.append(key)
        fc.extend(reversed(bc))
        print(''.join(fc))

        


                    
if __name__ == '__main__':
    main()