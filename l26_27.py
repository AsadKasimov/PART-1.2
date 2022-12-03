def hello(name, word):
    print('Hello, ' + name + '. Say ' + word)

hello('John', 'hi')
hello('Katy', 'hello')
# узнал что функции нужны ну и про сами функции

# в 27 уроке прошли возврат т.е. return и *args
def func(**kwargs):
    print(kwargs)

func(a=1, b=5, c=20)

# def get_sum(a=0, b=0, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, d=5))

