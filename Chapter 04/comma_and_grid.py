"""Comma Code."""

spam = ['apples', 'bananas', 'tofu', 'cats']


def list_joiner(list):
    """Take a list and print it as an Oxford comma having sentence."""
    count = 0
    joined = ''
    while count < len(list) - 2:
        joined += list[count] + ', '
        count += 1
    joined += list[-2] + ' and '
    joined += list[-1] + '.'
    return joined


print(list_joiner(spam))

''' Random flip coins '''


import random
data=[]
count=0
numberOfStreaks=0
for exprimentNumber in range(10000):
    for i in range(100):
        res=random.randint(0,1)
        if res==0:
            data.append('H')
        else :
            data.append('T')
i=0
for value in data :
    
    if data[int(int(i)-1)]==data[i]:
        count+=1
    elif count==6:
        numberOfStreaks+=1
        count=0
    else:
        count=0
    i+=1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))



"""Character Picture Grid"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print()
