import time
import random



opening_comment ='''\n
##################################################\n
            모의 Lotto 추첨기 입니다.
            1부터 45까지의 숫자 중에서 
        6개의 숫자를 차레대로 입력해 주세요.\n
##################################################\n\n\n
'''
print(opening_comment)

user_numbers = []

for i in range(6):
    input_string = str(i+1)+'번째 숫자를 입력하시오 : '
    N = input(input_string)
    is_valid_num = False

    while not is_valid_num:
        try:
            N = int(N)
            is_int = True
        except:
            is_int = False

        if not is_int:
            input_string = '정수를 입력하시오 : '
            N = input(input_string)

        elif (N > 45) | (N <1):
            input_string = '1~45 사이의 정수를 입력하시오 : '
            N = input(input_string)

        elif N in user_numbers:
            input_string = '중복되지 않는 숫자를 입력하시오 : '
            N = input(input_string)

        else:
            is_valid_num = True
            user_numbers.append(N)

user_numbers.sort()

print('\n')
print('선택하신 번호는', end = ' ')
print(', '.join([str(num) for num in user_numbers]), end = ' ')
print('입니다.')
time.sleep(2)

print('\n')
print('추첨을 시작합니다.\n')
time.sleep(3)

winnig_numbers = []

for i in range(6):
    N = random.randint(1, 45)
    while N in winnig_numbers:
        N = random.randint(1, 45)
    winnig_numbers.append(N)

    print('%d번째 추첨번호는 : %d' % (i+1, N))
    time.sleep(3)

N = random.randint(1, 45)
while N in winnig_numbers:
    N = random.randint(1, 45)
winnig_numbers.append(N)
print('보너스 번호는 : %d' % N)
time.sleep(3)

winnig_numbers.sort()

print('\n')
print('추첨 번호는', end = ' ')
print(', '.join([str(num) for num in winnig_numbers]), end = ' ')
print('입니다.')
time.sleep(2)

common_numbers = []

for num1 in user_numbers:
    for num2 in winnig_numbers:
        if num1==num2:
            common_numbers.append(num1)
print()
print('--------------------------------------------------')
print('  선택한 번호 : '+', '.join([str(num) for num in user_numbers]))
print('  추첨 번호   : '+', '.join([str(num) for num in winnig_numbers]))
print('  당첨 번호   : '+', '.join([str(num) for num in common_numbers]))
print('--------------------------------------------------', end='\n\n')


if len(common_numbers)==6:
    print('축하합니다~ 1등입니다!!')
elif len(common_numbers)==5:
    print('굉장하군요 2등입니다!')
elif len(common_numbers)==4:
    print('3등입니다~')
elif len(common_numbers)==3:
    print('4등입니다.')
else:
    print('아쉽지만 꽝ㅠㅠ')
