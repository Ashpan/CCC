cities = input().split(' ')
cities.insert(0, 0)
cities = [int(x) for x in cities]
matrix = [[0 for x in range(5)] for y in range(5)]
for x in range(5):
    matrix[0][x] = abs(0-cities[x])+matrix[0][x-1]
counter = 0
for x in matrix[0]:
    matrix[counter][0] = x
    counter += 1
# edges are now setup

for x in range(4):
    for y in range(4):
        matrix[x+1][y+1] = abs(matrix[x+1][0] - matrix[0][y+1])




for x in range(5):
    for y in range(5):
        print(matrix[x][y], end=" ", flush=True)
    print()