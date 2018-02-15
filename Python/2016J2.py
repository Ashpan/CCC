import sys
matrix = [[0 for x in range(4)] for y in range(4)]
for x in range(4):
    n = ''
    lst = str(input()).split(' ')
    lst = [int(y) for y in lst]
    matrix[x] = lst
    sum = 0
    magic = 'magic'
    for x in range(4):
        sum += matrix[0][x]
    # print('sum',sum)
    for x in range(4):
        yRange = 0
        for y in range(4):
            yRange += matrix[y][x]
        if yRange != sum:
            magic = 'not magic'
    for x in range(4):
        yRange = 0
        for y in range(4):
            yRange += matrix[x][y]
        if yRange != sum:
            magic = 'not magic'
print(magic)