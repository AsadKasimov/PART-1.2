# поиграем
import random

x = random.randint(0, 10)
user_num = 0
cnt = 0

while user_num!='Quit':
    user_num = input('Я загадал число от 1 до 100 - угадай его.\nДля выхода отправь Quit: \n')
    cnt += 1
    if user_num.isalnum() == x:
        print(f'Ты угадал число за {cnt} попыток')
        print('Спасибо за игру')
        break
    elif user_num.isalnum() > x:
        print('Мое число меньше')
    elif user_num=='Quit':
        print('fufu')
    elif user_num.isalnum() < x:
        print('Мое число больше')

'''
узнал про модули или по другому библиотеки. можно даже создать свой
модуль. так же как импортировать, мопенять имя модуля, ипорт части
программы и т.д.
'''