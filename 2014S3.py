def minimum(lst):
    small = lst[0]
    for a in lst:
        if a < small:
            small = a
    return small

if __name__ == '__main__':
    tests = int(input())
    mountain = []
    river = []
    branch = []
    possible = ''
    for x in range(0, tests):       # runs whole program number of times as the tests
        numberOfCars = int(input())
        for y in range(0, numberOfCars):    # runs input to collect the number of cars
            mountain.append(int(input()))
        while not len(mountain) == 0:
            if mountain[-1] == minimum(mountain):
                river.append(mountain.pop(-1))
            else:
                branch.append(mountain.pop(-1))
        while len(mountain) == 0 and not len(branch) == 0:
            if branch[-1] == minimum(branch):
                river.append(branch.pop(-1))
            else:
                possible = 'N'
                break
        if len(mountain) == 0 and len(branch) == 0:
            possible = 'Y'
        print(possible)
    # print('mountain', mountain)
    # print('branch', branch)
    # print('river', river)


