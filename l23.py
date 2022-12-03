"""
Узнали что есть словари. То что могут быть словари в списках или наоборот. кортежи в списках или
наоборот. и словари в словарях
"""
users = [
    ['bob@gmail.com', 'Bob'],
    ['katy@gmail.com', 'Katy'],
    ['john@gmail.com', 'John']
]
d_users = dict(users)

users_t = (
    ('bob@gmail.com', 'Bob'),
    ('katy@gmail.com', 'Katy'),
    ('john@gmail.com', 'John')
)
t_users = dict(users_t)
