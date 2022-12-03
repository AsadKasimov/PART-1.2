"""
# homework
Дан список words. Составьте из него список слов-палиндромов. Попробуйте это сделать двумя способами
: произвольное решение и решение в одну строчку кода.
Дан список my_str со строками, часть из которых являются палиндромами.
Составьте новый список строк-палиндромов.
"""

'''words = ['мадам', 'топот', 'test', 'madam', 'word']
words2 = []
for i in words:
    a = i[::-1]
    if i == a:
        words2.append(i)
    else:
        del i
print(words2)'''

my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
my_str2=[]
for t in my_str:
    h = (t.lower().replace(' ', ''))[::-1]
    if h == t.lower().replace(' ', ''):
        my_str2.append(t)
    else:
        del t
print(my_str2)