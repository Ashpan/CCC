def rotate(list):
    newMatrix = [[0 for x in range(N)] for y in range(N)]
    for x in range(N):
        for y in range(N):
            newMatrix[x][y] = list[y][N-x-1]
    return newMatrix

if __name__ == '__main__':
    toRotate = True
    N = int(input())
    matrix = [[0 for x in range(N)] for y in range(N)]
    for x in range(N):
        lst1 = input().split(' ')
        lst1 = [int(x) for x in lst1]
        matrix[x] = lst1
    while toRotate:
        toRotate = False
        for x in range(N-1):
            if matrix[0][x] > matrix[0][x+1]:
                toRotate = True
        for x in range(N - 1):
            if matrix[x][0] > matrix[x+1][0]:
                toRotate = True
        if toRotate:
            matrix = rotate(matrix)
for x in range(N):
    for y in range(N):
        print(matrix[x][y], end=" ", flush=True)
    print()