input()
lst1 = list(input())
lst2 = list(input())
counter = 0
for x in range(len(lst1)):
    if lst1[x] == 'C' and lst2[x] == 'C':
        counter += 1
print(counter)