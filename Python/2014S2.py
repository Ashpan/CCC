amountOfPeople = int(input()) #lol i dont even use this lmfao
line1 = (str(input())).split(' ')
line2 = (str(input())).split(' ')
for x in range(0,len(line1)):
    if line1[x] == line2[x]:
        print('bad')
        break

    sameindex = line2.index(line1[x])
    if line1[x] == line2[sameindex] and line1[sameindex] == line2[x]:
        
    if line1[x] in line2 == :
        print('bad')
        break
    elif x == len(line1) - 1:
        print('good')
        break