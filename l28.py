'''def odd_ball(ar):
    t=0
    for i in ar:
        t += 1
        if i == 'odd':
            break
    if t-1 in ar:
        print("True")
    else:
        print('False')

odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"])
odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"])
odd_ball(["even",10,"odd",2,"even"])'''
"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности 
включительно. Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. 




def find_sum(n):
    sum1 = 0
    for i in range(n+1):
        if i % 3 == 0 or i % 5 == 0:
            sum1 += i
    print(i)


find_sum(5)  # return 8 (3 + 5)
find_sum(10)  # return 33 (3 + 5 + 6 + 9 + 10)"""

"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]
names4=[]
def get_names(name):
    for i in name:
        if len(i)==4:
            names4.append(i)
    print(names4)
    names4.clear()
get_names(names)
print(names4)