'''
# 예외처리 : 에러 
try:
    print('나누기 전용 계산기')
    nums = []
    nums.append(int(input('첫 번째 : ')))
    nums.append(int(input('두 번째 : ')))
    # nums.append(int(nums[0]/nums[1]))
    print(f'{nums[0]} / {nums[1]} = {nums[2]}')
except ValueError: # 트라이를 시도하다가 잘못된 부분이 있으면 exept를 찾는다.
    print('잘못된 값을 입력했습니다.')
except ZeroDivisionError as err:
    print(err)
except Exception as err: # 나머지 모든 에러 처리 + exeption : 어떤 에러인지 알고 싶을 때
    print('알 수 없는 에러 발생')
    print(err)




#에러발생시키기
try:
    print('한자리 숫자 전용 나누기 계산기')
    num1 = int(input('첫 : '))
    num2 = int(input('두 : ')) 
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print(f'{num1} / {num2} = {int(num1/num2)}')
except ValueError:
    print('잘못된 값')
    
    
 '''



 # 사용자 정의 예외 처리

class BigNumberError(Exception):
    pass

try:
    print('한자리 숫자 전용 나누기 계산기')
    num1 = int(input('첫 : '))
    num2 = int(input('두 : ')) 
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError
    print(f'{num1} / {num2} = {int(num1/num2)}')
except ValueError:
    print('잘못된 값')
except BigNumberError:
    print('한자리 숫자만 입력해주세요.')
finally: # 잘 작동 되던지 안되던지 무조건 출력됨.
    print('계산기를 이용해 주셔서 감사합니다.')