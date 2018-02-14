oglist = []
finalsize = []
numberof = int(input())
for x in range(numberof):
    oglist.append(float(input()))
oglist.sort()
for x in range(1, len(oglist)-1):
    finalsize.append(((oglist[x+1]-oglist[x])/2) + ((oglist[x]-oglist[x-1])/2))
print(min(finalsize))