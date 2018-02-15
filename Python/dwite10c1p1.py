lst = []
date = str(input())
lst = date.split(' ')
lst = [int(y) for y in lst]

if lst[2]>1997:
    printOut = 'too young'
elif lst[2]==1997 and lst[1]>10:
    printOut = 'too young'
elif lst[2]==1997 and lst[1]==10 and lst[0]>27:
    printOut = 'too young'
else:
    printOut = 'old enough'
print(printOut)