speed = 0
dmoj = []
peg = []
minmax = int(input())
n = int(input())
string1 = str(input())
string2 = str(input())
dmoj = string1.split(' ')
dmoj = [int(x) for x in dmoj]
peg = string2.split(' ')
peg = [int(x) for x in peg]
if minmax == 1:
    dmoj.sort()
    peg.sort()
    for x in range(n):
        speed += max(int(dmoj[x]),int(peg[x]))
elif minmax == 2:
    dmoj.sort()
    peg.sort()
    peg = peg[::-1]
    # print('dmoj', dmoj, '\npeg', peg)
    for x in range(n):
        speed += max(int(dmoj[x]), int(peg[x]))
print(speed)