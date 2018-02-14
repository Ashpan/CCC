def minimum(lst, lst2=[]):
    small = lst[0]
    for a in lst:
        if a < small:
            small = a
    for a in lst2:
        if a < small:
            small = a
    return small

if __name__ == '__main__':
    tests = int(input())
    mountain = []
    river = []
    branch = []
    possible = ''
    YN = []
    for x in range(0, tests):       # runs whole program number of times as the tests
        numberOfCars = int(input())
        for y in range(0, numberOfCars):    # runs input to collect the number of cars
            mountain.append(int(input()))
        # print(mountain)
        while len(mountain) != 0 and len(branch) == 0:
            if mountain[-1] == minimum(mountain):
                river.append(mountain.pop(-1))
            else:
                branch.append(mountain.pop(-1))
        while len(mountain) != 0 and len(branch) != 0:
            if mountain[-1] == minimum(mountain, branch):
                river.append(mountain.pop(-1))
            elif branch[-1] == minimum(mountain, branch):
                river.append(branch.pop(-1))
            else:
                branch.append(mountain.pop(-1))
        while len(mountain) == 0 and len(branch) != 0:
            if branch[-1] == minimum(branch):
                river.append(branch.pop(-1))
            else:
                YN.append('N')
                break
        if len(mountain) == 0 and len(branch) == 0:
            YN.append('Y')
        # print('-------end of test---------')
        mountain = []
        branch = []
        river = []
    for x in YN:
        print(x)