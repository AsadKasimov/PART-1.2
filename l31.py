import os
'''print("Текущая деректория:", os.getcwd())'''

if not os.path.isdir("First file"):
     os.makedirs('First file/inside')


print("Текущая деректория:", os.getcwd())


tree=os.walk('First file')
for i in tree:
    print(i)

