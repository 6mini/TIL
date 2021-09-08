'''
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
'''

# 예외처리

try:
    print('나누기 전용 계산기입니다.')
    num1 = int(input('첫 번째 숫자 : '))
    num2 = int(input('두 번째 숫자 : '))
    print(f'{num1} / {num2} = {int(num1/num2)}')
except ValueError:
    print('니 잘못된 문자 넣음.')
except ZeroDivisionError as err:
    print(err) 