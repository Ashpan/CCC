

if __name__ == '__main__':
    dimen = (input().split(' '))
    dimen = [int(x) for x in dimen]
    # INDEX 0 IS HEIGHT
    # INDEX 1 IS WIDTH
    matrix = [[0 for x in range(int(dimen[1]))] for y in range(int(dimen[0]))]
    # print(matrix)
    for x in range(dimen[0]):
        lst1 = list(input())
        matrix[x] = lst1
        for x in range(dimen[0]):
            for y in range(dimen[1]):
                matrix[x]= list(matrix[x])


    print(matrix)
    exitpos = [0, 0]
    robotpos = [0, 0]
    exits = 0
    currentTime = 0
    leave = False
    pos = False
    for x in range(exitpos[0], dimen[0]):
        for y in range(exitpos[1], dimen[1]):
            if matrix[x][y] == '.':
                exits += 1
    print('exits', exits)

    for x in range(dimen[0]):
        if pos:
            break
        for y in range(dimen[1]):
            if pos:
                break
            if matrix[x][y] == 'S':
                pos = True
                robotpos[0] = x
                robotpos[1] = y

    while currentTime < exits:
        print('currentTime', currentTime)
        for x in range(exitpos[0], dimen[0]):
            if leave:
                break
            for y in range(exitpos[1], dimen[1]):
                if leave:
                    break
                if matrix[x][y] == '.':
                    leave = True
                    exitpos[0] = x
                    exitpos[1] = y
                    currentTime += 1
        print('exitpos', exitpos)
        leave = False


        steps = 0
        print(exitpos)
        print(matrix)
        print(exitpos[1]+1)
        if matrix[exitpos[0]][exitpos[1]] == 'W' and matrix[exitpos[1]][exitpos[0]] == 'W' and matrix[exitpos[1]][exitpos[0]] == 'W' and matrix[exitpos[1]][exitpos[0]] == 'W':
            print(-1)
        else:
            while robotpos[0]>exitpos[0]:
                if matrix[robotpos[0] - 1][robotpos[1]] != 'W':
                    robotpos[0] -= 1
                    steps += 1

            while robotpos[0]<exitpos[0]:
                if matrix[robotpos[0] + 1][robotpos[1]] != 'W':
                    robotpos[0] += 1
                    steps += 1

            while robotpos[1]>exitpos[1]:
                if matrix[robotpos[0]][robotpos[1] - 1] != 'W':
                    robotpos[1] -= 1
                    steps += 1


            while robotpos[1]<exitpos[1]:
                if matrix[robotpos[0]][robotpos[1]+ 1] != 'W':
                    robotpos[1] += 1
                    steps += 1
        print('STEPS',steps)
        if[exitpos[1] < dimen[1]-1]:
            exitpos[1] += 1
            print('y exitpos changed')
        elif[exitpos[0] != dimen[0]-1]:
            exitpos[0] += 1
            print('x exitpos changed')


