'''
В этом занятии мы прошли IF/elif/else. If проверяет входящие данные на верность и если
они подходят производит над ним действия. Если оно не подходит выполняется Else. Если нужно доп условие
пишется elif схож с if.
'''
light = 'blue'

if light == 'red':
    print('Stop')
elif light == 'yellow':
    print('Wait')
elif light == 'green':
    print('Go')
else:
    print('What?')