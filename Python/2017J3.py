start = input().split(' ')
start = [int(x) for x in start]
end = input().split(' ')
end = [int (x) for x in end]
fuel = int(input())

distance = abs(end[0] - start[0]) + abs(end[1] - start[1])
if abs(fuel-distance) % 2 == 1:
    print('N')
else:
    print('Y')