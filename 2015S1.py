readout = []
sum = 0
k = eval(input())
for x in range(0, k):
    line = int(input())
    readout.append(line)
x=0
while x<len(readout):
    if readout[x] == 0:
        del readout[x-1]
        del readout[x-1]
        x=0
    x+=1
for x in readout:
    sum += x
print(sum)