def toList(string, list):
    for x in string:
        if x != '*':
            ordinal = 0
            if ord(x) > 64 and ord(x) < 91:
                ordinal = ord(x) - 65
            elif ord(x) > 96 and ord(x) < 123:
                ordinal = ord(x) - 97
            list[ordinal] += 1
        else:
            list[-1] += 1

def fillList(list):
    for x in range(27):
        list.append(0)

if __name__ == '__main__':
    lst1 = []
    lst2 = []
    fillList(lst1)
    fillList(lst2)
    string1 = str(input())
    string2 = str(input())
    toList(string1, lst1)
    toList(string2, lst2)

    for x in range(26):
        if(lst1[x]>lst2[x] and lst2[-1]>0):
            lst2[-1] -= lst1[x]-lst2[x]
            lst2[x] += lst1[x]-lst2[x]

    if lst1 == lst2:
        print('A')
    else:
        print('N')

