amountOfPeople = int(input()) #lol i dont even use this lmfao
line1 = str(input())
line2 = str(input())
list1 = []
list1 = line1.split(' ')
list2 = line2.split(' ')
for x in range(0,len(list1)):
    if not list1[x] == list2[len(list2)-1-x]:
        print('bad')
        break
    elif x == len(list1) - 1:
        print('good')
        break